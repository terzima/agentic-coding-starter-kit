# Intake And Seeding Reference

Use when a project starts from a large raw overview, brainstorming document, or owner-provided project summary.

## Purpose

Seeding converts raw source material into durable project context. It is not implementation and it is not a license to fully plan the entire product.

Seeding produces source-of-truth docs, early specs/plans only where clear, open questions, ADR candidates, and a carry-forward worklog. Batch execution comes later, after specs and plans exist and are accepted.

## Inputs

- `AGENTS.md`
- `docs/intake/PROJECT_OVERVIEW_RAW.md` or a named intake file approved by the user.

Optional inputs, if present:

- `AGENTS.md`
- existing templates under `docs/`
- prior research notes or owner-provided constraints
- existing repo notes or architecture notes
- existing repo files only if the project is already partly scaffolded

Do not require optional inputs when the raw overview is sufficient. Do not read raw intake during routine implementation.

## Outputs

Create or update only useful startup docs:

- `docs/project-charter.md`
- `docs/glossary.md`
- `docs/repo-map.md`
- `docs/roadmap.md`
- `docs/status/CURRENT_STATE.md`
- `docs/seed/SEED-0000-project-decomposition.md`
- `docs/seed/SEED-0000-results.md`
- `docs/worklog/0000-seeding-notes.md`
- `docs/specs/SPEC-0000-project-foundation.md`
- the first 1-3 implementation specs only if clear
- matching first 1-3 implementation plans only if clear
- at most 1-2 proposed batches
- `docs/adr/ADR-0000-architecture-direction.md` only when a decision is explicit or strongly implied

Do not create application code, production source files, dependency manifests, generated framework files, runtime config, or deployment files unless the user explicitly requests that separate mode.

## Extraction Rules

Separate:

- confirmed requirements;
- assumptions;
- non-goals;
- implementation guesses;
- contradictions;
- open questions;
- risks;
- deferred ideas;
- ADR candidates;
- future spec candidates.

Preserve intent, but do not invent missing architecture, product behavior, or dependencies.

## Depth Rules

- M1 for broad orientation docs.
- M2 for near-term specs with clear requirements and gates.
- M3 or M4 only for the first implementation-safe plans.
- Roadmap language for speculative or later work.

Do not create full specs/plans for every feature mentioned in raw intake.

## Document Guidance

- Project charter: purpose, target users, core problem, goals, non-goals, success criteria, constraints, and first meaningful human-testable milestone.
- Glossary: domain terms, project terms, acronyms, and ambiguous terms that need clarification.
- Repo map: expected top-level structure, directory responsibilities, architecture boundaries, first-read files, do-not-touch files, and known verification commands.
- Foundation spec: highest-level controlled contract for problem, confirmed requirements, product boundaries, technical boundaries, non-goals, assumptions, open questions, acceptance criteria, and first implementation slice.
- Initial specs: create only when the scope, boundaries, requirements, gates, dependencies, approval class, and stop conditions are clear.
- Initial plans: create only for accepted or clearly approvable specs where expected files, steps, validation, docs updates, risks, and stop conditions can be named without invention.
- Proposed batches: group related accepted specs/plans; never use a batch as a replacement for missing specs or plans.
- Roadmap: show sequence, dependencies, approval class, first human checkpoint, machine-verifiable work, and human-verifiable work.
- ADR: create only when the intake explicitly states or strongly implies a real architecture decision.

## First Slice Guidance

If the repo has governance docs but no application scaffold, the first implementation spec is usually `SPEC-0001-application-scaffold.md`.

The first scaffold slice should define directories, command surface, local prerequisites, placeholder checks, environment-file policy, README setup, and test structure. It should not implement product behavior or external integrations.

## Stop Conditions

Stop when:

- raw intake contradicts itself in a way that blocks decomposition,
- core product behavior cannot be inferred without invention,
- an architecture decision is required but not stated or strongly implied,
- implementation code would be needed,
- dependencies or network access would be needed,
- requested output paths are outside the approved seeding set.

## Self-Review

- Is the raw overview now source material rather than routine context?
- Are near-term docs specific enough for the first implementation slice?
- Is later work kept as roadmap/spec candidates?
- Are assumptions and open questions visible?
- Did seeding avoid creating a wall of speculative docs?
