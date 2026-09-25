# Change Sign-in Email — Body of Knowledge

Module **FRM-009** · Baseline **25 September 2026** · Application: **Feature-branch source; deployment unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](change-sign-in-email-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/change-sign-in-email.md) · [Field catalogue](change-sign-in-email-field-catalogue.md) · [Error register](change-sign-in-email-error-register.md) · [Practical examples](../10-assessments/change-sign-in-email-scenarios.md)

## Meaning and purpose

Change Sign-in Email changes the account identifier while preserving the person’s identity and transaction history.

There are two distinct journeys: the person confirms a link at their new address; an authorised office user changes another person’s address when needed. Dedicated email feature worktrees provide evidence that must not be advertised as deployed on all builds.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

Account identity, organisation, authorisation and current work context are separate. A credential change must not be described as creating operational permission. Passwords and verification codes do not belong in submitted meter evidence.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Choose own-account or authorised office change; do not edit only the profile email.
2. Review the person and destination address.
3. For own-account change, reauthenticate as requested and open the link in the new inbox; use the old address until the link takes effect.
4. For an office change, check the explicit server result before telling the person which email to use.
5. Sign in with the effective new address and existing password; verify the user record follows the authentication account.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| New email | New sign-in identifier. | Valid and not already in use; own-address equality is a no-op. |
| Current password | Fresh authentication for own-account change. | Own-account flow only; do not request another person’s password for an office action. |
| Target user | Person whose identifier is being corrected. | Office permission and organisational scope are action-specific. |

The [field catalogue](change-sign-in-email-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](change-sign-in-email-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

An office change updates authentication but the profile update fails. The new sign-in address remains effective; the next synchronisation must reconcile the record without changing the person’s UID.

## Exceptions, maturity and unresolved decisions

Verify deployment of email branches, permitted actor/target combinations and audit reconciliation. AU-R001 gives specific email-change permissions; it does not settle permission inheritance elsewhere.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-003:1](https://github.com/fikilek/ireps-mobile/blob/9a981d1882c388043bae6021a1dd33a3e758dfa8/app/(tabs)/admin/user/user-settings.js#L1) | `ireps-mobile-email/app/(tabs)/admin/user/user-settings.js` | feature/change-email / `9a981d1882c3` | clean |
| [FS-067:1](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/src/pages/users/UsersPage.jsx#L1) | `ireps-web-email/src/pages/users/UsersPage.jsx` | feature/change-email / `f9f0a09be4e3` | clean |
| [FS-004:1](https://github.com/fikilek/ireps-mobile/blob/9a981d1882c388043bae6021a1dd33a3e758dfa8/src/redux/authApi.js#L1) | `ireps-mobile-email/src/redux/authApi.js` | feature/change-email / `9a981d1882c3` | clean |
| [FS-064:1](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/functions/users/helpers.js#L1) | `ireps-web-email/functions/users/helpers.js` | feature/change-email / `f9f0a09be4e3` | clean |
| [FS-065:1](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/functions/users/index.js#L1) | `ireps-web-email/functions/users/index.js` | feature/change-email / `f9f0a09be4e3` | clean |
| [FS-066:1](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/functions/users/updateUserCallable.js#L1) | `ireps-web-email/functions/users/updateUserCallable.js` | feature/change-email / `f9f0a09be4e3` | clean |
| [FS-059:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/auth/auth-rules.md#L1) | `ireps-rules/auth/auth-rules.md` | main / `f5dc84e44c9f` | clean |
