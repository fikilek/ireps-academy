# Email Verification — Body of Knowledge

Module **FRM-006** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](email-verification-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/email-verification-user-manual.md) · [Field catalogue](email-verification-field-catalogue.md) · [Error register](email-verification-error-register.md) · [Practical examples](../10-assessments/email-verification-scenarios.md)

## Meaning and purpose

Email Verification records evidence that a person can receive and open the link at the account’s email address.

The screen offers resend and an already-verified check. Verification does not authorise work or change organisation. A screen existing in the code does not establish that it is a mandatory current onboarding gate.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

Account identity, organisation, authorisation and current work context are separate. A credential change must not be described as creating operational permission. Passwords and verification codes do not belong in submitted meter evidence.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Check the displayed email.
2. Use the verification link in that inbox.
3. Return and request the verification check.
4. Use resend only when needed and wait for the screen cooldown.
5. Confirm the account advances only after verification is actually recognised.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Email | Address being verified. | Inherited from authenticated account; not editable on this screen. |
| Resend/check actions | Request a link or refresh verified state. | Source has a 30-second resend cooldown; backend limits may also apply. |

The [field catalogue](email-verification-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](email-verification-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

A person clicks Already verified before opening the link. The expected teaching outcome is to complete verification, not repeatedly tap the check.

## Exceptions, maturity and unresolved decisions

Routing and mutation connectivity require release verification. Do not merge this with Password Reset or Change Sign-in Email.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-033:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/verify-email.js#L1) | `ireps-mobile/app/onboarding/verify-email.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-054:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/redux/authApi.js#L1) | `ireps-mobile/src/redux/authApi.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
