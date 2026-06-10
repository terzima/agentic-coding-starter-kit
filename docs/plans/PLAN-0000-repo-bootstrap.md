# PLAN-0000: Repo Bootstrap

Status: Draft
Owner: TBD
Created: YYYY-MM-DD
Updated: YYYY-MM-DD
Related spec: `docs/specs/SPEC-0000-project-foundation.md`

## Scope

Bootstrap the controlled agentic development process and documentation scaffold.

## Preconditions

- [ ] Repository created.
- [ ] Starter files copied.
- [ ] No application code implementation has started.

## Files expected to change

- `AGENTS.md`: agent operating rules.
- `docs/`: controlled documentation scaffold.
- `.github/`: PR and CI gates.
- `.githooks/`: local Git safety hooks.
- `.codex/`, `.claude/`, `.cursor/`: optional tool adapters.
- `scripts/agent/`: deterministic workflow helpers.

## Implementation steps

1. Install scaffold files.
2. Install local Git hooks.
3. Commit scaffold.
4. Paste large raw overview into `docs/intake/PROJECT_OVERVIEW_RAW.md`.
5. Run seeding prompt in Spec mode only.
6. Review generated seed docs.
7. Accept first application spec and plan.

## Test plan

- Run `scripts/agent/agent_preflight.sh`.
- Run `bash -n scripts/agent/*.sh .githooks/*`.
- Run `python3 -m py_compile scripts/agent/*.py .codex/hooks/*.py`.

## Documentation plan

- Update `docs/project-charter.md`.
- Update `docs/repo-map.md` once stack is chosen.

## Stop conditions requiring Change Request

- Application code is requested before seed docs are accepted.
- A new dependency is required.
- Network access is required.

## Risks

- Risk: Overbuilding process.
  - Mitigation: Use only one spec and one plan per small slice.
