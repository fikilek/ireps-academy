# Invited Profile and Admin Confirmation — Body of Knowledge

Module **FRM-005** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](invited-profile-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/invited-profile-user-manual.md) · [Field catalogue](invited-profile-field-catalogue.md) · [Error register](invited-profile-error-register.md) · [Practical examples](../10-assessments/invited-profile-scenarios.md)

## Meaning and purpose

Invitation completion lets an invited manager, supervisor or administrator replace their initial credential and supply the remaining profile information.

The repository contains both complete-invited-profile and confirm-admin screens. They are recorded as variants of one onboarding topic, not proof that every current route reaches both. Invitations are separate from fieldworker self-signup.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

Account identity, organisation, authorisation and current work context are separate. A credential change must not be described as creating operational permission. Passwords and verification codes do not belong in submitted meter evidence.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Use the invited identity and the securely supplied initial credential.
2. Follow the onboarding route actually offered by the release.
3. Enter and confirm the permanent password; capture the requested cell number.
4. Submit and distinguish password success from profile-update success.
5. Check the resulting role, provider and workbase; report an incorrect association rather than creating another identity.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| New permanent/admin password | Permanent replacement credential. | Use the current authentication rule; verify older screen validation against it. |
| Confirm password | Password cross-check. | Must match. |
| Cell number | Invited person’s contact number. | Phone keyboard assists entry but does not prove number ownership. |

The [field catalogue](invited-profile-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](invited-profile-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

An invited supervisor completes a password change but has no assigned workbase. That is an assignment issue, not a reason to repeat an invitation.

## Exceptions, maturity and unresolved decisions

Legacy screen validation/routing may differ from the current mandatory-password design. Invitation delivery and account-change sequencing must be tested without exposing real credentials.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-030:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/complete-invited-profile.js#L1) | `ireps-mobile/app/onboarding/complete-invited-profile.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-031:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/confirm-admin.js#L1) | `ireps-mobile/app/onboarding/confirm-admin.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-054:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/redux/authApi.js#L1) | `ireps-mobile/src/redux/authApi.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-059:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/auth/auth-rules.md#L1) | `ireps-rules/auth/auth-rules.md` | main / `f5dc84e44c9f` | clean |
