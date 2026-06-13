#!/usr/bin/env python3
"""Validate ReqMd requirement documents and indexes."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ID_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")
HELPER_RE = re.compile(r"^[a-z][a-z0-9_]*$")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING_LINK_RE = re.compile(r"^(#{1,6})\s+\[([^\]]+)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FENCE_RE = re.compile(r"^\s*```(\w+)?\s*$")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def markdown_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if p.is_file())


def is_index(path: Path) -> bool:
    return path.name in {"@.md", "=.md"}


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def iter_links(text: str):
    for match in LINK_RE.finditer(text):
        yield match.group(1), match.group(2)


def in_code_block_lines(text: str) -> set[int]:
    in_fence = False
    lines: set[int] = set()
    for idx, line in enumerate(text.splitlines(), start=1):
        if FENCE_RE.match(line):
            lines.add(idx)
            in_fence = not in_fence
            continue
        if in_fence:
            lines.add(idx)
    return lines


def index_kind(path: Path) -> str | None:
    if path.name == "@.md":
        return "@"
    if path.name == "=.md":
        return "="
    return None


def target_index_path(source: Path, target: str) -> Path | None:
    base = target.split("#", 1)[0]
    if base == "@":
        return source.parent / "@.md"
    if base == "=":
        return source.parent / "=.md"
    if base.endswith("/@"):
        return (source.parent / (base + ".md")).resolve()
    if base.endswith("/="):
        return (source.parent / (base + ".md")).resolve()
    return None


def collect_index_sections(root: Path) -> dict[Path, set[str]]:
    sections: dict[Path, set[str]] = {}
    for path in markdown_files(root):
        if not is_index(path):
            continue
        kind = index_kind(path)
        found: set[str] = set()
        for line in read_text(path).splitlines():
            m = re.match(rf"^##\s+\[([^\]]+)\]\({re.escape(kind)}#([^)]+)\)", line)
            if m:
                found.add(m.group(2))
        sections[path.resolve()] = found
    return sections


def line_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def validate(root: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    sections = collect_index_sections(root)

    for path in markdown_files(root):
        text = read_text(path)
        relative = rel(path, root)
        code_lines = in_code_block_lines(text)

        if is_index(path):
            validate_index_file(path, root, text, sections, errors)
            continue

        for lineno, line in enumerate(text.splitlines(), start=1):
            m = HEADING_LINK_RE.match(line)
            if not m:
                continue
            name, target = m.group(2), m.group(3)
            if target == "@" or target.endswith("/@") or target.startswith("@#"):
                if not ID_RE.match(name):
                    errors.append(f"{relative}:{lineno}: invalid identifier name '{name}'")

        for match in LINK_RE.finditer(text):
            lineno = line_for_offset(text, match.start())
            if lineno in code_lines:
                continue
            label, target = match.group(1), match.group(2)
            if target == "=" or target.endswith("/=") or target.startswith("=#"):
                if label.startswith("="):
                    continue
                if not HELPER_RE.match(label):
                    errors.append(f"{relative}:{lineno}: invalid helper name '{label}'")

    return errors, warnings


def validate_index_file(
    path: Path,
    root: Path,
    text: str,
    sections: dict[Path, set[str]],
    errors: list[str],
) -> None:
    kind = index_kind(path)
    assert kind is not None
    relative = rel(path, root)

    if re.search(r"^```yaml\s*$", text, flags=re.MULTILINE):
        errors.append(f"{relative}: index files must not contain YAML blocks")

    seen: set[str] = set()
    for lineno, line in enumerate(text.splitlines(), start=1):
        if line.startswith("## "):
            m = re.match(rf"^##\s+\[([^\]]+)\]\({re.escape(kind)}#([^)]+)\)\s*$", line)
            if not m:
                errors.append(f"{relative}:{lineno}: index heading must use {kind}#fragment")
                continue
            label, fragment = m.group(1), m.group(2)
            if label != fragment:
                errors.append(f"{relative}:{lineno}: heading label and fragment differ")
            if fragment in seen:
                errors.append(f"{relative}:{lineno}: duplicate index section '{fragment}'")
            seen.add(fragment)
            if kind == "@" and not ID_RE.match(label):
                errors.append(f"{relative}:{lineno}: invalid identifier section '{label}'")
            if kind == "=" and not label.startswith("=") and not HELPER_RE.match(label):
                errors.append(f"{relative}:{lineno}: invalid helper section '{label}'")

    for match in LINK_RE.finditer(text):
        lineno = line_for_offset(text, match.start())
        label, target = match.group(1), match.group(2)
        if target in {"@", "="} or target.endswith("/@") or target.endswith("/="):
            errors.append(f"{relative}:{lineno}: index link to '{label}' must include fragment")
            continue
        if target.startswith("@#") or target.startswith("=#") or "/@#" in target or "/=#" in target:
            target_path = target_index_path(path, target)
            fragment = target.split("#", 1)[1]
            if target_path and target_path.exists():
                target_sections = sections.get(target_path.resolve(), set())
                if fragment not in target_sections:
                    errors.append(
                        f"{relative}:{lineno}: target fragment '{fragment}' not found in {rel(target_path, root)}"
                    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate ReqMd documents")
    parser.add_argument("root", nargs="?", default=".", help="Requirement root to validate")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        print(f"ERROR: root does not exist: {root}", file=sys.stderr)
        return 2

    errors, warnings = validate(root)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"OK: {len(markdown_files(root))} markdown file(s) checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
