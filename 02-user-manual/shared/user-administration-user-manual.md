# User Authorisation and Role Management — User Manual

Module **FRM-022** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/user-administration-body-of-knowledge.md) · [User Manual](user-administration-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/user-administration-field-catalogue.md) · [Error register](../../01-body-of-knowledge/user-administration-error-register.md) · [Practical examples](../../10-assessments/user-administration-scenarios.md)

## Before you start

Fieldworker authorisation and web role editing are separate actions. A visible status dropdown is not proof that status saving is enabled. The catalogue excludes Guest; SPU means Super User. There is no approved blanket inheritance rule.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Locate the intended user and check their provider and current approval state.
2. Choose the specific action supported in that release: authorise, role change or another implemented action.
3. Review the target role/workbase and the actor’s authority.
4. Confirm and submit; do not treat changing a selector as saving.
5. Reload the user record and verify only the intended changes.

## What to check in the result

An office user changes the status selection but Save is disabled. The account has not changed; training must not instruct the learner to proceed as if approval succeeded.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Capture action-level permissions in a tested matrix. Role labels alone are not authority. Review the current branch against other user-management feature worktrees.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/user-administration-error-register.md) and [field catalogue](../../01-body-of-knowledge/user-administration-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/user-administration-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
