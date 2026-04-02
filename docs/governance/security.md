# Security

Security in agentic workflows is mostly about boundaries, visibility, and safe defaults.

## Core Security Concerns

- Secret exposure
- Over-broad permissions
- Destructive actions without approval
- Unsafe tool use
- Missing audit trail

## Safe Defaults

- Treat secrets as off-limits unless explicitly required and approved
- Require ask-first gates for destructive or external actions
- Keep actions inspectable through files and logs
- Prefer least-privilege workflows

## Teaching Points

- Security is part of workflow design, not a late review item
- The safest workflow is one where risky actions are hard to perform accidentally
- Approval boundaries should be explicit and easy to understand
