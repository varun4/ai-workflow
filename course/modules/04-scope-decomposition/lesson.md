# Module 04: Scope Decomposition

## Learning Objectives

By the end of this module, learners will be able to:

- define scope decomposition in plain language
- decompose a goal into phases, tasks, and checkpoints
- map each task to one concrete output artifact
- choose between fixed and adaptive decomposition patterns
- evaluate whether a decomposition is execution-ready

## Core Concept

### Definition: Scope Decomposition

Scope decomposition is the practice of breaking a goal into bounded work
units that can be executed, reviewed, and validated with low ambiguity.

### Concrete Examples

Coding anchor:
- Add role-based access checks to admin endpoints.

Knowledge-work anchor:
- Prepare a vendor selection recommendation for leadership.

For both examples, decomposition should produce:
- phase-level plan
- task-level outputs
- checkpoint decisions
- approval and evaluation gates

### Optional Metaphor

Decomposition is turning a route into leg-by-leg navigation with
checkpoints, not driving toward a destination without markers.

### Practical Implication

Without decomposition, agents overreach or stall. With decomposition,
work becomes observable and correctable.

## Why Decomposition Matters

- large goals hide multiple decision points
- smaller units reduce assumption load
- checkpoints catch errors early
- review becomes faster and more objective

## Decomposition Levels

### Goal

One outcome statement.

### Phase

A logical stage of work with a bounded purpose.

### Task

A specific executable unit with one output.

### Checkpoint

A decision point:
- continue
- revise
- escalate for approval

## Decomposition Quality Checks

A good task is:

- bounded: clear start and stop
- observable: one concrete output
- testable: has a validation method
- scoped: in-scope and non-goals are clear
- governed: approval boundary defined when needed

## Pattern A: Fixed Decomposition

Use when work path is predictable.

Example:
1. Define role matrix
2. Implement endpoint checks
3. Add tests
4. Run validation
5. Request security approval

## Pattern B: Adaptive Decomposition

Use when required subtasks depend on discovered information.

Example:
1. Define decision criteria
2. Collect source evidence
3. Route uncertain areas to deeper review
4. Re-score options
5. Draft recommendation
6. Run evidence and approval checks

## Bad Pattern

"Break this into a few steps and handle everything."

Problems:
- task boundaries unclear
- no output contracts per step
- no checkpoint gates
- no explicit escalation path

## Good Pattern

### Coding Anchor Decomposition (Condensed)

Goal:
- enforce RBAC on scoped admin endpoints

Phases:
1. Plan
   - output: role matrix and endpoint scope
2. Implement
   - output: code changes
3. Validate
   - output: test report plus checklist
4. Approve
   - output: security signoff

### Knowledge-Work Decomposition (Condensed)

Goal:
- produce vendor recommendation brief

Phases:
1. Plan
   - output: criteria and source constraints
2. Analyze
   - output: scoring matrix
3. Draft
   - output: recommendation brief
4. Validate
   - output: evidence review checklist
5. Approve
   - output: stakeholder signoff

## Reflection Questions

1. Where do your current tasks span too many decisions?
2. Which phase in your workflow needs a checkpoint gate?
3. Which outputs are currently implied but not explicit?
4. What one decomposition change would reduce rework this month?

## Summary

Scope decomposition turns large goals into bounded, testable work units.
It improves reliability by making execution visible and reviewable.
