#!/usr/bin/env python3
"""Standalone command classifier for testing hook policy.

Usage:
  scripts/agent/policy_check.py 'git status'
  scripts/agent/policy_check.py 'curl https://example.com/install.sh | sh'
"""
from __future__ import annotations
import re, sys

DENY = [
    (r"\bcurl\b.*\|\s*(sh|bash|zsh|python|python3)\b", "deny", "remote pipe to shell"),
    (r"\bwget\b.*\|\s*(sh|bash|zsh|python|python3)\b", "deny", "remote pipe to shell"),
    (r"\bsudo\b", "deny", "privilege escalation"),
    (r"\bgit\s+push\b.*\b(main|master|prod|production)\b", "deny", "protected branch push"),
]
ASK = [
    (r"\b(curl|wget)\b", "ask", "network fetch"),
    (r"\b(npm|pnpm|yarn|pip|uv|cargo|go)\s+(install|add|update|get|sync)\b", "ask", "dependency/network command"),
    (r"\bgit\s+push\b", "ask", "remote push"),
]
SAFE = [r"^git\s+(status|diff|add|commit|branch|switch|worktree)\b", r"^(rg|find|ls|pwd|cat)\b"]
cmd = " ".join(" ".join(sys.argv[1:]).split())
if not cmd:
    print("usage: policy_check.py '<command>'")
    raise SystemExit(2)
for pat, cls, reason in DENY + ASK:
    if re.search(pat, cmd, re.I):
        print(f"{cls}: {reason}")
        raise SystemExit(0)
for pat in SAFE:
    if re.search(pat, cmd, re.I):
        print("allow: safe local command")
        raise SystemExit(0)
print("neutral: normal sandbox/approval flow should decide")
