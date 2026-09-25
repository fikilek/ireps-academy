# Workbase Selection and Account Settings — User Manual

Module **FRM-008** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/workbase-selection-body-of-knowledge.md) · [User Manual](workbase-selection-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/workbase-selection-field-catalogue.md) · [Error register](../../01-body-of-knowledge/workbase-selection-error-register.md) · [Practical examples](../../10-assessments/workbase-selection-scenarios.md)

## Before you start

Mobile onboarding, mobile Account Settings and web Profile contain related views. Contact/profile editing is a separate action from sign-in email change and from authorising a new workbase.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Check the signed-in identity and the available workbases.
2. Select the intended workbase from the assigned list.
3. Wait for the active-workbase update.
4. Check the geography shown by the next screen.
5. If no workbase exists, ask the responsible administrator or manager to correct assignment.

## What to check in the result

A worker has two assigned areas. Selecting Workbase B changes context; it does not reassign all Workbase A work orders to B.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Primary select-workbase code clears mustChangePassword without changing a password, contrary to AU-R001. Keep this discrepancy visible. No blanket role inheritance is accepted.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/workbase-selection-error-register.md) and [field catalogue](../../01-body-of-knowledge/workbase-selection-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/workbase-selection-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
