# Module 06: Skills and Reusable Capabilities

## Learning Objectives

By the end of this module, learners will be able to:

- define a workflow skill in plain language
- identify repeatable tasks that should be converted into skills
- design a skill contract with explicit inputs, outputs, and constraints
- apply one reusable skill to each anchor workflow
- evaluate whether a skill reduced ambiguity and rework

## Core Concept

### Definition: Workflow Skill

A workflow skill is a reusable instruction package for one repeatable
capability in a workflow.

### Concrete Examples

Coding anchor:
- Add role-based access checks to admin endpoints.

Knowledge-work anchor:
- Prepare a vendor selection recommendation for leadership.

In both examples, a skill is a contract that defines:
- purpose
- inputs
- outputs
- constraints
- checklist
- verification

### Optional Metaphor

A skill is a reusable jig in a workshop. It does one job consistently.

### Practical Implication

Without skills, repeated tasks drift across people and sessions.
With skills, repeated tasks become consistent, testable, and easier to
review.

## Failure Mode

Common skill failure patterns:

- skill scope is too broad ("handle everything")
- required inputs are not explicit
- outputs are not observable
- verification is missing
- skill invocation timing is undefined
- stale skill logic persists after workflow changes

## Good Pattern

A strong skill has:

- one capability and one clear trigger
- explicit required inputs
- explicit output artifact
- hard constraints and stop conditions
- a deterministic checklist
- a verification step tied to evaluation artifacts

## Bad Pattern

A weak skill looks like:

- long prompt fragments without structure
- mixed capabilities in one file
- no entry criteria or approval boundary
- no measurable verification output

Result:
- inconsistent execution
- hidden assumptions
- unclear review outcomes

## Real Example

### Developer Track Example

`SKILL_RBAC_CONTEXT_REFRESH.md`:
- Purpose: refresh context package before each RBAC phase.
- Trigger: before Plan, Implement, Validate, and Approve phases.
- Output: phase context note with include/exclude/precedence decisions.
- Verification: cross-check with `SPEC.md` and `EVAL_CHECKLIST.md`.

### Knowledge-Worker Track Example

`SKILL_EVIDENCE_CONTEXT_REFRESH.md`:
- Purpose: refresh evidence context before scoring and briefing phases.
- Trigger: before Analyze, Draft, Validate, and Approve phases.
- Output: approved-source context note and conflict-resolution log.
- Verification: cross-check with `SPEC.md` and `EVAL_CHECKLIST.md`.

## Reflection Questions

1. Which repeated task in your workflow is currently skill-worthy?
2. Which skill field is usually missing in your team artifacts?
3. What verification step would make your skills auditable?
4. What one skill could reduce rework this month?

## Summary

Skills convert repeated workflow behaviors into explicit, reusable
capabilities. The goal is not more process. The goal is less ambiguity
and more reliable execution.
