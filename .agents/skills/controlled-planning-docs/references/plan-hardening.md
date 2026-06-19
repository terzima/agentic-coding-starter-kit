# Plan Hardening Reference

Use for `docs/plans/PLAN-*.md`.

## Purpose

A hardened plan tells an agent exactly how to implement the accepted spec without redesigning. Spend tokens where they prevent drift: file responsibilities, function signatures, fixtures, commands, expected outputs, and task order.

## Required Shape

- Header: goal, architecture, tech stack.
- Preconditions: accepted spec, branch/worktree state, approvals.
- File structure: create/modify/read/test entries with responsibilities.
- Contracts to implement: functions/classes, API responses, data/schema examples, config, errors.
- Tasks: ordered, small, checkbox steps.
- Validation: exact commands and expected pass conditions.
- Documentation updates.
- Rollback plan.
- Risks and mitigations.
- Stop conditions.

## Plan-To-Spec Fidelity

Use this section when risk, ambiguity, deletion, broad refactors, borrowed examples, or prior execution drift could cause a plan to miss the spec's real intent.

Required concepts for those plans:

- **Spec Picture**: short plain-language restatement of the linked spec's intended outcome.
- **Plan Result**: what the current plan would actually produce if implemented exactly.
- **Proof Strategy**: automated, manual, human, or audit evidence that proves the plan result matches the spec picture.
- **Failure Ownership**: which layer, file, actor, or decision owns failure when a gate does not pass.
- **No-Drift Gates**: non-negotiable conditions that stop implementation before unsupported scope appears.
- **Expected Failure / Expected Pass**: focused before/after evidence for tasks where a failing test, audit, or command can prove the work is meaningful.

Simple low-risk docs plans may keep these ideas as one concise paragraph or omit labels when the ordinary file map, tasks, validation, and stop conditions already prove the outcome.

## Repairable Blockers

A blocker should name the missing contract, failing layer, and next concrete repair action. Avoid blockers that only say a thing does not work. If the first failing owner is unknown, split to a Spike or audit task with a budget and promotion rule.

## Spike / Research Plans

Use a spike plan when the next step is evidence gathering, not production implementation. A spike plan must include:

- Research question.
- Allowed scope.
- Evidence to collect.
- Budget and kill criteria.
- Output destination, usually `docs/worklog/` or a concise report.
- Promotion rule that says what must be captured in a spec or plan before implementation resumes.

Spike tasks may inspect, prototype locally, or measure within the allowed scope. They must not ship behavior, mutate accepted specs mid-implementation, or turn failed attempts into production work.

## Detail Standard

Use execution-grade detail for:

- cross-module APIs;
- schema/model fields;
- route responses;
- test fixtures and assertions;
- parser/validator rules;
- state machines and reducers;
- migrations or data transforms;
- UI DOM IDs/classes when renderer/input code depends on them.
- deletion, migration, or cleanup tasks where losing a workflow is possible.

Use concise bullets for:

- low-risk directory creation;
- docs-only edits;
- obvious package markers;
- simple README updates.

## Task Pattern

Each meaningful task should include:

- files touched;
- failing test, audit, or fixture first when possible;
- command to run and expected failure/pass;
- minimal implementation step;
- focused re-run;
- commit suggestion only if useful.

## No-Drift Checklist

- No “add appropriate validation/error handling/tests.”
- No vague implementation verbs unless exact files, commands, assertions, data shapes, or stop conditions make them concrete.
- No functions/types mentioned before they are defined.
- No broad task that touches unrelated layers.
- No dependency or network action unless approved or listed as a stop point.
- No duplicated `AGENTS.md` policy.
- No research task without a kill criterion and promotion rule.
- No downstream task that assumes a failed proof passed.

## When To Split

Split into another plan if a task needs a different approval class, creates a user-testable checkpoint, requires a dependency decision, or cannot be verified by the same gates.

Split into a spike if the agent cannot name exact implementation files, tests, and expected behavior without further evidence.
