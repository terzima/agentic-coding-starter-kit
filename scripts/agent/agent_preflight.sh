#!/usr/bin/env bash
set -euo pipefail

echo "== Agent preflight =="

git rev-parse --is-inside-work-tree >/dev/null
branch=$(git symbolic-ref --short HEAD 2>/dev/null || echo "detached")
echo "Branch: $branch"

if [ "$branch" = "main" ] || [ "$branch" = "master" ] || [ "$branch" = "prod" ] || [ "$branch" = "production" ]; then
  echo "WARNING: you are on a protected/base branch. Create a task branch or worktree before implementation." >&2
fi

status=$(git status --short)
if [ -n "$status" ]; then
  echo "Working tree is not clean:" >&2
  echo "$status" >&2
  echo "Start implementation only if this dirty state is intentional and understood." >&2
else
  echo "Working tree clean."
fi

missing=0
for f in AGENTS.md docs/repo-map.md docs/specs/_template.md docs/plans/_template.md docs/change-requests/_template.md; do
  if [ ! -f "$f" ]; then
    echo "Missing required scaffold file: $f" >&2
    missing=1
  fi
done

if [ "$missing" -ne 0 ]; then
  exit 1
fi

echo "Preflight complete."
