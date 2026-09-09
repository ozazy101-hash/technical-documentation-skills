#!/usr/bin/env python3
"""Create a technical HTML documentation page from the bundled starter."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--title", default="Technical documentation")
    parser.add_argument("--system", default="System or domain")
    parser.add_argument("--filename", default="index.html")
    parser.add_argument("--mermaid", type=Path, help="Path to a local mermaid.min.js")
    parser.add_argument("--echarts", type=Path, help="Path to a local echarts.min.js")
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def vendor_tag(source: Path | None, filename: str) -> str:
    if source is None:
        return ""
    return f'<script src="assets/{filename}"></script>'


def main() -> int:
    args = parse_args()
    starter = Path(__file__).resolve().parents[1] / "assets" / "starter" / "technical-page.html"
    destination = args.output_dir.resolve()
    output = destination / args.filename

    if output.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite {output}; pass --force to replace it.")

    destination.mkdir(parents=True, exist_ok=True)
    assets = destination / "assets"

    for supplied, target_name in ((args.mermaid, "mermaid.min.js"), (args.echarts, "echarts.min.js")):
        if supplied is not None:
            supplied = supplied.expanduser().resolve()
            if not supplied.is_file():
                raise SystemExit(f"Vendor file not found: {supplied}")
            assets.mkdir(exist_ok=True)
            shutil.copy2(supplied, assets / target_name)

    html = starter.read_text(encoding="utf-8")
    replacements = {
        "{{DOC_TITLE}}": args.title,
        "{{SYSTEM_NAME}}": args.system,
        "{{MERMAID_SCRIPT}}": vendor_tag(args.mermaid, "mermaid.min.js"),
        "{{ECHARTS_SCRIPT}}": vendor_tag(args.echarts, "echarts.min.js"),
    }
    for token, value in replacements.items():
        html = html.replace(token, value)
    output.write_text(html, encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
