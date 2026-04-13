# Module 07: Evaluation and Failure Patterns

## Learning Objectives

By the end of this module, learners will be able to:

- define an evaluation loop and failure pattern in plain language
- design phase-level pass/fail gates for workflow execution
- identify recurring failure patterns using explicit detection signals
- apply recovery and escalation rules when blocking failures occur
- use evaluation evidence to update workflow artifacts

## Core Concept

### Definition: Evaluation Loop and Failure Pattern

An evaluation loop is a repeated cycle of generate, check, decide, and
correct, executed at defined checkpoints.

A failure pattern is a recurring workflow miss documented with:
symptom, root cause, detection signal, prevention pattern, and
recovery action.

### Concrete Examples

Coding anchor:
- Expected: unauthorized roles return `403` on all scoped admin
  endpoints.
- Observed: one endpoint returns `200` for a denied role.
- Evaluation decision: fail Validate phase and block approval.
- Recovery: fix role-check path and rerun tests.

Knowledge-work anchor:
- Expected: each major recommendation claim has an approved citation.
- Observed: two claims have no approved source.
- Evaluation decision: fail Draft phase and block distribution.
- Recovery: add approved evidence or remove unsupported claims.

### Optional Metaphor

Evaluation loops are braking systems. Failure patterns are dashboard
error codes. Both are required for safe speed.

### Practical Implication

Without evaluation loops, teams accept plausible output.
Without failure patterns, the same defects repeat across sessions.

## Failure Mode

Common failure patterns in workflow design:

- evaluation happens only at the end
- pass/fail criteria are implicit or missing
- failures are logged as one-off incidents with no pattern ID
- blocking failures are treated as non-blocking
- recovery steps are undefined
- approvals happen before failed checks are resolved

## Good Pattern

Use a phase-level evaluation loop with explicit gates:

- define objective and pass/fail criteria before execution
- run checkpoint checks at each phase
- classify failures with reusable pattern IDs
- require recovery evidence before continuing
- escalate unresolved blocking failures at approval boundaries
- update spec and checklist artifacts from repeated failure evidence

## Bad Pattern

"We will review quality after drafting everything."

Problems:

- no early detection
- no deterministic stop conditions
- no failure reuse across future tasks
- no traceable reason for acceptance decisions

## Real Example

### Developer Track Example

- Phase: Validate
- Check: unauthorized role must return `403` for all scoped endpoints
- Failure pattern: `FP-RBAC-02` (missing deny-path enforcement)
- Recovery action: patch middleware mapping and rerun auth and
  regression tests
- Gate decision: continue only after check passes

### Knowledge-Worker Track Example

- Phase: Draft
- Check: each major claim must map to approved source evidence
- Failure pattern: `FP-VENDOR-03` (unsupported recommendation claim)
- Recovery action: attach approved citation or remove claim
- Gate decision: distribute only after validation pass

## Reflection Questions

1. Which checkpoint in your workflow currently lacks a clear pass/fail
   gate?
2. Which failure repeats most often but is not documented as a pattern?
3. Which recovery rule would prevent your most common rework cycle?
4. Which approval should be blocked by a stricter evaluation condition?

## Summary

Evaluation loops convert quality expectations into executable checks.
Failure patterns convert repeated mistakes into reusable prevention and
recovery logic.
