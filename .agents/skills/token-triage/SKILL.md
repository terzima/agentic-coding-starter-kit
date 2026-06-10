---
name: token-triage
description: Use when reducing token usage in agentic coding sessions by shrinking always-loaded instructions, moving workflows to skills, filtering logs, and improving context discipline.
---

# Token Triage Skill

## Inspect

- Always-loaded instruction files.
- Active specs/plans.
- Logs and test outputs.
- MCP/tool/plugin overhead if visible.
- Repeated context that should be durable docs.

## Recommend

1. Shorten base instructions.
2. Move task-specific workflows to skills.
3. Use bare implementation output.
4. Use filtered test/log output.
5. Clear/compact between unrelated tasks.
6. Use subagents for broad investigation where supported.
7. Replace pasted history with file references.

## Output

Return a concise edit plan. Do not edit files unless explicitly asked.
