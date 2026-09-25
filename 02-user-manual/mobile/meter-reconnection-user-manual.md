# Meter Reconnection — User Manual

Module **FRM-018** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/meter-reconnection-body-of-knowledge.md) · [User Manual](meter-reconnection-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/meter-reconnection-field-catalogue.md) · [Error register](../../01-body-of-knowledge/meter-reconnection-error-register.md) · [Practical examples](../../10-assessments/meter-reconnection-scenarios.md)

## Before you start

The observed server transition is DISCONNECTED to CONNECTED after the required instruction, positive supply-reconnected confirmation and evidence. The instruction label is Reconnect meter. Reconnection is not registration, commissioning of a new meter, or proof that an account balance was settled.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Open the accepted instruction or permitted field route and verify the meter is the intended one.
2. Read Reconnect meter and its context.
3. Record access; use No Access if the work cannot be reached.
4. After authorised work, confirm supply was reconnected and capture the required proof.
5. Submit and read the server result.
6. Verify CONNECTED and the linked transaction; report a refusal or uncertain result without pretending the supply changed.

## What to check in the result

An instruction was accepted but the worker cannot access the meter. The work record can document No Access while the meter remains DISCONNECTED.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Do not infer debt clearance, safety clearance or authority solely from the form’s existence. Document the utility-approved prerequisite separately when agreed.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/meter-reconnection-error-register.md) and [field catalogue](../../01-body-of-knowledge/meter-reconnection-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/meter-reconnection-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
