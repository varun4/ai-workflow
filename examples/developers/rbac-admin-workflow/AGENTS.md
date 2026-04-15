# Example AGENTS.md (Developer Workflow)

## Scope

- Work only in the API service repository area for RBAC changes.
- Limit edits to endpoint authorization checks and related tests.

## Allowed Without Prompt

- Read code and tests needed for admin endpoint authorization.
- Implement role-check logic in scoped endpoints.
- Add or update tests for authorized and unauthorized role behavior.
- Run approved test commands.

## Ask First

- Changing role model definitions.
- Modifying auth provider integration.
- Making database schema changes.
- Disabling existing security checks.
- Merging or deploying changes.
- Promoting rollout from sandbox to pilot.
- Promoting rollout from pilot to production.
- Overriding a blocking security or adoption gate.
- Skipping a rollback trigger after a failed gate.

## Delivery Rules

- Keep diffs scoped to RBAC endpoint checks.
- Record meaningful implementation steps in `PROGRESS.md`.
- Report validation results before requesting review.
