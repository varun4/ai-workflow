# Evaluation Checklist

## Correctness

- All scoped endpoints enforce role checks.
- Authorization logic matches approved role matrix.

## Completeness

- All scoped endpoints are covered by tests.
- Both allow and deny flows are validated.

## Constraint Compliance

- Error responses preserve expected schema.
- No out-of-scope endpoint changes were made.

## Safety

- No permission broadening without approval.
- No security control regressions detected.

## Approval

- Security reviewer signoff recorded.
- Merge approval captured.

## Decomposition Quality

- Each phase has bounded tasks.
- Each phase has one concrete output.
- Each phase has a checkpoint decision.
- Escalation conditions are explicit at approval gates.

## Context Quality

- Required context set is complete for current phase.
- Excluded context set removes irrelevant files and notes.
- Source precedence is applied when context conflicts.
- Context refresh triggers are evaluated at each checkpoint.

## Skill Quality

- Required skills were invoked at defined phase checkpoints.
- Skill output artifacts were produced and logged.
- Skill constraints and stop conditions were respected.
- Skill verification steps were completed and recorded.

## Evaluation Loop Quality

- Plan, Implement, Validate, and Approve phases each have explicit
  pass/fail decisions.
- Blocking failures stop progression until recovery evidence is
  recorded.
- Approval is blocked when any blocking failure remains unresolved.

## Failure Pattern Checks

- Every failed checkpoint is mapped to a `FP-RBAC-*` pattern ID in
  `SPEC.md`.
- Detection signals are recorded for each failure.
- Recovery action and rerun result are recorded before closure.
- Repeated failures trigger prevention updates in workflow artifacts.

## Security Control Checks

- High-risk actions map to explicit controls in `SPEC.md`.
- Ask-first boundaries were enforced before risky actions.
- No permission broadening occurred without required signoff.
- Release is blocked when unresolved blocking failures exist.

## Adoption Gate Checks

- Sandbox gate evidence is recorded before pilot entry.
- Pilot gate evidence is recorded before production entry.
- Gate decisions include named owner and go/no-go outcome.
- Rollback triggers were evaluated before each gate exit.
- Production release is blocked when gate evidence is incomplete.
