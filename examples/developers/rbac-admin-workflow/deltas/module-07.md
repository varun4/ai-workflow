# Module 07 Delta

## Concept Applied

- Evaluation loops and failure pattern management.

## Files Updated

- `SPEC.md`
- `EVAL_CHECKLIST.md`
- `README.md`

## Module Takeaway Diff

- Before: evaluation relied on static checklist completion with limited
  failure reuse.
- After: phase-level evaluation loop and embedded `FP-RBAC-*` failure
  patterns define detection, prevention, recovery, and approval gates.

## Demonstration Scenario

- Input: RBAC workflow with a deny-path bug on one endpoint.
- Expected: Validate phase fails, bug maps to `FP-RBAC-02`, recovery
  runs, tests rerun, and approval remains blocked until pass.
- Actual: evaluation loop and failure pattern mapping are now explicit
  in workflow artifacts.

## Validation Evidence

- Checks run: markdown lint on changed files.
- Result: pass.

## Impact

- Reliability gain: checkpoint decisions are measurable and traceable.
- Risk reduced: plausible but unsafe output passing to approval.
- Remaining gap: security and adoption controls in Module 08.
