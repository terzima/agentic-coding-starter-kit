# Spec Writing Reference

Use for `docs/specs/SPEC-*.md`.

## Purpose

A spec says what must be true. It should be precise enough that a plan can be written without inventing behavior, but it should not prescribe every implementation step.

## Outcome Picture

A spec must preserve the intended product or system picture, not only implementation facts. When the owner cares about a shape, experience, quality bar, workflow, or failure mode, capture that as accepted behavior or a non-goal.

Use examples only when they remove ambiguity. Do not turn examples into hard-coded implementation tracks unless the user explicitly requires that.

## Required Shape

- Context: source docs, current evidence, why this slice now.
- Problem: 1-3 concrete sentences.
- Goals and non-goals: short, scope-setting bullets.
- Users / actors: only actors that affect behavior.
- Behavioral contract: user-visible behavior, system responsibilities, explicitly unchanged behavior.
- Interface and data contract: exact names/shapes for files, modules, APIs, data, config, and errors when crossing boundaries.
- Requirements: functional and non-functional.
- Dependencies and approvals: task-specific only.
- Acceptance gates: automated, human, manual.
- Risks/open questions: only unresolved items that affect implementation.
- Stop conditions: when to pause or open a Change Request.

## Evidence Threshold

Accepted behavior must come from durable repo evidence: source docs, accepted Change Requests, ADRs, tests, current source, or a recorded spike/worklog. Prior chat can explain why the work is happening, but a spec must summarize the durable evidence it relies on.

If evidence is missing, make that an open question or require a Spike. Do not hide uncertainty in broad requirements.

## Repairable Boundaries

When a future plan might fail, the spec should make failure diagnosable:

- name the boundary that owns each important behavior;
- define what evidence proves the behavior;
- state when a failure needs a Change Request, Spike, owner decision, or scoped implementation fix;
- avoid blockers that only say "does not work" without a repair path.

## Good Detail

- Exact API route and response shape.
- Exact data model fields and required invariants.
- Exact error code/message contract.
- Exact product rule with examples only when ambiguity is likely.
- Testable acceptance gate.
- Human approval gate tied to real judgment.
- Stop condition that prevents scope creep.

## Bad Detail

- Step-by-step implementation order.
- Repo-wide permission or git policy copied from `AGENTS.md`.
- Large raw overview excerpts.
- Vague acceptance such as “works correctly” or “has tests.”
- Treating a spike result or manual experiment as accepted product behavior without capturing the contract.
- Hiding a product-quality requirement as a loose plan suggestion.

## Self-Review

- Can a planner identify the files and interfaces without rereading raw source?
- Does every requirement have a plausible automated, manual, or human gate?
- Are non-goals strong enough to prevent scope creep?
- Are open questions separated from accepted requirements?
- Are evidence gaps explicit enough that planning will not invent behavior?
- Would an exact plan execution produce the intended spec picture?
