# Approval Boundaries

## Ask-First Conditions

- Any change to role model definitions.
- Any auth provider integration change.
- Any broadening of admin access permissions.
- Any deployment of RBAC changes to production.
- Any promotion from sandbox to pilot.
- Any promotion from pilot to production.
- Any override of a blocking security or adoption gate.
- Any decision to ignore an active rollback trigger.

## Required Signoffs

- Security review signoff before merge.
- Service owner approval before pilot rollout.
- Security reviewer and service owner approval before production.
- Incident owner approval before rollback closure.
