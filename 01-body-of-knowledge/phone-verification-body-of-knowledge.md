# Phone Verification — Body of Knowledge

Module **FRM-007** · Baseline **25 September 2026** · Application: **Partial source foundation; service and release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](phone-verification-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/phone-verification-user-manual.md) · [Field catalogue](phone-verification-field-catalogue.md) · [Error register](phone-verification-error-register.md) · [Practical examples](../10-assessments/phone-verification-scenarios.md)

## Meaning and purpose

Phone Verification is a coded verification screen for the account’s phone number.

The source renders a six-character code input and optional mutation hooks. This is a partial foundation, not evidence of a working SMS service or a required production step.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

Account identity, organisation, authorisation and current work context are separate. A credential change must not be described as creating operational permission. Passwords and verification codes do not belong in submitted meter evidence.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. During a controlled release review, confirm that the account phone number and verification service are available.
2. Enter the received code, retaining leading zeros.
3. Submit once and read the result.
4. Use resend after its cooldown when appropriate.
5. If the service is unavailable, report the incomplete feature; never substitute a fabricated code.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Code | Verification code received for the account phone. | Screen requires length 6 and numeric keyboard; backend verification hooks must exist. |
| Phone number | Number to which the code is expected to be sent. | Inherited from user record; not an editable contact form here. |

The [field catalogue](phone-verification-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](phone-verification-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

The screen appears but its optional verify mutation is absent. The correct assessment is “feature incomplete for this release”, not “the worker entered the wrong code”.

## Exceptions, maturity and unresolved decisions

VerifyPhone and resendPhoneCode endpoints are not established by the optional-hook syntax. Delivery, expiry, attempt limits and routing remain acceptance gaps. The primary API exposes sendPhoneOtp and confirmPhoneOtp instead of the verifyPhone/resendPhoneCode names used by this screen.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-034:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/verify-phone.js#L1) | `ireps-mobile/app/onboarding/verify-phone.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-054:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/redux/authApi.js#L1) | `ireps-mobile/src/redux/authApi.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
