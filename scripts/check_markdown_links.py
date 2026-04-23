#!/usr/bin/env python3
"""Validate local Markdown links and heading anchors.

This checker is repository-local and deterministic:
- checks relative file and directory links
- checks same-file and cross-file heading anchors for `.md` targets
- skips external URLs (`http`, `https`, `mailto`, `tel`)

Usage:
    python3 scripts/check_markdown_links.py .
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote

INLINE_LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.*)$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
TRAILING_HEADING_HASHES_RE = re.compile(r"\s+#+\s*$")

SKIP_SCHEMES = ("http://", "https://", "mailto:", "tel:")
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__"}


@dataclass
class LinkIssue:
    file_path: Path
    line_number: int
    target: str
    reason: str


def normalize_anchor(text: str) -> str:
    """Normalize heading text to a GitHub-style anchor slug."""
    text = unquote(text).strip().lower()
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = text.replace("_", "-")
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def clean_link_target(raw_target: str) -> str:
    """Extract the destination path from a markdown link target."""
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        return target[1 : target.index(">")].strip()

    # For standard markdown links, the URL is the first token.
    # This matches repository usage where paths do not contain spaces.
    return target.split()[0].strip()


def markdown_files(root: Path) -> Iterable[Path]:
    for file_path in sorted(root.rglob("*.md")):
        if any(part in SKIP_DIRS for part in file_path.parts):
            continue
        yield file_path


def anchors_for_markdown(markdown_path: Path) -> set[str]:
    anchors: set[str] = set()
    duplicate_counts: dict[str, int] = defaultdict(int)

    try:
        lines = markdown_path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        return anchors

    in_fence = False
    for line in lines:
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        match = HEADING_RE.match(line)
        if not match:
            continue

        heading_text = TRAILING_HEADING_HASHES_RE.sub("", match.group(1)).strip()
        if not heading_text:
            continue

        base_slug = normalize_anchor(heading_text)
        if not base_slug:
            continue

        count = duplicate_counts[base_slug]
        slug = base_slug if count == 0 else f"{base_slug}-{count}"
        duplicate_counts[base_slug] += 1
        anchors.add(slug)

    return anchors


def resolve_target_path(
    current_file: Path, repo_root: Path, path_fragment: str
) -> Path:
    target_path = unquote(path_fragment)
    if target_path.startswith("/"):
        return (repo_root / target_path.lstrip("/")).resolve()
    return (current_file.parent / target_path).resolve()


def collect_issues(file_path: Path, repo_root: Path) -> tuple[list[LinkIssue], int]:
    issues: list[LinkIssue] = []
    links_checked = 0

    try:
        lines = file_path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        issues.append(
            LinkIssue(file_path, 1, str(file_path), "file is not valid UTF-8")
        )
        return issues, links_checked

    in_fence = False
    anchor_cache: dict[Path, set[str]] = {}

    for line_number, line in enumerate(lines, start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        for match in INLINE_LINK_RE.finditer(line):
            target = clean_link_target(match.group(2))
            if not target:
                continue

            links_checked += 1
            lowered = target.lower()
            if lowered.startswith(SKIP_SCHEMES):
                continue

            path_part, anchor_part = (target.split("#", 1) + [""])[:2]
            if target.startswith("#"):
                path_part = ""
                anchor_part = target[1:]

            if not path_part and not anchor_part:
                issues.append(
                    LinkIssue(file_path, line_number, target, "empty local link")
                )
                continue

            resolved_target = (
                file_path.resolve()
                if not path_part
                else resolve_target_path(file_path, repo_root, path_part)
            )

            if not resolved_target.exists():
                issues.append(
                    LinkIssue(
                        file_path,
                        line_number,
                        target,
                        f"target path does not exist: {resolved_target}",
                    )
                )
                continue

            if not anchor_part:
                continue

            if resolved_target.suffix.lower() != ".md":
                continue

            normalized_anchor = normalize_anchor(anchor_part)
            if not normalized_anchor:
                issues.append(
                    LinkIssue(file_path, line_number, target, "empty anchor")
                )
                continue

            if resolved_target not in anchor_cache:
                anchor_cache[resolved_target] = anchors_for_markdown(
                    resolved_target
                )

            if normalized_anchor not in anchor_cache[resolved_target]:
                issues.append(
                    LinkIssue(
                        file_path,
                        line_number,
                        target,
                        f"anchor not found in {resolved_target}",
                    )
                )

    return issues, links_checked


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check local markdown links and anchors."
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Repository root to scan (default: current directory).",
    )
    args = parser.parse_args()

    repo_root = Path(args.root).resolve()
    if not repo_root.exists() or not repo_root.is_dir():
        print(f"ERROR: root path does not exist or is not a directory: {repo_root}")
        return 2

    all_issues: list[LinkIssue] = []
    total_files = 0
    total_links = 0

    for md_file in markdown_files(repo_root):
        total_files += 1
        issues, links_checked = collect_issues(md_file, repo_root)
        total_links += links_checked
        all_issues.extend(issues)

    if all_issues:
        print("Markdown link check failed:\n")
        for issue in all_issues:
            rel_path = issue.file_path.resolve().relative_to(repo_root)
            print(
                f"- {rel_path}:{issue.line_number}: "
                f"`{issue.target}` -> {issue.reason}"
            )
        print(
            f"\nResult: FAIL ({len(all_issues)} issue(s), "
            f"{total_links} link(s) checked across {total_files} file(s))"
        )
        return 1

    print(
        f"Result: PASS ({total_links} link(s) checked "
        f"across {total_files} file(s))"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
