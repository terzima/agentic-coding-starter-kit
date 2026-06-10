# Token Optimization Playbook for Agentic Coding

## Primary causes of token waste

1. Re-reading the whole repo on every task.
2. Pasting long conversation history into new sessions.
3. Letting the agent narrate routine implementation details.
4. Loading specialized instructions globally.
5. Running broad tests and dumping full logs into context.
6. Keeping failed attempts in the same session too long.
7. Using one large “forever chat” for unrelated tasks.
8. Letting MCP/tool definitions or unused plugins sit in every context.

## Core practices

### 1. Use persistent repo memory

Do not repeatedly explain the repo. Maintain these files:

```txt
AGENTS.md
docs/repo-map.md
docs/project-charter.md
docs/standards/*.md
```

`AGENTS.md` is for always-on operating rules. `repo-map.md` is for stable repo structure. Detailed domain/process knowledge belongs in specs, ADRs, and skills.

### 2. Use mode-specific prompts

Do not ask the agent to “figure it out and implement.” Say which mode it is in:

```txt
Mode: Discovery only
Mode: Spec only
Mode: Plan only
Mode: Implementation only
Mode: Review only
```

Mode declarations prevent the agent from loading unnecessary context and taking unnecessary actions.

### 3. Use bare implementation output

During implementation, require this output contract:

```txt
No step-by-step narration.
Report only blockers, Change Requests, failed checks, and final DONE summary.
```

This saves output tokens and reduces distraction.

### 4. Use skills for progressive disclosure

Specialized workflows should live in `.agents/skills/`. The agent sees only the skill name and description up front, then loads the full instructions only when relevant.

Good skill candidates:

```txt
large-spec-seeding
controlled-agentic-development
pr-review-gate
token-triage
migration-review
api-contract-review
```

### 5. Keep base instructions small

Aim for:

```txt
AGENTS.md:       150-300 lines max
CLAUDE.md:       pointer to AGENTS.md + Claude-specific notes only
Cursor rules:    short always-on behavior only
Skills:          detailed task-specific workflows
Specs/plans:     one task each
```

### 6. Use filtered logs

Do not let a failed test dump 5,000 lines into context. Use helper scripts and hooks to return the relevant tail, failures, and command summary.

Included helper:

```bash
scripts/agent/filter_output.py
```

Example:

```bash
pytest 2>&1 | scripts/agent/filter_output.py --kind test --limit 200
npm test 2>&1 | scripts/agent/filter_output.py --kind test --limit 200
```

### 7. New task, new context

Use a fresh session when switching workstreams. Carry forward only durable docs and a short worklog summary.

### 8. Compact deliberately

When a session has to continue, compact with instructions:

```txt
Compact this session. Preserve only:
1. Accepted spec and plan references.
2. Files changed.
3. Test commands and results.
4. Open blockers.
5. Any accepted Change Requests.
Discard failed approaches and routine narration.
```

### 9. Audit token usage periodically

Use this prompt:

```txt
Mode: Token audit only.
Review the current agent setup and identify what is likely wasting context.
Return:
1. Always-loaded files that should be shortened.
2. Instructions that should move to skills.
3. Commands producing excessive output.
4. Repeated context that should become repo docs.
5. Specific edits to reduce token usage without weakening safety.
Do not edit files.
```

## Token budget by mode

| Mode | Context budget | Output budget | Notes |
|---|---:|---:|---|
| Discovery | Medium | Medium | Read selectively; return file map and risks. |
| Spec | Medium | Medium | Convert ambiguity into acceptance criteria. |
| Plan | Low/Medium | Low | Exact files, tests, stop conditions. |
| Implementation | Low | Very low | Bare output only. |
| Review | Medium | Medium | Compare diff to accepted spec/plan. |

## Anti-patterns

Avoid these prompts:

```txt
Read the whole codebase and improve it.
Implement this entire giant spec.
Keep going and update the plan as needed.
Fix whatever you find.
Use your judgment and do all necessary cleanup.
```

Use these instead:

```txt
Mode: Discovery only. Identify the smallest coherent first slice from docs/intake/PROJECT_OVERVIEW_RAW.md.
Mode: Spec only. Produce SPEC-0001 for the onboarding flow; exclude billing, notifications, and admin UI.
Mode: Plan only. Plan implementation for SPEC-0001; list exact files and tests.
Mode: Implementation only. Implement accepted PLAN-0001. Stop for Change Request if scope changes.
```
