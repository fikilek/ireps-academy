# Meter Commissioning — User Manual

Module **FRM-014** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/meter-commissioning-body-of-knowledge.md) · [User Manual](meter-commissioning-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/meter-commissioning-field-catalogue.md) · [Error register](../../01-body-of-knowledge/meter-commissioning-error-register.md) · [Practical examples](../../10-assessments/meter-commissioning-scenarios.md)

## Before you start

The dedicated commissioning callable requires an existing FIELD meter and electricity or water service. Prepaid electricity has vending confirmation, final switch-on and keypad checks. Conventional electricity has the switch-on check. Water has operational/service and reading/flow checks. The confirmation of vending is not an implemented token-selling module.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Open Commissioning for the intended FIELD meter.
2. Check service type and meter kind so the correct questions are shown.
3. Record each applicable yes/no answer honestly; supply notes when the answer is no.
4. Capture evidence for each confirmed check using its required media tag.
5. Submit and read both the transaction result and commissioning outcome.
6. For a pass verify CONNECTED on the asset; for a valid unsuccessful outcome verify that FIELD remains and arrange the outstanding work.

## What to check in the result

A prepaid meter passes vending and switch-on but no keypad was issued. Record no with notes. A valid submitted form does not imply a pass; the meter remains FIELD under the observed validator.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Current generic lifecycle helper also contains older commissioning logic, but the dedicated callable is the relevant route. Verify the callable/trigger pair and result refresh in the chosen environment.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/meter-commissioning-error-register.md) and [field catalogue](../../01-body-of-knowledge/meter-commissioning-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/meter-commissioning-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
