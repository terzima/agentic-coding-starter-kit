#!/usr/bin/env python3
# Adapter wrapper; policy patterns live in scripts/agent/policy_lib.py.
import sys, os as _os
sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', 'scripts', 'agent'))
from policy_lib import classify_command, codex_pretool_deny, emit, get_command, load_stdin_json

payload = load_stdin_json()
tool_name = payload.get("tool_name") or payload.get("toolName") or ""
cmd = get_command(payload)
classification, reason = classify_command(cmd)

if classification == "deny":
    emit(codex_pretool_deny(reason or "Blocked by repository policy."))
elif classification == "ask":
    emit(codex_pretool_deny((reason or "Approval required.") + " Stop and ask the human owner before running this command."))
else:
    emit({})
