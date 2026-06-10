---
name: controlled-agentic-development
description: Use when creating or enforcing the repo's Discovery → Spec → Plan → Implementation → Review workflow, including Change Requests and documentation gates.
---

# Controlled Agentic Development Skill

Use this skill when the user asks for structured implementation, formal planning, repo process, specs, plans, or change control.

## Required behavior

1. Identify the current mode: Discovery, Spec, Plan, Implementation, or Review.
2. Do not combine modes unless explicitly instructed.
3. If implementation reveals scope drift, stop and create a Change Request.
4. Keep outputs concise and tied to repo files.
5. Reference existing templates in `docs/`.

## Mode deliverables

- Discovery: file map, patterns, risks, unknowns, next mode.
- Spec: goals, non-goals, acceptance criteria, constraints, open questions.
- Plan: file list, ordered steps, tests, docs, rollback, stop conditions.
- Implementation: code changes only within accepted plan; bare output.
- Review: diff vs spec/plan, blockers, tests, risks.

## Stop condition

If the task requires network, new dependencies, protected file changes, secrets, or broad scope expansion, stop and ask for approval or create a Change Request.
