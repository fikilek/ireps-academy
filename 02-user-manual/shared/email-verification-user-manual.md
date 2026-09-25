# Email Verification — User Manual

Module **FRM-006** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/email-verification-body-of-knowledge.md) · [User Manual](email-verification-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/email-verification-field-catalogue.md) · [Error register](../../01-body-of-knowledge/email-verification-error-register.md) · [Practical examples](../../10-assessments/email-verification-scenarios.md)

## Before you start

The screen offers resend and an already-verified check. Verification does not authorise work or change organisation. A screen existing in the code does not establish that it is a mandatory current onboarding gate.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Check the displayed email.
2. Use the verification link in that inbox.
3. Return and request the verification check.
4. Use resend only when needed and wait for the screen cooldown.
5. Confirm the account advances only after verification is actually recognised.

## What to check in the result

A person clicks Already verified before opening the link. The expected teaching outcome is to complete verification, not repeatedly tap the check.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Routing and mutation connectivity require release verification. Do not merge this with Password Reset or Change Sign-in Email.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/email-verification-error-register.md) and [field catalogue](../../01-body-of-knowledge/email-verification-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/email-verification-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
