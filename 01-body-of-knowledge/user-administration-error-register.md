# User Authorisation and Role Management — Error Register

Module **FRM-022** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](user-administration-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/user-administration-user-manual.md) · [Field catalogue](user-administration-field-catalogue.md) · [Error register](user-administration-error-register.md) · [Practical examples](../10-assessments/user-administration-scenarios.md)

## How to interpret this register

Academy IDs identify documentation entries; they are not runtime codes. Source messages can be dynamic templates. Informational or success notifications found beside errors are labelled source messages and must not be counted as failures. A refusal before the business commit differs from an unknown outcome after a network timeout.

| Situation | Meaning / data state | User response |
| --- | --- | --- |
| Local validation | The current attempt has not passed the form validator; a prior draft or prior attempt can still exist. | Correct the named field and recheck dependent fields/evidence. |
| Server permission/state refusal | The request was refused at a checked condition; inspect the code-specific stage before asserting that nothing at all was saved. | Retain the reference and resolve authority, subject or state; do not bypass the check with another identity. |
| Timeout or dropped connection | Outcome can be uncertain; late processing may succeed. | Reconcile the original attempt and use the workflow’s duplicate-safe recovery path when verified. |
| Local save or media failure | The intended evidence or draft may not be durable yet. | Retain the screen/context and verify storage/upload before leaving. |
| Partial success | One system step may have succeeded while a later write failed. | Follow the effective credential/record state and escalate the incomplete step with identifiers. |

## Source error and message evidence

[Complete extracted register with trigger expressions (CSV)](user-administration-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-022-E001 | `unauthenticated` | Mission denied: Authentication required. | Server source: authorizeFieldWorker · [FS-088:3268](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L3268) |
| FRM-022-E002 | `invalid-argument` | Field worker uid is required. | Server source: authorizeFieldWorker · [FS-088:3277](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L3277) |
| FRM-022-E003 | `permission-denied` | Mission denied: Caller profile not found. | Server source: authorizeFieldWorker · [FS-088:3285](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L3285) |
| FRM-022-E004 | `permission-denied` | Mission denied: Only MNG may authorize field workers. | Server source: authorizeFieldWorker · [FS-088:3299](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L3299) |
| FRM-022-E005 | `failed-precondition` | Caller is not linked to a valid service provider. | Server source: authorizeFieldWorker · [FS-088:3306](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L3306) |
| FRM-022-E006 | `not-found` | Field worker was not found. | Server source: authorizeFieldWorker · [FS-088:3317](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L3317) |
| FRM-022-E007 | `failed-precondition` | Selected user is not a field worker. | Server source: authorizeFieldWorker · [FS-088:3331](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L3331) |
| FRM-022-E008 | `failed-precondition` | Field worker is not linked to a valid service provider. | Server source: authorizeFieldWorker · [FS-088:3338](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L3338) |
| FRM-022-E009 | `failed-precondition` | Field worker is not awaiting manager confirmation. | Server source: authorizeFieldWorker · [FS-088:3348](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L3348) |
| FRM-022-E010 | `permission-denied` | This field worker is outside the manager structure. | Server source: authorizeFieldWorker · [FS-088:3369](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L3369) |
| FRM-022-E011 | `failed-precondition` | No inherited workbases were resolved for this field worker. | Server source: authorizeFieldWorker · [FS-088:3383](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L3383) |
| FRM-022-E012 | `internal` | error.message &#124;&#124; "Could not authorize field worker." | Server source: authorizeFieldWorker · [FS-088:3420](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L3420) |
| FRM-022-E013 | `invalid-argument` | `${label} must be one of ${VALID_USER_ROLES.join(", ")}.` | Server source: assertValidRole · [FS-151:58](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/users/helpers.js#L58) |
| FRM-022-E014 | `permission-denied` | Only SPU, ADM or MNG may change user roles. | Server source: assertRoleManager · [FS-151:71](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/users/helpers.js#L71) |
| FRM-022-E015 | `unauthenticated` | Authentication is required. | Server source: assertNotSelfRoleChange · [FS-151:85](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/users/helpers.js#L85) |
| FRM-022-E016 | `invalid-argument` | Target user uid is required. | Server source: assertNotSelfRoleChange · [FS-151:89](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/users/helpers.js#L89) |
| FRM-022-E017 | `permission-denied` | You cannot change your own role. | Server source: assertNotSelfRoleChange · [FS-151:93](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/users/helpers.js#L93) |
| FRM-022-E018 | `permission-denied` | You cannot change a user at your role level or above. | Server source: assertRoleHierarchy · [FS-151:122](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/users/helpers.js#L122) |
| FRM-022-E019 | `permission-denied` | You cannot assign a role at your role level or above. | Server source: assertRoleHierarchy · [FS-151:129](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/users/helpers.js#L129) |
| FRM-022-E020 | `failed-precondition` | `User already has role ${normalizedPreviousRole}.` | Server source: assertRoleActuallyChanges · [FS-151:147](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/users/helpers.js#L147) |
| FRM-022-E021 | `not-found` | `${label} user was not found.` | Server source: getUserSnapshotOrThrow · [FS-153:23](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/users/updateUserCallable.js#L23) |
| FRM-022-E022 | `failed-precondition` | User is currently assigned to an operational team. Remove the user from the team before assigning this role. | Server source: assertTargetMayLeaveOperationalRole · [FS-153:39](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/users/updateUserCallable.js#L39) |
| FRM-022-E023 | `internal` | Could not update the user role. | Server source: toCallableError · [FS-153:49](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/users/updateUserCallable.js#L49) |
| FRM-022-E024 | `unauthenticated` | Authentication is required. | Server source: updateUserCallable · [FS-153:59](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/users/updateUserCallable.js#L59) |
| FRM-022-E025 | `invalid-argument` | Target user uid is required. | Server source: updateUserCallable · [FS-153:66](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/users/updateUserCallable.js#L66) |
| FRM-022-E026 | `failed-precondition` | Target user does not have a matching Firebase Auth account. | Server source: updateUserCallable · [FS-153:101](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/users/updateUserCallable.js#L101) |
| FRM-022-E027 | `internal` | Role update failed and Firebase Auth rollback also failed. Administrator investigation is required. | Server source: updateUserCallable · [FS-153:147](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/users/updateUserCallable.js#L147) |

## Module-specific recovery and unresolved cases

Capture action-level permissions in a tested matrix. Role labels alone are not authority. Review the current branch against other user-management feature worktrees.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.
