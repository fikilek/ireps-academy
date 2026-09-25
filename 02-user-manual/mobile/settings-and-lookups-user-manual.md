# Settings and Lookup Administration — User Manual

Module **FRM-034** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/settings-and-lookups-body-of-knowledge.md) · [User Manual](settings-and-lookups-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/settings-and-lookups-field-catalogue.md) · [Error register](../../01-body-of-knowledge/settings-and-lookups-error-register.md) · [Practical examples](../../10-assessments/settings-and-lookups-scenarios.md)

## Before you start

The source includes legacy settings arrays, lookup creation/editing, option creation/editing and status actions. UI-R003 now requires field-form choice lists to live in the phone’s formOptions module. Editing a database lookup is therefore not evidence that a current field-form dropdown will change.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Identify the setting or lookup and the application component that actually consumes it.
2. Inspect existing codes and historical use.
3. Create/edit the supported metadata or option deliberately.
4. Review label, code, sort order and status implications before saving.
5. Verify the consumer’s behaviour on the relevant release; coordinate code-owned list changes with engineering.

## What to check in the result

An administrator adds a database reason but the current Meter Reading form uses its local shared list. The absence on the phone is a source-of-list mismatch, not a sync failure to be fixed by repeated edits.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Map every lookup consumer before changing or retiring options. Common form standards must reference engineering rules rather than create a competing list authority.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/settings-and-lookups-error-register.md) and [field catalogue](../../01-body-of-knowledge/settings-and-lookups-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/settings-and-lookups-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
