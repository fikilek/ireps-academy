# Workbase Selection and Account Settings — Body of Knowledge

Module **FRM-008** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](workbase-selection-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/workbase-selection-user-manual.md) · [Field catalogue](workbase-selection-field-catalogue.md) · [Error register](workbase-selection-error-register.md) · [Practical examples](../10-assessments/workbase-selection-scenarios.md)

## Meaning and purpose

A workbase scopes the person’s operational context. Selecting one chooses among assignments already available to that identity.

Mobile onboarding, mobile Account Settings and web Profile contain related views. Contact/profile editing is a separate action from sign-in email change and from authorising a new workbase.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

Account identity, organisation, authorisation and current work context are separate. A credential change must not be described as creating operational permission. Passwords and verification codes do not belong in submitted meter evidence.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Check the signed-in identity and the available workbases.
2. Select the intended workbase from the assigned list.
3. Wait for the active-workbase update.
4. Check the geography shown by the next screen.
5. If no workbase exists, ask the responsible administrator or manager to correct assignment.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Workbase | Assigned operational area selected as active. | Use an offered authorised reference; do not infer access from a place name. |
| Profile/contact values | User profile details supported by the settings variant. | Inspect the per-control evidence; sign-in email must use the dedicated account flow. |

The [field catalogue](workbase-selection-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](workbase-selection-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

A worker has two assigned areas. Selecting Workbase B changes context; it does not reassign all Workbase A work orders to B.

## Exceptions, maturity and unresolved decisions

Primary select-workbase code clears mustChangePassword without changing a password, contrary to AU-R001. Keep this discrepancy visible. No blanket role inheritance is accepted.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-032:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/select-workbase.js#L1) | `ireps-mobile/app/onboarding/select-workbase.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-018:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/user/user-settings.js#L1) | `ireps-mobile/app/(tabs)/admin/user/user-settings.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-175:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/profile/ProfilePage.jsx#L1) | `ireps-web/src/pages/profile/ProfilePage.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-054:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/redux/authApi.js#L1) | `ireps-mobile/src/redux/authApi.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-059:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/auth/auth-rules.md#L1) | `ireps-rules/auth/auth-rules.md` | main / `f5dc84e44c9f` | clean |
