# Lifecycle Instruction Control — Error Register

Module **FRM-027** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](instruction-control-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/instruction-control-user-manual.md) · [Field catalogue](instruction-control-field-catalogue.md) · [Error register](instruction-control-error-register.md) · [Practical examples](../10-assessments/instruction-control-scenarios.md)

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

[Complete extracted register with trigger expressions (CSV)](instruction-control-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-027-E001 | `LOCAL_MESSAGE` | Only ISSUED or REJECTED workorders can be reassigned. | Client source: handleReassign · [FS-008:642](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/dashboard/control.js#L642) |
| FRM-027-E002 | `LOCAL_MESSAGE` | `Cancel ${trnId}? This action should only be used before field acceptance or after rejection.` | Client source: handleCancel · [FS-008:655](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/dashboard/control.js#L655) |
| FRM-027-E003 | `LOCAL_MESSAGE` | result?.message &#124;&#124; "Lifecycle instruction cancelled." | Client source: handleCancel · [FS-008:671](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/dashboard/control.js#L671) |
| FRM-027-E004 | `error?.code` | error?.message | Client source: handleCancel · [FS-008:676](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/dashboard/control.js#L676) |
| FRM-027-E005 | `LOCAL_MESSAGE` | error?.data?.message &#124;&#124;<br>                  error?.message &#124;&#124;<br>                  "Could not cancel lifecycle instruction." | Client source: handleCancel · [FS-008:684](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/dashboard/control.js#L684) |
| FRM-027-E006 | `LOCAL_MESSAGE` | result?.message &#124;&#124; "Lifecycle instruction reassigned successfully." | Client source: handleSubmitReassign · [FS-008:708](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/dashboard/control.js#L708) |
| FRM-027-E007 | `error?.code` | error?.message | Client source: handleSubmitReassign · [FS-008:715](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/dashboard/control.js#L715) |
| FRM-027-E008 | `LOCAL_MESSAGE` | error?.data?.message &#124;&#124;<br>          error?.message &#124;&#124;<br>          "Could not reassign lifecycle instruction." | Client source: handleSubmitReassign · [FS-008:724](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/dashboard/control.js#L724) |
| FRM-027-E009 | `LOCAL_MESSAGE` | Select a USER, TEAM or SP target. | Client source: submit · [FS-008:1267](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/dashboard/control.js#L1267) |
| FRM-027-E010 | `LOCAL_MESSAGE` | Give a short reason for this reassignment. | Client source: submit · [FS-008:1274](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/dashboard/control.js#L1274) |
| FRM-027-E011 | `INVALID_ASSIGNMENT_TARGETS` | assignment.targets must contain at least one USER, TEAM, or SP target | Server source: validateNewTargets · [FS-079:216](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/manageInstructionCallable.js#L216) |
| FRM-027-E012 | `UNAUTHENTICATED` | Authentication is required | Server source: onManageLifecycleInstructionCallable · [FS-079:465](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/manageInstructionCallable.js#L465) |
| FRM-027-E013 | `UNAUTHORIZED_LCT_MANAGER` | Only MNG and SPV(MNC) can reassign or cancel lifecycle instructions | Server source: onManageLifecycleInstructionCallable · [FS-079:481](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/manageInstructionCallable.js#L481) |
| FRM-027-E014 | `INVALID_MANAGE_ACTION` | action must be REASSIGN or CANCEL | Server source: onManageLifecycleInstructionCallable · [FS-079:502](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/manageInstructionCallable.js#L502) |
| FRM-027-E015 | `INVALID_TRN_IDS` | At least one TRN id is required | Server source: onManageLifecycleInstructionCallable · [FS-079:509](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/manageInstructionCallable.js#L509) |
| FRM-027-E016 | `TOO_MANY_TRNS` | A maximum of 50 TRNs can be managed at once | Server source: onManageLifecycleInstructionCallable · [FS-079:516](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/manageInstructionCallable.js#L516) |
| FRM-027-E017 | `dynamic code` | targetsCheck.message | Server source: onManageLifecycleInstructionCallable · [FS-079:531](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/manageInstructionCallable.js#L531) |
| FRM-027-E018 | `CANCEL_REASON_REQUIRED` | Cancel reason is required when cancelling lifecycle instructions | Server source: onManageLifecycleInstructionCallable · [FS-079:538](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/manageInstructionCallable.js#L538) |
| FRM-027-E019 | `TRN_NOT_FOUND` | One or more TRNs were not found | Server source: onManageLifecycleInstructionCallable · [FS-079:566](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/manageInstructionCallable.js#L566) |
| FRM-027-E020 | `INVALID_MANAGED_LCT_TYPE` | Only INSPECTION, DISCONNECTION, RECONNECTION and REMOVAL instructions can be managed here | Server source: onManageLifecycleInstructionCallable · [FS-079:606](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/manageInstructionCallable.js#L606) |
| FRM-027-E021 | `INVALID_AST_ID` | TRN is missing ast.astData.astId | Server source: onManageLifecycleInstructionCallable · [FS-079:619](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/manageInstructionCallable.js#L619) |
| FRM-027-E022 | `AST_NOT_FOUND` | The referenced AST does not exist | Server source: onManageLifecycleInstructionCallable · [FS-079:634](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/manageInstructionCallable.js#L634) |
| FRM-027-E023 | `TRN_ALREADY_COMPLETED` | Completed lifecycle instructions cannot be reassigned or cancelled | Server source: onManageLifecycleInstructionCallable · [FS-079:648](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/manageInstructionCallable.js#L648) |
| FRM-027-E024 | `TRN_ALREADY_CANCELLED` | Cancelled lifecycle instructions cannot be changed | Server source: onManageLifecycleInstructionCallable · [FS-079:662](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/manageInstructionCallable.js#L662) |
| FRM-027-E025 | `TRN_IN_PROGRESS` | In-progress lifecycle instructions cannot be reassigned or cancelled | Server source: onManageLifecycleInstructionCallable · [FS-079:676](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/manageInstructionCallable.js#L676) |
| FRM-027-E026 | `INVALID_REASSIGN_STATE` | Only ISSUED or REJECTED lifecycle instructions can be reassigned | Server source: onManageLifecycleInstructionCallable · [FS-079:693](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/manageInstructionCallable.js#L693) |
| FRM-027-E027 | `INVALID_CANCEL_STATE` | Only ISSUED or REJECTED lifecycle instructions can be cancelled | Server source: onManageLifecycleInstructionCallable · [FS-079:710](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/manageInstructionCallable.js#L710) |
| FRM-027-E028 | `UNKNOWN_ERROR` | Lifecycle instruction management action was not processed | Server source: onManageLifecycleInstructionCallable · [FS-079:839](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/manageInstructionCallable.js#L839) |
| FRM-027-E029 | `UNKNOWN_ERROR` | error?.message &#124;&#124; "Failed to manage lifecycle instruction" | Server source: onManageLifecycleInstructionCallable · [FS-079:850](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/manageInstructionCallable.js#L850) |

## Module-specific recovery and unresolved cases

Confirm concurrency and the handling of an offline execution submitted after reassignment. Do not silently discard either party’s evidence.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.
