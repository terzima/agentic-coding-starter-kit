#!/usr/bin/env python3
"""Filter noisy command output for agent sessions.

Usage:
  pytest 2>&1 | scripts/agent/filter_output.py --kind test --limit 200
"""
from __future__ import annotations

import argparse
import re
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--kind", choices=["test", "log", "generic"], default="generic")
parser.add_argument("--limit", type=int, default=200, help="Maximum output lines")
args = parser.parse_args()

lines = sys.stdin.read().splitlines()
patterns = {
    "test": re.compile(r"(FAIL|FAILED|ERROR|Error|AssertionError|Traceback|panic:|failed|✗|×)", re.I),
    "log": re.compile(r"(ERROR|WARN|CRITICAL|Exception|Traceback)", re.I),
    "generic": re.compile(r"(ERROR|FAIL|WARN|Exception|Traceback)", re.I),
}
pat = patterns[args.kind]

selected: list[str] = []
for i, line in enumerate(lines):
    if pat.search(line):
        start = max(0, i - 5)
        end = min(len(lines), i + 20)
        selected.extend(lines[start:end])
        selected.append("---")

if not selected:
    selected = lines[-args.limit:]
else:
    # de-duplicate adjacent repeated context while preserving order
    out = []
    prev = None
    for line in selected:
        if line != prev:
            out.append(line)
        prev = line
    selected = out[: args.limit]

print("\n".join(selected[-args.limit:]))
print(f"\n[filter_output.py: showed {min(len(selected), args.limit)} of {len(lines)} input lines]", file=sys.stderr)
