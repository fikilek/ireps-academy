# BGO Planning — User Manual

Module **FRM-031** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/bgo-planning-body-of-knowledge.md) · [User Manual](bgo-planning-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/bgo-planning-field-catalogue.md) · [Error register](../../01-body-of-knowledge/bgo-planning-error-register.md) · [Practical examples](../../10-assessments/bgo-planning-scenarios.md)

## Before you start

BMD and TC planning screens have create/delete actions. Preserve the actual screen labels and keep prototype or legacy variants marked; do not infer a universal batch lifecycle from their similar names.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Select the appropriate BMD or TC planning route.
2. Review source rows, geography and target context.
3. Create the proposed work object and inspect the returned result.
4. Track acceptance through My Work Orders.
5. Use deletion only where the source permits an unaccepted object to be removed.

## What to check in the result

An office user tries to delete work after acceptance. The relevant rule is the BGO action’s guard, not whether the row is currently visible in a filtered table.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

This family needs route-by-route release review. Do not treat every historical BGO screen as a current recommended workflow.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/bgo-planning-error-register.md) and [field catalogue](../../01-body-of-knowledge/bgo-planning-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/bgo-planning-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
