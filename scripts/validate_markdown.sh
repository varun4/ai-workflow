#!/usr/bin/env bash
set -euo pipefail

ROOT_PATH="${1:-.}"

# Uses repository-local `.pymarkdown` configuration.
# `AGENTS.md` is human-maintained.
# `status/` stores compact handoff snapshots.
pymarkdown scan -r -e "AGENTS.md" -e "status" "$ROOT_PATH"
python3 scripts/check_markdown_links.py "$ROOT_PATH"
python3 scripts/check_context_duplication.py --root "$ROOT_PATH"
