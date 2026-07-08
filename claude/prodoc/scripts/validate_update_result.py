#!/usr/bin/env python3
"""Validate ProDoc UpdateContent result reports."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQ_HEADING_RE = re.compile(r"^#{1,6}\s+\[([A-Z][A-Z0-9_]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
SECTION_RE = re.compile(r"^##\s+(changed_content|trace|review|next_queue)\s*$", re.I | re.M)
ID_RE = re.compile(r"\b[A-Z][A-Z0-9_]{2,}\b")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def requirement_ids(path: Path | None) -> set[str]:
    if path is None:
        return set()
    return set(REQ_HEADING_RE.findall(read_text(path)))


def collect_req_ids(path: Path | None) -> set[str]:
    if path is None:
        return set()
    ids: set[str] = set()
    for line in read_text(path).splitlines():
        m = REQ_HEADING_RE.match(line)
        if m:
            ids.add(m.group(1))
    return ids


def split_contract_sections(text: str) -> dict[str, str]:
    matches = list(SECTION_RE.finditer(text))
    sections: dict[str, str] = {}
    for idx, match in enumerate(matches):
        name = match.group(1).lower()
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        sections[name] = text[start:end].strip()
    return sections


def ids_in(text: str) -> set[str]:
    if text.strip().lower() == "none":
        return set()
    return set(ID_RE.findall(text))


def validate_queue(text: str, errors: list[str]) -> None:
    if text.strip().lower() == "none":
        return
    required = {"target", "source", "direction", "input_sections", "change_summary"}
    blocks = [block for block in re.split(r"(?m)^-\s+", text) if block.strip()]
    if not blocks:
        errors.append("next_queue: expected 'none' or one or more '- target:' Queue blocks")
        return
    for block in blocks:
        keys = set()
        for line in block.splitlines():
            m = re.match(r"\s*([A-Za-z_]+)\s*:", line)
            if m:
                keys.add(m.group(1))
        missing = required - keys
        if missing:
            errors.append(f"next_queue: Queue block missing keys: {', '.join(sorted(missing))}")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Validate ProDoc UpdateContent result report")
    parser.add_argument("result", help="Markdown result report")
    parser.add_argument("--source", help="Source ProDoc document")
    parser.add_argument("--target", help="Target ProDoc document")
    parser.add_argument("--input-section", action="append", default=[], help="Allowed input RequirementSection ID")
    args = parser.parse_args(argv)

    result = Path(args.result).resolve()
    if not result.exists():
        print(f"ERROR: result file does not exist: {result}", file=sys.stderr)
        return 2

    source = Path(args.source).resolve() if args.source else None
    target = Path(args.target).resolve() if args.target else None
    source_ids = collect_req_ids(source)
    target_ids = collect_req_ids(target)
    allowed_input_ids = source_ids | set(args.input_section)

    sections = split_contract_sections(read_text(result))
    required_sections = ["changed_content", "trace", "review", "next_queue"]
    errors: list[str] = []

    for name in required_sections:
        if name not in sections:
            errors.append(f"missing section: ## {name}")

    changed_ids = ids_in(sections.get("changed_content", ""))
    if target and changed_ids:
        missing = changed_ids - target_ids
        if missing:
            errors.append(f"changed_content references IDs not found in target: {', '.join(sorted(missing))}")

    trace_ids = ids_in(sections.get("trace", ""))
    if trace_ids:
        known_ids = allowed_input_ids | target_ids
        missing = trace_ids - known_ids
        if missing:
            errors.append(f"trace references IDs not found in source/input/target: {', '.join(sorted(missing))}")

    validate_queue(sections.get("next_queue", ""), errors)

    if errors:
        print("FAILED: ProDoc update result validation")
        for error in errors:
            print(f"- {error}")
        return 1
    print("OK: ProDoc update result contract valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
