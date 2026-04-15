# Project Approval Boundaries

## Ask-First Actions

- Install dependencies or packages.
- Push to remote repositories.
- Delete files or large content sections.
- Rename or move major repository structure.
- Change license, repository positioning, or audience.
- Add external tooling, CI, or publishing infrastructure.
- Promote adoption stage from `sandbox` to `pilot`.
- Promote adoption stage from `pilot` to `operational`.
- Override a blocking security or adoption gate.
- Continue execution when an active rollback trigger exists.

## Course Content Boundary

- Draft and review in chat first.
- Write to `course/`, `docs/`, `templates/`, `examples/`, `tracks/`,
  or `sessions/` only after explicit approval.

## Validation Boundary

- If expected checker is unavailable, stop and ask.
- Use manual validation only with explicit user approval.

## Security and Adoption Boundary

- Stage promotion requires explicit owner decision and recorded
  evidence.
- A no-go or rollback decision remains in force until closure evidence
  is recorded.
- If gate evidence is missing, stop and ask.

## Module Automation Stop Conditions

- Stop and ask if SOTA research evidence is missing.
- Stop and ask if required module contract sections are missing.
- Stop and ask if either track workflow update is incomplete.
- Stop and ask if validation fails or expected checker is unavailable.
- Do not mark a module complete until all module output gates pass.
- Stop and ask if project context package is missing, stale, or has unresolved conflicts.
- Stop and ask if security control map, adoption gate evidence, or
  rollback status is missing for active work.
