# Premise Registration — User Manual

Module **FRM-010** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/premise-registration-body-of-knowledge.md) · [User Manual](premise-registration-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/premise-registration-field-catalogue.md) · [Error register](../../01-body-of-knowledge/premise-registration-error-register.md) · [Practical examples](../../10-assessments/premise-registration-scenarios.md)

## Before you start

Creation, copying a premise, editing a supported premise record and editing an unsent queued draft are different modes. Copying creates another individual unit and must not carry an existing unit identity or an unrelated Sales-row association. A premise is neither an account nor a meter.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Reach the ERF through the Normal Path or the assigned Sales Path.
2. Check the Premise Picker for the individual unit before creating another.
3. Use New premise, Copy a premise or the supported edit route deliberately; confirm ERF and path context.
4. Record property type, occupancy, address, required name/unit details, confirmed position and evidence.
5. Review and submit; distinguish a saved phone draft from server acceptance.
6. On the Sales Path verify that the intended row joins the intended premise. Open that premise before Meter Discovery or Meter Installation.

## What to check in the result

ERF TRAIN-101 has Example Court flats 1–4. Choose Premise: Flat 2 for its own service, even when its meter is in a shared outside kiosk. A Sales row allocated to Flat 1 must not be completed from Flat 2.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Current source uses a 10-second premise submit timeout, unlike the proposed universal 15-second policy. Some successful queued submissions remove the local queue item. Cross-batch picker labels can understate server locks; ambiguous multi-meter ERF fallback remains open.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/premise-registration-error-register.md) and [field catalogue](../../01-body-of-knowledge/premise-registration-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/premise-registration-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
