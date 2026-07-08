#!/usr/bin/env python3
"""Repair bare ReqMd index links when the target index section is known."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def slug(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text.strip())
    return re.sub(r"-+", "-", text)


def markdown_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if p.is_file())


def is_index(path: Path) -> bool:
    return path.name in {"@.md", "=.md"}


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def index_kind(path: Path) -> str | None:
    if path.name == "@.md":
        return "@"
    if path.name == "=.md":
        return "="
    return None


def target_base(target: str) -> str:
    return target.split("#", 1)[0]


def is_bare_index_target(target: str) -> bool:
    if "#" in target:
        return False
    base = target_base(target)
    return base in {"@", "=", "@.md", "=.md"} or base.endswith("/@") or base.endswith("/=") or base.endswith("/@.md") or base.endswith("/=.md")


def target_index_path(source: Path, target: str) -> Path | None:
    base = target_base(target)
    if base in {"@", "@.md"}:
        return source.parent / "@.md"
    if base in {"=", "=.md"}:
        return source.parent / "=.md"
    if base.endswith("/@"):
        return (source.parent / (base + ".md")).resolve()
    if base.endswith("/@.md"):
        return (source.parent / base).resolve()
    if base.endswith("/="):
        return (source.parent / (base + ".md")).resolve()
    if base.endswith("/=.md"):
        return (source.parent / base).resolve()
    return None


def collect_index_sections(root: Path) -> dict[Path, set[str]]:
    sections: dict[Path, set[str]] = {}
    for path in markdown_files(root):
        if not is_index(path):
            continue
        kind = index_kind(path)
        found: set[str] = set()
        for line in read_text(path).splitlines():
            if kind == "@":
                m = re.match(r"^##\s+\[([^\]]+)\]\([^)]+\)", line)
                if m:
                    found.add(slug(m.group(1)))
            elif kind == "=":
                m = re.match(r"^##\s+(.+?)\s*$", line)
                if m:
                    label = LINK_RE.sub(lambda link: link.group(1), m.group(1)).strip()
                    found.add(slug(label))
        sections[path.resolve()] = found
    return sections


def repair_file(path: Path, root: Path, sections: dict[Path, set[str]]) -> tuple[bool, list[str]]:
    text = read_text(path)
    unresolved: list[str] = []

    def replace(match: re.Match[str]) -> str:
        label = match.group(1)
        target = match.group(2)
        if not is_bare_index_target(target):
            return match.group(0)

        target_path = target_index_path(path, target)
        target_slug = slug(label)
        if target_path and target_path.exists() and target_slug in sections.get(target_path.resolve(), set()):
            return f"[{label}]({target}#{target_slug})"

        unresolved.append(f"{rel(path, root)}: cannot resolve [{label}]({target})")
        return match.group(0)

    repaired = LINK_RE.sub(replace, text)
    if repaired != text:
        write_text(path, repaired)
        return True, unresolved
    return False, unresolved


def main() -> int:
    parser = argparse.ArgumentParser(description="Repair bare ReqMd index links")
    parser.add_argument("root", nargs="?", default=".", help="Requirement root to repair")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    sections = collect_index_sections(root)
    changed: list[str] = []
    unresolved: list[str] = []

    for path in markdown_files(root):
        if not is_index(path):
            continue
        did_change, did_unresolve = repair_file(path, root, sections)
        if did_change:
            changed.append(rel(path, root))
        unresolved.extend(did_unresolve)

    for item in sorted(set(changed)):
        print(f"updated {item}")
    for item in sorted(set(unresolved)):
        print(f"REVIEW: {item}")
    if not changed and not unresolved:
        print("No index link repairs needed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
