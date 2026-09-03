#!/usr/bin/env python3
"""Emit a compact, deterministic inventory of Markdown headings, bullets, and tables."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def inventory(path: Path) -> dict:
    headings: list[dict] = []
    bullets: list[dict] = []
    tables: list[dict] = []
    section = None
    in_table = False
    table_rows = 0

    for number, raw in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        line = raw.rstrip()
        heading = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if heading:
            section = heading.group(2)
            headings.append({"line": number, "level": len(heading.group(1)), "text": section})
            in_table = False
            continue

        if re.match(r"^\s*[-*+]\s+", line):
            bullets.append({"line": number, "section": section, "text": re.sub(r"^\s*[-*+]\s+", "", line)})

        if "|" in line and line.strip().startswith("|"):
            if not in_table:
                tables.append({"line": number, "section": section, "rows": 0})
                in_table = True
            if not re.match(r"^\s*\|?\s*:?-{3,}", line):
                tables[-1]["rows"] += 1
            table_rows += 1
        elif line.strip() == "":
            in_table = False

    return {
        "path": str(path),
        "headings": headings,
        "heading_count": len(headings),
        "bullet_count": len(bullets),
        "bullets": bullets,
        "tables": tables,
        "table_count": len(tables),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()
    payload = [inventory(path) for path in args.paths]
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
