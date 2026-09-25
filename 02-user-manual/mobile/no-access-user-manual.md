# No Access — User Manual

Module **FRM-020** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/no-access-body-of-knowledge.md) · [User Manual](no-access-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/no-access-field-catalogue.md) · [Error register](../../01-body-of-knowledge/no-access-error-register.md) · [Practical examples](../../10-assessments/no-access-scenarios.md)

## Before you start

No Access is shared across registration and lifecycle capture and also has a targeted-batch visit route. It is an outcome of an attempted visit, not a meter state or evidence that an installation, reading, removal or disconnection succeeded. Lack of access and an unreadable display are different facts.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Identify the intended task, premise/meter or targeted-batch row.
2. Select the No Access outcome in that workflow.
3. Choose the actual reason and provide Other details when required.
4. Capture the required contextual evidence without inventing a meter serial or register value.
5. Review the result and submit through the parent workflow.
6. Verify the visit/transaction result and the work-order follow-up; do not assume the asset state changed.

## What to check in the result

The display is blank but the meter is reachable: use the form’s no-reading reason. A locked gate preventing access is No Access. Neither should be represented by a reading of zero.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Reason lists and evidence rules must be checked per workflow. Row completion and reallocation after No Access are workflow-specific; a generic automatic revisit policy is not approved.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/no-access-error-register.md) and [field catalogue](../../01-body-of-knowledge/no-access-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/no-access-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
