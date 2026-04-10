# Vendor Selection Brief Spec

## Objective

Deliver a leadership-ready recommendation for one vendor based on
defined criteria and evidence.

## Scope

- Compare Vendor A, Vendor B, and Vendor C.
- Evaluate criteria:
  - total cost
  - security posture
  - integration effort
  - support quality
- Produce a two-page recommendation brief with a scoring table.

## Non-Goals

- No contract negotiation plan.
- No implementation project plan.
- No legal approval memo.

## Constraints

- Use only approved internal notes and approved public sources.
- Include citation for every major claim.
- Clearly label assumptions where evidence is incomplete.

## Success Criteria

- All vendors are scored on the same rubric.
- Tradeoffs are explicit and evidence-backed.
- Final recommendation is clear and defensible.

## Validation

- Run evidence and citation traceability review.
- Run bias and completeness checklist.
- Obtain stakeholder review before distribution.

## Scope Decomposition (Module 04)

### Phase 1: Plan

- Tasks:
  - confirm decision criteria and scoring rubric
  - confirm approved source set
- Output:
  - criteria and source constraints note
- Checkpoint:
  - approve criteria before evidence collection

### Phase 2: Analyze

- Tasks:
  - collect evidence for each vendor
  - score vendors against rubric
- Output:
  - scored vendor comparison matrix
- Checkpoint:
  - verify all vendors have complete evidence coverage

### Phase 3: Draft

- Tasks:
  - produce recommendation narrative
  - state tradeoffs and assumptions
- Output:
  - recommendation brief draft
- Checkpoint:
  - confirm recommendation aligns with matrix

### Phase 4: Validate

- Tasks:
  - run evidence traceability review
  - run bias and completeness checks
- Output:
  - completed evaluation checklist
- Checkpoint:
  - stop if unsupported claims remain

### Phase 5: Approve

- Tasks:
  - stakeholder signoff
  - leadership distribution approval
- Output:
  - recorded approvals
- Checkpoint:
  - do not distribute without approvals

## Context Architecture (Module 05)

### Required Context

- approved source list
- scoring rubric and criteria definitions
- policy constraints on evidence usage
- output format and approval requirements

### Excluded Context

- non-approved external sources
- stale drafts with unresolved assumptions
- notes without source attribution

### Source Precedence

1. approved spec and policy rules
2. validated evidence sources
3. recent reviewed scoring artifacts

### Refresh Triggers

- criteria or rubric change
- source policy update
- failed evidence traceability validation

### Context Owner

- workflow owner maintains context package per phase
- stakeholder reviewer confirms context quality before approval

## Skills and Reusable Capabilities (Module 06)

### Skill Set

- `SKILL_EVIDENCE_REVIEW.md`
- `SKILL_EVIDENCE_CONTEXT_REFRESH.md`

### Skill Invocation by Phase

- Plan: run `SKILL_EVIDENCE_CONTEXT_REFRESH.md`
- Analyze: run `SKILL_EVIDENCE_CONTEXT_REFRESH.md`
- Draft: run `SKILL_EVIDENCE_CONTEXT_REFRESH.md`
- Validate: run `SKILL_EVIDENCE_CONTEXT_REFRESH.md`, then
  `SKILL_EVIDENCE_REVIEW.md`
- Approve: run `SKILL_EVIDENCE_CONTEXT_REFRESH.md`, then
  `SKILL_EVIDENCE_REVIEW.md`

### Skill Output Contract

- Context refresh output:
  - phase evidence context note
  - escalation flag when blocking source issues exist
- Evidence review output:
  - review findings
  - approval recommendation

### Skill Revision Triggers

- scoring rubric changes
- source policy changes
- recurring evidence validation failures linked to stale context
