# AI Workflow Course

An open knowledge base and structured course for developers and
knowledge workers who want to integrate AI agents into real workflows.

This repository is about workflow design, not prompt tricks. The core
idea is simple: AI agents become much more reliable when work is
structured through explicit artifacts, bounded delegation, evaluation
loops, and security guardrails.

## Why This Exists

Many teams try to use AI agents by jumping straight into prompting. That
often produces output that is fast, plausible, and hard to trust.

This project teaches a more durable approach:

- define clear operating rules
- break work into bounded tasks
- preserve continuity across sessions
- evaluate outputs before accepting them
- introduce security and approval boundaries early

## Who This Is For

- Developers building software with AI agents
- Knowledge workers using AI agents for research, writing, operations,
  and synthesis
- Team leads designing repeatable AI-assisted workflows
- Trainers and facilitators who want course material they can turn into
  workshops or slide decks

## What You Will Learn

- How to use `AGENTS.md`, `PROGRESS.md`, specs, and skills as workflow
  primitives
- How to improve reliability through specification precision, scope
  decomposition, and context architecture
- How to design evaluation loops and recognize common failure patterns
- How to add security, approvals, and governance without making
  workflows unusable
- How to adapt the same operating model for both software delivery and
  knowledge work

## Core Workflow

```mermaid
flowchart LR
    A[Goal] --> B[Spec]
    B --> C[AGENTS.md Rules]
    C --> D[Agent Execution]
    D --> E[PROGRESS.md]
    D --> F[Skills]
    E --> G[Evaluation]
    F --> G
    G --> H{Approval Boundary?}
    H -- Yes --> I[Human Review]
    H -- No --> J[Complete]
    I --> D
```

## Repository Structure

- `docs/`: canonical reference for the framework
- `course/`: lesson material, slide outlines, exercises, and
  facilitator notes
- `tracks/`: audience-specific guidance for developers and knowledge
  workers
- `templates/`: reusable artifacts split into shared, developer, and
  knowledge-worker templates
- `examples/`: end-to-end case studies
- `skills/`: reusable workflow skills and a shared index
- `sessions/`: workshop formats and delivery plans
- `PROGRESS.md`: append-only execution log for repository development

## Start Here

1. Read `docs/foundations/operating-model.md`
2. Read `docs/primitives/agents-md.md`,
   `docs/primitives/progress-md.md`, `docs/primitives/skills.md`, and
   `docs/primitives/specs.md`
3. Read the reliability docs in `docs/reliability/`
4. Read the governance docs in `docs/governance/`
5. Work through `course/modules/01-introduction/` and
   `course/modules/02-workflow-operating-system/`
6. Adapt the templates in `templates/` for your own workflow
7. Use the examples in `examples/` as reference implementations

## Course Design Standard

Each module is designed to include:

1. Learning objectives
2. Core concept
3. Failure mode
4. Good pattern
5. Bad pattern
6. Real example
7. Exercise
8. Reflection questions

This structure keeps the course useful for both self-study and live
facilitation.

## Audience Tracks

The framework is shared, but the application differs by audience.

- Developers: feature delivery, bugfixes, code review, validation,
  release readiness
- Knowledge workers: research briefs, writing workflows, meeting
  outputs, operational processes, review loops

The split happens mainly in `tracks/`, `templates/`, and `examples/`,
while the core concepts remain shared in `docs/`.

## Current Status

This repository is in active buildout.

Current v1 focus:

- shared reference docs for the operating model and reliability concepts
- introductory course modules with teaching assets
- shared and audience-specific templates
- developer and knowledge-worker case studies
- workshop-ready session plans

## How To Use This Repository

### If you want to learn the system

Follow the reading path above, then complete the module exercises and
adapt a template to one real workflow you own.

### If you want to teach the system

Use the content in `course/` and `sessions/` as your base, then turn
the slide outlines into presentation decks and adapt exercises for your
audience.

### If you want to apply it immediately

Start with:

- `templates/shared/AGENTS.example.md`
- `templates/shared/PROGRESS.example.md`
- `templates/shared/SPEC.example.md`

Then move into the audience-specific templates that match your work.

## Roadmap

- Expand the developer and knowledge-worker template packs
- Build out the remaining modules in `course/modules/`
- Add deeper end-to-end case studies
- Add reusable skills to `skills/`
- Package the material into workshop and session sequences

## Working Principles

- Structure beats prompting
- Bounded autonomy beats vague delegation
- Artifacts beat chat history
- Evaluation is part of the work
- Security must be designed in

## Repository Notes

- `AGENTS.md` defines operating rules for agent sessions in this
  repository
- `PROGRESS.md` is append-only and records major implementation steps
- Course content under `course/`, `docs/`, `templates/`, `examples/`,
  `tracks/`, and `sessions/` follows a preview-first review workflow
