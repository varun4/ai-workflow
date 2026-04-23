#!/usr/bin/env python3
"""Detect duplicated normative lines across context policy files.

This check helps keep workflow context compact by enforcing
"reference, do not restate" for policy text.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

DEFAULT_FILES = [
    "PROJECT_CONTEXT_ARCHITECTURE.md",
    "SPEC.md",
    "APPROVAL_BOUNDARIES.md",
    "EVAL_CHECKLIST.md",
    "SKILL_EVIDENCE_REVIEW.md",
    "docs/standards/MODULE_DONE_CHECKLIST_TEMPLATE.md",
]

MIN_WORDS = 8
MIN_CHARS = 45

# Normalized lines that are intentionally shared across files.
ALLOWLIST = {
    "learning objectives are measurable and action-oriented.",
    "do not approve vague quality language without criteria.",
}


@dataclass(frozen=True)
class Occurrence:
    path: Path
    line_number: int
    original: str


def normalize_line(text: str) -> str:
    normalized = text.strip().lower()
    normalized = re.sub(r"^[-*]\s+", "", normalized)
    normalized = re.sub(r"^\d+\.\s+", "", normalized)
    normalized = re.sub(r"^-\s*\[.?\]\s+", "", normalized)
    normalized = re.sub(r"`", "", normalized)
    normalized = re.sub(r"\s+", " ", normalized)
    return normalized


def line_is_candidate(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    if stripped.startswith("#"):
        return False
    if stripped.startswith("```") or stripped.startswith("~~~"):
        return False
    if stripped.startswith("|"):
        return False

    normalized = normalize_line(stripped)
    if len(normalized) < MIN_CHARS:
        return False
    if len(normalized.split()) < MIN_WORDS:
        return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check duplicated policy lines across context files."
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root path (default: current directory).",
    )
    parser.add_argument(
        "--files",
        nargs="*",
        default=DEFAULT_FILES,
        help="Relative file paths to check.",
    )
    args = parser.parse_args()

    repo_root = Path(args.root).resolve()
    files = [repo_root / rel for rel in args.files]

    missing = [p for p in files if not p.exists()]
    if missing:
        for path in missing:
            print(f"ERROR: missing file: {path}")
        return 2

    seen: dict[str, list[Occurrence]] = defaultdict(list)

    for file_path in files:
        lines = file_path.read_text(encoding="utf-8").splitlines()
        for line_number, line in enumerate(lines, start=1):
            if not line_is_candidate(line):
                continue
            normalized = normalize_line(line)
            if normalized in ALLOWLIST:
                continue
            seen[normalized].append(Occurrence(file_path, line_number, line.strip()))

    duplicates = {
        line: occs
        for line, occs in seen.items()
        if len({occ.path for occ in occs}) > 1
    }

    if duplicates:
        print("Context duplication check failed:\n")
        for normalized, occs in sorted(duplicates.items()):
            print(f"- Duplicate line: {normalized}")
            for occ in occs:
                rel = occ.path.relative_to(repo_root)
                print(f"  - {rel}:{occ.line_number}: {occ.original}")
            print()
        print(f"Result: FAIL ({len(duplicates)} duplicated line(s))")
        return 1

    print("Result: PASS (no duplicated policy lines detected)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
