#!/usr/bin/env python3
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
    # No decision. Let Codex's normal sandbox/approval flow handle it.
    emit({})
