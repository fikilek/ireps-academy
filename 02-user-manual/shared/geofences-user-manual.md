# Geofence Planning — User Manual

Module **FRM-025** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/geofences-body-of-knowledge.md) · [User Manual](geofences-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/geofences-field-catalogue.md) · [Error register](../../01-body-of-knowledge/geofences-error-register.md) · [Practical examples](../../10-assessments/geofences-scenarios.md)

## Before you start

A geofence is a work-planning object. It does not replace a municipal boundary, ward, legal ERF, premise or asset location. Mobile creation and web drawing/planning interfaces must be distinguished from read-only map filters.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Choose the workbase and intended planning context.
2. Draw or select the supported boundary.
3. Enter its name and description and inspect included work.
4. Review geometry and overlapping operational areas.
5. Save and verify the stored boundary before using it in allocation.

## What to check in the result

A geofence crosses several ERFs for a reading route. Each meter retains its own premise and ERF identity even while assigned to that route.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Geometry validation and role scope are release-specific. Do not interpret a boundary selection as allocation or acceptance of work.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/geofences-error-register.md) and [field catalogue](../../01-body-of-knowledge/geofences-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/geofences-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
