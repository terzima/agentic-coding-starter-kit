#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 TASK_ID short-slug [base-branch]" >&2
  echo "Example: $0 0001 auth-login main" >&2
  exit 2
fi

TASK_ID="$1"
SLUG="$2"
BASE_BRANCH="${3:-main}"

repo_root=$(git rev-parse --show-toplevel)
repo_name=$(basename "$repo_root")
parent_dir=$(dirname "$repo_root")
worktree_root="$parent_dir/${repo_name}-worktrees"
branch="agent/${TASK_ID}-${SLUG}"
worktree_path="$worktree_root/${TASK_ID}-${SLUG}"

mkdir -p "$worktree_root"

if git show-ref --verify --quiet "refs/heads/$branch"; then
  echo "Branch already exists: $branch" >&2
  exit 1
fi

if [ -e "$worktree_path" ]; then
  echo "Worktree path already exists: $worktree_path" >&2
  exit 1
fi

git worktree add -b "$branch" "$worktree_path" "$BASE_BRANCH"

echo "Created worktree: $worktree_path"
echo "Branch: $branch"
echo "Next: cd '$worktree_path' && scripts/agent/agent_preflight.sh"
