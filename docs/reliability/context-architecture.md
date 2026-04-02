# Context Architecture

Context architecture determines what information an agent receives,
what remains persistent, and what should be excluded.

## Context Layers

- Permanent context: stable rules, policies, and glossary
- Task context: current spec, files, and constraints
- Historical context: prior decisions and progress log
- Excluded context: irrelevant detail that increases noise

## Good Context Design

- Include only information that changes the outcome
- Prefer durable artifacts over long chat memory
- Refresh context when the task changes significantly

## Common Failure Patterns

- Too little context: wrong assumptions
- Too much context: drift and confusion
- Wrong context: accurate work on the wrong problem
