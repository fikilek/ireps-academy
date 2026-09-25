# Change Sign-in Email — Error Register

Module **FRM-009** · Baseline **25 September 2026** · Application: **Feature-branch source; deployment unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](change-sign-in-email-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/change-sign-in-email.md) · [Field catalogue](change-sign-in-email-field-catalogue.md) · [Error register](change-sign-in-email-error-register.md) · [Practical examples](../10-assessments/change-sign-in-email-scenarios.md)

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

[Complete extracted register with trigger expressions (CSV)](change-sign-in-email-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-009-E001 | `LOCAL_MESSAGE` | Your details were not saved. Check your signal and try again. | Client source: handleSaveProfile · [FS-003:76](https://github.com/fikilek/ireps-mobile/blob/9a981d1882c388043bae6021a1dd33a3e758dfa8/app/(tabs)/admin/user/user-settings.js#L76) |
| FRM-009-E002 | `LOCAL_MESSAGE` | message | Client source: sendEmailLink · [FS-003:92](https://github.com/fikilek/ireps-mobile/blob/9a981d1882c388043bae6021a1dd33a3e758dfa8/app/(tabs)/admin/user/user-settings.js#L92) |
| FRM-009-E003 | `LOCAL_MESSAGE` | message | Client source: sendEmailLink · [FS-003:95](https://github.com/fikilek/ireps-mobile/blob/9a981d1882c388043bae6021a1dd33a3e758dfa8/app/(tabs)/admin/user/user-settings.js#L95) |
| FRM-009-E004 | `LOCAL_MESSAGE` | problem.message | Client source: handleChangeEmail · [FS-003:105](https://github.com/fikilek/ireps-mobile/blob/9a981d1882c388043bae6021a1dd33a3e758dfa8/app/(tabs)/admin/user/user-settings.js#L105) |
| FRM-009-E005 | `LOCAL_MESSAGE` | Type the password you sign in with. | Client source: handleChangeEmail · [FS-003:110](https://github.com/fikilek/ireps-mobile/blob/9a981d1882c388043bae6021a1dd33a3e758dfa8/app/(tabs)/admin/user/user-settings.js#L110) |
| FRM-009-E006 | `LOCAL_MESSAGE` | `From: ${signInEmail}\nTo: ${email}\n\nYour sign-in email changes only when you open the link in the new inbox.` | Client source: handleChangeEmail · [FS-003:114](https://github.com/fikilek/ireps-mobile/blob/9a981d1882c388043bae6021a1dd33a3e758dfa8/app/(tabs)/admin/user/user-settings.js#L114) |
| FRM-009-E007 | `String(error?.code &#124;&#124; "")` | String(error?.message &#124;&#124; fallbackMessage &#124;&#124; "").trim() &#124;&#124; fallbackMessage | Client source: plainAuthError · [FS-004:56](https://github.com/fikilek/ireps-mobile/blob/9a981d1882c388043bae6021a1dd33a3e758dfa8/src/redux/authApi.js#L56) |
| FRM-009-E008 | `auth/requires-recent-login` | Sign in again. | Client source:  · [FS-004:478](https://github.com/fikilek/ireps-mobile/blob/9a981d1882c388043bae6021a1dd33a3e758dfa8/src/redux/authApi.js#L478) |
| FRM-009-E009 | `invalid-argument` | `${label} must be one of ${VALID_USER_ROLES.join(", ")}.` | Server source: assertValidRole · [FS-064:58](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/functions/users/helpers.js#L58) |
| FRM-009-E010 | `permission-denied` | Only SPU, ADM or MNG may change user roles. | Server source: assertRoleManager · [FS-064:71](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/functions/users/helpers.js#L71) |
| FRM-009-E011 | `unauthenticated` | Authentication is required. | Server source: assertNotSelfRoleChange · [FS-064:85](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/functions/users/helpers.js#L85) |
| FRM-009-E012 | `invalid-argument` | Target user uid is required. | Server source: assertNotSelfRoleChange · [FS-064:89](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/functions/users/helpers.js#L89) |
| FRM-009-E013 | `permission-denied` | You cannot change your own role. | Server source: assertNotSelfRoleChange · [FS-064:93](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/functions/users/helpers.js#L93) |
| FRM-009-E014 | `permission-denied` | You cannot change a user at your role level or above. | Server source: assertRoleHierarchy · [FS-064:122](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/functions/users/helpers.js#L122) |
| FRM-009-E015 | `permission-denied` | You cannot assign a role at your role level or above. | Server source: assertRoleHierarchy · [FS-064:129](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/functions/users/helpers.js#L129) |
| FRM-009-E016 | `failed-precondition` | `User already has role ${normalizedPreviousRole}.` | Server source: assertRoleActuallyChanges · [FS-064:147](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/functions/users/helpers.js#L147) |
| FRM-009-E017 | `not-found` | `${label} user was not found.` | Server source: getUserSnapshotOrThrow · [FS-066:23](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/functions/users/updateUserCallable.js#L23) |
| FRM-009-E018 | `failed-precondition` | User is currently assigned to an operational team. Remove the user from the team before assigning this role. | Server source: assertTargetMayLeaveOperationalRole · [FS-066:39](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/functions/users/updateUserCallable.js#L39) |
| FRM-009-E019 | `internal` | Could not update the user role. | Server source: toCallableError · [FS-066:49](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/functions/users/updateUserCallable.js#L49) |
| FRM-009-E020 | `unauthenticated` | Authentication is required. | Server source: updateUserCallable · [FS-066:59](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/functions/users/updateUserCallable.js#L59) |
| FRM-009-E021 | `invalid-argument` | Target user uid is required. | Server source: updateUserCallable · [FS-066:66](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/functions/users/updateUserCallable.js#L66) |
| FRM-009-E022 | `failed-precondition` | Target user does not have a matching Firebase Auth account. | Server source: updateUserCallable · [FS-066:101](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/functions/users/updateUserCallable.js#L101) |
| FRM-009-E023 | `internal` | Role update failed and Firebase Auth rollback also failed. Administrator investigation is required. | Server source: updateUserCallable · [FS-066:147](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/functions/users/updateUserCallable.js#L147) |

## Module-specific recovery and unresolved cases

Verify deployment of email branches, permitted actor/target combinations and audit reconciliation. AU-R001 gives specific email-change permissions; it does not settle permission inheritance elsewhere.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.

## Documented authentication messages and remedies

The following tables preserve AU-R001’s wording and intended response. They are documented rules; apply the module’s branch/deployment qualifications before claiming that every message occurs in a particular build.

### Change my sign-in email (section 11.1)

| What happened | What the worker sees | What they do |
| --- | --- | --- |
| The link was sent | **Check your new inbox** — "We sent a link to the new email. Your sign-in email changes when you open it. Until then, keep signing in with the old one. Once it changes you will be signed out: sign in with the new email and the same password." | Open the link from the new inbox |
| The password they typed is wrong | **Password not right** — "Type the password you sign in with." | Type it again |
| The new email is the one they already have | **Nothing to change** — "That is already your sign-in email." | Nothing |
| The email is not a real email address | **Check the email** — "That does not look like an email address." | Correct it |
| Another account already uses it | **Email already used** — "Another iREPS account uses that email. Choose another." Where Firebase keeps that private, the **Check your new inbox** window instead, and no link ever arrives | Choose another |
| The sign-in is too old for such a change | **Sign in again** — "For your safety, iREPS needs a fresh sign-in before you change your email." | Sign out, sign in, try again |
| Too many tries from this phone | **Too many tries** — "Wait a few minutes and try again." | Wait, then try again |
| The phone has no connection | **No connection** — "Check your signal and try again." | Try again |
| Anything else | **Email not changed** — "Try again, and tell your manager if it keeps happening." | Try again, then report |

### Change someone's sign-in email (section 11.2)

| What happened | What the office sees | What they do |
| --- | --- | --- |
| It changed | **Email changed** — "They now sign in as NEW instead of OLD, with the same password as before. If iREPS is open on their phone they are signed out, and sign in again with the new email." | Tell the person |
| The new email is the one they already have | **Nothing to change** — "That is already their sign-in email." | Nothing |
| The email is not a real email address | **Check the email** — "That does not look like an email address." | Correct it |
| Another account already uses it | **Email already used** — "Another iREPS account uses that email." | Check who has it |
| The person is not one they may change | **Not yours to change** — "You may only change the email of people you manage." | Ask an admin |
| It is their own account | **Use Account Settings** — "Change your own email from Account Settings." | Use Account Settings |
| The phone has no connection | **No connection** — "Check your signal and try again." | Try again |
| Anything else | **Email not changed** — the reason the back end gave; if there is none, "Try again, and tell your manager if it keeps happening." | Try again, then report |
