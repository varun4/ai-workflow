# Module 04 Facilitator Notes

## Teaching Emphasis

- Teach decomposition as a reliability mechanism.
- Use both anchor examples for transferability.
- Enforce one-output-per-task discipline.
- Keep checkpoint design explicit.

## Core Message

If work cannot be decomposed into bounded, testable units, it is not
ready for reliable agent execution.

## Definitions To Enforce

Learners should be able to state:

- phase: logical stage with a bounded purpose
- task: executable unit with one output
- checkpoint: decision gate before proceeding

## Common Student Mistakes

- phases that are too broad
- tasks without outputs
- missing validation per phase
- no escalation criteria at checkpoints
- mixing approvals into implementation tasks without boundaries

## Facilitation Prompts

- "What output proves this task is done?"
- "What decision is made at this checkpoint?"
- "What should trigger escalation?"
- "Which tasks can be parallelized safely?"

## Suggested Timing

- 10 min: definitions and framing
- 15 min: decomposition patterns and quality checks
- 20 min: dual-anchor decomposition exercise
- 10 min: debrief and pattern extraction

## Exit Check

Before closing, ask each learner to provide:

- one decomposition map for coding anchor
- one decomposition map for knowledge-work anchor
- one checkpoint they will add to their real workflow
