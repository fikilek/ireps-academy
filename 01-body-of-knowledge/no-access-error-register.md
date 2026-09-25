# No Access — Error Register

Module **FRM-020** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](no-access-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/no-access-user-manual.md) · [Field catalogue](no-access-field-catalogue.md) · [Error register](no-access-error-register.md) · [Practical examples](../10-assessments/no-access-scenarios.md)

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

[Complete extracted register with trigger expressions (CSV)](no-access-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-020-E001 | `LOCAL_MESSAGE` | message | Client source: finish · [FS-011:61](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/targeted-batch-no-access.js#L61) |
| FRM-020-E002 | `LOCAL_MESSAGE` | result.message &#124;&#124; "This row is no longer executable." | Client source: submit · [FS-011:109](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/targeted-batch-no-access.js#L109) |
| FRM-020-E003 | `LOCAL_MESSAGE` | error?.message &#124;&#124; "No Access could not be submitted." | Client source: submit · [FS-011:120](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/targeted-batch-no-access.js#L120) |

## Module-specific recovery and unresolved cases

Reason lists and evidence rules must be checked per workflow. Row completion and reallocation after No Access are workflow-specific; a generic automatic revisit policy is not approved.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.

## Interpreted module recovery cases

These entries explain selected inspected checks; use the source register for the exact function/stage. Validation refusal does not erase earlier records or establish rollback of an earlier attempt.

| Code / outcome | Trigger and meaning | Specific remedy |
| --- | --- | --- |
| NO_ACCESS_REASON_REQUIRED | A No Access branch lacks its explanation. | Choose the actual reason and required Other text. |
| MISSING_NO_ACCESS_PHOTO | The inspected lifecycle branch requires a No Access evidence image. | Provide appropriate visit context where authorised; do not invent an inaccessible meter’s reading or identifier. |
