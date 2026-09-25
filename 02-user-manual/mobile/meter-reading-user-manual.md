# Meter Reading — User Manual

Module **FRM-015** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/meter-reading-body-of-knowledge.md) · [User Manual](meter-reading-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/meter-reading-field-catalogue.md) · [Error register](../../01-body-of-knowledge/meter-reading-error-register.md) · [Practical examples](../../10-assessments/meter-reading-scenarios.md)

## Before you start

The owner’s module covers conventional electricity and water readings. The inspected server explicitly rejects prepaid MREAD and token readings for Sprint 1, even though phone source contains token-related branches. A read does not reconnect a meter, issue a bill or demonstrate payment. Reading differences need interval, units and exception context before they become usable consumption.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Open the assigned or permitted reading task for the correct conventional meter.
2. Confirm the premise, meter serial, service and instruction.
3. Record access; if access or a usable reading is unavailable, use the appropriate reason with evidence.
4. Read the actual register, record capture time and GPS and take the required photograph.
5. Review a reading lower than the previous one; record the available exception reason rather than changing the value to make it look plausible.
6. Submit, verify the transaction and current reading information, and let the authorised web workflow prepare the billing export.

## What to check in the result

Last month’s electricity reading was 12400.0 and this month’s is 12540.6 in the same verified unit. The arithmetic difference is 140.6 units; billing still requires the correct period, account, tariff and exception review. A blank display is an exception, not a zero reading.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Production readiness remains open by owner direction. Do not teach prepaid token capture as accepted MREAD. Validate exact proximity threshold, units, register multipliers and export acceptance on the relevant release.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/meter-reading-error-register.md) and [field catalogue](../../01-body-of-knowledge/meter-reading-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/meter-reading-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
