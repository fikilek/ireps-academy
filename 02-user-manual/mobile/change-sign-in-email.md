# Change Sign-in Email — User Manual

Module **FRM-009** · Baseline **25 September 2026** · Application: **Feature-branch source; deployment unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/change-sign-in-email-body-of-knowledge.md) · [User Manual](change-sign-in-email.md) · [Field catalogue](../../01-body-of-knowledge/change-sign-in-email-field-catalogue.md) · [Error register](../../01-body-of-knowledge/change-sign-in-email-error-register.md) · [Practical examples](../../10-assessments/change-sign-in-email-scenarios.md)

## Before you start

There are two distinct journeys: the person confirms a link at their new address; an authorised office user changes another person’s address when needed. Dedicated email feature worktrees provide evidence that must not be advertised as deployed on all builds.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Choose own-account or authorised office change; do not edit only the profile email.
2. Review the person and destination address.
3. For own-account change, reauthenticate as requested and open the link in the new inbox; use the old address until the link takes effect.
4. For an office change, check the explicit server result before telling the person which email to use.
5. Sign in with the effective new address and existing password; verify the user record follows the authentication account.

## What to check in the result

An office change updates authentication but the profile update fails. The new sign-in address remains effective; the next synchronisation must reconcile the record without changing the person’s UID.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Verify deployment of email branches, permitted actor/target combinations and audit reconciliation. AU-R001 gives specific email-change permissions; it does not settle permission inheritance elsewhere.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/change-sign-in-email-error-register.md) and [field catalogue](../../01-body-of-knowledge/change-sign-in-email-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/change-sign-in-email-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.

## Preserved task details and current qualification

The documented own-account mobile route is Account Settings → Email → CHANGE; the office mobile route is Users → person → CHANGE EMAIL in the email feature. Verify those routes in the intended build. AU-R001 specifically allows Super User to change others’ addresses, Admin except a Super User target, and a Manager for their own providers’ fieldworkers/supervisors. Nobody uses the office route to change their own address. These are email-action rules, not blanket permission inheritance.
