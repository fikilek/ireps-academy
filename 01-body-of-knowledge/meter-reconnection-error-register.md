# Meter Reconnection — Error Register

Module **FRM-018** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](meter-reconnection-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/meter-reconnection-user-manual.md) · [Field catalogue](meter-reconnection-field-catalogue.md) · [Error register](meter-reconnection-error-register.md) · [Practical examples](../10-assessments/meter-reconnection-scenarios.md)

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

[Complete extracted register with trigger expressions (CSV)](meter-reconnection-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-018-E001 | `LOCAL_MESSAGE` | {<br>          path: "accessData.access.reasonSelect",<br>          message: "No-access reason is required",<br>        } | Client source:  · [FS-027:441](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/reconnection.jsx#L441) |
| FRM-018-E002 | `LOCAL_MESSAGE` | {<br>          path: "media",<br>          message: "No access photo is required",<br>        } | Client source:  · [FS-027:448](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/reconnection.jsx#L448) |
| FRM-018-E003 | `LOCAL_MESSAGE` | {<br>        path: "media",<br>        message: "The photo showing the supply is back on is required",<br>      } | Client source:  · [FS-027:458](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/reconnection.jsx#L458) |
| FRM-018-E004 | `LOCAL_MESSAGE` | Could not open this instruction media item. | Client source: openActiveMediaExternal · [FS-027:571](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/reconnection.jsx#L571) |
| FRM-018-E005 | `LOCAL_SAVE_ONLY` | Saved locally only. Not submitted. | Client source: saveDraftToQueue · [FS-027:1300](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/reconnection.jsx#L1300) |
| FRM-018-E006 | `LOCAL_MESSAGE` | Failed to save reconnection draft locally. | Client source: saveDraftToQueue · [FS-027:1326](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/reconnection.jsx#L1326) |
| FRM-018-E007 | `LOCAL_MESSAGE` | error?.message &#124;&#124; "Failed to save this RCN form locally." | Client source: handleSaveReconnection · [FS-027:1361](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/reconnection.jsx#L1361) |
| FRM-018-E008 | `LOCAL_MESSAGE` | This RCN execution form must be opened from an accepted WMS instruction. | Client source: handleSubmitReconnection · [FS-027:1547](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/reconnection.jsx#L1547) |
| FRM-018-E009 | `LOCAL_MESSAGE` | AST data not found. | Client source: handleSubmitReconnection · [FS-027:1555](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/reconnection.jsx#L1555) |
| FRM-018-E010 | `LOCAL_MESSAGE` | Only DISCONNECTED meters can be reconnected. | Client source: handleSubmitReconnection · [FS-027:1560](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/reconnection.jsx#L1560) |
| FRM-018-E011 | `LOCAL_MESSAGE` | You are offline. Use SAVE to keep this RCN execution form locally, then submit when online. | Client source: handleSubmitReconnection · [FS-027:1576](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/reconnection.jsx#L1576) |
| FRM-018-E012 | `LOCAL_MESSAGE` | error?.message &#124;&#124; "Meter reconnection submission failed." | Client source: handleSubmitReconnection · [FS-027:1652](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/reconnection.jsx#L1652) |
| FRM-018-E013 | `LOCAL_MESSAGE` | result?.message &#124;&#124; "Meter reconnection submission failed." | Client source: handleSubmitReconnection · [FS-027:1663](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/reconnection.jsx#L1663) |
| FRM-018-E014 | `LOCAL_MESSAGE` | error?.message &#124;&#124; "Submission failed" | Client source: handleSubmitReconnection · [FS-027:1681](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/reconnection.jsx#L1681) |
| FRM-018-E015 | `LOCAL_MESSAGE` | This reconnection form has not been submitted. If you cancel now, the captured data will be lost unless you use SAVE. | Client source: confirmCancel · [FS-027:1699](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/reconnection.jsx#L1699) |
| FRM-018-E016 | `LOCAL_MESSAGE` | This will clear your changes and return the form to the state it had when it first loaded. | Client source: FormMeterReconnection · [FS-027:2132](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/reconnection.jsx#L2132) |
| FRM-018-E017 | `LCT_TYPE_NOT_IMPLEMENTED` | `${trnType} is not implemented yet` | Server source: getActionCheck · [FS-076:385](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L385) |
| FRM-018-E018 | `UNAUTHENTICATED` | Authentication is required | Server source: onMeterLifecycleTrnCallable · [FS-076:400](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L400) |
| FRM-018-E019 | `dynamic code` | commonCheck.message | Server source: onMeterLifecycleTrnCallable · [FS-076:413](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L413) |
| FRM-018-E020 | `LCT_TYPE_NOT_IMPLEMENTED` | `${trnType} is not implemented yet` | Server source: onMeterLifecycleTrnCallable · [FS-076:445](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L445) |
| FRM-018-E021 | `INSPECTION_OFFICE_WMS_ONLY` | Meter inspection execution must complete an accepted office-originated instruction TRN | Server source: onMeterLifecycleTrnCallable · [FS-076:463](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L463) |
| FRM-018-E022 | `UNAUTHORIZED_FIELD_ORIGIN` | Only FWR or SPV actors can originate this lifecycle transaction from the field | Server source: onMeterLifecycleTrnCallable · [FS-076:486](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L486) |
| FRM-018-E023 | `dynamic code` | assignmentCheck.message | Server source: onMeterLifecycleTrnCallable · [FS-076:507](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L507) |
| FRM-018-E024 | `AST_NOT_FOUND` | The referenced AST does not exist | Server source: onMeterLifecycleTrnCallable · [FS-076:537](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L537) |
| FRM-018-E025 | `PREMISE_NOT_FOUND` | The referenced premise does not exist | Server source: onMeterLifecycleTrnCallable · [FS-076:551](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L551) |
| FRM-018-E026 | `dynamic code` | batchWorkCheck.message | Server source: onMeterLifecycleTrnCallable · [FS-076:591](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L591) |
| FRM-018-E027 | `INSTRUCTION_TRN_NOT_FOUND` | The lifecycle instruction TRN does not exist | Server source: onMeterLifecycleTrnCallable · [FS-076:612](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L612) |
| FRM-018-E028 | `INVALID_INSTRUCTION_TRN_TYPE` | The referenced instruction TRN type does not match the execution payload | Server source: onMeterLifecycleTrnCallable · [FS-076:630](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L630) |
| FRM-018-E029 | `INSTRUCTION_NOT_EXECUTABLE` | Rejected or cancelled lifecycle instructions cannot be executed | Server source: onMeterLifecycleTrnCallable · [FS-076:670](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L670) |
| FRM-018-E030 | `INSTRUCTION_NOT_ACCEPTED` | Lifecycle instruction must be accepted before execution can be submitted | Server source: onMeterLifecycleTrnCallable · [FS-076:685](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L685) |
| FRM-018-E031 | `dynamic code` | actionCheck?.message | Server source: onMeterLifecycleTrnCallable · [FS-076:708](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L708) |
| FRM-018-E032 | `dynamic code` | servicePatchResult.message | Server source: onMeterLifecycleTrnCallable · [FS-076:744](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L744) |
| FRM-018-E033 | `dynamic code` | actionCheck?.message | Server source: onMeterLifecycleTrnCallable · [FS-076:969](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L969) |
| FRM-018-E034 | `dynamic code` | servicePatchResult.message | Server source: onMeterLifecycleTrnCallable · [FS-076:1005](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L1005) |
| FRM-018-E035 | `UNKNOWN_ERROR` | Lifecycle TRN was not processed | Server source: onMeterLifecycleTrnCallable · [FS-076:1146](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L1146) |
| FRM-018-E036 | `dynamic code` | error?.message &#124;&#124; "Failed to submit lifecycle transaction" | Server source: onMeterLifecycleTrnCallable · [FS-076:1160](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L1160) |
| FRM-018-E037 | `INVALID_AST_STATE` | Only DISCONNECTED meters can be reconnected | Server source: validateMeterReconnection · [FS-077:2896](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L2896) |
| FRM-018-E038 | `INVALID_METER_TYPE` | Only electricity or water meters can be reconnected | Server source: validateMeterReconnection · [FS-077:2904](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L2904) |
| FRM-018-E039 | `RECONNECTION_INSTRUCTION_REQUIRED` | Reconnection instruction is required | Server source: validateMeterReconnection · [FS-077:2915](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L2915) |
| FRM-018-E040 | `NO_ACCESS_REASON_REQUIRED` | No-access reason is required | Server source: validateMeterReconnection · [FS-077:2924](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L2924) |
| FRM-018-E041 | `MISSING_NO_ACCESS_PHOTO` | No access photo is required | Server source: validateMeterReconnection · [FS-077:2936](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L2936) |
| FRM-018-E042 | `INVALID_RECONNECTION_ANSWER` | Supply reconnected answer must be yes or no | Server source: validateMeterReconnection · [FS-077:2961](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L2961) |
| FRM-018-E043 | `SUPPLY_RECONNECTION_NOT_CONFIRMED` | Supply must be confirmed as reconnected before submit | Server source: validateMeterReconnection · [FS-077:2969](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L2969) |
| FRM-018-E044 | `MISSING_RECONNECTION_EVIDENCE` | Reconnection evidence media is required | Server source: validateMeterReconnection · [FS-077:2981](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L2981) |
| FRM-018-E045 | `NAv` | NAv | Client source: addSubmissionQueueItem · [FS-058:87](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L87) |
| FRM-018-E046 | `result?.code &#124;&#124; "SUCCESS"` | result?.message &#124;&#124; "Synced successfully" | Client source: markSubmissionQueueItemSuccess · [FS-058:288](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L288) |
| FRM-018-E047 | `result?.code &#124;&#124; "SYNC_FAILED"` | result?.message &#124;&#124; "Sync failed. This draft remains pending for retry." | Client source: markSubmissionQueueItemFailed · [FS-058:319](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L319) |
| FRM-018-E048 | `result?.code &#124;&#124; "SYNC_FAILED"` | result?.message &#124;&#124;<br>          "Sync failed. This draft remains pending for retry." | Client source: markSubmissionQueueItemFailed · [FS-058:333](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L333) |
| FRM-018-E049 | `error?.code` | error?.message | Client source: removeSubmissionQueueItemsByInstructionTrnId · [FS-058:510](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L510) |
| FRM-018-E050 | `SERVER_CONFIRMED` | Server confirmed this queued TRN was saved successfully. | Client source: reconcileSubmissionQueueWithServerTrns · [FS-058:664](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L664) |

## Module-specific recovery and unresolved cases

Do not infer debt clearance, safety clearance or authority solely from the form’s existence. Document the utility-approved prerequisite separately when agreed.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.

## Interpreted module recovery cases

These entries explain selected inspected checks; use the source register for the exact function/stage. Validation refusal does not erase earlier records or establish rollback of an earlier attempt.

| Code / outcome | Trigger and meaning | Specific remedy |
| --- | --- | --- |
| INVALID_AST_STATE | Successful reconnection requires a DISCONNECTED asset. | Check identity and current state; an installation needing commissioning is a different task. |
| SUPPLY_RECONNECTION_NOT_CONFIRMED | The successful-execution path requires explicit confirmation that supply was restored. | Do not confirm work that did not happen. Record the applicable failed-visit outcome or escalate. |
| MISSING_RECONNECTION_EVIDENCE | The required reconnection media is absent. | Provide the correct proof and verify upload before resubmission. |
