#!/usr/bin/env python3
from policy_lib import classify_command, codex_permission_allow, codex_permission_deny, emit, get_command, load_stdin_json

payload = load_stdin_json()
cmd = get_command(payload)
classification, reason = classify_command(cmd)

if classification == "allow":
    emit(codex_permission_allow())
elif classification in {"deny", "ask"}:
    emit(codex_permission_deny(reason or "Blocked by repository approval policy."))
else:
    # No decision. User's normal approval flow applies.
    emit({})
