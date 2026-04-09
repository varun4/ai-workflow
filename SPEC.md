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
- Follow `PROJECT_CONTEXT_ARCHITECTURE.md` for context package design,
  source precedence, phase owners, and refresh triggers.
- Keep shared framework in `docs/` and split by audience mainly in
  `tracks/`, `templates/`, and `examples/`.

### Scope Decomposition Principles

- Separate architecture from implementation.
- Separate scaffold from content depth.
- Break work into bounded phases and tasks.
- Keep one concrete output per task.
- Insert checkpoints before risky actions.
- Define escalation and approval gates explicitly.

### Module Automation Constraints

- Use the module generation contract for all new module work.
- Use `docs/standards/MODULE_DONE_CHECKLIST_TEMPLATE.md` and keep one
  `MODULE_DONE_CHECKLIST.md` instance in every module folder.
- Apply definition-first writing in all module content:
  1. definition
  2. concrete example
  3. optional metaphor
  4. practical implication
- Apply scope decomposition for multi-step module work:
  - bounded phases and tasks
  - one output per task
  - explicit checkpoints

## Success Criteria

- Module content is practical, measurable, and aligned with module rules.
- Artifacts are reusable and internally consistent.
- Validation is run and reported before completion.

### Module Output Rule

- Every module must produce concrete updates to both track workflows:
  `examples/developers/rbac-admin-workflow/` and
  `examples/knowledge-workers/vendor-selection-workflow/`.
- For each module, update the relevant workflow artifacts, record deltas
  in each track's `MODULE_UPDATES.md`, and log completion in
  `PROGRESS.md`.
- A module is not complete until both track workflows reflect the module
  concept with validated, traceable changes.

### Module Completion Criteria

- A module is complete only when all of the following are true:
  - required module files are present and aligned
  - both track workflows are updated for the module concept
  - both `deltas/module-0X.md` files exist and are linked
  - both `MODULE_UPDATES.md` files are updated
  - validation is run and recorded in `PROGRESS.md`

## Validation

- Approved markdown checks on changed files.
- Link/path/internal reference checks on changed files.
- `PROGRESS.md` updated with step details.
- `README.md` reviewed after each `PROGRESS.md` update.
