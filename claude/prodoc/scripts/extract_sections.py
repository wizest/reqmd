#!/usr/bin/env python3
"""Extract ProDoc RequirementSection ranges and local links."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)")
REQ_HEADING_RE = re.compile(r"^(#{1,6})\s+\[([A-Z][A-Z0-9_]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)(.*)")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FENCE_RE = re.compile(r"^\s*```(\w+)?\s*$")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def frontmatter_end(lines: list[str]) -> int:
    if not lines or lines[0].strip() != "---":
        return 0
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            return idx + 1
    return 0


def is_prodoc(lines: list[str]) -> bool:
    end = frontmatter_end(lines)
    return end > 0 and any(line.strip() == "reqmd_prodoc:" for line in lines[:end])


def yaml_attributes(lines: list[str], start: int, end: int) -> list[str]:
    attrs: list[str] = []
    in_fence = False
    is_yaml = False
    for line in lines[start:end]:
        m = FENCE_RE.match(line)
        if m:
            if not in_fence:
                in_fence = True
                is_yaml = (m.group(1) or "").lower() in {"yaml", "yml"}
                continue
            in_fence = False
            is_yaml = False
            continue
        if in_fence and is_yaml and ":" in line:
            key = line.split(":", 1)[0].strip()
            if key and key not in attrs:
                attrs.append(key)
    return attrs


def section_links(lines: list[str], start: int, end: int) -> list[str]:
    links: list[str] = []
    in_fence = False
    for line in lines[start:end]:
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for label, target in LINK_RE.findall(line):
            rendered = f"[{label}]({target})"
            if rendered not in links:
                links.append(rendered)
    return links


def extract(path: Path) -> list[dict[str, object]]:
    lines = read_text(path).splitlines()
    sections: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    current_level = 0

    for idx, line in enumerate(lines, start=1):
        m_req = REQ_HEADING_RE.match(line)
        m_heading = HEADING_RE.match(line)
        if m_req:
            if current:
                current["end_line"] = idx - 1
                sections.append(current)
            current_level = len(m_req.group(1))
            current = {
                "id": m_req.group(2),
                "target": m_req.group(3),
                "title": m_req.group(4).strip(),
                "start_line": idx,
                "end_line": len(lines),
            }
            continue
        if current and m_heading and len(m_heading.group(1)) <= current_level:
            current["end_line"] = idx - 1
            sections.append(current)
            current = None
            current_level = 0

    if current:
        sections.append(current)

    for item in sections:
        start = int(item["start_line"])
        end = int(item["end_line"])
        item["attributes"] = yaml_attributes(lines, start, end)
        item["links"] = section_links(lines, start, end)
    return sections


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Extract ProDoc RequirementSections")
    parser.add_argument("document", help="ProDoc markdown document")
    args = parser.parse_args(argv)

    doc = Path(args.document).resolve()
    if not doc.exists():
        print(f"ERROR: document does not exist: {doc}", file=sys.stderr)
        return 2

    lines = read_text(doc).splitlines()
    print(f"document: {doc}")
    print(f"prodoc: {'yes' if is_prodoc(lines) else 'no'}")
    print("sections:")
    for item in extract(doc):
        print(f"- id: {item['id']}")
        print(f"  lines: {item['start_line']}-{item['end_line']}")
        print(f"  title: {item['title'] or '-'}")
        print(f"  attributes: {', '.join(item['attributes']) if item['attributes'] else '-'}")
        print(f"  links: {', '.join(item['links']) if item['links'] else '-'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
