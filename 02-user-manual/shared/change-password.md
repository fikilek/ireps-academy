# Change Password — User Manual

Module **FRM-004** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/change-password-body-of-knowledge.md) · [User Manual](change-password.md) · [Field catalogue](../../01-body-of-knowledge/change-password-field-catalogue.md) · [Error register](../../01-body-of-knowledge/change-password-error-register.md) · [Practical examples](../../10-assessments/change-password-scenarios.md)

## Before you start

A credential update and clearing the iREPS must-change flag are separate writes. If the first succeeds and the second fails, the new password is already effective. Do not tell the person to keep using the old password.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Sign in and follow the mandatory Change Password route when shown.
2. Enter a new password and matching confirmation.
3. Confirm and wait for the result.
4. If the password changed but recording failed, use the new password and report the incomplete onboarding acknowledgement.
5. Verify that the required gate clears and the expected next onboarding step appears.

## What to check in the result

The network fails after Firebase changes the credential. The result states that the change was not recorded in iREPS. The person signs in using the new password; the manager investigates the remaining flag.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

The rule records no voluntary signed-in password-change route at present. The primary select-workbase screen still clears mustChangePassword: this conflicts with the rule that only an actual password change clears it. Flag for engineering review; Academy does not patch it.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/change-password-error-register.md) and [field catalogue](../../01-body-of-knowledge/change-password-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/change-password-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
