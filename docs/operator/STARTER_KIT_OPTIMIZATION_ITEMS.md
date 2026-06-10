# Starter Kit Optimization Items

This document lists the optimization tasks that should be completed near the beginning of a new repo created from the agentic coding starter kit.

The goal is to reduce token usage, reduce approval noise, and make future agent sessions more deterministic.

---

## Phase 0 — Before seeding

Complete before running the large-spec seeding prompt.

### Required

- [ ] Copy starter-kit files into the repo.
- [ ] Confirm `AGENTS.md` exists.
- [ ] Confirm `README.md` exists.
- [ ] Confirm `PROMPT_LIBRARY.md` exists.
- [ ] Confirm `BOUNDARY_AND_SANDBOX_POLICY.md` exists.
- [ ] Confirm `docs/intake/` exists.
- [ ] Add `docs/intake/PROJECT_OVERVIEW_RAW.md`.
- [ ] Install repo-local Git hooks.
- [ ] Run agent setup verification script, if available.

### Recommended

- [ ] Confirm the agent is not running in full YOLO mode.
- [ ] Confirm network access requires approval.
- [ ] Confirm dependency installs require approval.
- [ ] Confirm local Git commits are allowed.
- [ ] Confirm Git push / PR creation requires approval unless explicitly authorized.

---

## Phase 1 — Seeding optimization

Complete during or immediately after seeding.

### Required

- [ ] Create project charter.
- [ ] Create foundation spec.
- [ ] Create repo map.
- [ ] Create roadmap.
- [ ] Create glossary if terms exist.
- [ ] Create seeding results/worklog.
- [ ] Create first 1–3 implementation specs only.
- [ ] Create first 1–3 implementation plans only.
- [ ] Create first 1–2 proposed batches only.

### Guardrails

- [ ] Do not create full specs/plans for the entire project.
- [ ] Do not write application code.
- [ ] Do not install dependencies.
- [ ] Do not access the network.
- [ ] Do not use framework generators.

---

## Phase 2 — Application scaffold optimization

Complete during the first implementation batch.

### Required

- [ ] Create backend/frontend/shared/test directories as applicable.
- [ ] Create `.env.example` if environment variables are expected.
- [ ] Create `docs/setup/local-prerequisites.md`.
- [ ] Create or update project README setup instructions.
- [ ] Create canonical command surface, usually `Makefile` or package scripts.
- [ ] Create `scripts/dev/check_prerequisites.sh`.
- [ ] Create `scripts/dev/run_all_checks.sh`.

### Guardrails

- [ ] Do not implement product behavior yet.
- [ ] Do not install dependencies without approval.
- [ ] Do not make deployment decisions unless already accepted.
- [ ] Do not commit secrets.

---

## Phase 3 — Agent context optimization

Complete before heavy implementation begins.

### Required

- [ ] `docs/repo-map.md` tells agents what to read first.
- [ ] `docs/repo-map.md` tells agents what not to casually modify.
- [ ] `AGENTS.md` remains concise.
- [ ] Long process explanations live in docs or skills, not repeated prompts.
- [ ] Implementation prompts reference paths instead of pasting long content.
- [ ] `PROJECT_OVERVIEW_RAW.md` is no longer required for routine work.

### Recommended

- [ ] Add a `print_agent_context.sh` script if agents frequently ask what to read.
- [ ] Add an `audit_specs_plans.sh` script if spec/plan drift becomes common.
- [ ] Add an `audit_docs.sh` script if README/repo-map drift becomes common.

---

## Phase 4 — Approval optimization

Complete once the first batch is ready.

### Required

- [ ] A0/A1/A2/A3 approval classes are documented.
- [ ] Batches say whether they are machine-verifiable or human-verifiable.
- [ ] Agents are told not to stop after every commit/spec/plan.
- [ ] Agents stop only for A2/A3 gates, failed checks, Change Requests, or user-testable checkpoints.

### Approval policy summary

```txt
A0 — no human approval needed
A1 — batch approval only
A2 — human checkpoint required
A3 — hard approval required
```

---

## Phase 5 — Validation optimization

Complete once real code exists.

### Required

- [ ] One command runs all required checks.
- [ ] CI mirrors local checks where practical.
- [ ] README documents local commands.
- [ ] Agents use documented scripts instead of guessing.
- [ ] PR template asks for linked spec/plan/batch.
- [ ] PR template asks for tests/checks run.
- [ ] PR template asks for deviations and risks.

---

## Done state

The repo is optimized for agentic work when:

- future agents know what to read,
- future agents know what not to read,
- implementation uses specs/plans/batches instead of raw overview,
- repeated commands are scripts,
- repeated instructions are docs,
- approval requests are rare and meaningful,
- dependency/network/system actions require approval,
- local repo work can proceed without low-value interruptions.
