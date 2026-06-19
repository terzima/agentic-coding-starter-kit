---
name: spike-research
description: Use when the next step is bounded research, local experimentation, or evidence gathering before a spec, plan, or implementation can be written safely.
---

# Spike Research

Use this skill when the project needs evidence before it can make a durable decision. A Spike produces findings and a promotion rule, not accepted implementation behavior.

## Core Rule

Define the question before researching. Evidence from a Spike must be captured in a spec or plan before it becomes accepted behavior.

## Workflow

1. State the question or hypothesis in one sentence.
2. Name the allowed files, surfaces, tools, and commands.
3. Name evidence to collect before starting.
4. Set a budget or kill criteria.
5. Choose an output destination, usually `docs/worklog/` or a concise report in the current response.
6. Run only the bounded research or local experiment needed for the question.
7. Record results separately from accepted requirements.
8. State the promotion rule: what must be captured in a spec or plan before implementation resumes.
9. Recommend exactly one next prompt.

## Stop Conditions

Stop and report the blocker when:

- the question is too broad to answer within the budget;
- research requires network, dependency, secret, deployment, remote Git, or external-service access without approval;
- the Spike starts producing product behavior instead of evidence;
- the evidence shows the accepted spec or plan needs a Change Request.

## Output Contract

```txt
Question or hypothesis:
Allowed scope:
Evidence to collect:
Budget or kill criteria:
Output destination:
Promotion rule:
Result:
Recommended next prompt:
```

## What To Avoid

- Letting research sprawl into implementation.
- Treating a successful experiment as accepted behavior.
- Reading unrelated source files because the question is vague.
- Omitting kill criteria.
- Ending with multiple possible next prompts.
