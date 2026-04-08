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

## Ask First

- Installing dependencies or packages.
- `git push`.
- Deleting files or large sections of content.
- Renaming or moving major parts of the repository structure.
- Changing license, repository positioning, or course audience.
- Adding external tooling, CI, site generators, or publishing infrastructure.

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

## Module Research Rules
- Before creating or revising any file under `course/modules/`, perform a state-of-the-art research pass and summarize it in-chat for approval first.
- The research pass must include at least:
  - one official model-provider source (e.g., OpenAI/Anthropic docs),
  - one practitioner/implementation source,
  - one relevant research paper (or equivalent technical publication).
- The summary must include:
  - source list with links,
  - 5-10 actionable patterns,
  - confidence level for each pattern (official guidance, practitioner evidence, or research evidence),
  - implications for module content and exercises.
- Only after explicit user approval may module files be written or updated.

## Definition-First Writing Rule
- Do not introduce abstract concepts without first defining them in plain language.
- For every key concept in course content, use this sequence:
  1. definition (what it is),
  2. concrete example (from course anchor examples where possible),
  3. optional metaphor (only after definition and example),
  4. practical implication (how it changes execution or evaluation).
- Avoid generic learning objectives such as "understand X" unless they are followed by observable outcomes.
- Learning objectives must be measurable and action-oriented, using verbs such as define, identify, compare, apply, evaluate, and design.
- Avoid vague claims and filler terms (e.g., "improve", "better", "high-quality") unless they are tied to explicit criteria.
- During content review, reject any section that discusses a concept before defining it and grounding it in an example.

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

## Quality And Validation Rules

- Before marking work complete, run and report validation relevant to the
  changed files.
- For this repository, validation should usually include:
  - approved markdown quality checks on changed markdown files
  - markdown link, path, and internal reference verification across changed
    markdown files
  - path and structure consistency
  - internal reference consistency where practical
  - Python syntax verification for all Python files in the repository when
    Python files are added or modified
  - relevant test or verification commands for changed Python code when
    available
- For Python verification, use an approved repository command such as
  `python -m compileall` or an equivalent agreed checker.
- If the expected checker is unavailable, stop and ask the user how to proceed
  instead of silently falling back to manual validation.
- If the user approves manual validation, report clearly that only manual
  review was performed.
- Keep diffs focused and small.

## Progress Tracking Rules

- Every implementation step must be logged in `PROGRESS.md` with:
  - step name
  - files changed
  - status
  - validation run
  - next step
- After every `PROGRESS.md` update, review `README.md` and update it if the
  repository status, structure, scope, learning path, or roadmap has
  materially changed.
- Keep the log append-only; do not rewrite old entries.

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

## Documentation Pointers

- Project overview: `README.md`
- Skills index: `skills/SKILLS_INDEX.md`
- Progress log: `PROGRESS.md`
- Shared framework: `docs/`
- Teaching materials: `course/`
