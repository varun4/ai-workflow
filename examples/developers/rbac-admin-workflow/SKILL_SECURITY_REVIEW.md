# Skill: RBAC Security Review

## Purpose

Provide a repeatable review checklist for role-based endpoint changes.

## Inputs

- Scoped spec
- Changed endpoint files
- Test output

## Outputs

- Security review notes
- Required fixes (if any)
- Approval recommendation

## Constraints

- Review only scoped endpoints and related authorization paths.
- Flag any broadened permissions as blocking.

## Checklist

- Verify denied roles always return `403`.
- Verify allowed roles still support expected workflows.
- Check for bypass paths in middleware or controller logic.
- Confirm test coverage for both allow and deny paths.
- Confirm no sensitive data exposure in denied responses.

## Verification

- Cross-check findings with `EVAL_CHECKLIST.md` results.
- Require explicit approval for unresolved high-severity findings.
