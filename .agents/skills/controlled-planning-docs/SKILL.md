---
name: controlled-planning-docs
description: Use when writing, revising, hardening, or reviewing repo specs, implementation plans, spike/research plans, batch plans, status dashboards, handoffs, or worklogs. Applies automatically to Spec and Plan mode document authoring, plan-hardening passes, batch grouping work, durable planning-doc cleanup, and intake/seeding work.
---

# Controlled Planning Docs

Use this skill to produce precise, execution-ready planning docs without bloating always-loaded context.

## Core Rule

Do not copy `AGENTS.md` policy into specs/plans/batches. Put reusable repo rules in `AGENTS.md`; put task-local contracts, interfaces, fixtures, commands, and gates in the planning doc.

## Pick The Document Type

- **Spec**: read `references/spec-writing.md`.
- **Plan**: read `references/plan-hardening.md`.
- **Spike / Research**: use `.agents/skills/spike-research/SKILL.md` to frame the question, evidence, budget, output destination, and promotion rule; read `references/plan-hardening.md` only when writing a durable spike plan.
- **Batch**: read `references/batch-writing.md`.
- **Intake / Seeding**: use `.agents/skills/project-intake-seeding/SKILL.md`; read `references/intake-seeding.md` when writing or revising seeded docs.
- **Change Request**: use `.agents/skills/change-request-control/SKILL.md`; read `references/change-request-writing.md` when creating or revising the durable CR file.
- **Status / Handoff / Worklog**: read `references/status-handoff-worklog.md`.
- **Template edits**: read `references/template-writing.md`.
- **Plan-to-spec alignment review**: use `.agents/skills/spec-plan-alignment/SKILL.md`.
- **Mixed request**: write or revise in this order: spec, plan, batch.

## Depth Ladder

- M1 seeded docs: concise orientation, open questions, no execution detail.
- M2 spec: exact behavior, boundaries, interfaces, and acceptance gates.
- M3 plan: concrete file map, contracts, task slices, tests, commands, stop conditions.
- M4 execution plan: enough detail to implement without redesign; include small code/test snippets where they prevent ambiguity.
- Spike plan: exact question, allowed scope, evidence to collect, budget/kill criteria, output destination, and promotion rule.
- Seeding pass: broad but shallow project decomposition; deep only for the first implementation-safe slices.

## Workflow

1. Identify mode: Spec, Plan, or documentation cleanup. Do not combine with Implementation unless explicitly instructed.
2. Read only `AGENTS.md`, `docs/repo-map.md`, active source docs, and the relevant reference below.
3. Classify maturity and approval class.
4. Frame the target state before writing: "what must be true when this document is accepted?" Answer in one sentence. This anchors the depth-ladder choice and the scope-exclusion step below before any prose is written.
5. State explicitly what this document will NOT cover. One line is enough. This becomes the first boundary the self-review checks.
6. Write the doc using the matching repo template or established local shape.
7. For all M3 and M4 plans (not only risky or drift-prone ones), include a concise spec picture, plan result, proof strategy, failure ownership, no-drift gates, and expected fail/pass evidence per task.
8. Self-review:
   - no placeholders or template guidance left;
   - no duplicated `AGENTS.md` policy blocks;
   - exact contracts and validation commands are present;
   - scope is small enough for the declared maturity;
   - stop conditions are task-specific;
   - research findings are not treated as accepted behavior unless a spec or plan captures them;
   - rollback steps are ordered by dependency, not just "revert the commit";
   - each M3/M4 plan task has both expected-failure and expected-pass evidence.
9. Optionally run:

```bash
python3 .agents/skills/controlled-planning-docs/scripts/check_planning_doc.py docs/plans/PLAN-XXXX-title.md
```

## Output Contract

Return the path changed or created, source docs used, approval class or status, open questions when relevant, checks run, and the exact next prompt when the workflow has a predictable next step.

## What To Preserve From The Exemplars

- Product/spec docs define principles, vocabulary, contracts, gates, failure owners, and remediation paths.
- Plans define exact files, exact tests, expected failures/passes, task order, and acceptance evidence.
- Batches stay short: included specs/plans, execution contract, required checks, human gates, and final report.
- Seeded docs preserve raw intent while separating requirements, assumptions, roadmap candidates, and open questions.
- Status, handoff, and worklog files each have a different job; do not let one file become all three.

## What To Avoid

- Long pasted source material or logs.
- Generic prose that does not constrain implementation.
- “Add tests” without naming fixtures, assertions, or commands.
- Repeating permission, git, hook, approval-class, or Change Request rules from `AGENTS.md`.
- Huge plan detail for low-risk scaffold work where exact file contents are enough.
- Letting spike evidence bypass the spec/plan approval path.
- Recreating a large prompt library when a focused reference file will do.
