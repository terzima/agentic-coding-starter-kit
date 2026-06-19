#!/usr/bin/env bash
set -euo pipefail

echo "== Agent finalize =="

echo "-- git status --short"
git status --short

echo "-- git diff --stat"
git diff --stat || true

echo "-- framework checks"
bash scripts/agent/run_framework_checks.sh docs/status/CURRENT_STATE.md docs/AGENTIC_WORKFLOW_MANUAL.md agent-adapters.md scripts/agent/README.md

echo "Finalize complete. Run project-specific lint/typecheck/test/build commands listed in the active plan or docs/repo-map.md."
