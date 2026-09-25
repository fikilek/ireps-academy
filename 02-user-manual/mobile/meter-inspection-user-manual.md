# Meter Inspection — User Manual

Module **FRM-016** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/meter-inspection-body-of-knowledge.md) · [User Manual](meter-inspection-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/meter-inspection-field-catalogue.md) · [Error register](../../01-body-of-knowledge/meter-inspection-error-register.md) · [Practical examples](../../10-assessments/meter-inspection-scenarios.md)

## Before you start

Inspection is a later observation of an existing asset. It does not silently rewrite the original discovery transaction. Current source supports confirming differences and updating the current asset view; observed Connected/Disconnected status can change that view in either direction. This is distinct from the future QA rejection/correction module.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Open the accepted office instruction or a permitted field-origin inspection for the intended meter.
2. Read Existing iREPS values, then inspect the actual equipment.
3. Use SAME only when the observed value genuinely matches; capture changed values and their required proof.
4. Record access, reading/context, anomalies, any work actually performed and observed connection state.
5. Review and explicitly confirm the comparison when differences exist.
6. Choose SAVE to keep an unfinished phone draft or SUBMIT to transmit; follow-on work waits for the inspection to be sent.
7. After acknowledgement verify the inspection transaction, asset changes and any linked disconnection/removal/installation task.

## What to check in the result

The asset says Connected, but the inspector finds it disconnected. Record the observed state with evidence and confirm the comparison. The new inspection updates the current asset view while the earlier discovery remains historical evidence.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

The screen may say a timed-out inspection was NOT sent. A timeout does not prove the server received nothing; this wording is a release-review concern. Current saved-form success is retained with SUCCESS, unlike screens that remove successful queue items. QA corrections and financial effects remain open.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/meter-inspection-error-register.md) and [field catalogue](../../01-body-of-knowledge/meter-inspection-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/meter-inspection-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
