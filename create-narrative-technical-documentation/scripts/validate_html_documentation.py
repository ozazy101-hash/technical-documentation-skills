#!/usr/bin/env python3
"""Validate structure and portability of a technical HTML documentation page."""

from __future__ import annotations

import argparse
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


class Inspector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tags: list[str] = []
        self.attrs: list[tuple[str, dict[str, str]]] = []
        self.heading_levels: list[int] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        self.tags.append(tag)
        self.attrs.append((tag, values))
        if re.fullmatch(r"h[1-6]", tag):
            self.heading_levels.append(int(tag[1]))


def local_reference(value: str, base: Path) -> Path | None:
    parsed = urlparse(value)
    if parsed.scheme in {"data", "mailto", "tel"} or parsed.netloc or value.startswith("#"):
        return None
    if parsed.scheme:
        return None
    return (base / unquote(parsed.path)).resolve()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path)
    parser.add_argument("--strict-self-contained", action="store_true")
    args = parser.parse_args()

    path = args.html.resolve()
    source = path.read_text(encoding="utf-8")
    lowered = source.lower()
    inspector = Inspector()
    inspector.feed(source)
    errors: list[str] = []
    warnings: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    require(lowered.lstrip().startswith("<!doctype html>"), "missing <!doctype html>")
    require(bool(re.search(r"<html\b[^>]*\blang=", lowered)), "missing html lang")
    require(bool(re.search(r"<meta\b[^>]*name=[\"']viewport[\"']", lowered)), "missing viewport metadata")
    require("<title" in lowered, "missing title")
    require("<main" in lowered, "missing main landmark")
    require("<nav" in lowered, "missing nav landmark")
    require("<h1" in lowered, "missing h1")
    require("prefers-reduced-motion" in lowered, "missing reduced-motion treatment")
    require(":focus-visible" in lowered, "missing visible keyboard focus style")
    require(bool(re.search(r"rel=[\"']icon[\"'][^>]*href=[\"']data:", lowered)), "missing self-contained favicon")
    require(not re.search(r"\{\{[A-Z0-9_]+\}\}", source), "unresolved template token")

    if "class=\"slide\"" in lowered or "class='slide'" in lowered:
        warnings.append("slide class found; confirm this is documentation rather than a deck")
    if "<figure" in lowered and "<figcaption" not in lowered:
        warnings.append("figure without figcaption")
    if len(inspector.heading_levels) > 1:
        for previous, current in zip(inspector.heading_levels, inspector.heading_levels[1:]):
            if current > previous + 1:
                warnings.append(f"heading level jumps from h{previous} to h{current}")
                break

    refs: list[str] = []
    for tag, attrs in inspector.attrs:
        key = "href" if tag in {"link", "a"} else "src" if tag in {"script", "img", "iframe"} else ""
        if not key or key not in attrs:
            continue
        value = attrs[key]
        if value.startswith(("http://", "https://", "//")):
            refs.append(value)
            if args.strict_self_contained:
                errors.append(f"external dependency in strict mode: {value}")
            continue
        local = local_reference(value, path.parent)
        if local is not None and tag != "a" and not local.is_file():
            errors.append(f"missing local asset: {value}")

    if refs and not args.strict_self_contained:
        warnings.append(f"external references present: {len(refs)}")
    if "<table" not in lowered:
        warnings.append("no semantic table found; confirm repeated technical fields are represented appropriately")
    if "source" not in lowered and "evidence" not in lowered:
        warnings.append("no visible source or evidence language found")

    for warning in dict.fromkeys(warnings):
        print(f"WARN: {warning}")
    for error in dict.fromkeys(errors):
        print(f"ERROR: {error}")
    if errors:
        return 1
    print(f"OK: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
