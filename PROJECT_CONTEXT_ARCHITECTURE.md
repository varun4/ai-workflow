# Project Context Architecture

## Canonical Rule

This file is the single source of truth for project-level context
package rules, source precedence, context owners, and refresh triggers.
Other files should reference this file, not duplicate its rules.

## Agent Context Source Policy

- Agents must load operating context from `AGENTS.md` and the operating
  files referenced there.
- `README.md` is for human onboarding and navigation only.
- `README.md` is not an authoritative policy source for agent execution.

## Purpose

Define how context is selected, ordered, refreshed, and validated before
module generation and track workflow updates.

## Context Package Contract (Required)

Before module generation, define:
1. required context
2. excluded context
3. persistent context
4. source precedence
5. refresh triggers
6. context owners by phase
7. validation checks

## Required Context (Default)

- `AGENTS.md`
- `PROJECT_CONTEXT_ARCHITECTURE.md`
- `SPEC.md`
- `APPROVAL_BOUNDARIES.md`
- `EVAL_CHECKLIST.md`
- `SKILL_EVIDENCE_REVIEW.md`
- `PROGRESS.md`
- `docs/standards/MODULE_DONE_CHECKLIST_TEMPLATE.md`
- active module folder: `course/modules/NN-*`
- both track workflows:
  - `examples/developers/rbac-admin-workflow/`
  - `examples/knowledge-workers/vendor-selection-workflow/`

## Excluded Context (Default)

- unrelated module folders not in current scope
- stale drafts without approved status
- generated exports not required by module contract
- unrelated historical notes not referenced by current task

## Persistent Context (Always Loaded, Reference-Backed)

Load these exact rules from these exact locations:
- Repository purpose and scope:
  - `AGENTS.md` -> `## Repository Purpose`
  - `AGENTS.md` -> `## Scope`
- Module generation contract:
  - `AGENTS.md` -> `## Module Generation Contract Rule`
- Module output rule:
  - `AGENTS.md` -> `## Module Output Rule`
  - `SPEC.md` -> `### Module Output Rule`
- Automation verification rule:
  - `AGENTS.md` -> `## Automation Verification Rule`
  - `EVAL_CHECKLIST.md` -> `## Module Quality Gates (Blocking)`
  - `EVAL_CHECKLIST.md` -> `## Module Output Gates (Blocking)`
- Crisp language rule:
  - `AGENTS.md` -> `## Crisp Language Rule`
- Definition-first writing rule:
  - `SPEC.md` -> `### Module Automation Constraints`
  - `EVAL_CHECKLIST.md` -> `## Module Quality Gates (Blocking)`
If any referenced heading is missing or renamed, stop and ask.

## Source Precedence (Conflict Resolution)

If sources conflict, resolve in this order:
1. `AGENTS.md`
2. `PROJECT_CONTEXT_ARCHITECTURE.md`
3. `APPROVAL_BOUNDARIES.md`
4. `EVAL_CHECKLIST.md`
5. `SPEC.md`
6. active module files under `course/modules/NN-*`
7. active track workflow files under `examples/...`
8. `PROGRESS.md`
`README.md` is excluded from policy precedence.
If conflict remains unresolved, stop and ask.

## Context Owners by Workflow Phase

### Phase 1: SOTA Research

- Owner: module-generation agent
- Accountability: source quality and completeness

### Phase 2: Module Drafting

- Owner: module-generation agent
- Accountability: contract-compliant module content

### Phase 3: Track Workflow Updates

- Owner: workflow-update agent
- Accountability: both track updates and delta files

### Phase 4: Validation and Checklist

- Owner: validation agent
- Accountability: quality gates and PASS/FAIL checklist integrity

### Phase 5: Approval and Delivery

- Owner: human maintainer
- Accountability: final approval and commit/push decision

## Refresh Triggers (Mandatory Rebuild)

Rebuild context package when any of these occur:
- module scope or module number changes
- SOTA summary is approved
- any change to:
  - `AGENTS.md`
  - `SPEC.md`
  - `APPROVAL_BOUNDARIES.md`
  - `EVAL_CHECKLIST.md`
  - `SKILL_EVIDENCE_REVIEW.md`
- validation failure occurs
- source conflict is detected
- before setting `MODULE_DONE_CHECKLIST.md` to PASS

## Validation Requirements

Before writing:
- context package is defined and complete
- source precedence is present
- active module and both tracks are included
Before completion:
- refresh triggers were evaluated
- no unresolved source conflicts remain
- context decisions and validation are logged in `PROGRESS.md`
