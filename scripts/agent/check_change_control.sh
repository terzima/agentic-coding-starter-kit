#!/usr/bin/env bash
set -euo pipefail

base_ref="${BASE_REF:-}"
if [ -n "$base_ref" ] && git rev-parse --verify "origin/$base_ref" >/dev/null 2>&1; then
  base="origin/$base_ref"
elif git rev-parse --verify origin/main >/dev/null 2>&1; then
  base="origin/main"
elif git rev-parse --verify origin/master >/dev/null 2>&1; then
  base="origin/master"
else
  echo "No origin base branch found; running local-only policy checks."
  base=""
fi

if [ -n "$base" ]; then
  changed=$(git diff --name-only "$base"...HEAD)
else
  changed=$(git ls-files)
fi

fail=0

echo "Checking for likely secrets and unsafe files..."
if echo "$changed" | grep -E '(^|/)\.env(\.|$)|\.pem$|\.key$|id_rsa|id_ed25519' >/dev/null; then
  echo "Policy failure: likely secret file included." >&2
  fail=1
fi

if git diff ${base:+"$base"...HEAD} -- . ':!*.lock' | grep -E '(AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9_]{36,}|BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY)' >/dev/null; then
  echo "Policy failure: possible secret detected in diff." >&2
  fail=1
fi

if echo "$changed" | grep -E '(^|/)(src|app|lib|packages|services|tests)/' >/dev/null; then
  if ! echo "$changed" | grep -E '^docs/(specs|plans)/' >/dev/null; then
    echo "Policy warning: code/test changes without spec/plan changes in this PR." >&2
    echo "If the spec/plan already existed before this branch, this warning is informational." >&2
  fi
fi

if [ "$fail" -ne 0 ]; then
  exit 1
fi

echo "Change-control checks passed."
