# AGENTS.md

## Cardinal Rules (Non-Negotiable)

- Do not edit `AGENTS.md` from any agent session.
- Only human maintainers may change `AGENTS.md`.

## Repository Purpose

- This repository is a course and knowledge base for helping developers and
  knowledge workers integrate AI agents into real workflows.
- The repository teaches artifact-driven workflows using materials such as
  `AGENTS.md`, `PROGRESS.md`, specs, skills, templates, examples, and
  teaching modules.

## Scope

- Scope is limited to this repository only.
- Prefer improving existing structure over creating parallel systems unless
  there is a clear reason.

## Agent Context Loading Rules

- Agents must load operating context from this file and the operating
  files referenced here.
- `README.md` is for human onboarding and navigation only.
- `README.md` is not an authoritative policy source for agent execution.

### Required Context Sources (Load Before Module Work)

1. `AGENTS.md`
2. `SPEC.md`
3. `APPROVAL_BOUNDARIES.md`
4. `EVAL_CHECKLIST.md`
5. `SKILL_EVIDENCE_REVIEW.md`
6. `PROGRESS.md`
7. `docs/standards/MODULE_DONE_CHECKLIST_TEMPLATE.md`
8. Active module folder under `course/modules/NN-*`
9. Track workflow artifacts under:
   - `examples/developers/rbac-admin-workflow/`
   - `examples/knowledge-workers/vendor-selection-workflow/`

### Source Precedence (If Conflict Exists)

1. `AGENTS.md`
2. `APPROVAL_BOUNDARIES.md`
3. `EVAL_CHECKLIST.md`
4. `SPEC.md`
5. Active module files (`course/modules/NN-*`)
6. Active track workflow files (`examples/...`)
7. `PROGRESS.md`
8. If unresolved conflict remains, stop and ask.

## Allowed Without Prompt

- Read files and list directories.
- Propose or implement content and structure changes within approved scope.
- Add or refine docs, course modules, templates, examples, tracks, sessions,
  and skills.
- Update `README.md` and `PROGRESS.md`.
- Run safe read-only validation commands for Markdown or repository inspection.

## Documentation Pointers

Primary operating files (use these first):
- Project scope and constraints: `SPEC.md`
- Project context package and precedence: `PROJECT_CONTEXT_ARCHITECTURE.md`
- Approval and ask-first actions: `APPROVAL_BOUNDARIES.md`
- Validation and completion checks: `EVAL_CHECKLIST.md`
- Evidence and content review skill: `SKILL_EVIDENCE_REVIEW.md`
- Deterministic module done checklist template:
  `docs/standards/MODULE_DONE_CHECKLIST_TEMPLATE.md`
- Execution history and handoff trail: `PROGRESS.md`
Backup rule:
- If any operational rule is unclear in this file, defer to the
  project operating files listed above, then record the decision in
  `PROGRESS.md`.

## Repository Architecture Rules

- `docs/` is the canonical reference layer for shared concepts.
- `course/` contains teaching assets derived from the shared concepts.
- `templates/` contains reusable artifacts people can adapt directly.
- `examples/` contains end-to-end worked examples and case studies.
- `tracks/` contains audience-specific guidance for developers and
  knowledge workers.
- `skills/` contains reusable workflow skills and an index.
- `sessions/` contains workshop and delivery formats.
- Prefer one shared conceptual framework across audiences; split by
  audience mainly in `tracks/`, `templates/`, and `examples/`.

## Course Content Review Rule

- Any new or revised course-content material must follow a preview-first
  workflow: draft the proposed content in-chat, request user approval, and
  only write the content to repository files after explicit approval.
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
- Treat developers and knowledge workers as two application tracks built on
  the same operating model.

## Crisp Language Rule

- Write in plain, concrete, and testable language.
- Do not use vague terms (e.g., "improve", "better", "high-quality")
  unless tied to explicit criteria.
- Use measurable verbs such as define, identify, compare, apply, evaluate,
  and design.
- Keep one idea per sentence when possible.
- Treat unresolved vague language as a blocking review issue.

## Module Rules

- Each course module should include:
  - learning objectives
  - core concept
  - failure mode
  - good pattern
  - bad pattern
  - real example
  - exercise
  - reflection questions
- `slides-outline.md`, `exercise.md`, and `facilitator-notes.md` must stay
  aligned with `lesson.md`.

## Module SOTA Research Rule

- Before creating or revising any module content under `course/modules/`,
  complete a state-of-the-art research pass and present a summary in-chat
  for user approval.
- The research pass must include at least:
  - one official model-provider source,
  - one practitioner implementation source,
  - one relevant research paper or technical publication.
- The summary must include:
  - source links,
  - actionable takeaways,
  - confidence level per takeaway (official/practitioner/research),
  - implications for module design and exercises.
- Only after explicit user approval may module files be written or updated.

## Module Generation Contract Rule

- Every module folder must include:
  - `lesson.md`
  - `slides-outline.md`
  - `exercise.md`
  - `facilitator-notes.md`
  - `MODULE_DONE_CHECKLIST.md` (from
    `docs/standards/MODULE_DONE_CHECKLIST_TEMPLATE.md`)
- `lesson.md` must include:
  - learning objectives
  - core concept
  - failure mode
  - good pattern
  - bad pattern
  - real example
  - reflection questions
- `slides-outline.md` must include:
  - slide sequence aligned to lesson flow
  - exercise instruction slide
  - bridge slide to next module
- `exercise.md` must include:
  - scenario
  - task
  - required output format
  - evaluation rubric
  - debrief questions
- `facilitator-notes.md` must include:
  - teaching emphasis
  - core message
  - common student mistakes
  - facilitation prompts
  - suggested timing
  - exit check

## Module Output Rule

- Every module must produce concrete updates to both track workflows:
  - `examples/developers/rbac-admin-workflow/`
  - `examples/knowledge-workers/vendor-selection-workflow/`
- For each module:
  - update relevant workflow artifacts in both tracks
  - add both delta files:
    - `examples/developers/rbac-admin-workflow/deltas/module-NN.md`
    - `examples/knowledge-workers/vendor-selection-workflow/deltas/module-NN.md`
  - update both `MODULE_UPDATES.md` files
  - log completion in `PROGRESS.md`
- A module is not complete until both tracks reflect the module concept with
  validated, traceable changes.

## Automation Verification Rule

- Module completion must be mechanically verifiable.
- `MODULE_DONE_CHECKLIST.md` must be filled for the module and include a
  PASS/FAIL decision.
- If any blocking gate fails in `EVAL_CHECKLIST.md`, stop and ask.
- Do not mark module work complete until all deterministic checks pass.

## Template And Example Rules

- Templates should be short, fillable, and immediately reusable.
- Shared templates should stay audience-neutral.
- Audience-specific templates should reflect developer or knowledge-worker
  needs without duplicating the shared framework.
- Examples should demonstrate full artifact flow where possible:
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
