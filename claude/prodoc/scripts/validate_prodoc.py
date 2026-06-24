#!/usr/bin/env python3
"""Validate ProDoc frontmatter without external YAML dependencies.

This validator intentionally supports the ProDoc subset used by this skill:

reqmd_prodoc:
  requirement_refs:
    - path/to/reqmd-root-or-index:
      - REQ_ID
  knowledge_files:
    - file.md
  propagation_docs:
    lateral:
      - peer.md
    upstream:
      - parent.md
    downstream:
      - child.md
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ID_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")
INDEX_HEADING_RE = re.compile(r"^## \[([A-Z][A-Z0-9_]*)\]", re.M)


class ProDocError(Exception):
    pass


def extract_frontmatter(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8-sig")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ProDocError("missing YAML frontmatter fence")
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[1:i]
    raise ProDocError("unterminated YAML frontmatter")


def parse_prodoc(lines: list[str]) -> dict:
    if not any(line.strip() == "reqmd_prodoc:" for line in lines):
        raise ProDocError("missing reqmd_prodoc key")

    data = {"requirement_refs": [], "knowledge_files": [], "propagation_docs": {}}
    section: str | None = None
    direction: str | None = None
    current_req_path: str | None = None

    for raw in lines:
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        text = raw.strip()

        if indent == 0 and text == "reqmd_prodoc:":
            section = None
            direction = None
            current_req_path = None
            continue
        if indent == 2 and text.endswith(":"):
            key = text[:-1]
            if key not in {"requirement_refs", "knowledge_files", "propagation_docs"}:
                raise ProDocError(f"unsupported reqmd_prodoc key: {key}")
            section = key
            direction = None
            current_req_path = None
            continue

        if section == "requirement_refs":
            if indent == 4 and text.startswith("- ") and text.endswith(":"):
                current_req_path = text[2:-1].strip()
                if not current_req_path:
                    raise ProDocError("empty requirement_refs path")
                data["requirement_refs"].append({current_req_path: []})
                continue
            if indent == 6 and text.startswith("- "):
                if not current_req_path or not data["requirement_refs"]:
                    raise ProDocError("requirement ID without requirement_refs path")
                ident = text[2:].strip()
                if not ID_RE.match(ident):
                    raise ProDocError(f"invalid requirement ID: {ident}")
                data["requirement_refs"][-1][current_req_path].append(ident)
                continue

        if section == "knowledge_files" and indent == 4 and text.startswith("- "):
            data["knowledge_files"].append(text[2:].strip())
            continue

        if section == "propagation_docs":
            if indent == 4 and text.endswith(":"):
                direction = text[:-1]
                if direction not in {"lateral", "upstream", "downstream"}:
                    raise ProDocError(f"unsupported propagation direction: {direction}")
                data["propagation_docs"].setdefault(direction, [])
                continue
            if indent == 6 and text.startswith("- "):
                if not direction:
                    raise ProDocError("propagation target without direction")
                data["propagation_docs"].setdefault(direction, []).append(text[2:].strip())
                continue

        raise ProDocError(f"unsupported frontmatter line: {raw}")

    if not data["requirement_refs"]:
        raise ProDocError("requirement_refs is required")
    return data


def resolve_req_index(base: Path, ref: str) -> Path:
    p = (base / ref).resolve()
    if p.is_dir():
        return p / "@.md"
    if p.name == "@.md":
        return p
    if p.exists() and p.is_file():
        return p
    return p / "@.md"


def validate_doc(path: Path) -> list[str]:
    errors: list[str] = []
    base = path.parent
    try:
        data = parse_prodoc(extract_frontmatter(path))
    except (OSError, UnicodeError, ProDocError) as exc:
        return [f"{path}: {exc}"]

    for item in data["requirement_refs"]:
        for ref_path, ids in item.items():
            index = resolve_req_index(base, ref_path)
            if not index.exists():
                errors.append(f"{path}: missing requirement index {ref_path} -> {index}")
                continue
            try:
                available = set(INDEX_HEADING_RE.findall(index.read_text(encoding="utf-8-sig")))
            except OSError as exc:
                errors.append(f"{path}: cannot read requirement index {index}: {exc}")
                continue
            for ident in ids:
                if ident not in available:
                    errors.append(f"{path}: requirement ID {ident} not found in {index}")

    for rel in data["knowledge_files"]:
        if not (base / rel).resolve().exists():
            errors.append(f"{path}: missing knowledge file {rel}")

    for direction, targets in data["propagation_docs"].items():
        for rel in targets:
            if not (base / rel).resolve().exists():
                errors.append(f"{path}: missing {direction} propagation target {rel}")

    return errors


def iter_markdown(target: Path):
    if target.is_file():
        yield target
    else:
        yield from sorted(target.rglob("*.md"))


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Validate ProDoc frontmatter.")
    parser.add_argument("targets", nargs="+", help="ProDoc markdown files or directories")
    args = parser.parse_args(argv)

    errors: list[str] = []
    checked = 0
    for raw in args.targets:
        target = Path(raw)
        if not target.exists():
            errors.append(f"{target}: path does not exist")
            continue
        for path in iter_markdown(target):
            try:
                fm = extract_frontmatter(path)
            except ProDocError:
                continue
            if any(line.strip() == "reqmd_prodoc:" for line in fm):
                checked += 1
                errors.extend(validate_doc(path))

    if errors:
        print("ProDoc validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1
    print(f"OK: {checked} ProDoc file(s) checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
