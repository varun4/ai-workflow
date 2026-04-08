# Module Done Checklist Template

Use one instance per module folder as
`course/modules/NN-module-slug/MODULE_DONE_CHECKLIST.md`.

## Deterministic Checks

- [ ] `lesson.md` exists
- [ ] `slides-outline.md` exists
- [ ] `exercise.md` exists
- [ ] `facilitator-notes.md` exists

- [ ] `lesson.md` has required headings
- [ ] `exercise.md` has required headings
- [ ] `facilitator-notes.md` has required headings

- [ ] developer delta exists:
      `examples/developers/rbac-admin-workflow/deltas/module-NN.md`
- [ ] knowledge-worker delta exists:
      `examples/knowledge-workers/vendor-selection-workflow/deltas/module-NN.md`

- [ ] developer `MODULE_UPDATES.md` includes `module-NN.md`
- [ ] knowledge-worker `MODULE_UPDATES.md` includes `module-NN.md`

- [ ] at least one developer workflow artifact updated for this module
- [ ] at least one knowledge-worker workflow artifact updated for this
      module

- [ ] `PROGRESS.md` includes module completion entry with validation run
- [ ] `README.md` updated if module index or references changed
- [ ] markdown validation passed on changed files

## Validation Commands Used

- `pymarkdown scan <changed-files>`

## Completion Decision

- [ ] PASS (all checks true)
- [ ] FAIL (any check false)
