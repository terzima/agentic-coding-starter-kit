#!/usr/bin/env bash
set -euo pipefail

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Not inside a git repository." >&2
  exit 1
fi

git config core.hooksPath .githooks
chmod +x .githooks/*
echo "Installed local Git hooks from .githooks"
