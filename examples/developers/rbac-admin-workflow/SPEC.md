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
