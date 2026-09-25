# Change Password — Error Register

Module **FRM-004** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](change-password-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/change-password.md) · [Field catalogue](change-password-field-catalogue.md) · [Error register](change-password-error-register.md) · [Practical examples](../10-assessments/change-password-scenarios.md)

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

[Complete extracted register with trigger expressions (CSV)](change-password-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-004-E001 | `LOCAL_MESSAGE` | Please enter a new password. | Client source: validate · [FS-029:53](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/change-password.js#L53) |
| FRM-004-E002 | `LOCAL_MESSAGE` | Password must be at least 6 characters long. | Client source: validate · [FS-029:58](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/change-password.js#L58) |
| FRM-004-E003 | `LOCAL_MESSAGE` | Please confirm your new password. | Client source: validate · [FS-029:66](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/change-password.js#L66) |
| FRM-004-E004 | `LOCAL_MESSAGE` | New password and confirm password do not match. | Client source: validate · [FS-029:71](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/change-password.js#L71) |
| FRM-004-E005 | `LOCAL_MESSAGE` | Could not find the authenticated user. Please sign in again. | Client source: handleSave · [FS-029:88](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/change-password.js#L88) |
| FRM-004-E006 | `LOCAL_MESSAGE` | Password changed successfully. Next, select your active workbase. | Client source: handleSave · [FS-029:109](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/change-password.js#L109) |
| FRM-004-E007 | `LOCAL_MESSAGE` | message | Client source: handleSave · [FS-029:131](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/change-password.js#L131) |
| FRM-004-E008 | `String(error?.code &#124;&#124; "")` | String(error?.message &#124;&#124; fallbackMessage &#124;&#124; "").trim() &#124;&#124; fallbackMessage | Client source: plainAuthError · [FS-054:56](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/redux/authApi.js#L56) |

## Module-specific recovery and unresolved cases

The rule records no voluntary signed-in password-change route at present. The primary select-workbase screen still clears mustChangePassword: this conflicts with the rule that only an actual password change clears it. Flag for engineering review; Academy does not patch it.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.

## Documented authentication messages and remedies

The following tables preserve AU-R001’s wording and intended response. They are documented rules; apply the module’s branch/deployment qualifications before claiming that every message occurs in a particular build.

### Change password

| What happened | What the worker sees | What they do |
| --- | --- | --- |
| Shorter than 8 characters | **Password too short** — "Password must be at least 8 characters." | Use a longer one |
| The two passwords differ | **Passwords differ** — "The two passwords are not the same." | Retype them |
| The sign-in is too old for such a change | **Sign in again** — "For your safety, iREPS needs a fresh sign-in before you change your password." | Sign out, sign in, try again |
| The password changed, but iREPS could not record that it did | **Password changed, but not recorded** — "Your new password is in — use it from now on. iREPS could not record that you changed it, so it may ask you again." | Use the new password. Tell the manager if iREPS keeps asking |
| The phone has no connection | **No connection** — "Check your signal and try again." | Try again |
| Anything else | **Password not changed** — "Try again, and tell your manager if it keeps happening." | Try again, then report |
