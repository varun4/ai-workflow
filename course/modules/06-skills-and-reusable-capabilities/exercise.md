# Module 06 Exercise

## Scenario

You need to reduce repeated ambiguity in both anchor workflows:

1. Coding: add role-based access checks to admin endpoints.
2. Knowledge work: prepare a vendor selection recommendation for
   leadership.

Current gap:
- repeated context-refresh and quality checks are done inconsistently.

## Task

For each anchor, design one reusable skill that includes:

- purpose
- required inputs
- expected outputs
- constraints and stop conditions
- checklist
- verification method

Then define:

- when the skill is invoked in the workflow
- what artifact proves the skill run completed

## Required Output Format

For each anchor, submit:

1. Skill definition (all required fields)
2. Invocation map by workflow phase
3. Example output artifact produced by the skill
4. One failure case and escalation rule
5. One revision trigger for updating the skill

## Evaluation Rubric

A strong submission should:

- keep skill scope narrow and single-purpose
- define concrete inputs and outputs
- include explicit stop conditions
- include a deterministic checklist
- include a verification step tied to workflow artifacts

## Debrief Questions

1. Which skill field prevented the most ambiguity?
2. Which invocation point was hardest to define?
3. What failure still needs a separate skill?
4. What revision trigger is most critical for your workflow?
