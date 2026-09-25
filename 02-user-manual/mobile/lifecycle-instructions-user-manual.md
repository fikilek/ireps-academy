# Lifecycle Instruction Creation — User Manual

Module **FRM-026** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/lifecycle-instructions-body-of-knowledge.md) · [User Manual](lifecycle-instructions-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/lifecycle-instructions-field-catalogue.md) · [Error register](../../01-body-of-knowledge/lifecycle-instructions-error-register.md) · [Practical examples](../../10-assessments/lifecycle-instructions-scenarios.md)

## Before you start

Inspection, disconnection, reconnection, removal and meter reading have office-origin instruction types. Issuing the instruction changes the work state, not the physical meter state. The assigned actor must accept the instruction before the office-origin execution path can complete it.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Choose the meter and task type in TRN Origin.
2. Check meter eligibility and the intended premise.
3. Select the shared instruction and add relevant notes.
4. Choose the permitted target user/team and review the assignment.
5. Issue once, verify ISSUED, and monitor acceptance through work-order management.

## What to check in the result

Issuing a disconnection instruction leaves the meter connected until an accepted execution reports a completed disconnection. An office dashboard must not equate ISSUED with DISCONNECTED.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Role inheritance remains open. Field-origin exceptions have separate checks and do not make office acceptance optional for an office-issued instruction.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/lifecycle-instructions-error-register.md) and [field catalogue](../../01-body-of-knowledge/lifecycle-instructions-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/lifecycle-instructions-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
