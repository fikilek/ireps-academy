# Phone Verification — Error Register

Module **FRM-007** · Baseline **25 September 2026** · Application: **Partial source foundation; service and release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](phone-verification-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/phone-verification-user-manual.md) · [Field catalogue](phone-verification-field-catalogue.md) · [Error register](phone-verification-error-register.md) · [Practical examples](../10-assessments/phone-verification-scenarios.md)

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

[Complete extracted register with trigger expressions (CSV)](phone-verification-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-007-E001 | `LOCAL_MESSAGE` | Please try again. | Client source: handleVerify · [FS-034:38](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/verify-phone.js#L38) |
| FRM-007-E002 | `LOCAL_MESSAGE` | Unable to resend code. | Client source: handleResend · [FS-034:50](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/verify-phone.js#L50) |
| FRM-007-E003 | `String(error?.code &#124;&#124; "")` | String(error?.message &#124;&#124; fallbackMessage &#124;&#124; "").trim() &#124;&#124; fallbackMessage | Client source: plainAuthError · [FS-054:56](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/redux/authApi.js#L56) |

## Module-specific recovery and unresolved cases

VerifyPhone and resendPhoneCode endpoints are not established by the optional-hook syntax. Delivery, expiry, attempt limits and routing remain acceptance gaps. The primary API exposes sendPhoneOtp and confirmPhoneOtp instead of the verifyPhone/resendPhoneCode names used by this screen.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.
