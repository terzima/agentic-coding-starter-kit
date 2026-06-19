#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(git rev-parse --show-toplevel)"
cd "$ROOT_DIR"

docs=("$@")
if [ "${#docs[@]}" -eq 0 ]; then
  docs=(
    README.md
    agentic-workflow-manual.md
    agent-adapters.md
    scripts/agent/README.md
    docs/specs/_template.md
    docs/plans/_template.md
    docs/plans/batches/_template.md
    docs/change-requests/_template.md
    docs/status/_template.md
    docs/handoff/_template.md
    docs/worklog/_template.md
  )
fi

echo "== planning docs =="
python3 .agents/skills/controlled-planning-docs/scripts/check_planning_doc.py "${docs[@]}"

echo "== shell syntax =="
bash -n scripts/agent/*.sh .githooks/*

echo "== python syntax =="
export PYTHONPYCACHEPREFIX="${PYTHONPYCACHEPREFIX:-${TMPDIR:-/tmp}/agentic-framework-pycache}"
python3 -m py_compile scripts/agent/*.py .codex/hooks/*.py .claude/hooks/*.py

echo "== framework policy =="
python3 scripts/agent/test_framework_policy.py

echo "== whitespace =="
git diff --check
