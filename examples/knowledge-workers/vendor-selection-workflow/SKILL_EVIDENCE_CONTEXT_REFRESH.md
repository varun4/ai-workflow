# Skill: Evidence Context Refresh

## Purpose

Refresh the evidence context package before analysis and briefing phases.

## Inputs

- `SPEC.md`
- current phase name
- latest `PROGRESS.md` entry
- approved source list
- current scoring rubric

## Outputs

- phase evidence context note:
  - approved sources in use
  - excluded sources
  - source precedence
  - refresh-trigger check
- escalation flag if evidence context is incomplete or conflicting

## Constraints

- do not use non-approved sources
- stop if citation basis is missing for major claims
- stop if source conflict cannot be resolved by precedence rules

## Checklist

- approved source set is complete
- excluded source set is explicit
- precedence rules are applied
- refresh triggers are evaluated
- checkpoint decision is recorded

## Verification

- cross-check with `SPEC.md` context section
- cross-check with `EVAL_CHECKLIST.md` context quality gates
- record skill run in `PROGRESS.md`
