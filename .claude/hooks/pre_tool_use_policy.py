#!/usr/bin/env python3
"""Claude Code PreToolUse policy hook example.

This file intentionally duplicates simple policy logic instead of importing from
.codex so the hook remains easy to copy into user-level Claude config.
"""
from __future__ import annotations
import json, re, sys

DENY = [
    (r"\bcurl\b.*\|\s*(sh|bash|zsh|python|python3)\b", "Remote content piped into an interpreter is blocked."),
    (r"\bwget\b.*\|\s*(sh|bash|zsh|python|python3)\b", "Remote content piped into an interpreter is blocked."),
    (r"\bsudo\b", "Privilege escalation is blocked."),
    (r"\brm\s+-rf\s+(/|~|\$HOME)(\s|$)", "Destructive removal outside the repo is blocked."),
    (r"\bchmod\s+-R\s+777\b", "Broad world-writable permissions are blocked."),
    (r"\bgit\s+push\b.*\b(main|master|prod|production)\b", "Direct push to protected branch is blocked."),
    (r"\b(cat|less|more|sed|awk|grep|rg)\b.*(\.env|id_rsa|id_ed25519|\.pem|\.p12|\.pfx)", "Reading likely secret files is blocked."),
]
ASK = [
    (r"\b(curl|wget|Invoke-WebRequest|iwr)\b", "Network fetch requires approval."),
    (r"\b(npm|pnpm|yarn|bun)\s+(install|add|update|upgrade|remove|dlx|exec)\b", "Package manager/dependency command requires approval."),
    (r"\b(npx|pip|pipx|poetry|uv|cargo|go)\s+(install|add|update|get|run|sync)\b", "Dependency/tool installation or network sync requires approval."),
    (r"\bdocker\s+(pull|build|run|compose)\b", "Docker operations require approval."),
    (r"\bgit\s+push\b", "Pushing to remote requires approval unless already approved for this task."),
]

def out(decision: str, reason: str):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": decision,
            "permissionDecisionReason": reason
        }
    }))

try:
    payload = json.loads(sys.stdin.read() or "{}")
except json.JSONDecodeError:
    payload = {}
cmd = ""
if isinstance(payload, dict):
    tool_input = payload.get("tool_input") or payload.get("toolInput") or {}
    if isinstance(tool_input, dict):
        cmd = str(tool_input.get("command") or "")
cmd_norm = " ".join(cmd.split())

for pattern, reason in DENY:
    if re.search(pattern, cmd_norm, re.I):
        out("deny", reason)
        raise SystemExit(0)
for pattern, reason in ASK:
    if re.search(pattern, cmd_norm, re.I):
        out("ask", reason + " Ask the human owner before running it.")
        raise SystemExit(0)
print("{}")
