# Sign In — Error Register

Module **FRM-001** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](sign-in-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/signin.md) · [Field catalogue](sign-in-field-catalogue.md) · [Error register](sign-in-error-register.md) · [Practical examples](../10-assessments/sign-in-scenarios.md)

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

[Complete extracted register with trigger expressions (CSV)](sign-in-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-001-E001 | `LOCAL_MESSAGE` | message | Client source: Signin · [FS-006:64](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(auth)/signin.jsx#L64) |
| FRM-001-E002 | `LOCAL_MESSAGE` | message | Client source: handleSignin · [FS-006:98](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(auth)/signin.jsx#L98) |
| FRM-001-E003 | `String(error?.code &#124;&#124; "")` | String(error?.message &#124;&#124; fallbackMessage &#124;&#124; "").trim() &#124;&#124; fallbackMessage | Client source: plainAuthError · [FS-054:56](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/redux/authApi.js#L56) |

## Module-specific recovery and unresolved cases

Verify the actual post-login route on each release. A successful Firebase sign-in followed by a missing user record is a partial result. Do not describe it as an incorrect password.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.

## Documented authentication messages and remedies

The following tables preserve AU-R001’s wording and intended response. They are documented rules; apply the module’s branch/deployment qualifications before claiming that every message occurs in a particular build.

### Sign in

| What happened | What the worker sees | What they do |
| --- | --- | --- |
| Email or password is wrong, or there is no such account | **Sign in failed** — "Email or password is not right." | Try again, or use Lost access? |
| The email is not a real email address | **Check the email** — "That does not look like an email address." | Correct the email |
| The account has been stopped | **Account stopped** — "Speak to your manager." | Speak to their manager |
| Too many tries from this phone | **Too many tries** — "Wait a few minutes and try again." | Wait, then try again |
| The phone has no connection | **No connection** — "Check your signal and try again." | Move to signal, try again |
| Signed in, but the record did not arrive in 30 seconds | **Your details did not load** — "You are signed in, but they did not arrive. Check your signal and try again." | Try again |
| Anything else | **Sign in failed** — "Try again, and tell your manager if it keeps happening." | Try again, then report |
