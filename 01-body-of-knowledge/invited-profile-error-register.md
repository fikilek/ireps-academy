# Invited Profile and Admin Confirmation — Error Register

Module **FRM-005** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](invited-profile-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/invited-profile-user-manual.md) · [Field catalogue](invited-profile-field-catalogue.md) · [Error register](invited-profile-error-register.md) · [Practical examples](../10-assessments/invited-profile-scenarios.md)

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

[Complete extracted register with trigger expressions (CSV)](invited-profile-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-005-E001 | `LOCAL_MESSAGE` | Passwords must match. | Client source: handleFinalize · [FS-030:45](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/complete-invited-profile.js#L45) |
| FRM-005-E002 | `LOCAL_MESSAGE` | Password must be at least 6 characters. | Client source: handleFinalize · [FS-030:48](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/complete-invited-profile.js#L48) |
| FRM-005-E003 | `LOCAL_MESSAGE` | Please select your active workbase. | Client source: handleFinalize · [FS-030:54](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/complete-invited-profile.js#L54) |
| FRM-005-E004 | `LOCAL_MESSAGE` | Security rotated and jurisdiction locked. | Client source: handleFinalize · [FS-030:85](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/complete-invited-profile.js#L85) |
| FRM-005-E005 | `LOCAL_MESSAGE` | Session expired. Please sign out and in again. | Client source: handleFinalize · [FS-030:90](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/complete-invited-profile.js#L90) |
| FRM-005-E006 | `LOCAL_MESSAGE` | err.message &#124;&#124; "Could not finalize." | Client source: handleFinalize · [FS-030:95](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/complete-invited-profile.js#L95) |
| FRM-005-E007 | `LOCAL_MESSAGE` | Passwords must match. | Client source: handleFinalize · [FS-031:46](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/confirm-admin.js#L46) |
| FRM-005-E008 | `LOCAL_MESSAGE` | Security protocol requires 6+ characters. | Client source: handleFinalize · [FS-031:49](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/confirm-admin.js#L49) |
| FRM-005-E009 | `LOCAL_MESSAGE` | Select your initial operational context. | Client source: handleFinalize · [FS-031:55](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/confirm-admin.js#L55) |
| FRM-005-E010 | `LOCAL_MESSAGE` | Administrator credentials locked and loaded. | Client source: handleFinalize · [FS-031:88](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/confirm-admin.js#L88) |
| FRM-005-E011 | `LOCAL_MESSAGE` | err.message &#124;&#124; "Could not finalize ADM profile." | Client source: handleFinalize · [FS-031:95](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/confirm-admin.js#L95) |
| FRM-005-E012 | `String(error?.code &#124;&#124; "")` | String(error?.message &#124;&#124; fallbackMessage &#124;&#124; "").trim() &#124;&#124; fallbackMessage | Client source: plainAuthError · [FS-054:56](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/redux/authApi.js#L56) |

## Module-specific recovery and unresolved cases

Legacy screen validation/routing may differ from the current mandatory-password design. Invitation delivery and account-change sequencing must be tested without exposing real credentials.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.
