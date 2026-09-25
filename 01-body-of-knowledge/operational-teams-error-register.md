# Operational Teams — Error Register

Module **FRM-024** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](operational-teams-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/operational-teams-user-manual.md) · [Field catalogue](operational-teams-field-catalogue.md) · [Error register](operational-teams-error-register.md) · [Practical examples](../10-assessments/operational-teams-scenarios.md)

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

[Complete extracted register with trigger expressions (CSV)](operational-teams-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-024-E001 | `LOCAL_MESSAGE` | error?.message &#124;&#124; "Operation failed." | Client source: handleCreateOrUpdateTeam · [FS-012:237](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/teams.js#L237) |
| FRM-024-E002 | `LOCAL_MESSAGE` | error?.message &#124;&#124; "Could not add user to team." | Client source: handleAssignUserToTeam · [FS-012:287](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/teams.js#L287) |
| FRM-024-E003 | `LOCAL_MESSAGE` | Team cannot be deleted if it has members.<br>First remove all members. | Client source: handleDeleteTeam · [FS-012:314](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/teams.js#L314) |
| FRM-024-E004 | `LOCAL_MESSAGE` | Are you sure you want to delete this team? | Client source: handleDeleteTeam · [FS-012:322](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/teams.js#L322) |
| FRM-024-E005 | `LOCAL_MESSAGE` | error?.message &#124;&#124; "Could not delete team." | Client source: handleDeleteTeam · [FS-012:333](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/teams.js#L333) |
| FRM-024-E006 | `LOCAL_MESSAGE` | error?.message &#124;&#124; "Could not remove user from team." | Client source: handleRemoveUserFromTeam · [FS-012:356](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/teams.js#L356) |
| FRM-024-E007 | `unauthenticated` | Authentication is required. | Server source: createTeam · [FS-146:37](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/callables.js#L37) |
| FRM-024-E008 | `invalid-argument` | Team name is required. | Server source: createTeam · [FS-146:44](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/callables.js#L44) |
| FRM-024-E009 | `unauthenticated` | Authentication is required. | Server source: renameTeam · [FS-146:88](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/callables.js#L88) |
| FRM-024-E010 | `invalid-argument` | Team id is required. | Server source: renameTeam · [FS-146:95](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/callables.js#L95) |
| FRM-024-E011 | `invalid-argument` | Team name is required. | Server source: renameTeam · [FS-146:99](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/callables.js#L99) |
| FRM-024-E012 | `not-found` | Team not found. | Server source: renameTeam · [FS-146:112](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/callables.js#L112) |
| FRM-024-E013 | `unauthenticated` | Authentication is required. | Server source: addTeamMember · [FS-146:150](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/callables.js#L150) |
| FRM-024-E014 | `invalid-argument` | Team id and user uid are required. | Server source: addTeamMember · [FS-146:157](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/callables.js#L157) |
| FRM-024-E015 | `not-found` | Team not found. | Server source: addTeamMember · [FS-146:173](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/callables.js#L173) |
| FRM-024-E016 | `already-exists` | User is already a member of this team. | Server source: addTeamMember · [FS-146:195](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/callables.js#L195) |
| FRM-024-E017 | `unauthenticated` | Authentication is required. | Server source: removeTeamMember · [FS-146:252](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/callables.js#L252) |
| FRM-024-E018 | `invalid-argument` | Team id and user uid are required. | Server source: removeTeamMember · [FS-146:259](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/callables.js#L259) |
| FRM-024-E019 | `not-found` | Team not found. | Server source: removeTeamMember · [FS-146:275](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/callables.js#L275) |
| FRM-024-E020 | `not-found` | User is not a member of this team. | Server source: removeTeamMember · [FS-146:287](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/callables.js#L287) |
| FRM-024-E021 | `unauthenticated` | Authentication is required. | Server source: deleteTeam · [FS-146:338](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/callables.js#L338) |
| FRM-024-E022 | `invalid-argument` | Team id is required. | Server source: deleteTeam · [FS-146:344](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/callables.js#L344) |
| FRM-024-E023 | `not-found` | Team not found. | Server source: deleteTeam · [FS-146:357](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/callables.js#L357) |
| FRM-024-E024 | `unauthenticated` | Sign in to continue. | Server source: getFieldWorkSummary · [FS-148:18](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/fieldWorkSummaryCallable.js#L18) |
| FRM-024-E025 | `invalid-argument` | A valid LM is required. | Server source: getFieldWorkSummary · [FS-148:20](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/fieldWorkSummaryCallable.js#L20) |
| FRM-024-E026 | `permission-denied` | Only management users can see the Allocation Matrix. | Server source: getFieldWorkSummary · [FS-148:24](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/fieldWorkSummaryCallable.js#L24) |
| FRM-024-E027 | `permission-denied` | The LM must be one of your workbases. | Server source: getFieldWorkSummary · [FS-148:26](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/fieldWorkSummaryCallable.js#L26) |
| FRM-024-E028 | `invalid-argument` | User uid is required. | Server source: getUserDocByUid · [FS-149:131](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/helpers.js#L131) |
| FRM-024-E029 | `not-found` | `User [${safeUid}] was not found.` | Server source: getUserDocByUid · [FS-149:137](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/helpers.js#L137) |
| FRM-024-E030 | `unauthenticated` | Authentication is required. | Server source: getActorUserDoc · [FS-149:151](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/helpers.js#L151) |
| FRM-024-E031 | `permission-denied` | Only MNG or SPV may manage teams. | Server source: assertTeamManagerRole · [FS-149:161](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/helpers.js#L161) |
| FRM-024-E032 | `failed-precondition` | Actor is not linked to a valid service provider. | Server source: resolveActorMncContext · [FS-149:297](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/helpers.js#L297) |
| FRM-024-E033 | `not-found` | Actor service provider was not found. | Server source: resolveActorMncContext · [FS-149:309](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/helpers.js#L309) |
| FRM-024-E034 | `failed-precondition` | Could not resolve actor MNC context. | Server source: resolveActorMncContext · [FS-149:319](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/helpers.js#L319) |
| FRM-024-E035 | `permission-denied` | User is outside the allowed MNC hierarchy. | Server source: assertUserAllowedInMncHierarchy · [FS-149:374](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/helpers.js#L374) |
| FRM-024-E036 | `failed-precondition` | Only FWR or SPV users may be team members. | Server source: assertTeamEligibleUser · [FS-149:387](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/helpers.js#L387) |
| FRM-024-E037 | `failed-precondition` | Team ownership is missing a valid MNC service provider. | Server source: assertTeamBelongsToActorMnc · [FS-149:458](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/helpers.js#L458) |
| FRM-024-E038 | `permission-denied` | You may only manage teams in your MNC hierarchy. | Server source: assertTeamBelongsToActorMnc · [FS-149:465](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/helpers.js#L465) |
| FRM-024-E039 | `invalid-argument` | Team id is required. | Server source: buildTeamCreatePayload · [FS-149:487](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/helpers.js#L487) |
| FRM-024-E040 | `invalid-argument` | Team name is required. | Server source: buildTeamCreatePayload · [FS-149:493](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/helpers.js#L493) |

## Module-specific recovery and unresolved cases

Verify eligibility, deletion guards and assignment effects in the target release. The form inventory records both mobile and web implementations.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.
