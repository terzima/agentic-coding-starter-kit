#!/usr/bin/env python3
"""Claude Code PreToolUse policy hook. Policy patterns live in scripts/agent/policy_lib.py."""
from __future__ import annotations
import sys, os as _os
sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', 'scripts', 'agent'))
from policy_lib import classify_command, codex_pretool_deny, emit, get_command, load_stdin_json

payload = load_stdin_json()
cmd = get_command(payload)
classification, reason = classify_command(cmd)

if classification == "deny":
    emit(codex_pretool_deny(reason or "Blocked by repository policy."))
elif classification == "ask":
    emit(codex_pretool_deny((reason or "Approval required.") + " Ask the human owner before running this command."))
else:
    emit({})
