# Password Reset — User Manual

Module **FRM-003** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/password-reset-body-of-knowledge.md) · [User Manual](password-reset.md) · [Field catalogue](../../01-body-of-knowledge/password-reset-field-catalogue.md) · [Error register](../../01-body-of-knowledge/password-reset-error-register.md) · [Practical examples](../../10-assessments/password-reset-scenarios.md)

## Before you start

The same acknowledgement is intended for registered and unregistered email addresses. A reset must not be taught as changing role, approval or workbase. Firebase-hosted recovery is distinct from an iREPS campaign or report-email facility.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. From Sign In choose Lost access? or the password-reset link on the applicable platform.
2. Enter the sign-in email and confirm the request.
3. Read the acknowledgement, then check the inbox and junk folder.
4. Open the reset link and set the new password.
5. Return to Sign In; use the new credential and complete any remaining onboarding gate.

## What to check in the result

A mistyped but syntactically valid address receives the same on-screen acknowledgement. The learner must understand that this is not proof that the address has an iREPS account.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

The hosted link expiry and provider error conditions require release testing. Never promise delivery time or expose whether another person has an account. The primary mobile tree links to /pwdReset but that screen is absent there; it exists in the mobile-auth worktree. The feature must be integrated and verified before the primary mobile guide can be treated as executable.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/password-reset-error-register.md) and [field catalogue](../../01-body-of-knowledge/password-reset-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/password-reset-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.

## Preserved task details and current qualification

Primary mobile Sign In currently links to /pwdReset but the screen is absent in that worktree. The reset screen exists in mobile-auth and on the web. Until a tested release integrates the mobile feature, do not present the primary phone route as working. The rule’s acknowledgement is deliberately identical for an existing and a nonexistent account.
