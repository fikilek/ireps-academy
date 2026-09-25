# Meter Vending — Error Register

Module **FRM-040** · Baseline **25 September 2026** · Application: **Planned; no implemented form found**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](meter-vending-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/meter-vending-user-manual.md) · [Field catalogue](meter-vending-field-catalogue.md) · [Error register](meter-vending-error-register.md) · [Practical examples](../10-assessments/meter-vending-scenarios.md)

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

[Complete extracted register with trigger expressions (CSV)](meter-vending-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-040-E001 | `LCT_TYPE_NOT_IMPLEMENTED` | `${trnType} is not implemented yet` | Server source: getActionCheck · [FS-076:385](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L385) |
| FRM-040-E002 | `UNAUTHENTICATED` | Authentication is required | Server source: onMeterLifecycleTrnCallable · [FS-076:400](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L400) |
| FRM-040-E003 | `dynamic code` | commonCheck.message | Server source: onMeterLifecycleTrnCallable · [FS-076:413](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L413) |
| FRM-040-E004 | `LCT_TYPE_NOT_IMPLEMENTED` | `${trnType} is not implemented yet` | Server source: onMeterLifecycleTrnCallable · [FS-076:445](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L445) |
| FRM-040-E005 | `INSPECTION_OFFICE_WMS_ONLY` | Meter inspection execution must complete an accepted office-originated instruction TRN | Server source: onMeterLifecycleTrnCallable · [FS-076:463](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L463) |
| FRM-040-E006 | `UNAUTHORIZED_FIELD_ORIGIN` | Only FWR or SPV actors can originate this lifecycle transaction from the field | Server source: onMeterLifecycleTrnCallable · [FS-076:486](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L486) |
| FRM-040-E007 | `dynamic code` | assignmentCheck.message | Server source: onMeterLifecycleTrnCallable · [FS-076:507](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L507) |
| FRM-040-E008 | `AST_NOT_FOUND` | The referenced AST does not exist | Server source: onMeterLifecycleTrnCallable · [FS-076:537](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L537) |
| FRM-040-E009 | `PREMISE_NOT_FOUND` | The referenced premise does not exist | Server source: onMeterLifecycleTrnCallable · [FS-076:551](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L551) |
| FRM-040-E010 | `dynamic code` | batchWorkCheck.message | Server source: onMeterLifecycleTrnCallable · [FS-076:591](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L591) |
| FRM-040-E011 | `INSTRUCTION_TRN_NOT_FOUND` | The lifecycle instruction TRN does not exist | Server source: onMeterLifecycleTrnCallable · [FS-076:612](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L612) |
| FRM-040-E012 | `INVALID_INSTRUCTION_TRN_TYPE` | The referenced instruction TRN type does not match the execution payload | Server source: onMeterLifecycleTrnCallable · [FS-076:630](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L630) |
| FRM-040-E013 | `INSTRUCTION_NOT_EXECUTABLE` | Rejected or cancelled lifecycle instructions cannot be executed | Server source: onMeterLifecycleTrnCallable · [FS-076:670](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L670) |
| FRM-040-E014 | `INSTRUCTION_NOT_ACCEPTED` | Lifecycle instruction must be accepted before execution can be submitted | Server source: onMeterLifecycleTrnCallable · [FS-076:685](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L685) |
| FRM-040-E015 | `dynamic code` | actionCheck?.message | Server source: onMeterLifecycleTrnCallable · [FS-076:708](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L708) |
| FRM-040-E016 | `dynamic code` | servicePatchResult.message | Server source: onMeterLifecycleTrnCallable · [FS-076:744](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L744) |
| FRM-040-E017 | `dynamic code` | actionCheck?.message | Server source: onMeterLifecycleTrnCallable · [FS-076:969](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L969) |
| FRM-040-E018 | `dynamic code` | servicePatchResult.message | Server source: onMeterLifecycleTrnCallable · [FS-076:1005](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L1005) |
| FRM-040-E019 | `UNKNOWN_ERROR` | Lifecycle TRN was not processed | Server source: onMeterLifecycleTrnCallable · [FS-076:1146](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L1146) |
| FRM-040-E020 | `dynamic code` | error?.message &#124;&#124; "Failed to submit lifecycle transaction" | Server source: onMeterLifecycleTrnCallable · [FS-076:1160](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L1160) |

## Module-specific recovery and unresolved cases

Agree state transitions, permissions, custody/financial audit, duplicate handling and evidence requirements. METER_VENDING is recognised by name but is excluded from the implemented generic lifecycle list; it returns LCT_TYPE_NOT_IMPLEMENTED there.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.
