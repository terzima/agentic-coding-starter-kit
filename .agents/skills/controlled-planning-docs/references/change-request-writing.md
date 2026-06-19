# Change Request Writing Reference

Use for `docs/change-requests/CR-*.md`.

## Purpose

A Change Request records why accepted scope cannot continue cleanly. It is the controlled way to change direction after implementation starts.

## Trigger Types

- Implementation discovery: code or tests reveal the accepted contract is wrong or incomplete.
- Research failure: a spike or attempted approach does not produce enough evidence to proceed.
- Product decision: the owner changes desired behavior or priority.
- Policy/tooling limitation: hooks, CI, permissions, deployment, or tooling block the accepted path.

## Required Shape

- Trigger: what happened, with evidence.
- Current accepted spec/plan says: the relevant accepted contract.
- Proposed change: the new contract or scope adjustment.
- Why necessary: why continuing without the change would be unsafe or misleading.
- Impact: scope, files, tests, docs, dependencies, security/privacy, token/context, and timeline or PR size.
- Options considered: accept, reject, defer.
- Recommendation: one clear recommendation.
- Decision: owner decision and rationale.

## Good Detail

- Specific failed assumption.
- Exact accepted doc section or plan task affected.
- File/test/docs impact.
- What becomes in scope and what stays out of scope.
- Whether new approval class or human gate is needed.

## Bad Detail

- Rewriting the whole spec inside the CR.
- Treating the CR as implementation.
- Hiding unresolved questions.
- Saying only “update the plan” without naming what changed.

## Self-Review

- Can the owner decide accept/reject/defer from this file alone?
- Does it explain why the current plan cannot continue?
- Does it preserve reviewability by limiting scope?
- Does it identify follow-up spec/plan hardening if accepted?
