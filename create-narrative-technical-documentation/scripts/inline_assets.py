#!/usr/bin/env python3
"""Inline local stylesheet and script assets into a complete HTML document."""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path
from urllib.parse import unquote, urlparse


STYLE_RE = re.compile(
    r'<link\b(?=[^>]*\brel=["\']stylesheet["\'])(?=[^>]*\bhref=["\']([^"\']+)["\'])[^>]*>',
    re.IGNORECASE,
)
SCRIPT_RE = re.compile(
    r'<script\b(?=[^>]*\bsrc=["\']([^"\']+)["\'])[^>]*>\s*</script>',
    re.IGNORECASE,
)


def local_path(url: str, base: Path) -> Path | None:
    parsed = urlparse(html.unescape(url))
    if parsed.scheme or parsed.netloc or parsed.path.startswith("//"):
        return None
    return (base / unquote(parsed.path)).resolve()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    source = args.input.resolve()
    document = source.read_text(encoding="utf-8")

    def replace_style(match: re.Match[str]) -> str:
        path = local_path(match.group(1), source.parent)
        if path is None:
            return match.group(0)
        if not path.is_file():
            raise SystemExit(f"Missing stylesheet: {path}")
        css = path.read_text(encoding="utf-8").replace("</style", "<\\/style")
        return f"<style data-inlined-from=\"{html.escape(match.group(1))}\">\n{css}\n</style>"

    def replace_script(match: re.Match[str]) -> str:
        path = local_path(match.group(1), source.parent)
        if path is None:
            return match.group(0)
        if not path.is_file():
            raise SystemExit(f"Missing script: {path}")
        js = path.read_text(encoding="utf-8").replace("</script", "<\\/script")
        return f"<script data-inlined-from=\"{html.escape(match.group(1))}\">\n{js}\n</script>"

    document = STYLE_RE.sub(replace_style, document)
    document = SCRIPT_RE.sub(replace_script, document)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(document, encoding="utf-8")
    print(args.output.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
