# Sign Up — Error Register

Module **FRM-002** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](sign-up-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/signup.md) · [Field catalogue](sign-up-field-catalogue.md) · [Error register](sign-up-error-register.md) · [Practical examples](../10-assessments/sign-up-scenarios.md)

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

[Complete extracted register with trigger expressions (CSV)](sign-up-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-002-E001 | `LOCAL_MESSAGE` | Awaiting Manager authorization. | Client source: handleSignup · [FS-007:84](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(auth)/signup.jsx#L84) |
| FRM-002-E002 | `LOCAL_MESSAGE` | Please try again. | Client source: handleSignup · [FS-007:100](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(auth)/signup.jsx#L100) |
| FRM-002-E003 | `LOCAL_MESSAGE` | Unexpected error occurred. | Client source: handleSignup · [FS-007:104](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(auth)/signup.jsx#L104) |
| FRM-002-E004 | `invalid-argument` | Email, password, name, surname and service provider are required. | Server source: signupFieldWorker · [FS-088:3064](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L3064) |
| FRM-002-E005 | `invalid-argument` | Password must be at least 8 characters. | Server source: signupFieldWorker · [FS-088:3078](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L3078) |
| FRM-002-E006 | `not-found` | Selected service provider was not found. | Server source: signupFieldWorker · [FS-088:3098](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L3098) |
| FRM-002-E007 | `failed-precondition` | Selected service provider is not active. | Server source: signupFieldWorker · [FS-088:3109](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L3109) |
| FRM-002-E008 | `failed-precondition` | No responsible manager was found for the selected service provider. | Server source: signupFieldWorker · [FS-088:3145](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L3145) |
| FRM-002-E009 | `already-exists` | A user with this email already exists. | Server source: signupFieldWorker · [FS-088:3154](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L3154) |
| FRM-002-E010 | `internal` | err.message | Server source: signupFieldWorker · [FS-088:3161](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L3161) |
| FRM-002-E011 | `internal` | error.message &#124;&#124; "Could not complete field worker signup." | Server source: signupFieldWorker · [FS-088:3256](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L3256) |
| FRM-002-E012 | `String(error?.code &#124;&#124; "")` | String(error?.message &#124;&#124; fallbackMessage &#124;&#124; "").trim() &#124;&#124; fallbackMessage | Client source: plainAuthError · [FS-054:56](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/redux/authApi.js#L56) |

## Module-specific recovery and unresolved cases

Confirm backend/UI parity on the target release and whether account creation succeeded before retrying a network failure. Do not promise an invitation email for self-signup.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.

## Documented authentication messages and remedies

The following tables preserve AU-R001’s wording and intended response. They are documented rules; apply the module’s branch/deployment qualifications before claiming that every message occurs in a particular build.

### Sign up

| What happened | What the worker sees | What they do |
| --- | --- | --- |
| The service provider list could not be loaded | **Could not load the service providers** — "Check your signal and try again." | Try again |
| An account already uses that email | **Email already used** — "Sign in instead, or use Lost access?" | Sign in or reset |
| The service provider is no longer active | **Service provider not active** — "Choose another, or ask your manager." | Choose another |
| No manager is responsible for that service provider | **No manager for that service provider** — "Ask your manager to sort this out before you sign up." | Ask their manager |
| A field is missing or the password is too short | **Check the form** — the message names the field, for example "Password must be at least 8 characters." | Fix the field |
| The phone has no connection | **No connection** — "Check your signal and try again." | Try again |
| Anything else | **Sign up failed** — the reason the back end gave; if there is none, "Try again, and tell your manager if it keeps happening." | Try again, then report |
