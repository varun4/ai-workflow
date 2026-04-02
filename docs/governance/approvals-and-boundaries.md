# Approvals And Boundaries

Approval boundaries make it clear where human signoff is required.

## Typical Ask-First Actions

- Installing dependencies
- Pushing to remotes
- Deleting files or data
- Changing permissions
- Running destructive database operations
- Accessing sensitive systems or credentials

## Design Principles

- Keep approval rules visible in `AGENTS.md`
- Phrase boundaries as actions, not abstractions
- Escalate when uncertainty is high, not only when risk is certain

## Teaching Point

A workflow is safer when the agent knows exactly when to stop and ask.
