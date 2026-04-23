# Project Spec

## Objective

Build a practical, reusable AI workflow course for developers and
knowledge workers.

## Scope

- Build and refine content under `docs/`, `course/`, `templates/`,
  `examples/`, `tracks/`, and `sessions/`.
- Maintain project operating artifacts and progress tracking.

## Non-Goals

- No publishing infrastructure or site generator setup.
- No CI tooling additions unless explicitly approved.

## Constraints

- Follow preview-first content approval.
- Follow definition-first writing.
- Use `PROJECT_CONTEXT_ARCHITECTURE.md` for context package design,
  source precedence, owners, and refresh triggers.
- Use `APPROVAL_BOUNDARIES.md` for ask-first and stop conditions.
- Use `EVAL_CHECKLIST.md` for blocking gates and validation evidence.
- Keep shared framework in `docs/` and split by audience mainly in
  `tracks/`, `templates/`, and `examples/`.

### Scope Decomposition Principles

For multi-step work:

- use bounded phases and tasks
- keep one concrete output per task
- insert explicit checkpoints before risky actions

Reference: `docs/reliability/scope-decomposition.md`.

### Evaluation and Failure Pattern Principles

- Define evaluation objective and pass/fail criteria before execution.
- Map failed checkpoints to `FP-PROJECT-*` pattern IDs.
- Record symptom, root cause, detection signal, prevention pattern, and
  recovery action for each blocking failure.
- Stop progression until recovery evidence and rerun results exist.
- Update workflow artifacts when failure patterns repeat.

Reference: `docs/reliability/failure-patterns.md`.

### Security and Adoption Principles

- Map each high-risk action to control rule, required approval, and stop
  condition.
- Use least-privilege defaults and staged adoption gates:
  `sandbox`, `pilot`, `operational`.
- Record named owner decisions and rollback trigger status.

Reference: `docs/governance/security.md` and
`docs/governance/approvals-and-boundaries.md`.

### Module Automation Constraints

- Use the module generation contract in `AGENTS.md`.
- Use one `MODULE_DONE_CHECKLIST.md` per module from
  `docs/standards/MODULE_DONE_CHECKLIST_TEMPLATE.md`.
- Apply definition-first writing in this sequence:
  1. definition
  2. concrete example
  3. optional metaphor
  4. practical implication
- Apply scope decomposition principles for multi-step module work.

## Success Criteria

- Module content is practical, measurable, and aligned with module
  rules.
- Artifacts are reusable and internally consistent.
- Validation is run and reported before completion.
- Evaluation decisions are traceable with explicit checkpoint outcomes.
- Recurring failures trigger updates to prevention patterns and rules.
- Security controls and adoption gate decisions are explicit.

### Module Output Rule

Canonical output rule: `AGENTS.md` -> `## Module Output Rule`.

For this project, module work must update both track workflows, both
`deltas/module-NN.md` files, both `MODULE_UPDATES.md` files, and
`PROGRESS.md`.

### Module Completion Criteria

A module is complete only when deterministic checks in
`docs/standards/MODULE_DONE_CHECKLIST_TEMPLATE.md` pass and blocking
quality/output gates in `EVAL_CHECKLIST.md` pass.

## Validation

- Run markdown checks on changed files.
- Run link/path/internal reference checks with
  `python3 scripts/check_markdown_links.py .`.
- Run context duplication checks with
  `python3 scripts/check_context_duplication.py` when context files
  change.
- Record validation commands and results in `PROGRESS.md`.
