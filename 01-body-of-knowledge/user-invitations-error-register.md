# User Invitations — Error Register

Module **FRM-021** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](user-invitations-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/invite-a-user.md) · [Field catalogue](user-invitations-field-catalogue.md) · [Error register](user-invitations-error-register.md) · [Practical examples](../10-assessments/user-invitations-scenarios.md)

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

[Complete extracted register with trigger expressions (CSV)](user-invitations-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-021-E001 | `LOCAL_MESSAGE` | Only a Manager may create a Supervisor. | Client source: handleCreateSupervisor · [FS-022:143](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-supervisor.js#L143) |
| FRM-021-E002 | `LOCAL_MESSAGE` | This Manager is not linked to a valid Service Provider. | Client source: handleCreateSupervisor · [FS-022:148](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-supervisor.js#L148) |
| FRM-021-E003 | `LOCAL_MESSAGE` | Name, surname, email and service provider are required. | Client source: handleCreateSupervisor · [FS-022:156](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-supervisor.js#L156) |
| FRM-021-E004 | `LOCAL_MESSAGE` | Please enter a valid email address. | Client source: handleCreateSupervisor · [FS-022:164](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-supervisor.js#L164) |
| FRM-021-E005 | `LOCAL_MESSAGE` | Please choose the Service Provider the Supervisor belongs to. | Client source: handleCreateSupervisor · [FS-022:169](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-supervisor.js#L169) |
| FRM-021-E006 | `LOCAL_MESSAGE` | The Supervisor was created successfully. Default password is 'password' and must be changed on first login. | Client source: handleCreateSupervisor · [FS-022:187](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-supervisor.js#L187) |
| FRM-021-E007 | `LOCAL_MESSAGE` | error?.message &#124;&#124; "The Supervisor could not be created." | Client source: handleCreateSupervisor · [FS-022:193](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-supervisor.js#L193) |
| FRM-021-E008 | `LOCAL_MESSAGE` | Email, name and surname are required. | Client source: handleSubmit · [FS-021:69](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-manager.js#L69) |
| FRM-021-E009 | `LOCAL_MESSAGE` | Select a Main Contractor first. | Client source: handleSubmit · [FS-021:73](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-manager.js#L73) |
| FRM-021-E010 | `LOCAL_MESSAGE` | `Manager ${values.name.trim()} invited successfully.` | Client source: handleSubmit · [FS-021:87](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-manager.js#L87) |
| FRM-021-E011 | `LOCAL_MESSAGE` | err?.data &#124;&#124; err?.message &#124;&#124; "Could not invite manager." | Client source: handleSubmit · [FS-021:93](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-manager.js#L93) |
| FRM-021-E012 | `LOCAL_MESSAGE` | All identity fields are required. | Client source: handleSubmit · [FS-020:17](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-admin.js#L17) |
| FRM-021-E013 | `LOCAL_MESSAGE` | `Administrator ${values.name} appointed to smars.` | Client source: handleSubmit · [FS-020:29](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-admin.js#L29) |
| FRM-021-E014 | `LOCAL_MESSAGE` | err?.message &#124;&#124; "Could not appoint administrator" | Client source: handleSubmit · [FS-020:35](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-admin.js#L35) |
| FRM-021-E015 | `unauthenticated` | Authentication required | Server source: createAdminUser · [FS-088:775](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L775) |
| FRM-021-E016 | `permission-denied` | SPU only | Server source: createAdminUser · [FS-088:780](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L780) |
| FRM-021-E017 | `invalid-argument` | Missing required fields | Server source: createAdminUser · [FS-088:786](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L786) |
| FRM-021-E018 | `unauthenticated` | Mission denied: Authentication required. | Server source: inviteManagerUser · [FS-088:2285](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2285) |
| FRM-021-E019 | `invalid-argument` | Email, name, surname and MNC are required. | Server source: inviteManagerUser · [FS-088:2295](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2295) |
| FRM-021-E020 | `permission-denied` | Mission denied: Caller profile not found. | Server source: inviteManagerUser · [FS-088:2311](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2311) |
| FRM-021-E021 | `permission-denied` | Mission denied: Only SPU or ADM may create a manager. | Server source: inviteManagerUser · [FS-088:2322](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2322) |
| FRM-021-E022 | `not-found` | Selected service provider was not found. | Server source: inviteManagerUser · [FS-088:2333](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2333) |
| FRM-021-E023 | `failed-precondition` | Selected service provider is not active. | Server source: inviteManagerUser · [FS-088:2345](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2345) |
| FRM-021-E024 | `failed-precondition` | Selected service provider has no clients. | Server source: inviteManagerUser · [FS-088:2352](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2352) |
| FRM-021-E025 | `failed-precondition` | Selected service provider has no LM clients to inherit as workbases. | Server source: inviteManagerUser · [FS-088:2376](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2376) |
| FRM-021-E026 | `already-exists` | A user with this email already exists. | Server source: inviteManagerUser · [FS-088:2385](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2385) |
| FRM-021-E027 | `internal` | err.message | Server source: inviteManagerUser · [FS-088:2392](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2392) |
| FRM-021-E028 | `internal` | error.message &#124;&#124; "Could not create manager." | Server source: inviteManagerUser · [FS-088:2479](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2479) |
| FRM-021-E029 | `unauthenticated` | Mission denied: Authentication required. | Server source: inviteSupervisorUser · [FS-088:2491](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2491) |
| FRM-021-E030 | `invalid-argument` | Email, name, surname and service provider are required. | Server source: inviteSupervisorUser · [FS-088:2507](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2507) |
| FRM-021-E031 | `permission-denied` | Mission denied: Caller profile not found. | Server source: inviteSupervisorUser · [FS-088:2523](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2523) |
| FRM-021-E032 | `permission-denied` | Mission denied: Only MNG may create a supervisor. | Server source: inviteSupervisorUser · [FS-088:2538](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2538) |
| FRM-021-E033 | `failed-precondition` | Caller is not linked to a valid service provider. | Server source: inviteSupervisorUser · [FS-088:2545](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2545) |
| FRM-021-E034 | `not-found` | Selected service provider was not found. | Server source: inviteSupervisorUser · [FS-088:2564](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2564) |
| FRM-021-E035 | `failed-precondition` | Selected service provider is not active. | Server source: inviteSupervisorUser · [FS-088:2575](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2575) |
| FRM-021-E036 | `permission-denied` | Selected service provider is outside the manager structure. | Server source: inviteSupervisorUser · [FS-088:2588](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2588) |
| FRM-021-E037 | `failed-precondition` | Selected service provider has no inherited workbases to assign. | Server source: inviteSupervisorUser · [FS-088:2601](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2601) |
| FRM-021-E038 | `already-exists` | A user with this email already exists. | Server source: inviteSupervisorUser · [FS-088:2610](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2610) |
| FRM-021-E039 | `internal` | err.message | Server source: inviteSupervisorUser · [FS-088:2617](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2617) |
| FRM-021-E040 | `internal` | error.message &#124;&#124; "Could not create supervisor." | Server source: inviteSupervisorUser · [FS-088:2709](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2709) |
| FRM-021-E041 | `unauthenticated` | Mission denied. | Server source: inviteAdminUser · [FS-088:2720](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2720) |
| FRM-021-E042 | `internal` | error.message | Server source: inviteAdminUser · [FS-088:2797](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L2797) |

## Module-specific recovery and unresolved cases

Do not publish fixed-password examples from historical code. Verify the once-displayed password behaviour in the target build; invitations and re-invitations can have partial success.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.
