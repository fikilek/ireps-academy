# Meter Reading Staging and Export — Error Register

Module **FRM-032** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](reading-staging-body-of-knowledge.md) · [User Manual](../02-user-manual/web/reading-staging-user-manual.md) · [Field catalogue](reading-staging-field-catalogue.md) · [Error register](reading-staging-error-register.md) · [Practical examples](../10-assessments/reading-staging-scenarios.md)

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

[Complete extracted register with trigger expressions (CSV)](reading-staging-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-032-E001 | `failed-precondition` | Cycle window is missing or invalid. Cannot generate MREAD staging. | Server source: getCycleWindow · [FS-098:193](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/generateMreadStaging.js#L193) |
| FRM-032-E002 | `unauthenticated` | You must be signed in to generate MREAD staging. | Server source: assertCanGenerate · [FS-098:1064](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/generateMreadStaging.js#L1064) |
| FRM-032-E003 | `permission-denied` | Your role is not allowed to generate MREAD staging. | Server source: assertCanGenerate · [FS-098:1074](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/generateMreadStaging.js#L1074) |
| FRM-032-E004 | `permission-denied` | You are not authorised for this LM staging cycle. | Server source: assertCanGenerate · [FS-098:1082](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/generateMreadStaging.js#L1082) |
| FRM-032-E005 | `failed-precondition` | error?.message &#124;&#124; "Unable to resolve selected MREAD staging cycle." | Server source: resolveSelectedCycleContext · [FS-098:1362](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/generateMreadStaging.js#L1362) |
| FRM-032-E006 | `not-found` | MREAD staging cycle not found. | Server source: fetchCycleForGeneration · [FS-098:1379](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/generateMreadStaging.js#L1379) |
| FRM-032-E007 | `failed-precondition` | Cycle LM is missing. | Server source: fetchCycleForGeneration · [FS-098:1393](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/generateMreadStaging.js#L1393) |
| FRM-032-E008 | `not-found` | MREAD staging cycle not found. | Server source: lockCycleForGeneration · [FS-098:1406](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/generateMreadStaging.js#L1406) |
| FRM-032-E009 | `aborted` | MREAD staging generation is already running for this cycle. | Server source: lockCycleForGeneration · [FS-098:1423](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/generateMreadStaging.js#L1423) |
| FRM-032-E010 | `failed-precondition` | Cycle LM is missing. | Server source: lockCycleForGeneration · [FS-098:1432](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/generateMreadStaging.js#L1432) |
| FRM-032-E011 | `error?.code &#124;&#124; error?.details?.code &#124;&#124; "GENERATE_MREAD_STAGING_FAILED"` | error?.message &#124;&#124; "Failed to generate MREAD staging." | Server source: markGenerationFailed · [FS-098:1539](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/generateMreadStaging.js#L1539) |
| FRM-032-E012 | `invalid-argument` | cycleId is required. | Server source: generateMreadStaging · [FS-098:1602](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/generateMreadStaging.js#L1602) |
| FRM-032-E013 | `error?.code` | error?.message | Server source: generateMreadStaging · [FS-098:1821](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/generateMreadStaging.js#L1821) |
| FRM-032-E014 | `internal` | error?.message &#124;&#124; "Failed to generate MREAD staging." | Server source: generateMreadStaging · [FS-098:1847](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/generateMreadStaging.js#L1847) |
| FRM-032-E015 | `unauthenticated` | Authentication required | Server source: loadCallerContext · [FS-100:137](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/listMreadStagingCycles.js#L137) |
| FRM-032-E016 | `permission-denied` | Manager is not assigned to the requested LM workbase | Server source: assertCanReadMreadStagingCycles · [FS-100:172](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/listMreadStagingCycles.js#L172) |
| FRM-032-E017 | `permission-denied` | Supervisor is not linked to a service provider | Server source: assertCanReadMreadStagingCycles · [FS-100:186](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/listMreadStagingCycles.js#L186) |
| FRM-032-E018 | `permission-denied` | Supervisor service provider was not found | Server source: assertCanReadMreadStagingCycles · [FS-100:198](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/listMreadStagingCycles.js#L198) |
| FRM-032-E019 | `permission-denied` | Only main-contractor supervisors may view MREAD staging cycles | Server source: assertCanReadMreadStagingCycles · [FS-100:207](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/listMreadStagingCycles.js#L207) |
| FRM-032-E020 | `permission-denied` | Supervisor is not assigned to the requested LM workbase | Server source: assertCanReadMreadStagingCycles · [FS-100:214](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/listMreadStagingCycles.js#L214) |
| FRM-032-E021 | `permission-denied` | Only SPU, MNG, or SPV(MNC) may view MREAD staging cycles | Server source: assertCanReadMreadStagingCycles · [FS-100:226](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/listMreadStagingCycles.js#L226) |
| FRM-032-E022 | `invalid-argument` | lmPcode is required for non-SPU users | Server source: listMreadStagingCycles · [FS-100:369](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/listMreadStagingCycles.js#L369) |
| FRM-032-E023 | `invalid-argument` | stagingId is required | Server source: listMreadStagingRows · [FS-101:121](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/listMreadStagingRows.js#L121) |
| FRM-032-E024 | `invalid-argument` | wardPcode is required for MREAD staging row reads | Server source: listMreadStagingRows · [FS-101:125](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/listMreadStagingRows.js#L125) |
| FRM-032-E025 | `not-found` | Staging session not found | Server source: listMreadStagingRows · [FS-101:137](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/listMreadStagingRows.js#L137) |
| FRM-032-E026 | `invalid-argument` | Staging session does not match requested LM scope | Server source: listMreadStagingRows · [FS-101:149](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/listMreadStagingRows.js#L149) |
| FRM-032-E027 | `invalid-argument` | lmPcode is required for non-SPU users | Server source: listMreadStagingSessions · [FS-102:128](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/listMreadStagingSessions.js#L128) |
| FRM-032-E028 | `error?.code &#124;&#124; "LIST_MREAD_STAGING_SESSIONS_FAILED"` | error?.message &#124;&#124; String(error) | Server source: listMreadStagingSessions · [FS-102:164](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/listMreadStagingSessions.js#L164) |
| FRM-032-E029 | `LIST_MREAD_STAGING_SESSIONS_FAILED` | error?.message &#124;&#124; "Could not load MREAD staging sessions" | Server source: listMreadStagingSessions · [FS-102:173](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/listMreadStagingSessions.js#L173) |
| FRM-032-E030 | `PERMISSION_DENIED` | Only authorised users may rebuild registry_mread. | Server source: rebuildRegistryMreadCallable · [FS-105:43](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/rebuildRegistryMread.js#L43) |

## Module-specific recovery and unresolved cases

Owner states this module needs strengthening before production readiness. Automated billing-system integration and full customer billing remain future work. Do not invent an approval button where the page only filters or downloads.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.
