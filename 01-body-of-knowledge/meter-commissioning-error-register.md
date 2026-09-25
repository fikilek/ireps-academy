# Meter Commissioning — Error Register

Module **FRM-014** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](meter-commissioning-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/meter-commissioning-user-manual.md) · [Field catalogue](meter-commissioning-field-catalogue.md) · [Error register](meter-commissioning-error-register.md) · [Practical examples](../10-assessments/meter-commissioning-scenarios.md)

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

[Complete extracted register with trigger expressions (CSV)](meter-commissioning-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-014-E001 | `LOCAL_MESSAGE` | {<br>              message: "Vending evidence required",<br>            } | Client source: buildCommissioningSchema · [FS-023:261](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/commissioning.jsx#L261) |
| FRM-014-E002 | `LOCAL_MESSAGE` | {<br>              message: "Final switch-on evidence required",<br>            } | Client source: buildCommissioningSchema · [FS-023:271](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/commissioning.jsx#L271) |
| FRM-014-E003 | `LOCAL_MESSAGE` | {<br>              message: "Keypad issued evidence required",<br>            } | Client source: buildCommissioningSchema · [FS-023:281](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/commissioning.jsx#L281) |
| FRM-014-E004 | `LOCAL_MESSAGE` | {<br>              message: "Water operational evidence required",<br>            } | Client source: buildCommissioningSchema · [FS-023:291](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/commissioning.jsx#L291) |
| FRM-014-E005 | `LOCAL_MESSAGE` | {<br>              message: "Water reading / flow evidence required",<br>            } | Client source: buildCommissioningSchema · [FS-023:301](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/commissioning.jsx#L301) |
| FRM-014-E006 | `LOCAL_MESSAGE` | AST data not found. | Client source: handleSubmitCommissioning · [FS-023:714](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/commissioning.jsx#L714) |
| FRM-014-E007 | `LOCAL_MESSAGE` | Only FIELD electricity or water meters can be commissioned by FWR or SPV(SUBC). | Client source: handleSubmitCommissioning · [FS-023:719](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/commissioning.jsx#L719) |
| FRM-014-E008 | `NAv` | NAv | Client source: saveCommissioningDraftToQueue · [FS-023:773](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/commissioning.jsx#L773) |
| FRM-014-E009 | `LOCAL_MESSAGE` | Failed to save commissioning draft locally. | Client source: saveCommissioningDraftToQueue · [FS-023:798](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/commissioning.jsx#L798) |
| FRM-014-E010 | `LOCAL_MESSAGE` | error?.message &#124;&#124; "Meter commissioning submission failed." | Client source: handleSubmitCommissioning · [FS-023:898](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/commissioning.jsx#L898) |
| FRM-014-E011 | `LOCAL_MESSAGE` | result?.message &#124;&#124; "Meter commissioning submission failed." | Client source: handleSubmitCommissioning · [FS-023:910](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/commissioning.jsx#L910) |
| FRM-014-E012 | `LOCAL_MESSAGE` | error?.message &#124;&#124; "Submission failed" | Client source: handleSubmitCommissioning · [FS-023:952](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/commissioning.jsx#L952) |
| FRM-014-E013 | `UNAUTHENTICATED` | Authentication is required | Server source: onCreateMeterCommissioningCallable · [FS-069:30](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/callable.js#L30) |
| FRM-014-E014 | `dynamic code` | inputCheck.message | Server source: onCreateMeterCommissioningCallable · [FS-069:43](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/callable.js#L43) |
| FRM-014-E015 | `INVALID_COMMISSIONING_TRN_TYPE` | Only METER_COMMISSIONING is supported by this callable | Server source: onCreateMeterCommissioningCallable · [FS-069:57](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/callable.js#L57) |
| FRM-014-E016 | `AST_NOT_FOUND` | The referenced AST does not exist | Server source: onCreateMeterCommissioningCallable · [FS-069:111](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/callable.js#L111) |
| FRM-014-E017 | `PREMISE_NOT_FOUND` | The referenced premise does not exist | Server source: onCreateMeterCommissioningCallable · [FS-069:126](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/callable.js#L126) |
| FRM-014-E018 | `dynamic code` | batchWorkCheck.message | Server source: onCreateMeterCommissioningCallable · [FS-069:162](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/callable.js#L162) |
| FRM-014-E019 | `dynamic code` | commissioningCheck?.message | Server source: onCreateMeterCommissioningCallable · [FS-069:183](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/callable.js#L183) |
| FRM-014-E020 | `UNKNOWN_ERROR` | Commissioning TRN was not created | Server source: onCreateMeterCommissioningCallable · [FS-069:231](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/callable.js#L231) |
| FRM-014-E021 | `dynamic code` | error?.message &#124;&#124; "Failed to create commissioning TRN" | Server source: onCreateMeterCommissioningCallable · [FS-069:246](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/callable.js#L246) |
| FRM-014-E022 | `INVALID_COMMISSIONING_ANSWER` | `${fieldLabel} must be answered yes or no` | Server source: validateRequiredCommissioningCheck · [FS-070:100](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/helpers.js#L100) |
| FRM-014-E023 | `COMMISSIONING_NOTES_REQUIRED` | `Notes are required when ${fieldLabel} is no` | Server source: validateRequiredCommissioningCheck · [FS-070:108](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/helpers.js#L108) |
| FRM-014-E024 | `COMMISSIONING_EVIDENCE_REQUIRED` | `${evidenceLabel &#124;&#124; fieldLabel} evidence is required` | Server source: validateRequiredCommissioningCheck · [FS-070:116](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/helpers.js#L116) |
| FRM-014-E025 | `INVALID_TRN_ID` | Commissioning TRN id is required | Server source: validateCommissioningCreateInput · [FS-070:170](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/helpers.js#L170) |
| FRM-014-E026 | `INVALID_COMMISSIONING_TRN_ID` | `Commissioning TRN id must start with ${COMMISSIONING_TRN_PREFIX}` | Server source: validateCommissioningCreateInput · [FS-070:178](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/helpers.js#L178) |
| FRM-014-E027 | `INVALID_ACCESS_DATA` | accessData is required | Server source: validateCommissioningCreateInput · [FS-070:186](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/helpers.js#L186) |
| FRM-014-E028 | `INVALID_COMMISSIONING_TRN_TYPE` | accessData.trnType must be METER_COMMISSIONING | Server source: validateCommissioningCreateInput · [FS-070:194](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/helpers.js#L194) |
| FRM-014-E029 | `INVALID_AST_ID` | ast.astData.astId is required | Server source: validateCommissioningCreateInput · [FS-070:202](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/helpers.js#L202) |
| FRM-014-E030 | `INVALID_PREMISE_ID` | A valid premise id is required | Server source: validateCommissioningCreateInput · [FS-070:210](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/helpers.js#L210) |
| FRM-014-E031 | `INVALID_COMMISSIONING_DATA` | commissioning answers are required | Server source: validateCommissioningCreateInput · [FS-070:218](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/helpers.js#L218) |
| FRM-014-E032 | `AST_NOT_FIELD` | Only FIELD meters can be commissioned | Server source: validateCommissioningAgainstAst · [FS-070:243](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/helpers.js#L243) |
| FRM-014-E033 | `INVALID_COMMISSIONING_METER_TYPE` | Only electricity or water meters can be commissioned | Server source: validateCommissioningAgainstAst · [FS-070:256](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/helpers.js#L256) |
| FRM-014-E034 | `commissioningCheck?.code` | commissioningCheck?.message | Server source:  · [FS-071:134](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/trigger.js#L134) |
| FRM-014-E035 | `astPatchResult.code` | astPatchResult.message | Server source:  · [FS-071:162](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/trigger.js#L162) |
| FRM-014-E036 | `NAv` | NAv | Client source: addSubmissionQueueItem · [FS-058:87](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L87) |
| FRM-014-E037 | `result?.code &#124;&#124; "SUCCESS"` | result?.message &#124;&#124; "Synced successfully" | Client source: markSubmissionQueueItemSuccess · [FS-058:288](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L288) |
| FRM-014-E038 | `result?.code &#124;&#124; "SYNC_FAILED"` | result?.message &#124;&#124; "Sync failed. This draft remains pending for retry." | Client source: markSubmissionQueueItemFailed · [FS-058:319](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L319) |
| FRM-014-E039 | `result?.code &#124;&#124; "SYNC_FAILED"` | result?.message &#124;&#124;<br>          "Sync failed. This draft remains pending for retry." | Client source: markSubmissionQueueItemFailed · [FS-058:333](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L333) |
| FRM-014-E040 | `error?.code` | error?.message | Client source: removeSubmissionQueueItemsByInstructionTrnId · [FS-058:510](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L510) |
| FRM-014-E041 | `SERVER_CONFIRMED` | Server confirmed this queued TRN was saved successfully. | Client source: reconcileSubmissionQueueWithServerTrns · [FS-058:664](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L664) |

## Module-specific recovery and unresolved cases

Current generic lifecycle helper also contains older commissioning logic, but the dedicated callable is the relevant route. Verify the callable/trigger pair and result refresh in the chosen environment.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.

## Interpreted module recovery cases

These entries explain selected inspected checks; use the source register for the exact function/stage. Validation refusal does not erase earlier records or establish rollback of an earlier attempt.

| Code / outcome | Trigger and meaning | Specific remedy |
| --- | --- | --- |
| AST_NOT_FIELD | Dedicated commissioning requires the asset to be FIELD. | Verify the asset and its installation/state. Do not register a duplicate to bypass the guard. |
| INVALID_COMMISSIONING_METER_TYPE | The dedicated service accepts electricity or water. | Resolve the asset’s actual service with the responsible workstream. |
| Valid unsuccessful commissioning | Required no answers with notes can produce a valid record without a commissioning pass. | Arrange the outstanding work; verify FIELD remains. Do not report the meter connected from submission success alone. |
