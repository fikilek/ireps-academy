# Phone Verification — User Manual

Module **FRM-007** · Baseline **25 September 2026** · Application: **Partial source foundation; service and release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/phone-verification-body-of-knowledge.md) · [User Manual](phone-verification-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/phone-verification-field-catalogue.md) · [Error register](../../01-body-of-knowledge/phone-verification-error-register.md) · [Practical examples](../../10-assessments/phone-verification-scenarios.md)

## Before you start

The source renders a six-character code input and optional mutation hooks. This is a partial foundation, not evidence of a working SMS service or a required production step.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. During a controlled release review, confirm that the account phone number and verification service are available.
2. Enter the received code, retaining leading zeros.
3. Submit once and read the result.
4. Use resend after its cooldown when appropriate.
5. If the service is unavailable, report the incomplete feature; never substitute a fabricated code.

## What to check in the result

The screen appears but its optional verify mutation is absent. The correct assessment is “feature incomplete for this release”, not “the worker entered the wrong code”.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

VerifyPhone and resendPhoneCode endpoints are not established by the optional-hook syntax. Delivery, expiry, attempt limits and routing remain acceptance gaps. The primary API exposes sendPhoneOtp and confirmPhoneOtp instead of the verifyPhone/resendPhoneCode names used by this screen.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/phone-verification-error-register.md) and [field catalogue](../../01-body-of-knowledge/phone-verification-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/phone-verification-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
