# Module 03: Specification Precision

## Learning Objectives

By the end of this module, learners will be able to:

- define specification precision in plain language
- identify missing spec elements in vague requests
- rewrite vague requests into executable specs
- separate strict constraints from flexible implementation choices
- evaluate whether a spec is ready for agent execution

## Core Concept

### Definition: Specification Precision

Specification precision means defining work clearly enough that an agent
can execute it safely, correctly, and verifiably without guessing
critical intent.

### Concrete Examples

Coding anchor:
- Add role-based access checks to admin endpoints.

Knowledge-work anchor:
- Prepare a vendor selection recommendation for leadership.

For both examples, precision requires:
- objective
- scope
- non-goals
- constraints
- output contract
- acceptance criteria
- validation
- approval boundary

### Optional Metaphor

A precise spec is a flight plan with waypoints and landing criteria, not
a destination name alone.

### Practical Implication

If the spec is vague, execution quality depends on assumptions. If the
spec is precise, quality depends on validation.

## What Precision Is Not

- It is not long prose.
- It is not controlling every intermediate step.
- It is not generic quality language without criteria.
- It is not "do better" instructions.

A precise spec is short, bounded, and testable.

## Precision Framework

Use this sequence for every spec:

### Objective

- What exact outcome is required?

### Scope

- What is included?

### Non-goals

- What is explicitly excluded?

### Constraints

- What rules or boundaries apply?

### Output Contract

- What output format is required?

### Acceptance Criteria

- What must be true to mark complete?

### Validation

- How will correctness and completeness be checked?

### Approval Boundary

- What requires explicit human signoff?

## Strict vs Flexible

Be strict on:
- safety boundaries
- non-goals
- constraints
- acceptance criteria
- validation method

Allow flexibility on:
- intermediate sequence of subtasks
- wording and style
- low-risk implementation details

Rule:
- constrain what must be correct; allow flexibility where multiple good
  paths exist.

## Failure Mode

When specification precision is missing, execution quality depends on
assumptions.

Common failure patterns:
- objective ambiguity
- scope creep from missing non-goals
- non-testable acceptance criteria
- hidden assumptions in constraints
- missing approval gates for high-risk actions

## Real Example

Coding anchor upgrade:
- vague: "Add role checks to admin stuff quickly."
- precise: define endpoint scope, role matrix, test requirements, and
  security signoff boundary.

Knowledge-work anchor upgrade:
- vague: "Create a vendor recommendation."
- precise: define rubric, source rules, output contract, validation
  method, and stakeholder signoff boundary.

## Bad Pattern

### Vague Coding Request

"Add role checks to admin stuff quickly."

Missing:
- endpoint list
- role matrix
- non-goals
- test requirements
- merge approval boundary

### Vague Knowledge-Work Request

"Create a vendor recommendation."

Missing:
- evaluation rubric
- source rules
- output format
- acceptance criteria
- stakeholder approval boundary

## Good Pattern

### Executable Coding Spec (Condensed)

- Objective: enforce role checks on `/admin/users`, `/admin/roles`,
  `/admin/audit`.
- Scope: endpoint authorization + tests.
- Non-goals: no auth provider migration.
- Constraints: preserve response format; deny unauthorized with `403`.
- Output contract: code changes + tests + changelog note.
- Acceptance criteria: scoped endpoints enforce role matrix; tests pass.
- Validation: auth tests + regression suite.
- Approval boundary: security signoff before merge.

### Executable Knowledge-Work Spec (Condensed)

- Objective: deliver one vendor recommendation for leadership.
- Scope: compare Vendor A/B/C on cost, security, integration, support.
- Non-goals: no contract negotiation plan.
- Constraints: approved sources only; cite major claims.
- Output contract: 2-page brief + scoring table.
- Acceptance criteria: all vendors scored on same rubric;
  recommendation rationale explicit.
- Validation: evidence traceability and completeness checks.
- Approval boundary: director signoff before distribution.

## Reflection Questions

1. Which spec field is weakest in your current workflow?
2. Which constraints are currently implicit but should be explicit?
3. Where do you over-constrain and reduce useful agent flexibility?
4. What one spec upgrade would reduce rework this month?

## Summary

Specification precision is the control surface for agent reliability.
Precise specs reduce assumptions, improve validation quality, and make
handoff and review more dependable.
