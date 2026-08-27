#!/usr/bin/env python3
"""Convert each chapter's plain numbered "## Problems" list into MyST
{exercise}/{solution} directives (https://mystmd.org/guide/exercises).

Each numbered problem becomes a labeled {exercise} directive; an empty,
dropdown {solution} directive linked to it is inserted immediately after,
ready for solutions to be filled in later. Pre-existing explicit anchors
(e.g. "(ex-relativistic-dynamics-3)=") used for cross-references elsewhere
in the book are preserved as the exercise's label so existing links keep
resolving.

Usage: python3 scripts/convert_exercises.py [--check] chapters/*.md
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

LABEL_RE = re.compile(r"^\(([a-z0-9-]+)\)=$")
ITEM_RE = re.compile(r"^(\d+)\.\s+(.*)$")
CHAPTER_LABEL_RE = re.compile(r"^label:\s*ch-(\S+)\s*$", re.MULTILINE)
PROBLEMS_HEADING_RE = re.compile(r"^## Problems\s*$", re.MULTILINE)


def slug_for(text: str, path: Path) -> str:
    match = CHAPTER_LABEL_RE.search(text)
    if not match:
        raise ValueError(f"{path}: no 'label: ch-<slug>' found in frontmatter")
    return match.group(1)


def split_blocks(body: str) -> list[str]:
    """Split the problems region into blank-line-separated blocks."""
    return [b for b in re.split(r"\n\s*\n", body.strip("\n")) if b.strip()]


def convert_block(block: str, slug: str, n: int) -> tuple[str, int]:
    lines = block.splitlines()
    explicit_label = None
    if len(lines) == 2 and LABEL_RE.match(lines[0]):
        explicit_label = LABEL_RE.match(lines[0]).group(1)
        item_line = lines[1]
    elif len(lines) == 1:
        item_line = lines[0]
    else:
        raise ValueError(f"Unexpected block shape ({len(lines)} lines): {block!r}")

    match = ITEM_RE.match(item_line)
    if not match:
        raise ValueError(f"Line does not look like a numbered item: {item_line!r}")
    number, text = int(match.group(1)), match.group(2)
    if number != n:
        raise ValueError(f"Expected item {n}, found item {number}: {item_line!r}")

    label = explicit_label or f"ex-{slug}-{number}"
    sol_label = f"sol-{slug}-{number}"

    exercise = f":::{{exercise}}\n:label: {label}\n\n{text}\n:::"
    solution = (
        f":::{{solution}} {label}\n:label: {sol_label}\n:class: dropdown\n\n"
        f"_Solution not yet written._\n:::"
    )
    return f"{exercise}\n\n{solution}", number


def convert_file(path: Path) -> bool:
    """Return True if the file was changed."""
    text = path.read_text()
    slug = slug_for(text, path)

    heading_match = PROBLEMS_HEADING_RE.search(text)
    if not heading_match:
        raise ValueError(f"{path}: no '## Problems' heading found")

    head = text[: heading_match.end()]
    body = text[heading_match.end() :]

    # Already converted? Skip idempotently.
    if re.search(r"^:::\{exercise\}", body, re.MULTILINE):
        return False

    blocks = split_blocks(body)
    converted = []
    for i, block in enumerate(blocks, start=1):
        directive_text, _ = convert_block(block, slug, i)
        converted.append(directive_text)

    new_text = head.rstrip("\n") + "\n\n" + "\n\n".join(converted) + "\n"
    if new_text != text:
        path.write_text(new_text)
        return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument(
        "--check", action="store_true", help="Report what would change; do not write."
    )
    args = parser.parse_args()

    changed_any = False
    for path in args.files:
        try:
            if args.check:
                text = path.read_text()
                slug = slug_for(text, path)
                heading_match = PROBLEMS_HEADING_RE.search(text)
                if not heading_match:
                    print(f"SKIP  {path}: no '## Problems' heading")
                    continue
                body = text[heading_match.end() :]
                if re.search(r"^:::\{exercise\}", body, re.MULTILINE):
                    print(f"DONE  {path}")
                    continue
                blocks = split_blocks(body)
                for i, block in enumerate(blocks, start=1):
                    convert_block(block, slug, i)  # raises on problems
                print(f"OK    {path}: {len(blocks)} problems would convert")
            else:
                changed = convert_file(path)
                changed_any = changed_any or changed
                print(f"{'WROTE' if changed else 'SKIP '} {path}")
        except ValueError as exc:
            print(f"ERROR {path}: {exc}", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
