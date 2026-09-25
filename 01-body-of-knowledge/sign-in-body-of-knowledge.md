# Sign In — Body of Knowledge

Module **FRM-001** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](sign-in-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/signin.md) · [Field catalogue](sign-in-field-catalogue.md) · [Error register](sign-in-error-register.md) · [Practical examples](../10-assessments/sign-in-scenarios.md)

## Meaning and purpose

Sign In establishes the person’s authenticated identity. It does not by itself authorise fieldwork, select a workbase or accept an instruction.

Mobile and web share the account, but routing depends on the account record. A person may need a password change, manager authorisation or workbase selection before reaching operational screens. Sign In is not meter registration.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

Account identity, organisation, authorisation and current work context are separate. A credential change must not be described as creating operational permission. Passwords and verification codes do not belong in submitted meter evidence.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Open Sign In in the intended environment.
2. Enter the account email and password; check the email before submitting.
3. Wait for the authentication result and for the iREPS user record to load.
4. Follow the route offered: password change, pending approval, workbase selection or work.
5. Check your displayed identity and active workbase before capturing any operational information.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Email | Account identifier; use the sign-in email, not a separately edited contact address. | Required; valid email syntax; rule normalises whitespace/case. |
| Password | Authenticates the account; never include in a training screenshot or support report. | Required; entered by the person. Eight-character creation rule is not an instruction to alter an existing password. |

The [field catalogue](sign-in-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](sign-in-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

A newly registered fieldworker can authenticate but still sees pending approval. The correct next action is manager authorisation, not creating a second account.

## Exceptions, maturity and unresolved decisions

Verify the actual post-login route on each release. A successful Firebase sign-in followed by a missing user record is a partial result. Do not describe it as an incorrect password.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-006:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(auth)/signin.jsx#L1) | `ireps-mobile/app/(auth)/signin.jsx` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-155:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/LoginPage.jsx#L1) | `ireps-web/src/pages/LoginPage.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-054:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/redux/authApi.js#L1) | `ireps-mobile/src/redux/authApi.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-040:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/auth/authMessages.js#L1) | `ireps-mobile/src/features/auth/authMessages.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-059:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/auth/auth-rules.md#L1) | `ireps-rules/auth/auth-rules.md` | main / `f5dc84e44c9f` | clean |
