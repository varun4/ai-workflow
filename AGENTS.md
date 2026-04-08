# AGENTS.md

## Cardinal Rules (Non-Negotiable)

- Do not edit `AGENTS.md` from any agent session.
- Only human maintainers may change `AGENTS.md`.

## Repository Purpose

- This repository is a course and knowledge base for helping developers and
  knowledge workers integrate AI agents into real workflows.
- The repository teaches artifact-driven workflows using materials such as
  `AGENTS.md`, `PROGRESS.md`, specs, skills, templates, examples, and teaching
  modules.

## Scope

- Scope is limited to this repository only.
- Prefer improving existing structure over creating parallel systems unless
  there is a clear reason.

## Allowed Without Prompt

- Read files and list directories.
- Propose or implement content and structure changes within approved scope.
- Add or refine docs, course modules, templates, examples, tracks, sessions,
  and skills.
- Update `README.md` and `PROGRESS.md`.
- Run safe read-only validation commands for markdown or repository inspection.

## Documentation Pointers
Primary operating files (use these first):
- Project scope and constraints: `SPEC.md`
- Approval and ask-first actions: `APPROVAL_BOUNDARIES.md`
- Validation and completion checks: `EVAL_CHECKLIST.md`
- Evidence and content review skill: `SKILL_EVIDENCE_REVIEW.md`
- Execution history and handoff trail: `PROGRESS.md`
- If any operational rule is unclear in this file, defer to the
  project operating files listed above, then record the decision in
  `PROGRESS.md`.

## Repository Architecture Rules

- `docs/` is the canonical reference layer for shared concepts.
- `course/` contains teaching assets derived from the shared concepts.
- `templates/` contains reusable artifacts people can adapt directly.
- `examples/` contains end-to-end worked examples and case studies.
- `tracks/` contains audience-specific guidance for developers and knowledge
  workers.
- `skills/` contains reusable workflow skills and an index.
- `sessions/` contains workshop and delivery formats.
- Prefer one shared conceptual framework across audiences; split by audience
  mainly in `tracks/`, `templates/`, and `examples/`.

## Course Content Review Rule

- Any new or revised course-content material must follow a preview-first
  workflow: draft the proposed content in-chat, request user approval, and only
  write the content to repository files after explicit approval.
- This applies to all files under `course/`, `docs/`, `templates/`,
  `examples/`, `tracks/`, and `sessions/`.

## Writing And Teaching Rules

- Write in an educational, practical, and reusable style.
- Prefer concrete workflows, artifacts, examples, and exercises over abstract
  commentary.
- Avoid hype, generic AI claims, and tool-specific advice unless directly
  relevant.
- Keep the focus on workflow design, reliability, evaluation, and safe
  adoption.
- Treat developers and knowledge workers as two application tracks built on the
  same operating model.

## Module Rules

- Each course module should aim to include:
  - learning objectives
  - core concept
  - failure mode
  - good pattern
  - bad pattern
  - real example
  - exercise
  - reflection questions
- `slides-outline.md`, `exercise.md`, and `facilitator-notes.md` should stay
  aligned with the lesson content.

## Module Output Rule
- Every module must produce concrete updates to both track workflows:
  `examples/developers/rbac-admin-workflow/` and
  `examples/knowledge-workers/vendor-selection-workflow/`.
- For each module, update the relevant workflow artifacts, record deltas
  in each track's `MODULE_UPDATES.md`, and log completion in
  `PROGRESS.md`.
- A module is not complete until both track workflows reflect the module
  concept with validated, traceable changes.

## Template And Example Rules

- Templates should be short, fillable, and immediately reusable.
- Shared templates should stay audience-neutral.
- Audience-specific templates should reflect the needs of either developers or
  knowledge workers without duplicating the shared framework.
- Examples should demonstrate the full artifact flow where possible:
  - spec
  - rules or constraints
  - progress tracking
  - evaluation
  - approval boundaries

## Skills Rules

- Skills should capture reusable capabilities, not one-off prompts.
- Keep each skill narrow, explicit, and checklist-oriented.
- Each skill should define:
  - purpose
  - inputs
  - outputs
  - constraints
  - verification

## Git And Delivery Rules

- Do not commit or push unless explicitly requested.
- Keep commits and changes scoped to the task at hand.
- Do not include editor-specific local files or environment-specific noise.
- Do not commit generated slide decks or exported session artifacts unless
  explicitly requested.
- After significant content additions or structural changes, pause for user
  review.

## When Stuck

- Ask one focused clarifying question.
- Propose a short execution plan.
- Document assumptions and tradeoffs clearly.
