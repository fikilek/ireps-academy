# Email Verification — Error Register

Module **FRM-006** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](email-verification-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/email-verification-user-manual.md) · [Field catalogue](email-verification-field-catalogue.md) · [Error register](email-verification-error-register.md) · [Practical examples](../10-assessments/email-verification-scenarios.md)

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

[Complete extracted register with trigger expressions (CSV)](email-verification-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-006-E001 | `LOCAL_MESSAGE` | Please check your email inbox. | Client source: handleResend · [FS-033:27](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/verify-email.js#L27) |
| FRM-006-E002 | `LOCAL_MESSAGE` | Unable to send verification email. | Client source: handleResend · [FS-033:32](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/verify-email.js#L32) |
| FRM-006-E003 | `LOCAL_MESSAGE` | Verification not confirmed yet. | Client source: handleAlreadyVerified · [FS-033:41](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/verify-email.js#L41) |
| FRM-006-E004 | `String(error?.code &#124;&#124; "")` | String(error?.message &#124;&#124; fallbackMessage &#124;&#124; "").trim() &#124;&#124; fallbackMessage | Client source: plainAuthError · [FS-054:56](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/redux/authApi.js#L56) |

## Module-specific recovery and unresolved cases

Routing and mutation connectivity require release verification. Do not merge this with Password Reset or Change Sign-in Email.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.
