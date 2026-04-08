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
- Keep shared framework in `docs/` and split by audience mainly in
  `tracks/`, `templates/`, and `examples/`.

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

## Validation

- Approved markdown checks on changed files.
- Link/path/internal reference checks on changed files.
- `PROGRESS.md` updated with step details.
- `README.md` reviewed after each `PROGRESS.md` update.
