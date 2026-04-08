# Module 05: Context Architecture

## Learning Objectives

By the end of this module, learners will be able to:

- define context architecture in plain language
- identify what to include, exclude, and persist for a task
- design a context package for each workflow phase
- define context refresh triggers and ownership
- evaluate whether context quality is sufficient for execution

## Core Concept

### Definition: Context Architecture

Context architecture is the design of what information an agent gets,
what it keeps over time, and what it must ignore to execute reliably.

### Concrete Examples

Coding anchor:
- Add role-based access checks to admin endpoints.

Knowledge-work anchor:
- Prepare a vendor selection recommendation for leadership.

For both examples, context architecture must define:
- required context
- excluded context
- persistent context
- refresh policy

### Optional Metaphor

Context architecture is a mission briefing with approved maps, not a
dump of every document in the archive.

### Practical Implication

Too little context causes guessing. Too much context causes drift. Good
context design gives the minimum complete set for correct execution.

## Failure Mode

Common failure patterns:

- missing required context for critical decisions
- stale context reused after scope changes
- irrelevant context overwhelming key constraints
- conflicting context sources without precedence rules
- no ownership for context refresh and cleanup

## Good Pattern

Use a context package with explicit fields:

- Task context: current objective, scope, constraints
- Working context: files, data, and references for current phase
- Persistent context: stable rules and definitions
- Excluded context: known-noise or out-of-scope materials
- Refresh triggers: events that require context rebuild

Apply this package per phase, not once for the whole project.

## Bad Pattern

"Include all related files and prior discussions so the agent has
everything."

Problems:

- no relevance filter
- no source precedence
- no stale-data handling
- no phase-specific context boundaries

## Real Example

### Coding Anchor

- Include:
  - scoped endpoint list
  - role matrix
  - auth middleware paths
  - acceptance criteria and test commands
- Exclude:
  - unrelated non-admin endpoint files
  - old exploratory notes
- Refresh when:
  - endpoint scope changes
  - role matrix changes

### Knowledge-Work Anchor

- Include:
  - approved source list
  - scoring rubric
  - decision criteria
  - output format requirements
- Exclude:
  - non-approved sources
  - prior drafts with unresolved assumptions
- Refresh when:
  - criteria or source policy changes
  - leadership asks for new constraints

## Reflection Questions

1. Which context source in your workflow is usually stale?
2. What information should be explicitly excluded today?
3. Which refresh trigger is currently missing?
4. What one context package change would reduce rework this month?
