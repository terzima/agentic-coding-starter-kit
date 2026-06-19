# Batch Writing Reference

Use for `docs/plans/batches/BATCH-*.md`.

## Purpose

A batch groups already-written specs and plans for execution. It should be concise. It is not a replacement for either the spec or the plan.

## Required Shape

- Status, approval class, batch type, user-testable flag, human gate flag.
- Purpose: why these specs/plans belong together.
- Included work table: spec, plan, ADR, role.
- Scope summary: in/out.
- Execution contract: auto-continue, dependency/network approval, human checkpoint timing, special constraints.
- Required checks: exact commands from included plans.
- Human checks: only if human judgment adds value.
- Stop conditions: batch-specific.
- Commit strategy.
- Final report format.

Research checkpoints must not be mixed into normal implementation batches unless they share the same approval class and stop conditions. Prefer a separate spike or research batch when the output is evidence instead of shippable behavior.

## Good Detail

- Names of included specs/plans.
- Exact required commands.
- Human checkpoint timing.
- Approval-required actions unique to this batch.
- Expected final evidence.
- A2/A3 gate timing when human judgment, dependencies, network, deployment, or policy changes are involved.

## Bad Detail

- Repeating full plan tasks.
- Repeating `AGENTS.md` policy lists.
- Defining product behavior not already in specs.
- Using a batch to smuggle scope not present in included plans.
- Combining research failure handling with implementation work without a clear stop point.

## Self-Review

- Can the agent see what to execute first?
- Does every included plan have a matching spec?
- Are human gates tied to actual human judgment?
- Are stop conditions narrower than, or directly linked to, the included plans?
- Are research checkpoints separated from implementation checkpoints where approval classes differ?
