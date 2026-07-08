#!/usr/bin/env python3
"""Resolve ProDoc requirement_specs to ReqMd index entries and source files."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ID_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")
INDEX_HEADING_RE = re.compile(r"^##\s+\[([A-Z][A-Z0-9_]*)\]\(([^)]+)\)", re.M)


class ProDocError(Exception):
    pass


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def extract_frontmatter(path: Path) -> list[str]:
    lines = read_text(path).splitlines()
    if not lines or lines[0].strip() != "---":
        raise ProDocError("missing YAML frontmatter fence")
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            return lines[1:idx]
    raise ProDocError("unterminated YAML frontmatter")


def parse_requirement_specs(lines: list[str]) -> list[tuple[str, list[str]]]:
    if not any(line.strip() == "reqmd_prodoc:" for line in lines):
        raise ProDocError("missing reqmd_prodoc key")
    specs: list[tuple[str, list[str]]] = []
    section: str | None = None
    current_path: str | None = None

    for raw in lines:
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        text = raw.strip()
        if indent == 0 and text == "reqmd_prodoc:":
            section = None
            current_path = None
            continue
        if indent == 2 and text.endswith(":"):
            section = text[:-1]
            current_path = None
            continue
        if section != "requirement_specs":
            continue
        if indent == 4 and text.startswith("- ") and text.endswith(":"):
            current_path = text[2:-1].strip()
            specs.append((current_path, []))
            continue
        if indent == 6 and text.startswith("- "):
            ident = text[2:].strip()
            if not current_path:
                raise ProDocError("requirement ID without requirement_specs path")
            if not ID_RE.match(ident):
                raise ProDocError(f"invalid requirement ID: {ident}")
            specs[-1][1].append(ident)

    if not specs:
        raise ProDocError("requirement_specs is required")
    return specs


def resolve_req_index(base: Path, ref: str) -> Path:
    p = (base / ref).resolve()
    if p.is_dir():
        return p / "@.md"
    if p.name == "@.md":
        return p
    if p.exists() and p.is_file():
        return p
    return p / "@.md"


def line_for_heading(path: Path, req_id: str) -> int | None:
    for idx, line in enumerate(read_text(path).splitlines(), start=1):
        if re.match(rf"^##\s+\[{re.escape(req_id)}\]\(", line):
            return idx
    return None


def source_heading_line(source: Path, fragment: str) -> int | None:
    slug = fragment.lower()
    seen: dict[str, int] = {}
    for idx, line in enumerate(read_text(source).splitlines(), start=1):
        if not line.startswith("#"):
            continue
        text = re.sub(r"^#{1,6}\s+", "", line).strip()
        text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
        anchor = text.strip().lower()
        anchor = re.sub(r"[^\w\s-]", "", anchor, flags=re.UNICODE)
        anchor = re.sub(r"\s+", "-", anchor.strip())
        anchor = re.sub(r"-+", "-", anchor)
        count = seen.get(anchor, 0)
        seen[anchor] = count + 1
        candidate = anchor if count == 0 else f"{anchor}-{count}"
        if candidate == slug:
            return idx
    return None


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Resolve ProDoc requirement_specs")
    parser.add_argument("document", help="ProDoc markdown document")
    args = parser.parse_args(argv)

    doc = Path(args.document).resolve()
    if not doc.exists():
        print(f"ERROR: document does not exist: {doc}", file=sys.stderr)
        return 2

    try:
        specs = parse_requirement_specs(extract_frontmatter(doc))
    except ProDocError as exc:
        print(f"ERROR: {doc}: {exc}", file=sys.stderr)
        return 1

    print(f"document: {doc}")
    print("requirement_specs:")
    reviews: list[str] = []
    for ref, ids in specs:
        index = resolve_req_index(doc.parent, ref)
        print(f"- ref: {ref}")
        print(f"  index: {index}")
        if not index.exists():
            print("  status: missing-index")
            reviews.append(f"missing requirement index {ref} -> {index}")
            continue
        entries = dict(INDEX_HEADING_RE.findall(read_text(index)))
        print("  ids:")
        for ident in ids:
            target = entries.get(ident)
            if not target:
                print(f"  - id: {ident}")
                print("    status: missing-id")
                reviews.append(f"requirement ID {ident} not found in {index}")
                continue
            source_ref, fragment = target.split("#", 1) if "#" in target else (target, "")
            source = (index.parent / source_ref).resolve()
            index_line = line_for_heading(index, ident)
            source_line = source_heading_line(source, fragment) if source.exists() and fragment else None
            print(f"  - id: {ident}")
            print("    status: ok")
            print(f"    index_line: {index_line if index_line else '-'}")
            print(f"    source: {source}")
            print(f"    fragment: {fragment or '-'}")
            print(f"    source_line: {source_line if source_line else '-'}")
            if not source.exists():
                reviews.append(f"source document missing for {ident}: {source}")
            elif fragment and source_line is None:
                reviews.append(f"source fragment not found for {ident}: {fragment}")
    if reviews:
        print("REVIEW:")
        for item in sorted(set(reviews)):
            print(f"- {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
