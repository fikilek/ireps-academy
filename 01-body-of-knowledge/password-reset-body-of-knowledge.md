# Password Reset — Body of Knowledge

Module **FRM-003** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](password-reset-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/password-reset.md) · [Field catalogue](password-reset-field-catalogue.md) · [Error register](password-reset-error-register.md) · [Practical examples](../10-assessments/password-reset-scenarios.md)

## Meaning and purpose

Password Reset is the recovery route when a person cannot sign in with the existing password. It changes the credential through the emailed reset link.

The same acknowledgement is intended for registered and unregistered email addresses. A reset must not be taught as changing role, approval or workbase. Firebase-hosted recovery is distinct from an iREPS campaign or report-email facility.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

Account identity, organisation, authorisation and current work context are separate. A credential change must not be described as creating operational permission. Passwords and verification codes do not belong in submitted meter evidence.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. From Sign In choose Lost access? or the password-reset link on the applicable platform.
2. Enter the sign-in email and confirm the request.
3. Read the acknowledgement, then check the inbox and junk folder.
4. Open the reset link and set the new password.
5. Return to Sign In; use the new credential and complete any remaining onboarding gate.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Email | Destination associated with the sign-in account. | Valid email required; acknowledgement does not reveal account existence. |

The [field catalogue](password-reset-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](password-reset-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

A mistyped but syntactically valid address receives the same on-screen acknowledgement. The learner must understand that this is not proof that the address has an iREPS account.

## Exceptions, maturity and unresolved decisions

The hosted link expiry and provider error conditions require release testing. Never promise delivery time or expose whether another person has an account. The primary mobile tree links to /pwdReset but that screen is absent there; it exists in the mobile-auth worktree. The feature must be integrated and verified before the primary mobile guide can be treated as executable.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-156:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/PasswordResetPage.jsx#L1) | `ireps-web/src/pages/PasswordResetPage.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-006:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(auth)/signin.jsx#L1) | `ireps-mobile/app/(auth)/signin.jsx` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-001:1](https://github.com/fikilek/ireps-mobile/blob/7bc9884325ff3db9bfe4493062f2450d8a7c83c0/app/(auth)/pwdReset.jsx#L1) | `ireps-mobile-auth/app/(auth)/pwdReset.jsx` | feature/mobile-auth / `7bc9884325ff` | clean |
| [FS-054:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/redux/authApi.js#L1) | `ireps-mobile/src/redux/authApi.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-002:1](https://github.com/fikilek/ireps-mobile/blob/7bc9884325ff3db9bfe4493062f2450d8a7c83c0/src/redux/authApi.js#L1) | `ireps-mobile-auth/src/redux/authApi.js` | feature/mobile-auth / `7bc9884325ff` | clean |
| [FS-059:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/auth/auth-rules.md#L1) | `ireps-rules/auth/auth-rules.md` | main / `f5dc84e44c9f` | clean |
