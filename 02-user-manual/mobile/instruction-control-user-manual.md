# Lifecycle Instruction Control — User Manual

Module **FRM-027** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/instruction-control-body-of-knowledge.md) · [User Manual](instruction-control-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/instruction-control-field-catalogue.md) · [Error register](../../01-body-of-knowledge/instruction-control-error-register.md) · [Practical examples](../../10-assessments/instruction-control-scenarios.md)

## Before you start

Work state and meter state must remain separate. Reassigning an instruction changes responsibility; it does not perform the physical job or remove its history.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Find the instruction and inspect its current workflow state.
2. Choose a supported action and check whether it is still executable.
3. For reassignment select the new eligible target and provide the reason.
4. Review and confirm the action.
5. Verify the new instruction state and ownership, then notify through the organisation’s normal process.

## What to check in the result

An unexecuted job is reassigned from Team A to Team B. The asset’s CONNECTED state stays unchanged, and the instruction records the management event.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Confirm concurrency and the handling of an offline execution submitted after reassignment. Do not silently discard either party’s evidence.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/instruction-control-error-register.md) and [field catalogue](../../01-body-of-knowledge/instruction-control-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/instruction-control-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
