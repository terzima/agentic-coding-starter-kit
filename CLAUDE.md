# CLAUDE.md

Read `AGENTS.md` first. It is the canonical repository instruction file.

Claude-specific preferences:

- Use bare implementation output unless the user asks for explanation.
- Use Discovery or Spike mode for ambiguous work.
- Do not add dependencies, access network, or run downloaded code without approval.
- Prefer local CLI tools over MCP servers when a simple CLI command is enough.
- Use subagents for broad investigation so the main context stays clean.

Repo-local skills:

- Skills live at `.agents/skills/{skill-name}/SKILL.md`.
- Invoke skills via `/skill-name` slash commands (`.claude/commands/`); each command reads the matching `SKILL.md` and routes `$ARGUMENTS`.
- When slash commands are unavailable, read the matching `SKILL.md` completely before acting — this is the supported explicit fallback.
- Keep skill guidance task-scoped; do not paste long skill content into unrelated context.

Accepted-plan implementation shortcut:

```text
Mode: Implementation.

Use the repo-local accepted-plan-implementation skill.

Execute [PLAN or BATCH path] exactly.
```

Compact instructions:

When compacting, preserve only:

1. Active spec and plan paths.
2. Files changed.
3. Test commands and results.
4. Accepted Change Requests.
5. Open blockers and risks.
6. Worklog or handoff pointers when they change future action.

Discard routine narration and failed approaches.
