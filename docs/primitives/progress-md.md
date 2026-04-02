# `PROGRESS.md`

`PROGRESS.md` is an append-only execution log that records what changed,
what was validated, and what comes next.

## Why It Matters

- Preserves continuity across sessions
- Makes work inspectable by humans and agents
- Reduces repeated rediscovery
- Supports accountability and handoff

## Recommended Entry Format

- Step name
- Files changed
- Status
- Validation run
- Next step

## Teaching Points

- Logging should be lightweight but specific
- The log should focus on meaningful execution steps, not every keystroke
- Validation should be reported even when it is not applicable

## Anti-Patterns

- Rewriting history instead of appending
- Logging vague statements such as "updated docs"
- Omitting validation or next-step information
