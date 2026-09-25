# Lifecycle Instruction Creation — Error Register

Module **FRM-026** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](lifecycle-instructions-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/lifecycle-instructions-user-manual.md) · [Field catalogue](lifecycle-instructions-field-catalogue.md) · [Error register](lifecycle-instructions-error-register.md) · [Practical examples](../10-assessments/lifecycle-instructions-scenarios.md)

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

[Complete extracted register with trigger expressions (CSV)](lifecycle-instructions-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-026-E001 | `LOCAL_MESSAGE` | message &#124;&#124;<br>        "No network. Lifecycle instruction saved to offline forms queue." | Client source: saveLifecycleInstructionToQueue · [FS-013:616](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/trn-origin.js#L616) |
| FRM-026-E002 | `LOCAL_MESSAGE` | result?.message &#124;&#124; "Lifecycle instruction created successfully." | Client source: handleCreateInstruction · [FS-013:689](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/trn-origin.js#L689) |
| FRM-026-E003 | `LOCAL_MESSAGE` | error?.message &#124;&#124;<br>          error?.data?.message &#124;&#124;<br>          "Could not create lifecycle instruction." | Client source: handleCreateInstruction · [FS-013:721](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/trn-origin.js#L721) |
| FRM-026-E004 | `UNAUTHENTICATED` | Authentication is required | Server source: onCreateMeterLifecycleInstructionCallable · [FS-078:250](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/instructionCallable.js#L250) |
| FRM-026-E005 | `UNAUTHORIZED_LCT_ORIGINATOR` | Only MNG can create lifecycle instructions | Server source: onCreateMeterLifecycleInstructionCallable · [FS-078:266](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/instructionCallable.js#L266) |
| FRM-026-E006 | `dynamic code` | inputCheck.message | Server source: onCreateMeterLifecycleInstructionCallable · [FS-078:280](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/instructionCallable.js#L280) |
| FRM-026-E007 | `dynamic code` | assignmentCheck.message | Server source: onCreateMeterLifecycleInstructionCallable · [FS-078:300](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/instructionCallable.js#L300) |
| FRM-026-E008 | `INSTRUCTION_MEDIA_REQUIRED` | Instruction media is required when assignment.instruction.mediaRequired is true | Server source: onCreateMeterLifecycleInstructionCallable · [FS-078:323](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/instructionCallable.js#L323) |
| FRM-026-E009 | `TRN_ALREADY_EXISTS` | A TRN with this id already exists | Server source: onCreateMeterLifecycleInstructionCallable · [FS-078:355](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/instructionCallable.js#L355) |
| FRM-026-E010 | `AST_NOT_FOUND` | The referenced AST does not exist | Server source: onCreateMeterLifecycleInstructionCallable · [FS-078:369](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/instructionCallable.js#L369) |
| FRM-026-E011 | `PREMISE_NOT_FOUND` | The referenced premise does not exist | Server source: onCreateMeterLifecycleInstructionCallable · [FS-078:383](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/instructionCallable.js#L383) |
| FRM-026-E012 | `ACTIVE_LCT_ALREADY_EXISTS` | This meter already has an active lifecycle instruction of this type | Server source: onCreateMeterLifecycleInstructionCallable · [FS-078:401](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/instructionCallable.js#L401) |
| FRM-026-E013 | `dynamic code` | eligibilityCheck.message | Server source: onCreateMeterLifecycleInstructionCallable · [FS-078:425](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/instructionCallable.js#L425) |
| FRM-026-E014 | `UNKNOWN_ERROR` | Lifecycle instruction TRN was not created | Server source: onCreateMeterLifecycleInstructionCallable · [FS-078:521](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/instructionCallable.js#L521) |
| FRM-026-E015 | `UNKNOWN_ERROR` | error?.message &#124;&#124; "Failed to create lifecycle instruction" | Server source: onCreateMeterLifecycleInstructionCallable · [FS-078:532](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/instructionCallable.js#L532) |
| FRM-026-E016 | `INVALID_TRN_ID` | TRN id is required | Server source: validateCreateLifecycleInstructionInput · [FS-077:3029](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L3029) |
| FRM-026-E017 | `INVALID_OFFICE_LCT_TYPE` | Only INSPECTION, DISCONNECTION, RECONNECTION, REMOVAL and METER READING instructions can be created from Operations. | Server source: validateCreateLifecycleInstructionInput · [FS-077:3037](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L3037) |
| FRM-026-E018 | `INVALID_AST_ID` | astId is required | Server source: validateCreateLifecycleInstructionInput · [FS-077:3046](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L3046) |
| FRM-026-E019 | `INVALID_PREMISE_ID` | premiseId is required | Server source: validateCreateLifecycleInstructionInput · [FS-077:3054](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L3054) |
| FRM-026-E020 | `INVALID_AST_STATE` | DECOMMISSIONED meters cannot be issued for inspection | Server source: validateLifecycleInstructionEligibility · [FS-077:3082](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L3082) |
| FRM-026-E021 | `INVALID_AST_STATE` | Only CONNECTED meters can be issued for disconnection | Server source: validateLifecycleInstructionEligibility · [FS-077:3094](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L3094) |
| FRM-026-E022 | `INVALID_AST_STATE` | Only DISCONNECTED meters can be issued for reconnection | Server source: validateLifecycleInstructionEligibility · [FS-077:3106](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L3106) |
| FRM-026-E023 | `INVALID_AST_STATE` | This meter has already been removed | Server source: validateLifecycleInstructionEligibility · [FS-077:3118](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L3118) |
| FRM-026-E024 | `INVALID_AST_STATE` | DECOMMISSIONED meters cannot be issued for meter reading | Server source: validateLifecycleInstructionEligibility · [FS-077:3130](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L3130) |
| FRM-026-E025 | `PREPAID_MREAD_NOT_SUPPORTED` | MREAD Sprint 1 supports conventional meters only | Server source: validateLifecycleInstructionEligibility · [FS-077:3138](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L3138) |
| FRM-026-E026 | `INVALID_OFFICE_LCT_TYPE` | Unsupported lifecycle instruction type | Server source: validateLifecycleInstructionEligibility · [FS-077:3148](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L3148) |

## Module-specific recovery and unresolved cases

Role inheritance remains open. Field-origin exceptions have separate checks and do not make office acceptance optional for an office-issued instruction.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.
