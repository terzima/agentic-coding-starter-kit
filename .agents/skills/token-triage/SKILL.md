---
name: token-triage
description: Use when reducing token usage in agentic coding sessions by auditing active context, moving durable knowledge to repo files, filtering noisy outputs, and deciding what should stay in L0/L1/L2 context.
---

# Token Triage

Use this skill when context feels bloated, repeated, stale, or expensive. It is report-only unless the user explicitly asks for edits.

## Core Rule

Keep active context limited to the smallest set needed for the current mode. Durable knowledge belongs in durable repo files; logs and failed approaches belong in worklogs; restart-critical state belongs in handoffs or `CURRENT_STATE.md`.

## Context Tiers

- **L0 always**: `AGENTS.md` and current user request.
- **L1 serious task**: `docs/repo-map.md`, `docs/status/CURRENT_STATE.md`, active spec, and active plan.
- **L2 only when needed**: directly affected source files, tests, relevant ADRs, targeted logs, and focused evidence.

## Workflow

1. Identify the current mode and active objective.
2. List the largest context costs: always-loaded instructions, specs/plans, status dashboard, logs, generated output, broad file reads, plugin/tool overhead, or pasted chat history.
3. Classify each context item as L0, L1, L2, durable-doc candidate, worklog candidate, handoff candidate, or discard/summarize.
4. Recommend the smallest edit or workflow change that reduces future context cost without losing restartability.
5. Provide one next prompt if the user wants edits.

## Symptoms

Use this skill when:

- `CURRENT_STATE.md` starts carrying narrative session history;
- specs or plans duplicate `AGENTS.md` policy;
- prompts repeatedly paste prior chat instead of pointing to durable files;
- test/log output is too large for the decision needed;
- a workflow skill is always loaded but rarely changes behavior;
- a handoff contains research narrative instead of restart-critical facts.

## Stop Conditions

Stop when:

- shrinking context would delete the only durable copy of a decision;
- the user asks for behavior changes outside a planning-doc or framework-cleanup scope;
- a proposed edit touches product behavior, secrets, dependencies, hooks, CI, deployment, or remote services without an accepted plan.

## Output Contract

```txt
Context diagnosis:
Largest context costs:
Keep in active context:
Move to durable docs:
Filter or summarize:
Suggested edits:
Recommended next prompt:
```

## What To Avoid

- Editing files unless explicitly asked.
- Removing evidence instead of moving it to the right durable file.
- Recommending subagents or tools when a targeted file read is enough.
- Treating context reduction as more important than accuracy or restartability.
- Collapsing distinct status, handoff, and worklog roles into one document.
