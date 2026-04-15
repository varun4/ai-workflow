# Module 08: Security and Adoption

## Learning Objectives

By the end of this module, learners will be able to:

- define security controls and adoption controls in plain language
- identify high-risk actions and map them to explicit approval gates
- design a phased adoption plan with measurable entry and exit
  criteria
- apply least-privilege and escalation rules to both anchor
  workflows
- evaluate go/no-go readiness using security and adoption evidence

## Core Concept

### Definition: Security and Adoption Controls

Security controls are explicit workflow rules that prevent unsafe
actions or force escalation before risky actions proceed.

Adoption controls are explicit rollout gates that decide when a
workflow is ready to move from test use to broader operational use.

### Concrete Examples

Coding anchor:

- RBAC endpoint changes require approval before merge.
- Permission broadening is blocking unless approved by security owner.
- Rollout moves from sandbox tests to pilot endpoints before full
  scope.

Knowledge-work anchor:

- Vendor recommendation drafts require citation and sharing controls.
- Distribution outside approved stakeholders is blocked before
  signoff.
- Rollout moves from internal review to limited leadership use before
  broader policy use.

### Optional Metaphor

Security controls are the brakes and guardrails.
Adoption controls are the lane-merging lights.

### Practical Implication

A workflow is not production-ready because it works once.
It is ready when risky actions are constrained and rollout gates are
explicit.

## Failure Mode

Common failure patterns:

- broad permissions granted without explicit approval
- secrets or sensitive details included in outputs
- risky actions executed before checkpoint review
- pilot and production scopes mixed without guardrails
- no rollback rule when quality or safety checks fail
- adoption decisions based on confidence, not evidence

## Good Pattern

Use a control stack with phase-level gates:

- define high-risk actions and required approvals
- define least-privilege access boundaries
- define data handling rules and prohibited content paths
- define escalation and stop conditions for blocking risks
- define phased rollout gates (sandbox, pilot, production)
- define rollback triggers and owners for each gate

## Bad Pattern

"Ship now, harden later."

Problems:

- unsafe behavior can reach real users
- no deterministic stop conditions
- unclear accountability for risky outcomes
- no evidence-based adoption decision

## Real Example

### Developer Track Example

Security controls:

- Block merge when unresolved `FP-RBAC-*` blocker exists.
- Block permission broadening without security signoff.
- Require explicit validation evidence before release approval.

Adoption controls:

- Gate 1 (sandbox): all scoped tests pass in isolated environment.
- Gate 2 (pilot): no blocker failures across pilot endpoints.
- Gate 3 (production): service owner and security approvals recorded.

Rollback triggers:

- repeated deny-path failures
- unexpected permission expansion
- unresolved high-severity security finding

### Knowledge-Worker Track Example

Security controls:

- Block non-approved source usage for major claims.
- Block external distribution without stakeholder and director
  approval.
- Require claim-to-citation traceability before approval.

Adoption controls:

- Gate 1 (internal draft): evidence quality checks pass.
- Gate 2 (limited leadership review): no unresolved `FP-VENDOR-*`
  blockers.
- Gate 3 (operational use): approved distribution scope and governance
  owner assigned.

Rollback triggers:

- unsupported major claims
- confidentiality boundary breach
- missing approval records

## Reflection Questions

1. Which risky action in your workflow currently lacks an explicit
   gate?
2. Which rollout decision is currently based on opinion instead of
   evidence?
3. What rollback trigger should be mandatory before wider adoption?
4. Which owner should be accountable for final go/no-go decisions?

## Summary

Security controls prevent unsafe actions.
Adoption controls prevent unsafe rollout.
Reliable workflows need both.
