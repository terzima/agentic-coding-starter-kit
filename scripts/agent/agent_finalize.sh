#!/usr/bin/env bash
set -euo pipefail

echo "== Agent finalize =="

echo "-- git status --short"
git status --short

echo "-- git diff --stat"
git diff --stat || true

echo "-- syntax check helper scripts"
bash -n scripts/agent/*.sh .githooks/*
python3 -m py_compile scripts/agent/*.py .codex/hooks/*.py

echo "Finalize complete. Run project-specific lint/typecheck/test/build commands listed in docs/repo-map.md."
