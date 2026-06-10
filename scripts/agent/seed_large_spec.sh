#!/usr/bin/env bash
set -euo pipefail

raw="docs/intake/PROJECT_OVERVIEW_RAW.md"
prompt="docs/intake/SEEDING_PROMPT.md"

if [ ! -f "$raw" ]; then
  echo "Missing $raw" >&2
  exit 1
fi

if grep -q "Paste the large project overview here" "$raw"; then
  echo "Raw overview still appears to be empty. Paste your project overview into $raw first." >&2
  exit 1
fi

cat <<MSG
Large spec is ready for seeding.

Open your coding agent and paste the prompt from:
  $prompt

Do not start implementation until generated seed docs are reviewed and accepted.
MSG
