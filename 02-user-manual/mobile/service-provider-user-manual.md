# Service Provider Registration and Editing — User Manual

Module **FRM-023** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/service-provider-body-of-knowledge.md) · [User Manual](service-provider-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/service-provider-field-catalogue.md) · [Error register](../../01-body-of-knowledge/service-provider-error-register.md) · [Practical examples](../../10-assessments/service-provider-scenarios.md)

## Before you start

The source has create and edit wrappers around a shared provider form. Trading identity, registered identity, ownership contact, manager and geographic coverage are distinct facts. Utility/main contractor/subcontractor hierarchy is owner context and must not be inferred solely from a provider name.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Check that the organisation is not already registered.
2. Open Create or Edit deliberately.
3. Record trading and registered details, ownership fields and the available responsible-manager/workbase selections.
4. Review the relationships before submitting.
5. Verify the saved provider and its intended availability for signup and assignments.

## What to check in the result

A provider exists but has no responsible manager. Fieldworker signup can be blocked even when the trading name appears correct.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Review hierarchy and status changes with the responsible product workstream. Provider deactivation, existing users and outstanding assignments require explicit transition rules.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/service-provider-error-register.md) and [field catalogue](../../01-body-of-knowledge/service-provider-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/service-provider-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
