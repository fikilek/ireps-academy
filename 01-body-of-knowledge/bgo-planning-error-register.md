# BGO Planning — Error Register

Module **FRM-031** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](bgo-planning-body-of-knowledge.md) · [User Manual](../02-user-manual/web/bgo-planning-user-manual.md) · [Field catalogue](bgo-planning-field-catalogue.md) · [Error register](bgo-planning-error-register.md) · [Practical examples](../10-assessments/bgo-planning-scenarios.md)

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

[Complete extracted register with trigger expressions (CSV)](bgo-planning-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-031-E001 | `error?.status &#124;&#124; error?.data?.code &#124;&#124; "BMD_BGO_CREATE_FAILED"` | error?.data?.message &#124;&#124;<br>            error?.message &#124;&#124;<br>            "Could not create MD BGO allocation." | Client source: handleConfirmCreateBgo · [FS-158:1015](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/BmdBgoPage.jsx#L1015) |
| FRM-031-E002 | `error?.status &#124;&#124; error?.data?.code &#124;&#124; "BMD_BGO_REMOVE_FAILED"` | error?.data?.message &#124;&#124;<br>          error?.message &#124;&#124;<br>          "Could not remove MD BGO allocation." | Client source: handleConfirmRemoveBmdBatch · [FS-158:1090](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/BmdBgoPage.jsx#L1090) |
| FRM-031-E003 | `error?.status &#124;&#124; error?.data?.code &#124;&#124; "BGO_CREATE_FAILED"` | error?.data?.message &#124;&#124; error?.message &#124;&#124; "Failed to create BGO." | Client source: handleConfirmCreateBgo · [FS-165:1372](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TcBgoPage.jsx#L1372) |
| FRM-031-E004 | `error?.status &#124;&#124; error?.data?.code &#124;&#124; "BGO_DELETE_FAILED"` | error?.data?.message &#124;&#124;<br>          error?.message &#124;&#124;<br>          "Failed to delete unaccepted BGO." | Client source: handleConfirmDeleteBgo · [FS-165:1422](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TcBgoPage.jsx#L1422) |

## Module-specific recovery and unresolved cases

This family needs route-by-route release review. Do not treat every historical BGO screen as a current recommended workflow.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.
