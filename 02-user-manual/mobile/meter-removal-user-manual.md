# Meter Removal — User Manual

Module **FRM-019** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/meter-removal-body-of-knowledge.md) · [User Manual](meter-removal-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/meter-removal-field-catalogue.md) · [Error register](../../01-body-of-knowledge/meter-removal-error-register.md) · [Practical examples](../../10-assessments/meter-removal-scenarios.md)

## Before you start

The observed transition is FIELD, CONNECTED or DISCONNECTED to REMOVED. Remove meter can end the physical job; Replace meter requires a linked installation of a different meter. Removal does not by itself prove return to a store, decommissioning approval, retirement, disposal or a customer refund.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Open the appropriate meter and Remove meter or Replace meter instruction/context.
2. Verify the serial and served premise; capture required final reading or prepaid credit evidence before removal.
3. Record No Access if the work cannot be reached.
4. For completed work confirm meter removed and capture removal evidence; do not use a success form to describe a failed attempt.
5. Submit and verify REMOVED on the old asset.
6. If replacement is required, continue the linked Meter Installation for the new serial. Record physical custody/return through the utility’s current process until iREPS stores are defined.

## What to check in the result

Old meter 00123456789 is removed and replaced by 00987654321. The old meter’s final reading remains attached to its history. A later store return references the old meter; it must not be attached to the new installation.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Current removal helper retains older answer/notes shapes alongside the updated confirmation UI. Decommissioned is also a legacy state guard. A single retirement/disposal policy and a stores return form are not established.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/meter-removal-error-register.md) and [field catalogue](../../01-body-of-knowledge/meter-removal-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/meter-removal-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
