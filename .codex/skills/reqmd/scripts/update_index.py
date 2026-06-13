#!/usr/bin/env python3
"""Add missing ReqMd index sections and source links."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ID_HEADING_RE = re.compile(r"^(#{1,6})\s+\[([A-Z][A-Z0-9_]*)\]\((?:@|[^)]*/@)(?:#[^)]+)?\)")
HELPER_LINK_RE = re.compile(r"\[([^\]]+)\]\((?:=|[^)]*/=)(?:#[^)]+)?\)")
FENCE_RE = re.compile(r"^\s*```")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def anchor(name: str) -> str:
    return name


def collect_requirements(doc: Path) -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    for line in read_text(doc).splitlines():
        m = ID_HEADING_RE.match(line)
        if m:
            req_id = m.group(2)
            found.append((req_id, f"{doc.name}#{req_id}"))
    return found


def collect_helpers(doc: Path) -> list[tuple[str, str]]:
    helpers: list[tuple[str, str]] = []
    current_req: str | None = None
    in_fence = False
    for line in read_text(doc).splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = ID_HEADING_RE.match(line)
        if m:
            current_req = m.group(2)
            continue
        if not current_req:
            continue
        for link in HELPER_LINK_RE.finditer(line):
            helpers.append((link.group(1), f"{doc.name}#{current_req}"))
    return helpers


def ensure_section(index: Path, kind: str, name: str, source: str) -> bool:
    if index.exists():
        text = read_text(index)
    else:
        title = "Identifier Index" if kind == "@" else "Helper Index"
        text = f"# {title}\n"

    heading = f"## [{name}]({kind}#{anchor(name)})"
    source_line = f"- [{name}]({source})"
    changed = False

    if heading not in text:
        block = f"\n\n{heading}\n\n{source_line}\n"
        text = text.rstrip() + block
        changed = True
    else:
        start = text.index(heading)
        next_heading = text.find("\n## ", start + 1)
        section = text[start:] if next_heading == -1 else text[start:next_heading]
        if source_line not in section:
            insert_at = next_heading if next_heading != -1 else len(text)
            text = text[:insert_at].rstrip() + f"\n{source_line}\n" + text[insert_at:]
            changed = True

    if changed:
        write_text(index, text.rstrip() + "\n")
    return changed


def update(root: Path) -> list[str]:
    changes: list[str] = []
    for directory in sorted({p.parent for p in root.rglob("*.md") if p.name not in {"@.md", "=.md"}}):
        docs = sorted(p for p in directory.glob("*.md") if p.name not in {"@.md", "=.md"})
        if not docs:
            continue
        id_index = directory / "@.md"
        helper_index = directory / "=.md"
        for doc in docs:
            for req_id, source in collect_requirements(doc):
                if ensure_section(id_index, "@", req_id, source):
                    changes.append(f"updated {id_index}")
            for helper, source in collect_helpers(doc):
                if ensure_section(helper_index, "=", helper, source):
                    changes.append(f"updated {helper_index}")
    return changes


def main() -> int:
    parser = argparse.ArgumentParser(description="Add missing ReqMd index sections and source links")
    parser.add_argument("root", nargs="?", default=".", help="Requirement root to update")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    changes = update(root)
    if changes:
        for item in sorted(set(changes)):
            print(item)
    else:
        print("No index changes needed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
