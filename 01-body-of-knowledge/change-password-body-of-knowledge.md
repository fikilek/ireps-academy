# Change Password — Body of Knowledge

Module **FRM-004** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](change-password-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/change-password.md) · [Field catalogue](change-password-field-catalogue.md) · [Error register](change-password-error-register.md) · [Practical examples](../10-assessments/change-password-scenarios.md)

## Meaning and purpose

Change Password replaces a credential while a person has an authenticated session. The mandatory onboarding gate requires a successful password change before access continues.

A credential update and clearing the iREPS must-change flag are separate writes. If the first succeeds and the second fails, the new password is already effective. Do not tell the person to keep using the old password.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

Account identity, organisation, authorisation and current work context are separate. A credential change must not be described as creating operational permission. Passwords and verification codes do not belong in submitted meter evidence.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Sign in and follow the mandatory Change Password route when shown.
2. Enter a new password and matching confirmation.
3. Confirm and wait for the result.
4. If the password changed but recording failed, use the new password and report the incomplete onboarding acknowledgement.
5. Verify that the required gate clears and the expected next onboarding step appears.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| New password | Replacement credential. | At least 8 characters under AU-R001; current session may need fresh sign-in. |
| Confirm password | Typing check. | Must equal the new password. |

The [field catalogue](change-password-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](change-password-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

The network fails after Firebase changes the credential. The result states that the change was not recorded in iREPS. The person signs in using the new password; the manager investigates the remaining flag.

## Exceptions, maturity and unresolved decisions

The rule records no voluntary signed-in password-change route at present. The primary select-workbase screen still clears mustChangePassword: this conflicts with the rule that only an actual password change clears it. Flag for engineering review; Academy does not patch it.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-029:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/change-password.js#L1) | `ireps-mobile/app/onboarding/change-password.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-154:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/ChangePasswordPage.jsx#L1) | `ireps-web/src/pages/ChangePasswordPage.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-054:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/redux/authApi.js#L1) | `ireps-mobile/src/redux/authApi.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-059:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/auth/auth-rules.md#L1) | `ireps-rules/auth/auth-rules.md` | main / `f5dc84e44c9f` | clean |
