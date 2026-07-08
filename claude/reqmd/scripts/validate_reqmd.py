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
HEADING_RE = re.compile(r"^#{1,6}\s+")
FENCE_RE = re.compile(r"^\s*```(\w+)?\s*$")


class Requirement:
    def __init__(self, path: Path, req_id: str, helpers: list[str]) -> None:
        self.path = path
        self.req_id = req_id
        self.helpers = helpers


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def slug(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text.strip())
    text = re.sub(r"-+", "-", text)
    return text


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


def target_base(target: str) -> str:
    return target.split("#", 1)[0]


def is_identifier_target(target: str) -> bool:
    base = target_base(target)
    if base == "@" or base.endswith("/@"):
        return True
    if base == "@.md" or base.endswith("/@.md"):
        return "#" in target
    return False


def is_helper_target(target: str) -> bool:
    base = target_base(target)
    if base == "=" or base.endswith("/="):
        return True
    if base == "=.md" or base.endswith("/=.md"):
        return "#" in target
    return False


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
        found: set[str] = set()
        kind = index_kind(path)
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


def collect_index_links(root: Path) -> dict[Path, dict[str, set[str]]]:
    index_links: dict[Path, dict[str, set[str]]] = {}
    for path in markdown_files(root):
        if not is_index(path):
            continue
        kind = index_kind(path)
        current: str | None = None
        found: dict[str, set[str]] = {}
        for line in read_text(path).splitlines():
            if line.startswith("## "):
                current = None
                if kind == "@":
                    m = re.match(r"^##\s+\[([^\]]+)\]\([^)]+\)", line)
                    if m:
                        current = slug(m.group(1))
                elif kind == "=":
                    m = re.match(r"^##\s+(.+?)\s*$", line)
                    if m:
                        label = LINK_RE.sub(lambda link: link.group(1), m.group(1)).strip()
                        current = slug(label)
                if current:
                    found.setdefault(current, set())
                continue
            if current:
                for label, _target in iter_links(line):
                    found.setdefault(current, set()).add(label)
        index_links[path.resolve()] = found
    return index_links


def collect_source_requirements(root: Path) -> dict[Path, list[Requirement]]:
    requirements: dict[Path, list[Requirement]] = {}
    for path in markdown_files(root):
        if is_index(path):
            continue
        current: Requirement | None = None
        in_fence = False
        for line in read_text(path).splitlines():
            if FENCE_RE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            m = HEADING_LINK_RE.match(line)
            if m and is_identifier_target(m.group(3)):
                current = Requirement(path, m.group(2), [])
                requirements.setdefault(path.parent, []).append(current)
                continue
            if HEADING_RE.match(line):
                current = None
                continue
            if current:
                for label, target in iter_links(line):
                    if is_helper_target(target) and label not in current.helpers:
                        current.helpers.append(label)
    return requirements


def line_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def validate(root: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    sections = collect_index_sections(root)
    index_links = collect_index_links(root)
    source_requirements = collect_source_requirements(root)

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
            if is_identifier_target(target):
                if not ID_RE.match(name):
                    errors.append(f"ERROR: {relative}:{lineno}: invalid identifier name '{name}'")

        for match in LINK_RE.finditer(text):
            lineno = line_for_offset(text, match.start())
            if lineno in code_lines:
                continue
            label, target = match.group(1), match.group(2)
            if is_helper_target(target):
                if label.startswith("="):
                    continue
                if not HELPER_RE.match(label):
                    errors.append(f"ERROR: {relative}:{lineno}: invalid helper name '{label}'")

    validate_source_index_consistency(root, source_requirements, sections, index_links, errors)
    return errors, warnings


def validate_source_index_consistency(
    root: Path,
    source_requirements: dict[Path, list[Requirement]],
    sections: dict[Path, set[str]],
    index_links: dict[Path, dict[str, set[str]]],
    errors: list[str],
) -> None:
    for directory, requirements in source_requirements.items():
        id_index = (directory / "@.md").resolve()
        helper_index = (directory / "=.md").resolve()
        id_sections = sections.get(id_index, set())
        helper_sections = sections.get(helper_index, set())
        id_links = index_links.get(id_index, {})
        helper_links = index_links.get(helper_index, {})

        for requirement in requirements:
            req_fragment = slug(requirement.req_id)
            req_location = rel(requirement.path, root)
            if not id_index.exists():
                errors.append(
                    f"REPAIRABLE: {req_location}: missing identifier index {rel(id_index, root)}; run update_index.py"
                )
                continue
            if req_fragment not in id_sections:
                errors.append(
                    f"REPAIRABLE: {req_location}: missing @.md section for '{requirement.req_id}'; run update_index.py"
                )
                continue

            linked_from_req = id_links.get(req_fragment, set())
            for helper in requirement.helpers:
                helper_fragment = slug(helper)
                if not helper_index.exists():
                    errors.append(
                        f"REPAIRABLE: {req_location}: missing helper index {rel(helper_index, root)}; run update_index.py"
                    )
                    continue
                if helper_fragment not in helper_sections:
                    errors.append(
                        f"REPAIRABLE: {req_location}: missing =.md section for helper '{helper}'; run update_index.py"
                    )
                if helper not in linked_from_req:
                    errors.append(
                        f"REPAIRABLE: {rel(id_index, root)}: missing helper link '{helper}' in section '{requirement.req_id}'; run update_index.py"
                    )
                helper_section_links = helper_links.get(helper_fragment, set())
                if requirement.req_id not in helper_section_links:
                    errors.append(
                        f"REPAIRABLE: {rel(helper_index, root)}: missing identifier link '{requirement.req_id}' in helper section '{helper}'; run update_index.py"
                    )


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
        errors.append(f"ERROR: {relative}: index files must not contain YAML blocks")

    seen: set[str] = set()
    for lineno, line in enumerate(text.splitlines(), start=1):
        if line.startswith("## "):
            if kind == "@":
                m = re.match(r"^##\s+\[([^\]]+)\]\(([^)]+)\)\s*$", line)
                if not m:
                    errors.append(f"ERROR: {relative}:{lineno}: malformed identifier index heading link")
                    continue
                label, target = m.group(1), m.group(2)
                if "#" not in target:
                    errors.append(f"REPAIRABLE: {relative}:{lineno}: index heading link must include source document fragment; run update_index.py")
                if target.startswith("@#"):
                    errors.append(f"ERROR: {relative}:{lineno}: index heading must link to source document section")
            else:
                if re.match(r"^##\s+\[[^\]]+\]\([^)]+\)\s*$", line):
                    errors.append(f"ERROR: {relative}:{lineno}: helper index heading must not be a link")
                    continue
                m = re.match(r"^##\s+(.+?)\s*$", line)
                if not m:
                    errors.append(f"ERROR: {relative}:{lineno}: malformed helper index heading")
                    continue
                label = m.group(1).strip()
            fragment = slug(label)
            if fragment in seen:
                errors.append(f"ERROR: {relative}:{lineno}: duplicate index section '{fragment}'")
            seen.add(fragment)
            if kind == "@" and not ID_RE.match(label):
                errors.append(f"ERROR: {relative}:{lineno}: invalid identifier section '{label}'")
            if kind == "=" and not label.startswith("=") and not HELPER_RE.match(label):
                errors.append(f"ERROR: {relative}:{lineno}: invalid helper section '{label}'")

    for match in LINK_RE.finditer(text):
        lineno = line_for_offset(text, match.start())
        label, target = match.group(1), match.group(2)
        target_without_fragment = target_base(target)
        if "#" not in target and (
            target_without_fragment in {"@", "=", "@.md", "=.md"}
            or target.endswith("/@")
            or target.endswith("/=")
            or target.endswith("/@.md")
            or target.endswith("/=.md")
        ):
            errors.append(
                f"REPAIRABLE: {relative}:{lineno}: index link to '{label}' must include fragment; run repair_index_links.py"
            )
            continue
        if target.startswith("@#") or target.startswith("=#") or target.startswith("@.md#") or target.startswith("=.md#") or "/@#" in target or "/=#" in target or "/@.md#" in target or "/=.md#" in target:
            target_path = target_index_path(path, target)
            fragment = target.split("#", 1)[1]
            if target_path and target_path.exists():
                target_sections = sections.get(target_path.resolve(), set())
                if fragment not in target_sections:
                    errors.append(
                        f"REVIEW: {relative}:{lineno}: target fragment '{fragment}' not found in {rel(target_path, root)}"
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
        print(error)

    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"OK: {len(markdown_files(root))} markdown file(s) checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
