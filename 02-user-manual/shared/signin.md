# Sign In — User Manual

Module **FRM-001** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/sign-in-body-of-knowledge.md) · [User Manual](signin.md) · [Field catalogue](../../01-body-of-knowledge/sign-in-field-catalogue.md) · [Error register](../../01-body-of-knowledge/sign-in-error-register.md) · [Practical examples](../../10-assessments/sign-in-scenarios.md)

## Before you start

Mobile and web share the account, but routing depends on the account record. A person may need a password change, manager authorisation or workbase selection before reaching operational screens. Sign In is not meter registration.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Open Sign In in the intended environment.
2. Enter the account email and password; check the email before submitting.
3. Wait for the authentication result and for the iREPS user record to load.
4. Follow the route offered: password change, pending approval, workbase selection or work.
5. Check your displayed identity and active workbase before capturing any operational information.

## What to check in the result

A newly registered fieldworker can authenticate but still sees pending approval. The correct next action is manager authorisation, not creating a second account.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Verify the actual post-login route on each release. A successful Firebase sign-in followed by a missing user record is a partial result. Do not describe it as an incorrect password.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/sign-in-error-register.md) and [field catalogue](../../01-body-of-knowledge/sign-in-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/sign-in-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.

## Preserved task details and current qualification

Sign In does not ask for routine confirmation. It shows progress, and successful navigation is the success outcome. The source waits up to 30 seconds for the user record; an authenticated identity with a missing record is a different failure from a wrong password. Current source trims email and password edges and lowercases the email. Preserve the distinction between a normalization rule and the actual inspected implementation.
