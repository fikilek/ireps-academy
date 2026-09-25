# Targeted Batch Planning and Allocation — User Manual

Module **FRM-029** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/targeted-batches-body-of-knowledge.md) · [User Manual](targeted-batches-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/targeted-batches-field-catalogue.md) · [Error register](../../01-body-of-knowledge/targeted-batches-error-register.md) · [Practical examples](../../10-assessments/targeted-batches-scenarios.md)

## Before you start

The web family contains upload, draft selection, confirmation, allocation targets, grouped allocation, unallocation, deletion and row take-out actions. These are separate actions with different guards. Search, sorting and map filters alter the view and do not alone mutate a batch.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Choose the correct source population and geographic scope.
2. Review draft rows and exceptions before confirmation.
3. Confirm the intended batch content.
4. Select the eligible allocation target and inspect affected rows/team members.
5. Submit the specific allocation action and check its result.
6. Use unallocation, take-out or deletion only through the supported action with its own confirmation; verify downstream work ownership.

## What to check in the result

A shared ERF contains three expected meter rows. Assign and later complete the appropriate row based on actual meter/premise evidence; the ERF itself is not a licence to close all three.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Eight multi-meter capture permutations remain deferred in the source rule’s release plan; ambiguous Test 15 still needs an agreed association rule. Reported DEV fixes are not a published acceptance certificate.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/targeted-batches-error-register.md) and [field catalogue](../../01-body-of-knowledge/targeted-batches-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/targeted-batches-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
