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
