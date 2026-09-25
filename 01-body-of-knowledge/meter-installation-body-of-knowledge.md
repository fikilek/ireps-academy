# Meter Installation — Body of Knowledge

Module **FRM-013** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](meter-installation-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/meter-installation-user-manual.md) · [Field catalogue](meter-installation-field-catalogue.md) · [Error register](meter-installation-error-register.md) · [Practical examples](../10-assessments/meter-installation-scenarios.md)

## Meaning and purpose

Meter Installation registers a meter as part of installing it at an identified premise. Meter Discovery registers a meter already found in the field. Both create registration evidence, but their business events differ.

Installation joins meter identity, service, premise, ERF, physical position, technical characteristics and evidence. The owner’s full lifecycle expects prior procurement and store check-out. The inspected installation callable does not establish an enforced store-dispatch prerequisite. Replacement is a linked removal of the old meter followed by registration of the new one.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

The transaction records a visit or action; the asset record presents the current view of a physical meter. A work instruction can be issued, accepted or completed independently of the meter’s physical connection status. An unsuccessful visit may produce valid evidence without the intended physical transition. Historical submissions support traceability and financial review; the future QA correction process is still undecided.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Select the correct premise and the Meter Installation route, or continue the explicitly linked replacement after a successful removal.
2. Confirm electricity or water and the new meter’s identity; do not use the removed meter’s number for its replacement.
3. Record the technical fields appropriate to the service and meter kind, location and photographs.
4. Capture the actual outcome, including No Access where supported; do not register an installation that did not happen.
5. Review the payload and any replacement origin, then submit.
6. Verify the new AST and registration transaction. The observed initial state is FIELD; carry out the separate commissioning workflow when applicable.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Meter number | Identity of the newly installed physical meter. | Current rule removes spaces, uppercases a–z, accepts A–Z and digits only; preserve leading zeros and enforce uniqueness at the server. |
| Service | Water or electricity being supplied. | Select before service-specific questions; do not infer it from a number. |
| Meter kind | Prepaid or conventional operation. | Controls credit/reading and keypad sections. |
| Manufacturer | Selected make of the installed equipment. | Installation omits Other because no companion make input exists. |
| Premise/ERF | Served unit and land context. | Must remain associated with the intended installation; position alone is insufficient. |
| Placement and GPS | Actual physical meter position. | Valid GPS and confirmation; may differ from served-premise position. |
| Infrastructure | Applicable seal, breaker, keypad and meter technical characteristics. | Use the shared component catalogue and conditional evidence rules. |
| Origin | Links replacement to its removal and original finding/instruction. | Do not manually invent an origin or close a different meter’s work. |
| Evidence | Proof of meter identity, installation and applicable infrastructure. | Photo tags and uploaded URLs must satisfy the relevant checks. |

The [field catalogue](meter-installation-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](meter-installation-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

Meter 00123456789 is removed from Flat 2 under Replace meter. Installation records new meter 00987654321 on Flat 2, with a link to the removal. The new meter starts FIELD, while the old one remains REMOVED; history is not renamed.

## Exceptions, maturity and unresolved decisions

Store custody and purchase evidence are lifecycle requirements, not current enforced installation fields. Confirm offline recovery and replacement linking on the target release. Backend and phone branches must be paired.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-042:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/meters/FormMeterIstallation.js#L1) | `ireps-mobile/src/features/meters/FormMeterIstallation.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-035:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/ElectricitySections.js#L1) | `ireps-mobile/components/forms/ElectricitySections.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-039:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/WaterSections.js#L1) | `ireps-mobile/components/forms/WaterSections.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-038:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/RemainingCreditSection.js#L1) | `ireps-mobile/components/forms/RemainingCreditSection.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-036:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/IrepsFieldCommentSection.js#L1) | `ireps-mobile/components/forms/IrepsFieldCommentSection.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-043:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/meters/WaterMeterEntry.js#L1) | `ireps-mobile/src/features/meters/WaterMeterEntry.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-073:1](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/index.js#L1) | `ireps-web-normalisation/functions/index.js` | feature/meter-normalisation-v1 / `d14992ce4ab6` | clean |
| [FS-074:1](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterInstallation/validation.js#L1) | `ireps-web-normalisation/functions/meterInstallation/validation.js` | feature/meter-normalisation-v1 / `d14992ce4ab6` | clean |
| [FS-045:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/meters/meterNumberRule.js#L1) | `ireps-mobile/src/features/meters/meterNumberRule.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-044:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/meters/formOptions.js#L1) | `ireps-mobile/src/features/meters/formOptions.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-058:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L1) | `ireps-mobile/src/utils/submissionQueue.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-061:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/logic-rules/meter-normalisation-rules.md#L1) | `ireps-rules/logic-rules/meter-normalisation-rules.md` | main / `f5dc84e44c9f` | clean |
| [FS-062:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/ui-rules/field-form-dropdowns.md#L1) | `ireps-rules/ui-rules/field-form-dropdowns.md` | main / `f5dc84e44c9f` | clean |
