# Informal ERF Capture — User Manual

Module **FRM-012** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/informal-erf-body-of-knowledge.md) · [User Manual](informal-erf-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/informal-erf-field-catalogue.md) · [Error register](../../01-body-of-knowledge/informal-erf-error-register.md) · [Practical examples](../../10-assessments/informal-erf-scenarios.md)

## Before you start

The drawn boundary and reason explain why the record exists. It does not establish a legal cadastral parcel or legal ownership, and a roadside meter by itself does not prove that a new ERF is necessary.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Inspect the mapped and nearby ERFs first.
2. Choose the informal ERF route only where the operational context warrants it.
3. Draw and confirm the boundary and review its position.
4. Select the creation reason; explain Other.
5. Capture the requested evidence, review and submit.
6. Verify the returned record and subsequently register the individual premise in that context.

## What to check in the result

A meter is outside a mapped boundary but serves an already known flat. Keep the served premise association; do not automatically create an informal ERF around the kiosk.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Operational geometry must not be described as cadastral proof. Confirm overlap handling, queue recovery and server validation on the intended release.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/informal-erf-error-register.md) and [field catalogue](../../01-body-of-knowledge/informal-erf-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/informal-erf-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
