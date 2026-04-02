# `AGENTS.md`

`AGENTS.md` is the workflow operating contract for a repository or workspace.

## What It Should Define

- Scope of the agent's authority
- Allowed and ask-first actions
- Tooling and environment expectations
- Validation requirements
- Delivery and git rules
- Escalation behavior when blocked

## Why It Matters

- Prevents unsafe assumptions
- Makes behavior consistent across sessions
- Creates visible approval boundaries
- Reduces repeated instruction overhead

## Teaching Points

- `AGENTS.md` should define behavior, not contain project documentation noise
- Rules should be actionable and testable
- Ask-first actions are as important as allowed actions

## Anti-Patterns

- Vague rules such as "be careful"
- Missing escalation instructions
- No distinction between safe and risky actions
- Mixing permanent rules with temporary task notes
