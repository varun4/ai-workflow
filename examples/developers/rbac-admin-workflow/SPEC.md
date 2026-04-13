# RBAC Admin Endpoints Spec

## Objective

Add role-based access checks to selected admin endpoints so only
authorized roles can perform privileged actions.

## Scope

- Add role checks to:
  - `GET /admin/users`
  - `POST /admin/roles`
  - `GET /admin/audit`
- Add tests for allowed and denied role behavior.

## Non-Goals

- No auth provider migration.
- No admin UI redesign.
- No changes to non-admin endpoints.

## Constraints

- Preserve existing response formats and status code conventions.
- Unauthorized access must return `403` with existing error shape.
- Do not degrade existing endpoint latency beyond accepted limits.

## Success Criteria

- All scoped endpoints enforce role checks.
- Authorized roles pass existing and new tests.
- Unauthorized roles receive `403` in all scoped endpoints.
- Existing regression suite remains green.

## Validation

- Run endpoint auth tests and API regression tests.
- Confirm error response shape for denied requests.
- Complete release-readiness checklist before review.

## Scope Decomposition (Module 04)

### Phase 1: Plan

- Tasks:
  - confirm endpoint inventory in scope
  - confirm role matrix mapping
- Output:
  - scoped endpoint and role matrix note
- Checkpoint:
  - approve scope before implementation begins

### Phase 2: Implement

- Tasks:
  - apply role checks to scoped endpoints
  - update authorization middleware where needed
- Output:
  - RBAC code diff for scoped endpoints
- Checkpoint:
  - confirm no out-of-scope endpoint changes

### Phase 3: Validate

- Tasks:
  - run authorization allow/deny tests
  - run regression suite
- Output:
  - validation report and checklist results
- Checkpoint:
  - verify all acceptance criteria are satisfied

### Phase 4: Approve

- Tasks:
  - security review
  - merge approval
- Output:
  - recorded signoff
- Checkpoint:
  - stop if signoff is missing

## Context Architecture (Module 05)

### Required Context

- scoped endpoint inventory
- approved role matrix
- auth middleware paths
- acceptance criteria and test commands

### Excluded Context

- non-admin endpoint code
- deprecated architecture notes
- outdated exploratory diffs

### Source Precedence

1. approved spec and role matrix
2. current codebase files in scope
3. recent validated progress notes

### Refresh Triggers

- endpoint scope change
- role matrix change
- failed authorization validation

### Context Owner

- implementation lead maintains phase context package
- security reviewer confirms context completeness before approval

## Skills and Reusable Capabilities (Module 06)

### Skill Set

- `SKILL_SECURITY_REVIEW.md`
- `SKILL_RBAC_CONTEXT_REFRESH.md`

### Skill Invocation by Phase

- Plan: run `SKILL_RBAC_CONTEXT_REFRESH.md`
- Implement: run `SKILL_RBAC_CONTEXT_REFRESH.md`
- Validate: run `SKILL_RBAC_CONTEXT_REFRESH.md`, then
  `SKILL_SECURITY_REVIEW.md`
- Approve: run `SKILL_RBAC_CONTEXT_REFRESH.md`, then
  `SKILL_SECURITY_REVIEW.md`

### Skill Output Contract

- Context refresh output:
  - phase context note
  - escalation flag when blocking context issues exist
- Security review output:
  - review findings
  - approval recommendation

### Skill Revision Triggers

- role matrix schema changes
- endpoint scope changes
- recurring validation failures linked to stale context

## Evaluation and Failure Patterns (Module 07)

### Evaluation Objective

Detect and stop RBAC quality failures before merge approval.

### Evaluation Loop by Phase

- Plan:
  - Check: scoped endpoints and role matrix are complete.
  - Pass condition: scope and role map are approved.
  - Fail action: stop implementation and correct scope inputs.
- Implement:
  - Check: changes are limited to scoped endpoints and auth paths.
  - Pass condition: no out-of-scope edits.
  - Fail action: remove out-of-scope changes and rerun checkpoint.
- Validate:
  - Check: allow/deny auth tests and regression suite pass.
  - Pass condition: all scoped checks pass with expected response shape.
  - Fail action: map failure to pattern ID and execute recovery.
- Approve:
  - Check: no unresolved blocking failure patterns.
  - Pass condition: security signoff and merge approval recorded.
  - Fail action: block merge and escalate unresolved blockers.

### Embedded Failure Patterns

- `FP-RBAC-01` Out-of-scope endpoint change
  - Symptom: unrelated endpoint modified.
  - Root cause: scope boundary not enforced in Implement phase.
  - Detection signal: diff includes non-scoped files.
  - Prevention pattern: implement-phase scope gate.
  - Recovery action: remove out-of-scope edits and rerun checkpoint.
- `FP-RBAC-02` Missing deny-path enforcement
  - Symptom: denied role gets `200` instead of `403`.
  - Root cause: incomplete middleware mapping.
  - Detection signal: allow/deny test failure in Validate phase.
  - Prevention pattern: role matrix to endpoint mapping check.
  - Recovery action: patch auth path and rerun tests.
- `FP-RBAC-03` Approval without resolved blockers
  - Symptom: merge requested with unresolved security finding.
  - Root cause: approval gate bypass.
  - Detection signal: missing signoff evidence in Approve phase.
  - Prevention pattern: blocking approval checklist rule.
  - Recovery action: halt merge and require reviewer signoff.

### Evaluation Evidence Requirements

Record in `PROGRESS.md` for each phase:

- checkpoint name
- pass/fail decision
- failure pattern ID (if failed)
- recovery action and rerun result
