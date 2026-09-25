# Premise Registration — Error Register

Module **FRM-010** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](premise-registration-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/premise-registration-user-manual.md) · [Field catalogue](premise-registration-field-catalogue.md) · [Error register](premise-registration-error-register.md) · [Practical examples](../10-assessments/premise-registration-scenarios.md)

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

[Complete extracted register with trigger expressions (CSV)](premise-registration-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-010-E001 | `NAv` | NAv | Client source: handleSubmit · [FS-048:1390](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/formPremise.js#L1390) |
| FRM-010-E002 | `NAv` | NAv | Client source: handleSubmit · [FS-048:1533](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/formPremise.js#L1533) |
| FRM-010-E003 | `invalid-argument` | premiseId is required | Server source: rebuildPremiseRegistryRowCallable · [FS-080:10](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/registry/premiseCallable.js#L10) |
| FRM-010-E004 | `internal` | error?.message &#124;&#124; "Failed to rebuild premise registry row" | Server source: rebuildPremiseRegistryRowCallable · [FS-080:27](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/registry/premiseCallable.js#L27) |
| FRM-010-E005 | `NAv` | NAv | Client source: addPremiseQueueItem · [FS-057:76](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/premiseSubmissionQueue.js#L76) |
| FRM-010-E006 | `result?.code &#124;&#124; "SUCCESS"` | result?.message &#124;&#124; "Synced" | Client source: markPremiseQueueItemSuccess · [FS-057:253](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/premiseSubmissionQueue.js#L253) |
| FRM-010-E007 | `result?.code &#124;&#124; "FAILED"` | result?.message &#124;&#124; "Sync failed. This draft remains pending for retry." | Client source: markPremiseQueueItemFailed · [FS-057:273](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/premiseSubmissionQueue.js#L273) |
| FRM-010-E008 | `result?.code &#124;&#124; "FAILED"` | result?.message &#124;&#124;<br>          "Sync failed. This draft remains pending for retry." | Client source: markPremiseQueueItemFailed · [FS-057:287](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/premiseSubmissionQueue.js#L287) |

## Module-specific recovery and unresolved cases

Current source uses a 10-second premise submit timeout, unlike the proposed universal 15-second policy. Some successful queued submissions remove the local queue item. Cross-batch picker labels can understate server locks; ambiguous multi-meter ERF fallback remains open.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.
