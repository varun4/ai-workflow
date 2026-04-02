# Scope Decomposition

Scope decomposition breaks large goals into phases, tasks, and
checkpoints that an agent can execute safely.

## Why It Matters

- Large requests hide multiple decision points
- Smaller tasks improve reliability and reviewability
- Checkpoints reduce silent failure

## Decomposition Rules

1. Separate architecture from implementation
2. Separate scaffold from content depth
3. Insert review points before risky actions
4. Keep each task tied to a clear output

## Example

Goal: build a public AI workflow course.

Phases:
1. Define information architecture
2. Create repository scaffold
3. Draft shared reference docs
4. Add audience-specific templates and examples
5. Build teaching modules and workshops

## Anti-Patterns

- Giving an agent a full program to design, write, teach, and publish in one step
- Treating a multi-phase initiative as a single task
