# Password Reset — Error Register

Module **FRM-003** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](password-reset-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/password-reset.md) · [Field catalogue](password-reset-field-catalogue.md) · [Error register](password-reset-error-register.md) · [Practical examples](../10-assessments/password-reset-scenarios.md)

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

[Complete extracted register with trigger expressions (CSV)](password-reset-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-003-E001 | `LOCAL_MESSAGE` | message | Client source: Signin · [FS-006:64](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(auth)/signin.jsx#L64) |
| FRM-003-E002 | `LOCAL_MESSAGE` | message | Client source: handleSignin · [FS-006:98](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(auth)/signin.jsx#L98) |
| FRM-003-E003 | `LOCAL_MESSAGE` | message | Client source: send · [FS-001:55](https://github.com/fikilek/ireps-mobile/blob/7bc9884325ff3db9bfe4493062f2450d8a7c83c0/app/(auth)/pwdReset.jsx#L55) |
| FRM-003-E004 | `LOCAL_MESSAGE` | message | Client source: send · [FS-001:61](https://github.com/fikilek/ireps-mobile/blob/7bc9884325ff3db9bfe4493062f2450d8a7c83c0/app/(auth)/pwdReset.jsx#L61) |
| FRM-003-E005 | `LOCAL_MESSAGE` | `We will send a password reset link to:\n\n${email}` | Client source: handleSend · [FS-001:71](https://github.com/fikilek/ireps-mobile/blob/7bc9884325ff3db9bfe4493062f2450d8a7c83c0/app/(auth)/pwdReset.jsx#L71) |
| FRM-003-E006 | `String(error?.code &#124;&#124; "")` | String(error?.message &#124;&#124; fallbackMessage &#124;&#124; "").trim() &#124;&#124; fallbackMessage | Client source: plainAuthError · [FS-054:56](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/redux/authApi.js#L56) |
| FRM-003-E007 | `String(error?.code &#124;&#124; "")` | String(error?.message &#124;&#124; fallbackMessage &#124;&#124; "").trim() &#124;&#124; fallbackMessage | Client source: plainAuthError · [FS-002:57](https://github.com/fikilek/ireps-mobile/blob/7bc9884325ff3db9bfe4493062f2450d8a7c83c0/src/redux/authApi.js#L57) |

## Module-specific recovery and unresolved cases

The hosted link expiry and provider error conditions require release testing. Never promise delivery time or expose whether another person has an account. The primary mobile tree links to /pwdReset but that screen is absent there; it exists in the mobile-auth worktree. The feature must be integrated and verified before the primary mobile guide can be treated as executable.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.

## Documented authentication messages and remedies

The following tables preserve AU-R001’s wording and intended response. They are documented rules; apply the module’s branch/deployment qualifications before claiming that every message occurs in a particular build.

### Password reset

| What happened | What the worker sees | What they do |
| --- | --- | --- |
| Sent, and the email has an account | **Reset link sent** — "If that email belongs to an iREPS account, a reset link is on its way. Check the inbox, and the junk folder." | Open the link |
| The email has no account | The same window, word for word | Nothing arrives; try another email |
| The email is not a real email address | **Check the email** — "That does not look like an email address." | Correct the email |
| Too many tries from this phone | **Too many tries** — "Wait a few minutes and try again." | Wait, then try again |
| The phone has no connection | **No connection** — "Check your signal and try again." | Try again |
| Anything else | **Could not send the reset link** — "Try again, and tell your manager if it keeps happening." | Try again, then report |
