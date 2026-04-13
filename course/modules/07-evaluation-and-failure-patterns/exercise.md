# Module 07 Exercise

## Scenario

You are reviewing two active workflows:

1. Coding workflow: RBAC checks for admin endpoints.
2. Knowledge-work workflow: vendor recommendation brief.

Each workflow has recurring quality misses and inconsistent acceptance
decisions. You must design a deterministic evaluation loop and embed
failure patterns in workflow artifacts.

## Task

For each anchor workflow, produce:

- phase-level evaluation gates with pass/fail criteria
- an embedded failure pattern catalog (minimum 3 patterns)
- recovery and escalation rules for blocking failures
- required evidence to log in progress artifacts

## Required Output Format

For each anchor, submit:

1. Evaluation loop table by phase (`Plan`, `Implement/Analyze`,
   `Validate`, `Approve`)
2. Failure pattern table with columns:
   - pattern ID
   - symptom
   - root cause
   - detection signal
   - prevention pattern
   - recovery action
3. Blocking gate definitions
4. Recovery runbook for one failed checkpoint
5. Approval decision rule with required evidence

## Evaluation Rubric

A strong submission should:

- define measurable pass/fail criteria per phase
- separate blocking and non-blocking checks
- use reusable failure pattern IDs
- define concrete recovery actions
- require explicit evidence before approval

## Debrief Questions

1. Which failure pattern had the highest downstream cost?
2. Which checkpoint most reduced false acceptance?
3. Which recovery action was most reliable?
4. What evidence should become mandatory in future reviews?
