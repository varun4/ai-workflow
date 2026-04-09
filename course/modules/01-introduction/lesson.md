# Module 01: Introduction

## Learning Objectives

- By the end of this module, learners will be able to:
- define an AI workflow in plain language
- identify workflow components in one coding and one knowledge-work
  example
- compare ad hoc prompting with artifact-driven workflow execution
- apply a first-pass specification structure to a vague request
- evaluate whether a request is executable or assumption-heavy

## Core Concept

### Definition: AI Workflow

An AI workflow is a repeatable sequence of tasks, artifacts, decisions,
and checks that turns intent into verifiable output.

### Concrete Examples

Coding example:
- Add role-based access checks to admin endpoints.

Knowledge-work example:
- Prepare a vendor selection recommendation for leadership.

In both cases, the workflow includes:
- a specification (what to do),
- operating rules (what is allowed),
- progress tracking (what was done),
- evaluation (how quality is checked),
- approval boundaries (when to stop and ask).

### Optional Metaphor

An AI workflow is a production line with quality gates, not a single
instruction shouted across a room.

### Practical Implication for Reliability

If a request has no scope, no criteria, and no boundaries, an agent
must guess. Guessing creates drift, rework, and safety risk.

## Failure Mode

Most failures come from missing workflow elements, not missing model
intelligence.

Common failure causes:
- objective ambiguity
- scope leakage
- missing constraints
- no acceptance criteria
- no approval boundary
- no evaluation loop

## Good Pattern

Use a minimum artifact set before execution:

- operating rules (`AGENTS.md`)
- executable specification
- progress tracking (`PROGRESS.md`)
- evaluation checklist
- approval boundary

Prompting can start work. Workflow design makes work reliable.

## Bad Pattern

Ad hoc prompting is issuing one-off requests without shared artifacts,
boundaries, or evaluation criteria.

Examples:
- "Add auth to admin APIs quickly."
- "Make a vendor recommendation."

Both are directionally useful but execution-unsafe as written.

## Real Example

Coding anchor:
- Add role-based access checks to admin endpoints.

Knowledge-work anchor:
- Prepare a vendor selection recommendation for leadership.

In both examples, learners build the same operating workflow:
- reusable operating model
- executable specification
- progress tracking
- evaluation checks
- approval boundaries

All modules use these two anchors to show transferability across
developer and knowledge-worker contexts.

## Reflection Questions

1. Define AI workflow in one sentence from your own context.
2. In the coding example, what is missing if no scope is defined?
3. In the knowledge-work example, what fails if no evaluation is
   defined?
4. Where does your current process rely on hidden assumptions?
