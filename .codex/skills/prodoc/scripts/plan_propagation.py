#!/usr/bin/env python3
"""Plan ProDoc propagation Queue items without external YAML dependencies."""

from __future__ import annotations

import argparse
import hashlib
import sys
from collections import deque
from dataclasses import dataclass
from pathlib import Path


class ProDocError(Exception):
    pass


@dataclass(frozen=True)
class QueueItem:
    target: Path
    source: Path | None
    direction: str
    input_sections: tuple[str, ...]
    change_summary: str

    def key(self, root: Path) -> str:
        digest = hashlib.sha1(self.change_summary.encode("utf-8")).hexdigest()[:12]
        source = rel(self.source, root) if self.source else "-"
        sections = ",".join(self.input_sections) if self.input_sections else "-"
        return "|".join([rel(self.target, root), source, self.direction, sections, digest])


def rel(path: Path | None, root: Path) -> str:
    if path is None:
        return "-"
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def extract_frontmatter(path: Path) -> list[str] | None:
    try:
        lines = path.read_text(encoding="utf-8-sig").splitlines()
    except OSError as exc:
        raise ProDocError(f"cannot read {path}: {exc}") from exc
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            frontmatter = lines[1:i]
            if any(line.strip() == "reqmd_prodoc:" for line in frontmatter):
                return frontmatter
            return None
    raise ProDocError(f"{path}: unterminated YAML frontmatter")


def parse_propagation_docs(lines: list[str]) -> dict[str, list[str]]:
    docs: dict[str, list[str]] = {}
    in_prodoc = False
    in_prop = False
    direction: str | None = None

    for raw in lines:
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        text = raw.strip()

        if indent == 0:
            in_prodoc = text == "reqmd_prodoc:"
            in_prop = False
            direction = None
            continue
        if not in_prodoc:
            continue
        if indent == 2:
            in_prop = text == "propagation_docs:"
            direction = None
            continue
        if in_prop and indent == 4 and text.endswith(":"):
            direction = text[:-1]
            if direction not in {"lateral", "upstream", "downstream"}:
                raise ProDocError(f"unsupported propagation direction: {direction}")
            docs.setdefault(direction, [])
            continue
        if in_prop and indent == 6 and text.startswith("- "):
            if direction is None:
                raise ProDocError("propagation target without direction")
            docs.setdefault(direction, []).append(text[2:].strip())
            continue

    return docs


def is_prodoc(path: Path) -> bool:
    return path.exists() and path.is_file() and extract_frontmatter(path) is not None


def child_items(item: QueueItem, root: Path, summary: str) -> tuple[list[QueueItem], list[str]]:
    reviews: list[str] = []
    lines = extract_frontmatter(item.target)
    if lines is None:
        reviews.append(f"REVIEW: {rel(item.target, root)} is not a ProDoc document")
        return [], reviews

    try:
        propagation_docs = parse_propagation_docs(lines)
    except ProDocError as exc:
        reviews.append(f"REVIEW: {rel(item.target, root)}: {exc}")
        return [], reviews

    children: list[QueueItem] = []
    for direction, targets in propagation_docs.items():
        for target_ref in targets:
            target = (item.target.parent / target_ref).resolve()
            if not target.exists():
                reviews.append(f"REVIEW: {rel(item.target, root)}: missing {direction} target {target_ref}")
                continue
            if not is_prodoc(target):
                reviews.append(f"REVIEW: {rel(target, root)} is not a ProDoc document")
                continue
            children.append(
                QueueItem(
                    target=target,
                    source=item.target,
                    direction=direction,
                    input_sections=item.input_sections,
                    change_summary=summary,
                )
            )
    return children, reviews


def plan(root: Path, start: Path, input_sections: tuple[str, ...], summary: str, max_depth: int) -> tuple[list[tuple[int, QueueItem]], list[str]]:
    root = root.resolve()
    start = start.resolve()
    queue = deque([(0, QueueItem(start, None, "self", input_sections, summary), (start,))])
    processed: set[str] = set()
    result: list[tuple[int, QueueItem]] = []
    reviews: list[str] = []

    while queue:
        depth, item, path_stack = queue.popleft()
        key = item.key(root)
        if key in processed:
            reviews.append(f"REVIEW: repeated Queue item skipped: {key}")
            continue
        processed.add(key)
        result.append((depth, item))

        if depth >= max_depth:
            reviews.append(f"REVIEW: max depth reached at {rel(item.target, root)}")
            continue

        children, child_reviews = child_items(item, root, summary)
        reviews.extend(child_reviews)
        for child in children:
            if child.target in path_stack:
                cycle = " -> ".join(rel(p, root) for p in (*path_stack, child.target))
                reviews.append(f"REVIEW: cycle skipped: {cycle}")
                continue
            queue.append((depth + 1, child, (*path_stack, child.target)))

    return result, reviews


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Plan ProDoc propagation Queue items")
    parser.add_argument("root", help="Project or document root used for relative output")
    parser.add_argument("start", help="Starting ProDoc document")
    parser.add_argument("--input-section", action="append", default=[], help="Changed input RequirementSection ID")
    parser.add_argument("--summary", default="unspecified change", help="One-line change summary")
    parser.add_argument("--max-depth", type=int, default=1, help="Maximum propagation depth")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    start = (Path(args.start) if Path(args.start).is_absolute() else root / args.start).resolve()
    if not start.exists():
        print(f"ERROR: start document does not exist: {start}", file=sys.stderr)
        return 2
    if not is_prodoc(start):
        print(f"ERROR: start document is not ProDoc: {start}", file=sys.stderr)
        return 2

    planned, reviews = plan(root, start, tuple(args.input_section), args.summary, args.max_depth)
    print("QUEUE:")
    for depth, item in planned:
        print(f"- depth: {depth}")
        print(f"  target: {rel(item.target, root)}")
        print(f"  source: {rel(item.source, root)}")
        print(f"  direction: {item.direction}")
        print(f"  input_sections: {', '.join(item.input_sections) if item.input_sections else '-'}")
        print(f"  change_summary: {item.change_summary}")
        print(f"  key: {item.key(root)}")
    if reviews:
        print("REVIEW:")
        for review in sorted(set(reviews)):
            print(f"- {review}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
