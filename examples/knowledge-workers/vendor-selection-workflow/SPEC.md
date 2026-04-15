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

## Evaluation and Failure Patterns (Module 07)

### Evaluation Objective

Detect and stop evidence and recommendation quality failures before
leadership distribution.

### Evaluation Loop by Phase

- Plan:
  - Check: criteria, rubric, and approved source set are confirmed.
  - Pass condition: planning inputs are approved.
  - Fail action: stop evidence collection and resolve input gaps.
- Analyze:
  - Check: each vendor has complete evidence across all criteria.
  - Pass condition: comparison matrix is complete and traceable.
  - Fail action: fill missing evidence or mark scoped limitation.
- Validate:
  - Check: recommendation claims map to approved citations.
  - Pass condition: no unsupported major claims remain.
  - Fail action: map failure to pattern ID and execute recovery.
- Approve:
  - Check: stakeholder review and distribution approval are recorded.
  - Pass condition: no unresolved blocking failures.
  - Fail action: block distribution and escalate.

### Embedded Failure Patterns

- `FP-VENDOR-01` Non-approved source usage
  - Symptom: claim cites source outside approved list.
  - Root cause: source boundary not enforced in Analyze phase.
  - Detection signal: source audit mismatch.
  - Prevention pattern: approved-source gate before scoring.
  - Recovery action: replace source or remove claim.
- `FP-VENDOR-02` Rubric mismatch
  - Symptom: scoring rationale does not match defined criteria.
  - Root cause: rubric applied inconsistently.
  - Detection signal: criterion-to-score traceability gap.
  - Prevention pattern: rubric consistency check before Draft.
  - Recovery action: rescore affected rows and update rationale.
- `FP-VENDOR-03` Unsupported recommendation claim
  - Symptom: recommendation statement has no approved citation.
  - Root cause: draft written ahead of evidence validation.
  - Detection signal: failed citation traceability check.
  - Prevention pattern: validate claim-to-source mapping before
    approval.
  - Recovery action: add approved evidence or remove claim.
- `FP-VENDOR-04` Distribution before approval
  - Symptom: brief shared without stakeholder signoff.
  - Root cause: approval gate bypass.
  - Detection signal: missing approval record.
  - Prevention pattern: hard distribution gate.
  - Recovery action: halt distribution and complete approvals.

### Evaluation Evidence Requirements

Record in `PROGRESS.md` for each phase:

- checkpoint name
- pass/fail decision
- failure pattern ID (if failed)
- recovery action and rerun result

## Security and Adoption Controls

### Security Objective

Prevent untrusted evidence and unsafe recommendation distribution.

### Security Control Map

- Risky action: use non-approved source for major claim.
  - Control rule: block draft and validate phases until corrected.
  - Required approval: workflow owner confirms approved source use.
  - Stop condition: source is outside approved list.
- Risky action: include legal or compliance claim without evidence.
  - Control rule: require explicit citation and reviewer check.
  - Required approval: stakeholder owner signoff.
  - Stop condition: citation basis is missing.
- Risky action: distribute brief outside approved group.
  - Control rule: enforce distribution boundary gate.
  - Required approval: stakeholder owner and director signoff.
  - Stop condition: required signoff record is missing.
- Risky action: proceed with unresolved blocking failures.
  - Control rule: block adoption stage promotion.
  - Required approval: decision owner records blocker closure.
  - Stop condition: unresolved blocking `FP-VENDOR-*` pattern.

### Adoption Gates

- Gate 1: Internal Draft
  - Entry criteria: criteria, rubric, and source set approved.
  - Required evidence: completed traceability and quality checks.
  - Decision owner: workflow owner.
  - Exit decision: go to leadership pilot only if blockers are clear.
- Gate 2: Limited Leadership Pilot
  - Entry criteria: internal draft gate passed with evidence.
  - Required evidence: pilot review notes and approval record.
  - Decision owner: stakeholder owner.
  - Exit decision: go operational only with director signoff.
- Gate 3: Operational Use
  - Entry criteria: leadership pilot gate passed.
  - Required evidence: distribution boundary check and approvals.
  - Decision owner: stakeholder owner and director.
  - Exit decision: operational use only if no rollback trigger is
    active.

### Rollback Triggers

- unsupported major recommendation claim
- non-approved source used in final brief
- confidentiality boundary breach
- missing required approval record at gate exit

### Security and Adoption Evidence Requirements

Record in `PROGRESS.md` for each gate:

- gate name and decision owner
- go/no-go decision
- blocking failure pattern IDs (if any)
- rollback trigger status and action taken
