# User Invitations — User Manual

Module **FRM-021** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/user-invitations-body-of-knowledge.md) · [User Manual](invite-a-user.md) · [Field catalogue](../../01-body-of-knowledge/user-invitations-field-catalogue.md) · [Error register](../../01-body-of-knowledge/user-invitations-error-register.md) · [Practical examples](../../10-assessments/user-invitations-scenarios.md)

## Before you start

Separate screens implement each invited role. Their provider selection and permitted inviter differ. The authentication rule describes a generated, once-displayed initial password and mandatory password change; verify the source variant and delivery method before publishing a task guide.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Choose the specific role invitation screen.
2. Confirm the person’s identity and email.
3. Select the provider context required for that role.
4. Review and submit once.
5. Pass the invitation result through the organisation’s approved channel and verify pending/onboarding state without publishing the initial credential.

## What to check in the result

A manager invites a supervisor for the correct provider. The supervisor changes the initial password, then checks the assigned workbase. Being invited does not create an accepted work order.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Do not publish fixed-password examples from historical code. Verify the once-displayed password behaviour in the target build; invitations and re-invitations can have partial success.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/user-invitations-error-register.md) and [field catalogue](../../01-body-of-knowledge/user-invitations-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/user-invitations-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.

## Preserved task details and current qualification

The authentication rule expects a generated initial password, displayed once to the inviter, followed by mandatory password change. Preserve the existing UID if the result is incomplete. If the credential is unavailable, use the established account recovery route after confirming that the account exists; do not create another identity under a different email simply to repeat an invitation. An expired/used initial credential is not a reason to alter employment history.
