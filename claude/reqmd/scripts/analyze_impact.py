#!/usr/bin/env python3
"""Report ReqMd impact links from existing index files only."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def slug(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text.strip())
    return re.sub(r"-+", "-", text)


def markdown_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if p.is_file())


def is_index(path: Path) -> bool:
    return path.name in {"@.md", "=.md"}


def index_kind(path: Path) -> str | None:
    if path.name == "@.md":
        return "@"
    if path.name == "=.md":
        return "="
    return None


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def iter_index_sections(path: Path):
    kind = index_kind(path)
    current_label: str | None = None
    current_slug: str | None = None
    links: list[tuple[str, str]] = []

    for line in read_text(path).splitlines():
        if line.startswith("## "):
            if current_label is not None and current_slug is not None:
                yield current_label, current_slug, links
            links = []
            current_label = None
            current_slug = None
            if kind == "@":
                m = re.match(r"^##\s+\[([^\]]+)\]\([^)]+\)", line)
                if m:
                    current_label = m.group(1)
                    current_slug = slug(current_label)
            elif kind == "=":
                m = re.match(r"^##\s+(.+?)\s*$", line)
                if m:
                    label = LINK_RE.sub(lambda link: link.group(1), m.group(1)).strip()
                    current_label = label
                    current_slug = slug(label)
            continue
        if current_label is not None:
            for match in LINK_RE.finditer(line):
                links.append((match.group(1), match.group(2)))

    if current_label is not None and current_slug is not None:
        yield current_label, current_slug, links


def collect_indexes(root: Path):
    sections = []
    for path in markdown_files(root):
        if not is_index(path):
            continue
        for label, section_slug, links in iter_index_sections(path):
            sections.append(
                {
                    "path": path,
                    "kind": index_kind(path),
                    "label": label,
                    "slug": section_slug,
                    "links": links,
                }
            )
    return sections


def matches(section, terms: set[str]) -> bool:
    labels = {section["label"], section["slug"]}
    return any(term in labels for term in terms)


def link_matches(links: list[tuple[str, str]], terms: set[str]) -> bool:
    for label, target in links:
        target_fragment = target.split("#", 1)[1] if "#" in target else ""
        if label in terms or slug(label) in terms or target_fragment in terms:
            return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze ReqMd impact from indexes")
    parser.add_argument("root", help="Requirement root to scan")
    parser.add_argument("terms", nargs="+", help="Identifiers or helpers to analyze")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    terms = set(args.terms)
    terms.update(slug(term) for term in args.terms)

    sections = collect_indexes(root)
    direct = [section for section in sections if matches(section, terms)]
    reverse = [section for section in sections if not matches(section, terms) and link_matches(section["links"], terms)]

    print("confirmed:")
    for section in direct:
        print(f"- {section['label']} ({rel(section['path'], root)}#{section['slug']})")
        for label, target in section["links"]:
            print(f"  - {label} -> {target}")

    print("inferred:")
    for section in reverse:
        print(f"- {section['label']} ({rel(section['path'], root)}#{section['slug']})")

    print("review needed:")
    print("- Semantic impact beyond indexed links was not inferred by this script.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
