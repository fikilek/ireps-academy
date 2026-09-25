# Meter Disconnection — Error Register

Module **FRM-017** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](meter-disconnection-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/meter-disconnection-user-manual.md) · [Field catalogue](meter-disconnection-field-catalogue.md) · [Error register](meter-disconnection-error-register.md) · [Practical examples](../10-assessments/meter-disconnection-scenarios.md)

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

[Complete extracted register with trigger expressions (CSV)](meter-disconnection-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-017-E001 | `LOCAL_MESSAGE` | {<br>          path: "accessData.access.reasonSelect",<br>          message: "No-access reason is required",<br>        } | Client source:  · [FS-024:483](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/disconnection.jsx#L483) |
| FRM-017-E002 | `LOCAL_MESSAGE` | {<br>          path: "media",<br>          message: "No access photo is required",<br>        } | Client source:  · [FS-024:490](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/disconnection.jsx#L490) |
| FRM-017-E003 | `LOCAL_MESSAGE` | {<br>        path: "disconnection.level",<br>        message: "Disconnection level is required",<br>      } | Client source:  · [FS-024:500](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/disconnection.jsx#L500) |
| FRM-017-E004 | `LOCAL_MESSAGE` | {<br>        path: "media",<br>        message: "Disconnection level evidence required",<br>      } | Client source:  · [FS-024:508](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/disconnection.jsx#L508) |
| FRM-017-E005 | `LOCAL_MESSAGE` | Could not open this instruction media item. | Client source: openActiveMediaExternal · [FS-024:622](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/disconnection.jsx#L622) |
| FRM-017-E006 | `LOCAL_SAVE_ONLY` | Saved locally only. Not submitted. | Client source: saveDraftToQueue · [FS-024:1426](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/disconnection.jsx#L1426) |
| FRM-017-E007 | `LOCAL_MESSAGE` | Failed to save disconnection draft locally. | Client source: saveDraftToQueue · [FS-024:1452](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/disconnection.jsx#L1452) |
| FRM-017-E008 | `LOCAL_MESSAGE` | error?.message &#124;&#124; "Failed to save this DCN form locally." | Client source: handleSaveDisconnection · [FS-024:1487](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/disconnection.jsx#L1487) |
| FRM-017-E009 | `LOCAL_MESSAGE` | This DCN execution form must be opened from an accepted WMS instruction. | Client source: handleSubmitDisconnection · [FS-024:1662](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/disconnection.jsx#L1662) |
| FRM-017-E010 | `LOCAL_MESSAGE` | AST data not found. | Client source: handleSubmitDisconnection · [FS-024:1670](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/disconnection.jsx#L1670) |
| FRM-017-E011 | `LOCAL_MESSAGE` | Only CONNECTED meters can be disconnected. | Client source: handleSubmitDisconnection · [FS-024:1675](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/disconnection.jsx#L1675) |
| FRM-017-E012 | `LOCAL_MESSAGE` | You are offline. Press SAVE to keep this disconnection on the phone, then submit it when you are online. | Client source: handleSubmitDisconnection · [FS-024:1711](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/disconnection.jsx#L1711) |
| FRM-017-E013 | `LOCAL_MESSAGE` | error?.message &#124;&#124; "Meter disconnection submission failed." | Client source: handleSubmitDisconnection · [FS-024:1787](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/disconnection.jsx#L1787) |
| FRM-017-E014 | `LOCAL_MESSAGE` | result?.message &#124;&#124; "Meter disconnection submission failed." | Client source: handleSubmitDisconnection · [FS-024:1798](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/disconnection.jsx#L1798) |
| FRM-017-E015 | `LOCAL_MESSAGE` | error?.message &#124;&#124; "Submission failed" | Client source: handleSubmitDisconnection · [FS-024:1822](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/disconnection.jsx#L1822) |
| FRM-017-E016 | `LOCAL_MESSAGE` | This disconnection form has not been submitted. If you cancel now, the captured data will be lost unless you use SAVE. | Client source: confirmCancel · [FS-024:1840](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/disconnection.jsx#L1840) |
| FRM-017-E017 | `LOCAL_MESSAGE` | This will clear your changes and return the form to the state it had when it first loaded. | Client source: FormMeterDisconnection · [FS-024:2290](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/disconnection.jsx#L2290) |
| FRM-017-E018 | `LCT_TYPE_NOT_IMPLEMENTED` | `${trnType} is not implemented yet` | Server source: getActionCheck · [FS-076:385](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L385) |
| FRM-017-E019 | `UNAUTHENTICATED` | Authentication is required | Server source: onMeterLifecycleTrnCallable · [FS-076:400](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L400) |
| FRM-017-E020 | `dynamic code` | commonCheck.message | Server source: onMeterLifecycleTrnCallable · [FS-076:413](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L413) |
| FRM-017-E021 | `LCT_TYPE_NOT_IMPLEMENTED` | `${trnType} is not implemented yet` | Server source: onMeterLifecycleTrnCallable · [FS-076:445](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L445) |
| FRM-017-E022 | `INSPECTION_OFFICE_WMS_ONLY` | Meter inspection execution must complete an accepted office-originated instruction TRN | Server source: onMeterLifecycleTrnCallable · [FS-076:463](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L463) |
| FRM-017-E023 | `UNAUTHORIZED_FIELD_ORIGIN` | Only FWR or SPV actors can originate this lifecycle transaction from the field | Server source: onMeterLifecycleTrnCallable · [FS-076:486](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L486) |
| FRM-017-E024 | `dynamic code` | assignmentCheck.message | Server source: onMeterLifecycleTrnCallable · [FS-076:507](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L507) |
| FRM-017-E025 | `AST_NOT_FOUND` | The referenced AST does not exist | Server source: onMeterLifecycleTrnCallable · [FS-076:537](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L537) |
| FRM-017-E026 | `PREMISE_NOT_FOUND` | The referenced premise does not exist | Server source: onMeterLifecycleTrnCallable · [FS-076:551](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L551) |
| FRM-017-E027 | `dynamic code` | batchWorkCheck.message | Server source: onMeterLifecycleTrnCallable · [FS-076:591](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L591) |
| FRM-017-E028 | `INSTRUCTION_TRN_NOT_FOUND` | The lifecycle instruction TRN does not exist | Server source: onMeterLifecycleTrnCallable · [FS-076:612](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L612) |
| FRM-017-E029 | `INVALID_INSTRUCTION_TRN_TYPE` | The referenced instruction TRN type does not match the execution payload | Server source: onMeterLifecycleTrnCallable · [FS-076:630](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L630) |
| FRM-017-E030 | `INSTRUCTION_NOT_EXECUTABLE` | Rejected or cancelled lifecycle instructions cannot be executed | Server source: onMeterLifecycleTrnCallable · [FS-076:670](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L670) |
| FRM-017-E031 | `INSTRUCTION_NOT_ACCEPTED` | Lifecycle instruction must be accepted before execution can be submitted | Server source: onMeterLifecycleTrnCallable · [FS-076:685](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L685) |
| FRM-017-E032 | `dynamic code` | actionCheck?.message | Server source: onMeterLifecycleTrnCallable · [FS-076:708](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L708) |
| FRM-017-E033 | `dynamic code` | servicePatchResult.message | Server source: onMeterLifecycleTrnCallable · [FS-076:744](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L744) |
| FRM-017-E034 | `dynamic code` | actionCheck?.message | Server source: onMeterLifecycleTrnCallable · [FS-076:969](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L969) |
| FRM-017-E035 | `dynamic code` | servicePatchResult.message | Server source: onMeterLifecycleTrnCallable · [FS-076:1005](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L1005) |
| FRM-017-E036 | `UNKNOWN_ERROR` | Lifecycle TRN was not processed | Server source: onMeterLifecycleTrnCallable · [FS-076:1146](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L1146) |
| FRM-017-E037 | `dynamic code` | error?.message &#124;&#124; "Failed to submit lifecycle transaction" | Server source: onMeterLifecycleTrnCallable · [FS-076:1160](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L1160) |
| FRM-017-E038 | `INVALID_AST_STATE` | Only CONNECTED meters can be disconnected | Server source: validateMeterDisconnection · [FS-077:2766](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L2766) |
| FRM-017-E039 | `INVALID_METER_TYPE` | Only electricity or water meters can be disconnected | Server source: validateMeterDisconnection · [FS-077:2774](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L2774) |
| FRM-017-E040 | `DISCONNECTION_INSTRUCTION_REQUIRED` | Disconnection instruction is required | Server source: validateMeterDisconnection · [FS-077:2783](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L2783) |
| FRM-017-E041 | `NO_ACCESS_REASON_REQUIRED` | No-access reason is required | Server source: validateMeterDisconnection · [FS-077:2792](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L2792) |
| FRM-017-E042 | `MISSING_NO_ACCESS_PHOTO` | No access photo is required | Server source: validateMeterDisconnection · [FS-077:2804](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L2804) |
| FRM-017-E043 | `INVALID_DISCONNECTION_LEVEL` | Valid disconnection level is required | Server source: validateMeterDisconnection · [FS-077:2830](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L2830) |
| FRM-017-E044 | `MISSING_DISCONNECTION_LEVEL_EVIDENCE` | Disconnection level evidence media is required | Server source: validateMeterDisconnection · [FS-077:2848](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L2848) |
| FRM-017-E045 | `NAv` | NAv | Client source: addSubmissionQueueItem · [FS-058:87](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L87) |
| FRM-017-E046 | `result?.code &#124;&#124; "SUCCESS"` | result?.message &#124;&#124; "Synced successfully" | Client source: markSubmissionQueueItemSuccess · [FS-058:288](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L288) |
| FRM-017-E047 | `result?.code &#124;&#124; "SYNC_FAILED"` | result?.message &#124;&#124; "Sync failed. This draft remains pending for retry." | Client source: markSubmissionQueueItemFailed · [FS-058:319](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L319) |
| FRM-017-E048 | `result?.code &#124;&#124; "SYNC_FAILED"` | result?.message &#124;&#124;<br>          "Sync failed. This draft remains pending for retry." | Client source: markSubmissionQueueItemFailed · [FS-058:333](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L333) |
| FRM-017-E049 | `error?.code` | error?.message | Client source: removeSubmissionQueueItemsByInstructionTrnId · [FS-058:510](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L510) |
| FRM-017-E050 | `SERVER_CONFIRMED` | Server confirmed this queued TRN was saved successfully. | Client source: reconcileSubmissionQueueWithServerTrns · [FS-058:664](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L664) |

## Module-specific recovery and unresolved cases

The generic validator accepts water and electricity while its disconnection levels describe circuit-breaker actions. Water-specific teaching and product rules need resolution. Physical work instructions require the utility’s authorised procedure.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.

## Interpreted module recovery cases

These entries explain selected inspected checks; use the source register for the exact function/stage. Validation refusal does not erase earlier records or establish rollback of an earlier attempt.

| Code / outcome | Trigger and meaning | Specific remedy |
| --- | --- | --- |
| INVALID_AST_STATE | Usual eligible state is CONNECTED, with a specific finding-linked exception in this source. | Verify current state and origin. Do not apply the exception to unrelated work. |
| INVALID_DISCONNECTION_LEVEL | The selected level is not in the inspected server set. | Choose the actual supported outcome; escalate service-specific mismatch, especially water. |
| MISSING_DISCONNECTION_LEVEL_EVIDENCE | Successful work lacks required action evidence. | Attach the correct completed-work evidence. No Access is a different outcome. |
