# Claude Code Adapter Notes

Claude Code commonly uses `CLAUDE.md`, `.claude/settings*.json`, output styles, hooks, and permission allowlists.

This starter repo includes:

```txt
CLAUDE.md
.claude/output-styles/Bare Engineering.md
.claude/settings.example.json
.claude/hooks/pre_tool_use_policy.py
```

Recommended setup:

1. Review `.claude/settings.example.json`.
2. Copy approved parts into `.claude/settings.local.json` or your user-level settings.
3. Select `Bare Engineering` output style through Claude Code config if desired.
4. Keep `AGENTS.md` as canonical repo policy.

Do not blindly copy permission settings. Validate syntax and behavior in your current Claude Code version.
