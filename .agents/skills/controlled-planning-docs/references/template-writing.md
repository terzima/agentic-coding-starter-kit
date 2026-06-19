# Template Writing Reference

Use when creating or revising templates under `docs/`.

## Purpose

Templates should help a user write the right document without making every future document verbose. They should be forms plus short guidance, not policy manuals.

## Template Rules

- Keep reusable policy in `AGENTS.md`.
- Keep detailed writing guidance in `.agents/skills/controlled-planning-docs/references/`.
- Include a short “How to write this” section only when it prevents confusion.
- Tell users to remove guidance sections before acceptance or finalization.
- Avoid repeated placeholder values.
- Prefer stable headings over long examples.
- Use examples only when they prevent likely ambiguity.

## Planning-Fidelity Template Fields

For plan templates, include optional prompts for:

- Spec Picture.
- Plan Result.
- Proof Strategy.
- Failure Ownership.
- No-Drift Gates.
- Expected Failure / Expected Pass.

Keep these prompts short. They should remind the writer to compare the plan against the spec picture, not force every small docs-only plan into a long ceremony.

## Good Template Guidance

- What this document is for.
- Which reference file to read.
- What sections are required.
- What to remove before acceptance.
- What not to include.
- When optional fidelity fields are useful.

## Bad Template Guidance

- Full copies of `AGENTS.md`.
- Long prompt libraries.
- Product-specific examples from another repo.
- Stale starter-kit instructions.
- Placeholder-heavy docs that look complete while saying little.
- Large exemplars that future agents will paste forward instead of distilling.

## Self-Review

- Can a new user tell what to write next?
- Will the generated document be concise after guidance is removed?
- Does the template point to the right reference instead of duplicating it?
- Does the template avoid project-specific history?
- Does optional guidance help the writer stop drift without bloating simple docs?
