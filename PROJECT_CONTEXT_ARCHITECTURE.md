# Project Context Architecture

## Canonical Rule

This file defines how context is packaged and refreshed.
Normative policy text must live in one owner file.
Other files should reference owner files instead of restating rules.

## Agent Context Source Policy

- Load required sources from `AGENTS.md` -> `Required Context Sources`.
- Treat `README.md` as human onboarding only.
- If a required heading is missing, stop and ask.

## Rule Ownership Matrix

- Execution protocol and precedence: `AGENTS.md`
- Objective, scope, constraints, success criteria: `SPEC.md`
- Ask-first actions and stop conditions: `APPROVAL_BOUNDARIES.md`
- Quality gates and validation evidence: `EVAL_CHECKLIST.md`
- Evidence review method: `SKILL_EVIDENCE_REVIEW.md`
- Deterministic module done checks:
  `docs/standards/MODULE_DONE_CHECKLIST_TEMPLATE.md`
- Security guidance: `docs/governance/security.md`
- Boundary guidance: `docs/governance/approvals-and-boundaries.md`

## Context Package Contract (Required)

Before module work, define:

1. required context
2. excluded context
3. persistent context
4. source precedence
5. refresh triggers
6. context owners by phase
7. validation checks
8. security control map
9. adoption gate state
10. rollback context

## Source Precedence (Conflict Resolution)

Use the same precedence as `AGENTS.md`:

1. `AGENTS.md`
2. `APPROVAL_BOUNDARIES.md`
3. `EVAL_CHECKLIST.md`
4. `SPEC.md`
5. active module files under `course/modules/NN-*`
6. active track workflow files under `examples/...`
7. `PROGRESS.md`

This file does not override precedence.
If conflict remains unresolved, stop and ask.

## Refresh Triggers (Mandatory Rebuild)

Rebuild the context package when any of these occur:

- module scope or module number changes
- SOTA summary is approved
- source files in the ownership matrix change
- adoption stage changes (`sandbox`, `pilot`, `operational`)
- rollback trigger is activated or cleared
- validation failure occurs
- source conflict is detected
- before setting `MODULE_DONE_CHECKLIST.md` to PASS

## Validation Requirements

Before writing:

- context package is defined and complete
- active module and both track workflows are included

Before completion:

- refresh triggers were evaluated
- no unresolved source conflicts remain
- active security controls were applied for risky actions
- adoption gate decision and owner were recorded
- rollback trigger status and action were recorded
- context decisions and validation are logged in `PROGRESS.md`

## Anti-Duplication Rule

If a rule already exists in an owner file, reference it by path and
heading.
Do not duplicate the same normative bullet list in another context file.
