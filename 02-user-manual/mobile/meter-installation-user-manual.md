# Meter Installation — User Manual

Module **FRM-013** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/meter-installation-body-of-knowledge.md) · [User Manual](meter-installation-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/meter-installation-field-catalogue.md) · [Error register](../../01-body-of-knowledge/meter-installation-error-register.md) · [Practical examples](../../10-assessments/meter-installation-scenarios.md)

## Before you start

Installation joins meter identity, service, premise, ERF, physical position, technical characteristics and evidence. The owner’s full lifecycle expects prior procurement and store check-out. The inspected installation callable does not establish an enforced store-dispatch prerequisite. Replacement is a linked removal of the old meter followed by registration of the new one.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Select the correct premise and the Meter Installation route, or continue the explicitly linked replacement after a successful removal.
2. Confirm electricity or water and the new meter’s identity; do not use the removed meter’s number for its replacement.
3. Record the technical fields appropriate to the service and meter kind, location and photographs.
4. Capture the actual outcome, including No Access where supported; do not register an installation that did not happen.
5. Review the payload and any replacement origin, then submit.
6. Verify the new AST and registration transaction. The observed initial state is FIELD; carry out the separate commissioning workflow when applicable.

## What to check in the result

Meter 00123456789 is removed from Flat 2 under Replace meter. Installation records new meter 00987654321 on Flat 2, with a link to the removal. The new meter starts FIELD, while the old one remains REMOVED; history is not renamed.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Store custody and purchase evidence are lifecycle requirements, not current enforced installation fields. Confirm offline recovery and replacement linking on the target release. Backend and phone branches must be paired.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/meter-installation-error-register.md) and [field catalogue](../../01-body-of-knowledge/meter-installation-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/meter-installation-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
