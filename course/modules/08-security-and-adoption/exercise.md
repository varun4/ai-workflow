# Module 08 Exercise

## Scenario

Your team wants to operationalize two workflows:

1. Coding workflow for RBAC admin endpoint changes.
2. Knowledge-work workflow for vendor recommendation briefs.

Both workflows have solid outputs in controlled conditions, but
neither has complete security controls or adoption gates for broader
rollout.

## Task

For each anchor workflow, design:

- a security control map for high-risk actions
- a phased adoption plan with explicit gate criteria
- escalation and rollback rules for blocking failures
- owner assignments for go/no-go decisions

## Required Output Format

For each anchor, submit:

1. Security control table with columns:
   - risky action
   - control rule
   - required approval
   - stop condition
2. Adoption gate table with columns:
   - gate name
   - entry criteria
   - required evidence
   - decision owner
   - exit decision (go/no-go)
3. Rollback trigger list (minimum 3 triggers)
4. One escalation runbook for a blocked gate
5. Final readiness statement:
   - approved for next gate or blocked, with reason

## Evaluation Rubric

A strong submission should:

- define explicit controls for concrete risky actions
- separate security controls from adoption gates clearly
- define measurable gate criteria and required evidence
- define clear rollback triggers and escalation ownership
- provide a defensible go/no-go decision

## Debrief Questions

1. Which risky action required the strongest control?
2. Which gate evidence was hardest to define and why?
3. Which rollback trigger is most likely in your real workflow?
4. What control gap remains before full adoption?
