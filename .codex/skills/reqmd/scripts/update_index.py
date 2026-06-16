#!/usr/bin/env python3
"""Add missing ReqMd index sections."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ID_HEADING_RE = re.compile(r"^(#{1,6})\s+\[([A-Z][A-Z0-9_]*)\]\((?:@|[^)]*/@)(?:#[^)]+)?\)")
HEADING_RE = re.compile(r"^#{1,6}\s+")
HELPER_LINK_RE = re.compile(r"\[([^\]]+)\]\((?:=|[^)]*/=)(?:#[^)]+)?\)")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
FENCE_RE = re.compile(r"^\s*```")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def heading_text(line: str) -> str:
    body = re.sub(r"^#{1,6}\s+", "", line).strip()
    return LINK_RE.sub(lambda m: m.group(1), body)


def anchor(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text.strip())
    return re.sub(r"-+", "-", text)


def collect_requirements(doc: Path) -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    for line in read_text(doc).splitlines():
        m = ID_HEADING_RE.match(line)
        if m:
            req_id = m.group(2)
            found.append((req_id, f"{doc.name}#{anchor(heading_text(line))}"))
    return found


def collect_helpers(doc: Path) -> list[tuple[str, str]]:
    helpers: dict[str, str] = {}
    current_req: str | None = None
    current_anchor: str | None = None
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
            current_anchor = anchor(heading_text(line))
            continue
        if HEADING_RE.match(line):
            current_req = None
            current_anchor = None
            continue
        if not current_req or not current_anchor:
            continue
        for link in HELPER_LINK_RE.finditer(line):
            helpers.setdefault(link.group(1), f"{doc.name}#{current_anchor}")
    return list(helpers.items())


def ensure_section(index: Path, kind: str, name: str, source: str) -> bool:
    if index.exists():
        text = read_text(index)
    else:
        title = "Identifier Index" if kind == "@" else "Helper Index"
        text = f"# {title}\n"

    heading_re = re.compile(rf"^##\s+\[{re.escape(name)}\]\([^)]+\)\s*$", re.MULTILINE)
    heading = f"## [{name}]({source})"
    changed = False

    match = heading_re.search(text)
    if not match:
        block = f"\n\n{heading}\n\n"
        text = text.rstrip() + block
        changed = True
    else:
        old_heading = match.group(0)
        if old_heading != heading:
            text = text[: match.start()] + heading + text[match.end() :]
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
    parser = argparse.ArgumentParser(description="Add missing ReqMd index sections")
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
