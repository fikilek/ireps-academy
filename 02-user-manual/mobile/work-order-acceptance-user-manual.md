# My Work Orders and Acceptance — User Manual

Module **FRM-028** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/work-order-acceptance-body-of-knowledge.md) · [User Manual](work-order-acceptance-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/work-order-acceptance-field-catalogue.md) · [Error register](../../01-body-of-knowledge/work-order-acceptance-error-register.md) · [Practical examples](../../10-assessments/work-order-acceptance-scenarios.md)

## Before you start

Lifecycle instructions, BGO batches and targeted batches use different mutations. Their status words may look similar but their permissions and reversal rules differ. The Premise Picker on a Sales row is a navigation/association step, not a new meter registration form.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Open My Work Orders in the correct workbase.
2. Inspect assignment identity, area and requested work.
3. Accept or reject the specific instruction/batch using the offered action and required reason.
4. Verify the returned workflow state.
5. Open the accepted task. On the Sales Path choose the correct row and premise; record the actual field outcome through its own form.

## What to check in the result

Two flats share an ERF. A worker accepts the targeted batch and chooses Flat 2 in the Premise Picker for its row. Acceptance does not justify completing every Sales row on the ERF.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

A wrong association has backend capabilities but may lack a phone correction interface. Cross-batch Not joined labels may be misleading; server refusal remains authoritative.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/work-order-acceptance-error-register.md) and [field catalogue](../../01-body-of-knowledge/work-order-acceptance-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/work-order-acceptance-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
