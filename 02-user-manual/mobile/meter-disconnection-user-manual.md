# Meter Disconnection — User Manual

Module **FRM-017** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/meter-disconnection-body-of-knowledge.md) · [User Manual](meter-disconnection-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/meter-disconnection-field-catalogue.md) · [Error register](../../01-body-of-knowledge/meter-disconnection-error-register.md) · [Practical examples](../../10-assessments/meter-disconnection-scenarios.md)

## Before you start

The usual source transition is CONNECTED to DISCONNECTED. There is a finding-linked exception allowing some disconnection follow-on work when the recorded state is already DISCONNECTED. That exception must not be taught as general permission to repeat any transaction. This manual records the digital workflow, not an electrical or water isolation procedure.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Open the correct accepted instruction or permitted finding-linked/field route.
2. Verify the meter, premise, instruction and source finding where present.
3. Record access; if access fails, record No Access and supporting evidence without claiming completion.
4. For completed work, select the actual disconnection level and capture its evidence.
5. Review and submit the transaction once.
6. Verify the completed outcome and DISCONNECTED state; distinguish an instruction being issued from supply actually being disconnected.

## What to check in the result

A worker reaches a locked enclosure and cannot do the disconnection. The No Access submission records the failed visit; it must not cause the learner to report successful disconnection or manually change the asset state.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

The generic validator accepts water and electricity while its disconnection levels describe circuit-breaker actions. Water-specific teaching and product rules need resolution. Physical work instructions require the utility’s authorised procedure.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/meter-disconnection-error-register.md) and [field catalogue](../../01-body-of-knowledge/meter-disconnection-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/meter-disconnection-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
