#!/usr/bin/env python3
"""Shared command policy helpers for agent hooks.

This is defense-in-depth, not a complete sandbox. The real boundary should come
from the agent sandbox, devcontainer/OS permissions, and GitHub PR protections.
"""
from __future__ import annotations

import json
import os
import re
import shlex
import sys
from dataclasses import dataclass
from typing import Any, Optional


DENY_PATTERNS = [
    (r"\bcurl\b.*\|\s*(sh|bash|zsh|python|python3|ruby|perl)\b", "Remote content piped into an interpreter is blocked."),
    (r"\bwget\b.*\|\s*(sh|bash|zsh|python|python3|ruby|perl)\b", "Remote content piped into an interpreter is blocked."),
    (r"\bsudo\b", "Privilege escalation is blocked."),
    (r"\brm\s+-rf\s+(/|~|\$HOME)(\s|$)", "Destructive removal outside the repo is blocked."),
    (r"\bchmod\s+-R\s+777\b", "Broad world-writable permissions are blocked."),
    (r"\bchown\s+-R\b", "Recursive ownership changes are blocked."),
    (r"\bmkfs\b|\bdiskutil\b|\bdd\s+if=", "Disk-level commands are blocked."),
    (r"\blaunchctl\b|\bcrontab\b", "Persistence/system scheduler changes are blocked."),
    (r"\bgit\s+push\b.*\b(main|master|prod|production)\b", "Direct push to protected branch is blocked."),
    (r"\bgit\s+push\b.*\s--force(\s|$)", "Force-push requires explicit human approval."),
    (r"\bdocker\s+run\b.*(-v|--volume)\s+/(\s|:)", "Docker host root mount is blocked."),
    (r"\bdocker\s+run\b.*--privileged", "Privileged Docker containers are blocked."),
    (r"\b(cat|less|more|sed|awk|grep|rg)\b.*(\.env|id_rsa|id_ed25519|\.pem|\.p12|\.pfx)", "Reading likely secret files is blocked."),
]

ASK_PATTERNS = [
    (r"\b(curl|wget|Invoke-WebRequest|iwr)\b", "Network fetch requires approval."),
    (r"\b(npm|pnpm|yarn|bun)\s+(install|add|update|upgrade|remove|dlx|exec)\b", "Package manager/dependency command requires approval."),
    (r"\b(npx|pip|pipx|poetry|uv|cargo|go)\s+(install|add|update|get|run|sync)\b", "Dependency/tool installation or network sync requires approval."),
    (r"\b(brew|apt|apt-get|dnf|yum|pacman|choco|winget)\s+(install|upgrade|update|remove)\b", "System package manager command requires approval."),
    (r"\bdocker\s+(pull|build|run|compose)\b", "Docker operations require approval."),
    (r"\bgh\s+pr\s+create\b", "Opening a PR is an external side effect and requires approval."),
    (r"\bgit\s+push\b", "Pushing to remote requires approval unless already approved for this task."),
]

SAFE_GIT_PATTERNS = [
    r"^git\s+status(\s|$)",
    r"^git\s+diff(\s|$)",
    r"^git\s+add\s+",
    r"^git\s+commit\s+",
    r"^git\s+branch(\s|$)",
    r"^git\s+switch\s+",
    r"^git\s+checkout\s+-b\s+",
    r"^git\s+worktree\s+(list|add)\b",
]

SAFE_READ_PATTERNS = [
    r"^(rg|grep|find|ls|pwd|cat|sed|awk)\b",
    r"^python3?\s+-m\s+py_compile\b",
    r"^bash\s+-n\b",
]


def normalize(command: str) -> str:
    return " ".join(command.strip().split())


def get_command(payload: dict[str, Any]) -> str:
    tool_input = payload.get("tool_input") or payload.get("toolInput") or {}
    if isinstance(tool_input, dict):
        command = tool_input.get("command") or tool_input.get("cmd") or ""
        if isinstance(command, str):
            return command
    return ""


def classify_command(command: str) -> tuple[str, Optional[str]]:
    cmd = normalize(command)
    if not cmd:
        return "neutral", None

    for pattern, reason in DENY_PATTERNS:
        if re.search(pattern, cmd, flags=re.IGNORECASE):
            return "deny", reason

    for pattern, reason in ASK_PATTERNS:
        if re.search(pattern, cmd, flags=re.IGNORECASE):
            return "ask", reason

    for pattern in SAFE_GIT_PATTERNS + SAFE_READ_PATTERNS:
        if re.search(pattern, cmd, flags=re.IGNORECASE):
            return "allow", None

    return "neutral", None


def codex_pretool_deny(reason: str) -> dict[str, Any]:
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }


def codex_permission_allow() -> dict[str, Any]:
    return {
        "hookSpecificOutput": {
            "hookEventName": "PermissionRequest",
            "decision": {"behavior": "allow"},
        }
    }


def codex_permission_deny(reason: str) -> dict[str, Any]:
    return {
        "hookSpecificOutput": {
            "hookEventName": "PermissionRequest",
            "decision": {"behavior": "deny", "message": reason},
        }
    }


def load_stdin_json() -> dict[str, Any]:
    raw = sys.stdin.read()
    if not raw.strip():
        return {}
    try:
        data = json.loads(raw)
        return data if isinstance(data, dict) else {}
    except json.JSONDecodeError:
        return {}


def emit(obj: dict[str, Any]) -> None:
    print(json.dumps(obj, separators=(",", ":")))
