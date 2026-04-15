# Project Evaluation Checklist

## Correctness

- Changes match approved scope.
- Content aligns with repository and module rules.

## Completeness

- Required companion files are updated where needed.
- Cross-references are present and valid.

## Constraint Compliance

- Project context package was defined and validated per
  `PROJECT_CONTEXT_ARCHITECTURE.md`.
- Preview-first approval was followed.
- Definition-first writing was applied.
- Ask-first boundaries were respected.
- Scope decomposition principles were applied for multi-step work:
  - bounded phases and tasks
  - one output per task
  - explicit checkpoints and escalation gates

## Evaluation Loop Quality (Blocking)

- Evaluation objective is defined before execution begins.
- Multi-step work has phase-level checkpoints with measurable pass or
  fail criteria.
- Blocking failures stop progression until recovery evidence is
  recorded.
- Approval gates block unresolved blocking failures.

## Failure Pattern Management (Blocking)

- Each failed checkpoint is mapped to a `FP-PROJECT-*` pattern ID.
- Each pattern record includes:
  - symptom
  - root cause
  - detection signal
  - prevention pattern
  - recovery action
- Recovery action and rerun result are recorded before closure.
- Repeated failure patterns trigger updates to workflow artifacts.

## Security Control Quality (Blocking)

- High-risk actions are mapped to explicit control rules.
- Each high-risk action has required approval and stop condition.
- Blocking security controls are not bypassed without ask-first
  approval.
- Unresolved security blockers prevent completion decisions.

## Adoption Gate Quality (Blocking)

- Current adoption stage and next gate are explicit.
- Gate entry criteria and required evidence are defined.
- Named owner records each go/no-go decision.
- Active rollback trigger blocks gate promotion until closure evidence.

## Quality

- Examples are concrete and reusable.
- Acceptance criteria and validation are explicit.

## Module Quality Gates (Blocking)

- SOTA research summary exists and was approved before module writing.
- Definition-first sequence is applied to core concepts.
- Learning objectives are measurable and action-oriented.
- Vague language is removed or tied to explicit criteria.
- Module generation contract sections are complete and aligned.

## Module Output Gates (Blocking)

- Developer track workflow updated for module concept.
- Knowledge-worker track workflow updated for module concept.
- `deltas/module-0X.md` exists for both tracks.
- `MODULE_UPDATES.md` updated for both tracks.
- Module folder includes `MODULE_DONE_CHECKLIST.md` with PASS/FAIL
  decision recorded.
- README links updated if module index or references changed.

## Validation

- Markdown checks passed on changed files.
- Link/path/internal reference checks completed.
- Validation results are recorded in `PROGRESS.md`.
- `PROGRESS.md` records checkpoint decisions and pattern IDs for failed
  checkpoints.
- `PROGRESS.md` records adoption gate decisions and rollback trigger
  status for gated work.
