# Operating Model

This course teaches an artifact-driven workflow for using AI agents safely and productively.

## Core Artifacts

- `AGENTS.md`: operating rules, scope, permissions, and validation expectations
- `PROGRESS.md`: append-only execution log for continuity and accountability
- Specs: task definition, scope, constraints, and acceptance criteria
- Skills: reusable instructions for repeated tasks
- Evaluation checklists: quality control before completion

## Workflow Loop

1. Define the goal
2. Write or refine the spec
3. Bound the scope
4. Package the necessary context
5. Execute with the agent
6. Evaluate the output
7. Log progress and decisions
8. Escalate or approve when needed

## Human Responsibilities

- Define intent and business context
- Set approval boundaries
- Review ambiguous or high-risk work
- Refine the system as failure patterns appear

## Agent Responsibilities

- Follow defined scope and rules
- Use the available context carefully
- Produce visible artifacts, not hidden reasoning
- Stop or escalate when boundaries are reached

## Common Breakdown

Most workflows fail because the human asks for a result but does not
define scope, context, or evaluation. The course should repeatedly show
that reliable output depends on workflow architecture, not raw model
capability.
