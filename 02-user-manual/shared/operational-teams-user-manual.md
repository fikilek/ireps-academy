# Operational Teams — User Manual

Module **FRM-024** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/operational-teams-body-of-knowledge.md) · [User Manual](operational-teams-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/operational-teams-field-catalogue.md) · [Error register](../../01-body-of-knowledge/operational-teams-error-register.md) · [Practical examples](../../10-assessments/operational-teams-scenarios.md)

## Before you start

Create, rename, add member, remove member and delete are distinct operations on the same team family. Team membership does not itself prove permission to execute every transaction or erase existing task assignments.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Select the correct provider/workbase context.
2. Create or choose a team and verify its members.
3. Use the intended membership or naming action.
4. Review any dependencies before a destructive team action.
5. Confirm the result and inspect relevant allocations separately.

## What to check in the result

Removing a fieldworker from a team does not prove every previously accepted job was reassigned. Check the affected allocations through their own workflow.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Verify eligibility, deletion guards and assignment effects in the target release. The form inventory records both mobile and web implementations.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/operational-teams-error-register.md) and [field catalogue](../../01-body-of-knowledge/operational-teams-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/operational-teams-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
