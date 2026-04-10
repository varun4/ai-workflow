# Module 06 Delta

## Concept Applied

- Skills and reusable capabilities.

## Files Updated

- `SPEC.md`
- `EVAL_CHECKLIST.md`
- `README.md`
- `SKILL_EVIDENCE_CONTEXT_REFRESH.md`

## Before -> After (Key Changes)

- Context quality depended on ad hoc practice -> reusable evidence-
  context-refresh skill added with explicit trigger points.
- Validation checked recommendation quality only -> skill invocation and
  verification checks added.

## Demonstration Scenario

- Input: run recommendation workflow through Plan, Analyze, Draft,
  Validate, and Approve phases.
- Expected: evidence context-refresh skill runs at each phase and
  records outputs before downstream work continues.
- Actual: skill contract and phase invocation map are now explicit.

## Validation Evidence

- Checks run: markdown lint on changed files.
- Result: pass.

## Impact

- Reliability gain: higher consistency of source quality checks across
  phases.
- Risk reduced: stale or non-approved evidence before recommendation
  validation.
- Remaining gap: add skill quality trend tracking in Module 07.
