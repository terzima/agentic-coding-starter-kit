#!/usr/bin/env python3
# Adapter wrapper; policy patterns live in scripts/agent/policy_lib.py.
import sys, os as _os
sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', 'scripts', 'agent'))
from policy_lib import classify_command, codex_permission_allow, codex_permission_deny, emit, get_command, load_stdin_json

payload = load_stdin_json()
cmd = get_command(payload)
classification, reason = classify_command(cmd)

if classification == "allow":
    emit(codex_permission_allow())
elif classification in {"deny", "ask"}:
    emit(codex_permission_deny(reason or "Blocked by repository approval policy."))
else:
    emit({})
