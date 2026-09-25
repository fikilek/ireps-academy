# Sign Up — Body of Knowledge

Module **FRM-002** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](sign-up-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/signup.md) · [Field catalogue](sign-up-field-catalogue.md) · [Error register](sign-up-error-register.md) · [Practical examples](../10-assessments/sign-up-scenarios.md)

## Meaning and purpose

Sign Up creates a fieldworker account associated with a selected service provider. Owner terminology excludes Guest from the active roles.

The current documented journey is mobile signup followed by approval. The web sign-in interface does not establish a web self-registration journey. Utility/main-contractor/subcontractor governance and permission inheritance remain separate decisions.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

Account identity, organisation, authorisation and current work context are separate. A credential change must not be described as creating operational permission. Passwords and verification codes do not belong in submitted meter evidence.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Open Sign Up on mobile.
2. Enter your surname, name, email, password and matching confirmation.
3. Load and select the correct active service provider; do not choose a different employer just to bypass a failure.
4. Review the email and service provider in the confirmation.
5. Submit once, retain the result, then use Sign In and await the responsible manager’s authorisation.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Surname | Person’s surname. | Required by signup rule. |
| Name | Person’s given name. | Required by signup rule. |
| Email | Unique sign-in identity. | Valid email; server uniqueness check; existing account uses Sign In or reset. |
| Password | Person’s chosen password. | At least 8 characters in the current rule; no mandatory composition beyond that rule. |
| Confirm Password | Typing cross-check, not a second credential. | Must match the password. |
| Service Provider | Employer/provider association selected from active providers. | Server rechecks active status and responsible manager; list loading may fail. |

The [field catalogue](sign-up-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](sign-up-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

Lebo chooses the correct provider, submits and receives a pending outcome. A manager must authorise the fieldworker; registration is not permission to start Meter Discovery.

## Exceptions, maturity and unresolved decisions

Confirm backend/UI parity on the target release and whether account creation succeeded before retrying a network failure. Do not promise an invitation email for self-signup.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-007:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(auth)/signup.jsx#L1) | `ireps-mobile/app/(auth)/signup.jsx` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-088:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L1) | `ireps-web/functions/index.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-054:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/redux/authApi.js#L1) | `ireps-mobile/src/redux/authApi.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-040:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/auth/authMessages.js#L1) | `ireps-mobile/src/features/auth/authMessages.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-059:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/auth/auth-rules.md#L1) | `ireps-rules/auth/auth-rules.md` | main / `f5dc84e44c9f` | clean |
