# Skill: RBAC Context Refresh

## Purpose

Refresh the RBAC context package before each workflow phase.

## Inputs

- `SPEC.md`
- current phase name
- latest `PROGRESS.md` entry
- approved role matrix
- scoped endpoint list

## Outputs

- phase context note:
  - required context
  - excluded context
  - source precedence
  - refresh-trigger check
- escalation flag if blocking context issue exists

## Constraints

- do not include non-admin endpoint scope
- stop if role matrix is missing or unapproved
- stop if context source conflict is unresolved

## Checklist

- required context is complete
- excluded context is explicit
- precedence order is applied
- refresh triggers are evaluated
- checkpoint decision is recorded

## Verification

- cross-check with `SPEC.md` context section
- cross-check with `EVAL_CHECKLIST.md` context quality gates
- record skill run in `PROGRESS.md`
