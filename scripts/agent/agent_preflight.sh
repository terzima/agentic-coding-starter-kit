#!/usr/bin/env bash
set -euo pipefail

echo "== Agent preflight =="

git rev-parse --is-inside-work-tree >/dev/null
branch=$(git symbolic-ref --short HEAD 2>/dev/null || echo "detached")
echo "Branch: $branch"

case "$branch" in
  main|master|prod|production|release/*)
  echo "WARNING: you are on a protected/base branch. Create a task branch or worktree before implementation." >&2
    ;;
esac

status=$(git status --short)
if [ -n "$status" ]; then
  echo "Worktree: dirty"
  echo "$status"
  echo "Start implementation only if this dirty state is intentional and understood."
else
  echo "Worktree: clean"
fi

echo "Startup docs:"
echo "- AGENTS.md"
echo "- docs/repo-map.md"
echo "- docs/status/CURRENT_STATE.md"
echo "- active spec/plan from CURRENT_STATE"
echo "Optional adapter docs:"
echo "- agent-adapters.md"
echo "- docs/AGENTIC_WORKFLOW_MANUAL.md"

missing=0
for f in AGENTS.md docs/AGENTIC_WORKFLOW_MANUAL.md docs/repo-map.md docs/status/CURRENT_STATE.md docs/specs/_template.md docs/plans/_template.md docs/change-requests/_template.md agent-adapters.md scripts/agent/README.md; do
  if [ ! -f "$f" ]; then
    echo "Missing required scaffold file: $f" >&2
    missing=1
  fi
done

if [ "$missing" -ne 0 ]; then
  exit 1
fi

echo "Preflight complete. Use Discovery for inspection, Spike for bounded evidence, and Implementation only with an accepted plan."
