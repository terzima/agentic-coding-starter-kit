# Agentic Coding Prompt Library

Use these prompts directly. Replace bracketed fields.

## 1. New repo seeding prompt

## New repo seeding prompt — SEED-0000

```txt
Mode: Project Seeding / Spec Decomposition.

Read:
1. AGENTS.md
2. docs/intake/PROJECT_OVERVIEW_RAW.md

Do not write application code.
Do not create production application files.
Do not install dependencies.
Do not access the network.
Do not run framework generators.
Do not execute implementation tasks.

Goal:
Convert the raw project overview into controlled project documents, decomposed specs, decomposed plans, and proposed execution batches.

Important distinction:
This is not batch execution.
This is repo seeding and project decomposition.

The purpose is to create the starting point that future batch execution will use.

Document Depth Policy:

The seeding pass must be broad but shallow across the whole project, and deep only for the first implementation-safe slices.

Do not fully specify or plan the entire project from the raw overview.

Create documents at these maturity levels:

M0 — Intake:
Raw unprocessed material. The raw overview remains here.

M1 — Seeded:
Extracted into controlled project docs, but not yet implementation-ready.

M2 — Specified:
Requirements and acceptance criteria are clear.

M3 — Planned:
Implementation steps, likely files, validation commands, and stop conditions are clear.

M4 — Executable:
Ready for agent implementation.

During seeding:

- `docs/project-charter.md` should reach M1/M2.
- `docs/specs/SPEC-0000-project-foundation.md` should reach M1/M2.
- The first 1–3 implementation specs should reach M2.
- The first 1–3 matching implementation plans should reach M3/M4.
- The first 1–2 proposed batches may be created if they group already-written specs/plans.
- Future work should remain in `docs/roadmap.md` as roadmap items, spec candidates, ADR candidates, open questions, or deferred decisions.

Only create a full SPEC file if:
1. the requirement is clear,
2. the boundaries are known,
3. acceptance criteria can be written,
4. it is likely to be implemented in the first 1–2 batches.

Only create a full PLAN file if:
1. the linked spec is clear,
2. expected files/directories can be named,
3. validation commands can be identified,
4. execution can happen without major unresolved decisions.

Do not create full specs/plans for late-stage or speculative features.

Do not create more than 3 initial implementation specs or 3 initial implementation plans unless the raw overview makes the early implementation sequence unusually clear.

All later work should be captured as:
- roadmap item,
- spec candidate,
- ADR candidate,
- open question,
- deferred decision,
- future batch candidate.

Approved output paths:
1. docs/project-charter.md
2. docs/glossary.md
3. docs/repo-map.md
4. docs/roadmap.md
5. docs/seed/SEED-0000-project-decomposition.md
6. docs/seed/SEED-0000-results.md
7. docs/specs/SPEC-0000-project-foundation.md
8. docs/specs/SPEC-0001-*.md and additional initial specs as needed
9. docs/plans/PLAN-0001-*.md and additional initial plans as needed
10. docs/plans/batches/BATCH-0001-*.md and additional proposed batch plans as needed
11. docs/worklog/0000-seeding-notes.md
12. docs/adr/ADR-0000-architecture-direction.md only if architecture choices are explicit or strongly implied

Required behavior:
- Treat docs/intake/PROJECT_OVERVIEW_RAW.md as an intake artifact, not the permanent working spec.
- Preserve the intent of the raw overview.
- Separate confirmed requirements from assumptions.
- Separate goals from non-goals.
- Separate product requirements from implementation guesses.
- Do not invent implementation details where the overview is silent.
- Do not turn brainstormed possibilities into committed requirements.
- List open questions explicitly.
- Identify contradictions, unresolved choices, and risky assumptions.
- Decompose the project into a small number of immediately useful implementation specs, and capture the rest as roadmap/spec candidates rather than full specs.- Write plans only for specs that are clear enough to implement.
- Group related specs/plans into proposed batches only after the specs/plans exist.
- Keep each generated file concise and useful for future agents.
- Do not ask for approval after each document.
- Stop only if a missing decision prevents useful decomposition.

Seeding outputs:

1. docs/project-charter.md
Must include:
- project purpose
- target users
- core problem
- product goals
- non-goals
- success criteria
- constraints
- first meaningful human-testable milestone

2. docs/glossary.md
Must include:
- domain terms
- project-specific terms
- acronyms
- ambiguous terms requiring clarification

3. docs/repo-map.md
Must include:
- expected top-level repo structure
- responsibility of each major directory
- architectural boundaries
- files future agents should read first
- files future agents should not casually modify
- expected local verification commands, if known

4. docs/specs/SPEC-0000-project-foundation.md
Must include:
- problem statement
- confirmed requirements
- product boundaries
- technical boundaries
- non-goals
- assumptions
- open questions
- acceptance criteria
- first implementation slice
- first human-testable milestone

5. Initial decomposed specs
Create initial SPEC files for the first coherent implementation areas.
First implementation spec rule:

If the repo already contains governance/documentation scaffold but does not contain the actual application structure, the first implementation spec must be:

docs/specs/SPEC-0001-application-scaffold.md

The matching plan must be:

docs/plans/PLAN-0001-application-scaffold.md

The first proposed batch should normally be:

docs/plans/batches/BATCH-0001-application-scaffold.md

This spec/plan/batch should define the actual project skeleton required before product implementation begins.

It should cover:
- backend directory structure
- frontend directory structure
- shared package/module structure if needed
- test directory structure
- package/dependency manifest strategy
- local development commands
- local prerequisite tools
- environment variable policy
- `.env.example`
- README setup instructions
- CI/test/lint/typecheck placeholders where appropriate

It must not cover:
- product behavior
- business logic
- real authentication
- real external integrations
- production deployment
- secrets
- large dependency installation without approval

Each spec must include:
- purpose
- scope
- non-goals
- requirements
- acceptance criteria
- dependencies
- approval class: A0, A1, A2, or A3
- automated gate
- human gate
- stop conditions

Do not create too many specs.
Prefer the smallest set needed to start implementation cleanly.

6. Initial implementation plans
Create PLAN files only for specs that are sufficiently clear.

Each plan must include:
- linked spec
- files expected to change
- implementation steps
- validation commands
- documentation updates
- local commit strategy
- risks
- stop conditions

7. Proposed batch plans
Create only the first 1–2 proposed BATCH files, and only if they group specs/plans created during this seeding pass. Later batches should remain roadmap candidates.

Each batch must include:
- included specs
- included plans
- approval class
- whether it is user-testable
- whether the agent may continue automatically
- automated gates
- human gates
- stop conditions
- final batch output

Batches should group small, related plans so execution is less risky.

Do not use a batch to define the project.
Use batches only to group already-defined implementation work.

8. docs/roadmap.md
Must include:
- proposed implementation sequence
- which specs are prerequisites for others
- proposed batches
- approval class for each batch
- first human-testable checkpoint
- what work should not require human approval
- what work must require human approval

9. docs/seed/SEED-0000-project-decomposition.md
Must include:
- how the raw overview was decomposed
- document map
- spec map
- plan map
- batch map
- decomposition rationale

10. docs/seed/SEED-0000-results.md
Must include:
- created documents
- assumptions made
- open questions
- risks
- recommended next prompt
- whether the next step is planning, implementation, or human clarification

11. docs/worklog/0000-seeding-notes.md
Must include:
- what was extracted from the raw overview
- what was excluded
- why anything was deferred
- unresolved questions
- recommendations for the next agent session

12. docs/adr/ADR-0000-architecture-direction.md
Create only if justified.

If created, it must include:
- context
- decision
- alternatives considered
- consequences
- assumptions
- reversal conditions

Stop conditions:
Stop and ask for human input only if:
- the raw overview has contradictions that block decomposition,
- the project cannot be decomposed without inventing core behavior,
- a major architecture choice is required but not specified or strongly implied,
- the agent would need to install dependencies,
- the agent would need network access,
- the agent would need to write application code,
- the agent would need to modify files outside the approved documentation paths.

Final response:
Return only:

1. Documents created or updated.
2. Specs created.
3. Plans created.
4. Proposed batches created.
5. Key assumptions made.
6. Open questions.
7. Recommended next prompt.

Do not include full document contents in the final response unless specifically requested.
```

## 1.5 Seeding review prompt

```txt
Mode: Review only.

Read:
1. AGENTS.md
2. docs/seed/SEED-0000-results.md
3. docs/roadmap.md
4. docs/specs/SPEC-0000-project-foundation.md
5. docs/plans/batches/BATCH-0001-*.md

Review the seeded project control documents.

Do not write code.
Do not install dependencies.

Check:
1. Are the specs decomposed into implementation-safe chunks?
2. Are the plans small enough to execute safely?
3. Are the proposed batches grouped correctly?
4. Are any batches too broad?
5. Is the first human-testable milestone clearly identified?
6. Are approval classes assigned correctly?
7. Are there missing docs before implementation should begin?

Return:
- blocking issues
- non-blocking improvements
- recommended edits
- whether BATCH-0001 is ready for execution
```

## 2. Discovery prompt

```txt
Mode: Discovery only.
Read AGENTS.md first.
Do not edit files.
Do not write code.
Do not write a full implementation plan.

Task:
[describe task]

Return:
1. Relevant files and why they matter.
2. Existing patterns to follow.
3. Risks and unknowns.
4. Whether this needs a spec, ADR, or direct implementation.
5. Recommended next mode.
```

## 3. Spec prompt

```txt
Mode: Spec only.
Use docs/specs/_template.md.
Do not write code.
Do not write a plan.

Input:
[brief task]

Return a new SPEC file with:
- problem statement
- goals
- non-goals
- user-visible behavior
- technical constraints
- acceptance criteria
- out-of-scope items
- open questions
```

## 4. Plan prompt

```txt
Mode: Plan only.
Use docs/plans/_template.md.
Do not edit code.
Do not change the accepted spec.

Accepted spec:
[spec path]

Return a plan with:
1. Exact file change list.
2. Ordered implementation steps.
3. Test plan.
4. Documentation plan.
5. Rollback plan.
6. Stop conditions requiring a Change Request.
```

## 5. Implementation prompt

```txt
Mode: Implementation only.

Read:
1. AGENTS.md
2. docs/repo-map.md
3. [SPEC path]
4. [PLAN path]

Implement only the accepted plan.

This is single-plan execution, not batch execution.

Rules:
- Bare output only.
- Do not change the spec.
- Do not rewrite the plan unless recording a minor execution note.
- Do not expand scope.
- Do not modify files outside the accepted plan unless you stop and open a Change Request.
- Do not install dependencies without approval.
- Do not access the network without approval.
- Do not run destructive commands without approval.
- Do not touch files outside the repo.
- Run relevant tests/checks.
- Make atomic local commits when coherent units are complete.

Human Approval Value Policy:
Do not stop for approval after local commits or routine machine-verifiable progress.

Continue automatically if:
- the task remains inside accepted scope,
- all required automated checks pass,
- no network/dependency/system/destructive action is needed,
- no human-verifiable behavior is being claimed complete,
- no Change Request is required.

Stop only when:
- an A2 human checkpoint is reached,
- an A3 approval is required,
- tests/build fail and cannot be resolved within scope,
- a Change Request is needed,
- a usable/manual/physical test point has been reached,
- continuing would require modifying files outside the plan.

When stopping:
- ask one targeted question, or
- provide one review package.

Do not ask for generic approval.

Completion response:
DONE

- Summary:
- Files changed:
- Local commits:
- Tests/checks run:
- Tests/checks not run:
- Docs updated:
- Deviations from plan:
- Change Requests opened:
- Remaining risks:
- Next recommended action:
```

## 5.5. Batch implementation prompt
```txt
Mode: Batch Implementation.

Read:
1. AGENTS.md
2. docs/repo-map.md
3. [BATCH path]
4. all SPEC files referenced by the batch
5. all PLAN files referenced by the batch

Execute only the accepted batch.

The batch is an execution grouping of already-written specs/plans.
Do not use the batch to redefine the project.

Rules:
- Bare output only.
- Do not change accepted specs.
- Do not expand batch scope.
- Do not execute specs/plans not listed in the batch.
- Do not modify files outside the referenced plans unless you stop and open a Change Request.
- Do not install dependencies without approval.
- Do not access the network without approval.
- Do not run destructive commands without approval.
- Do not touch files outside the repo.
- Run relevant tests/checks after each coherent implementation unit.
- Make atomic local commits when coherent units are complete.
- Continue through A0/A1 work without asking for approval.
- Do not stop after each spec, plan, or commit.

Human Approval Value Policy:
Human approval is required only when human judgment changes the outcome.

Continue automatically through the batch if:
- work remains inside the accepted batch,
- all required automated checks pass,
- no network/dependency/system/destructive action is needed,
- no human-verifiable behavior is being claimed complete,
- no Change Request is required,
- no A2/A3 gate is reached.

Stop only when:
- an A2 human checkpoint is reached,
- an A3 approval is required,
- tests/build fail and cannot be resolved within scope,
- a Change Request is needed,
- a usable/manual/physical test point has been reached,
- implementation requires files outside the batch,
- the batch stop condition is reached.

When stopping:
- ask one targeted question, or
- provide one review package.

Do not ask for generic approval.
Do not ask for approval merely because a local commit, spec, or plan is complete.

Completion response:
BATCH DONE

- Batch:
- Specs completed:
- Plans completed:
- Summary:
- Files changed:
- Local commits:
- Tests/checks run:
- Tests/checks not run:
- Docs updated:
- Deviations from batch:
- Change Requests opened:
- Deferred items:
- Remaining risks:
- Is the next step machine-verifiable or human-verifiable?
- Next recommended action:
```

## 6. Change Request prompt

```txt
Stop implementation.
Open a Change Request using docs/change-requests/_template.md.

Explain:
1. What assumption failed.
2. What the accepted spec/plan currently says.
3. What change is proposed.
4. Why implementation cannot continue cleanly without it.
5. Scope, file, test, docs, risk, and token/context impact.
6. Recommendation: accept, reject, or defer.

Do not edit code until the Change Request is accepted.
```

## 7. Review prompt

```txt
Mode: Review only.
Review the current diff against [SPEC path] and [PLAN path].
Do not implement fixes unless explicitly asked after the review.

Check:
1. Every acceptance criterion.
2. Unplanned files.
3. Scope creep.
4. Test adequacy.
5. Docs updates.
6. Dependency/security risk.
7. Naming, boundaries, duplication, dead code.

Return:
- Pass/fail.
- Blocking issues.
- Non-blocking improvements.
- Tests run or missing.
- Suggested PR summary.
```

## 8. Token audit prompt

```txt
Mode: Token audit only.
Inspect the repo's agent instructions and active task docs.
Do not edit files.

Return:
1. What is always loaded and should be shortened.
2. What should move into skills.
3. What output is too verbose.
4. What logs/tests should be filtered.
5. What repeated context should become durable docs.
6. A minimal edit plan to reduce token usage safely.
```

## 9. Dependency approval prompt

```txt
Mode: Dependency review only.
The implementation appears to need a new dependency.
Do not install anything yet.

Return:
1. Package name and exact version.
2. Why this dependency is necessary.
3. Alternatives considered.
4. License note.
5. Security/advisory considerations.
6. Transitive dependency impact if known.
7. Install command.
8. Files expected to change.
9. Rollback command.
```

## 10. PR creation prompt

```txt
Mode: PR preparation only.
Prepare the branch for PR.

Do:
1. Run scripts/agent/agent_finalize.sh.
2. Summarize final diff.
3. Ensure PR template is filled.
4. Confirm linked spec/plan/ADR/CRs.
5. Ask before pushing branch or opening PR if this is the first external side effect for this task.

Do not merge.
```
