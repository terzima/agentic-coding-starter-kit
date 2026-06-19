---
name: spec-plan-alignment
description: Use when reviewing whether an implementation plan will deliver its linked accepted spec without editing either document; returns a finite alignment verdict and one recommended next prompt.
---

# Spec Plan Alignment

Use this skill to answer one question:

```txt
If an agent executes this plan exactly, will the result match the linked spec's intended outcome?
```

## Core Rule

Report alignment; do not fix it. The skill prevents endless plan polish by naming only blockers that affect whether exact execution delivers the spec picture.

## Workflow

1. Read the linked accepted spec and the plan under review.
2. Translate the spec into a plain-language `Spec picture`.
3. State the `Plan result`: what the plan would actually produce if implemented literally.
4. Compare required outcomes, non-goals, interfaces, files, gates, stop conditions, and approvals.
5. Classify the plan with one verdict.
6. Return one recommended next prompt unless the verdict is `approval-ready` and approval is the obvious next action.

## Verdicts

Use exactly one:

```txt
approval-ready
targeted-edits-needed
spec-change-needed
spike-needed
begin-with-known-risk
```

## Blocking Findings

Only treat these as blocking:

- the plan would not deliver a required spec outcome;
- the plan adds unsupported scope;
- required validation is missing or not tied to acceptance gates;
- implementation choices left open could materially change the outcome;
- the plan relies on unstated assumptions, missing approvals, or missing evidence.

## Stop Conditions

Stop when:

- the spec is not accepted;
- the plan has no linked spec;
- the requested review asks you to directly edit the spec or plan;
- the plan cannot be assessed without a Spike or missing source document.

## Output Contract

```txt
Verdict:
Spec picture:
Plan result:
Alignment table:
Blocking gaps:
Invented scope:
Weak gates:
Non-blocking improvements:
Recommended next prompt:
```

Cap `Non-blocking improvements` at three items.

## What To Avoid

- Editing either document.
- Rewriting plan sections in the report.
- Requiring changes merely because the plan could be more elegant.
- Producing an open-ended list of improvements.
- Treating taste, wording, or polish as blockers when delivery would still match the spec.
