# SPEC-0000: Project Foundation

Status: Draft
Owner: TBD
Created: YYYY-MM-DD
Updated: YYYY-MM-DD
Related plan: `docs/plans/PLAN-0000-repo-bootstrap.md`

## Problem statement

The repository needs a controlled foundation before application implementation begins.

## Goals

- Establish agent instructions and process control.
- Seed project context from the raw project overview.
- Create review, CI, hook, and documentation scaffolding.
- Define the first implementable project slice.

## Non-goals

- Implementing production application features.
- Finalizing every architecture decision.
- Adding dependencies before review.

## Acceptance criteria

- [ ] `AGENTS.md` exists and defines operating modes, scope control, token discipline, and sandbox rules.
- [ ] Documentation templates exist for specs, plans, ADRs, Change Requests, and worklogs.
- [ ] Git hooks and CI policy checks exist.
- [ ] The raw project overview is stored in `docs/intake/PROJECT_OVERVIEW_RAW.md`.
- [ ] A first implementation slice is identified in a follow-up spec.

## Open questions

- [ ] What application stack will be used?
- [ ] What deployment target will be used?
- [ ] What data store, if any, is required?
