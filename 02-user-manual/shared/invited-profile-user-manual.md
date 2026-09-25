# Invited Profile and Admin Confirmation — User Manual

Module **FRM-005** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/invited-profile-body-of-knowledge.md) · [User Manual](invited-profile-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/invited-profile-field-catalogue.md) · [Error register](../../01-body-of-knowledge/invited-profile-error-register.md) · [Practical examples](../../10-assessments/invited-profile-scenarios.md)

## Before you start

The repository contains both complete-invited-profile and confirm-admin screens. They are recorded as variants of one onboarding topic, not proof that every current route reaches both. Invitations are separate from fieldworker self-signup.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Use the invited identity and the securely supplied initial credential.
2. Follow the onboarding route actually offered by the release.
3. Enter and confirm the permanent password; capture the requested cell number.
4. Submit and distinguish password success from profile-update success.
5. Check the resulting role, provider and workbase; report an incorrect association rather than creating another identity.

## What to check in the result

An invited supervisor completes a password change but has no assigned workbase. That is an assignment issue, not a reason to repeat an invitation.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Legacy screen validation/routing may differ from the current mandatory-password design. Invitation delivery and account-change sequencing must be tested without exposing real credentials.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/invited-profile-error-register.md) and [field catalogue](../../01-body-of-knowledge/invited-profile-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/invited-profile-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
