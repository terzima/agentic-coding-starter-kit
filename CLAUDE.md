# CLAUDE.md

Read `AGENTS.md` first. It is the canonical repository instruction file.

Claude-specific preferences:

- Use bare implementation output unless the user asks for explanation.
- Use plan/discovery mode for ambiguous work.
- Do not add dependencies, access network, or run downloaded code without approval.
- Prefer local CLI tools over MCP servers when a simple CLI command is enough.
- Use subagents for broad investigation so the main context stays clean.

Compact instructions:

When compacting, preserve only:

1. Active spec and plan paths.
2. Files changed.
3. Test commands and results.
4. Accepted Change Requests.
5. Open blockers and risks.

Discard routine narration and failed approaches.
