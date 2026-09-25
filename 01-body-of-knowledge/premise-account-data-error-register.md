# Premise Account Data — Error Register

Module **FRM-011** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](premise-account-data-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/premise-account-data-user-manual.md) · [Field catalogue](premise-account-data-field-catalogue.md) · [Error register](premise-account-data-error-register.md) · [Practical examples](../10-assessments/premise-account-data-scenarios.md)

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

[Complete extracted register with trigger expressions (CSV)](premise-account-data-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-011-E001 | `LOCAL_MESSAGE` | Premise id is required to save this draft. | Client source: handleSaveDraft · [FS-047:800](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L800) |
| FRM-011-E002 | `LOCAL_MESSAGE` | The form is still empty. Capture account data before saving a local draft. | Client source: handleSaveDraft · [FS-047:805](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L805) |
| FRM-011-E003 | `LOCAL_MESSAGE` | Capture at least one municipal account number before saving a local draft. | Client source: handleSaveDraft · [FS-047:813](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L813) |
| FRM-011-E004 | `LOCAL_MESSAGE` | result?.message &#124;&#124; "Account data draft saved locally." | Client source: handleSaveDraft · [FS-047:833](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L833) |
| FRM-011-E005 | `LOCAL_MESSAGE` | result?.message &#124;&#124; "Failed to save account data draft." | Client source: handleSaveDraft · [FS-047:846](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L846) |
| FRM-011-E006 | `LOCAL_MESSAGE` | This will clear the current edit form and open a clean account capture form. | Client source: handleAddAccountFromHeader · [FS-047:861](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L861) |
| FRM-011-E007 | `LOCAL_MESSAGE` | This will clear all captured account data, media, draft values, and edit mode for this premise. | Client source: handleResetAccountDataForm · [FS-047:917](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L917) |
| FRM-011-E008 | `LOCAL_MESSAGE` | No existing owner data is available for this premise yet. | Client source: handleUseExistingOwner · [FS-047:941](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L941) |
| FRM-011-E009 | `LOCAL_MESSAGE` | This will copy the existing owner details into the owner fields. You can still edit the fields after copying. | Client source: handleUseExistingOwner · [FS-047:948](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L948) |
| FRM-011-E010 | `LOCAL_MESSAGE` | result?.message &#124;&#124; "Failed to save account data to local queue." | Client source: saveSubmissionToLocalQueue · [FS-047:988](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L988) |
| FRM-011-E011 | `LOCAL_MESSAGE` | Premise id is required to submit this form. | Client source: handleSubmitAccountData · [FS-047:998](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L998) |
| FRM-011-E012 | `LOCAL_MESSAGE` | This premise is not available in the current synced ward. Please sync or select the correct ward and try again. | Client source: handleSubmitAccountData · [FS-047:1004](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L1004) |
| FRM-011-E013 | `LOCAL_MESSAGE` | result?.message &#124;&#124;<br>            "The backend did not accept this account data. Please correct the form and try again." | Client source: handleSubmitAccountData · [FS-047:1052](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L1052) |
| FRM-011-E014 | `error?.code` | error?.message | Client source: handleSubmitAccountData · [FS-047:1070](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L1070) |
| FRM-011-E015 | `LOCAL_MESSAGE` | error?.message &#124;&#124;<br>          "Account data could not be submitted. Please review the form and try again." | Client source: handleSubmitAccountData · [FS-047:1088](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L1088) |
| FRM-011-E016 | `LOCAL_MESSAGE` | Owner details will populate the occupant fields. You can still edit the occupant fields after copying. | Client source: copyOwnerToOccupant · [FS-047:1122](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L1122) |
| FRM-011-E017 | `unauthenticated` | Authentication required | Server source: onCreateAccountDataCallable · [FS-072:36](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/dataCleansing/callables.js#L36) |
| FRM-011-E018 | `dynamic code` | validation.message | Server source: onCreateAccountDataCallable · [FS-072:47](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/dataCleansing/callables.js#L47) |
| FRM-011-E019 | `PREMISE_NOT_FOUND` | Parent premise does not exist in premises collection | Server source: onCreateAccountDataCallable · [FS-072:66](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/dataCleansing/callables.js#L66) |
| FRM-011-E020 | `UNKNOWN_ERROR` | error?.message &#124;&#124; "Failed to create account data record" | Server source: onCreateAccountDataCallable · [FS-072:124](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/dataCleansing/callables.js#L124) |
| FRM-011-E021 | `NAv` | NAv | Client source: addAccountDataQueueItem · [FS-056:184](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/accountDataSubmissionQueue.js#L184) |
| FRM-011-E022 | `SYNCING` | Syncing account data with backend. | Client source: markAccountDataQueueItemSyncing · [FS-056:295](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/accountDataSubmissionQueue.js#L295) |
| FRM-011-E023 | `result?.code &#124;&#124; "SUCCESS"` | result?.message &#124;&#124; "Account data synced successfully." | Client source: markAccountDataQueueItemSuccess · [FS-056:327](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/accountDataSubmissionQueue.js#L327) |
| FRM-011-E024 | `result?.code &#124;&#124; "SYNC_FAILED"` | result?.message &#124;&#124; "Account data sync failed." | Client source: markAccountDataQueueItemFailed · [FS-056:357](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/accountDataSubmissionQueue.js#L357) |

## Module-specific recovery and unresolved cases

Blank-to-NAv transformations exist in source. Unknown, not applicable and unavailable need precise interpretation rather than guessed values. A network-unavailable submit can enter a separate account-data queue.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.
