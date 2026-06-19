# PLAN-XXXX: Title

Status: Draft | Accepted | Completed | Superseded
Maturity: M3 | M4
Owner: Unassigned
Created: YYYY-MM-DD
Updated: YYYY-MM-DD
Related spec: `docs/specs/SPEC-XXXX-title.md`
Related ADRs: None
Related Change Requests: None

## How to write this plan

Use this section while drafting, then remove it before marking the plan ready.

- Read `.agents/skills/controlled-planning-docs/references/plan-hardening.md`.
- Build only from an accepted spec and durable repo context.
- Name exact files, public interfaces, fixtures, tests, commands, expected outputs, docs updates, rollback steps, and stop conditions.
- Split work when approval classes, dependency/network gates, or human checkpoints differ.
- Put uncertain research into the Spike / Research Plan Addendum instead of pretending implementation is known.
- Keep repo-wide policy out of this file; reference `AGENTS.md`.

**Goal:** One sentence describing the implemented outcome.

**Architecture:** 2-4 sentences naming boundaries, data flow, and why this shape is safe.

**Tech stack:** Existing runtime/libraries and any approved additions.

## Plan-to-spec fidelity

Use this section when the work is risky, broad, ambiguous, deletion-heavy, or has drifted before. Keep it concise and remove it if it does not add value.

- Spec Picture: plain-language intended outcome from the accepted spec.
- Plan Result: what exact result this plan produces if followed literally.
- Proof Strategy: automated, manual, audit, or human evidence that proves the result matches the spec picture.
- Failure Ownership: file, layer, actor, or decision that owns each likely failure.
- No-Drift Gates: conditions that stop implementation before unsupported scope appears.
- Expected Failure / Expected Pass: before/after evidence for tasks where this is useful.

## Preconditions

- [ ] Spec is accepted.
- [ ] Worktree/branch state is understood.
- [ ] Required approvals are already granted or explicitly listed as stop points.

## File structure

- Create: `path/to/file` - responsibility.
- Modify: `path/to/file` - exact reason.
- Read first: `path/to/file` - why.

## Contracts to implement

List exact interfaces the worker must preserve or create.

- Function/class signatures:
- API routes and response shapes:
- Data/schema examples:
- Config/env keys:
- Error codes/messages:

## Tasks

### Task 0: Preflight

**Files:** None

- [ ] Run:

```bash
git status --short
```

- [ ] Confirm accepted scope and note any pre-existing dirty files.

### Task 1: Component Name

**Files:**

- Create/Modify/Test:

- [ ] Write or update the focused failing test/fixture.
- [ ] Run the smallest relevant check and confirm expected failure.
- [ ] Implement the minimal scoped change.
- [ ] Run the focused check and confirm pass.
- [ ] Update docs only if behavior or commands changed.

## Validation

```bash
git status --short
```

Add exact lint/typecheck/test/build commands with expected pass conditions. Include filtered commands for noisy outputs.

## Documentation updates

- Doc update:

## Rollback plan

State the smallest safe revert path.

## Risks

- Risk:
  - Mitigation:

## Stop conditions

- Stop if:

## Spike / Research Plan Addendum

Use this addendum only when the plan output is evidence instead of production behavior.

## Research Question

## Allowed Scope

## Evidence To Collect

## Budget And Kill Criteria

## Output

## Promotion Rule
