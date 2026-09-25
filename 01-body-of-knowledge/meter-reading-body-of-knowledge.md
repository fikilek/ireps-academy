# Meter Reading — Body of Knowledge

Module **FRM-015** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](meter-reading-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/meter-reading-user-manual.md) · [Field catalogue](meter-reading-field-catalogue.md) · [Error register](meter-reading-error-register.md) · [Practical examples](../10-assessments/meter-reading-scenarios.md)

## Meaning and purpose

Meter Reading captures a dated field observation of a meter register and its evidence for subsequent review and billing preparation.

The owner’s module covers conventional electricity and water readings. The inspected server explicitly rejects prepaid MREAD and token readings for Sprint 1, even though phone source contains token-related branches. A read does not reconnect a meter, issue a bill or demonstrate payment. Reading differences need interval, units and exception context before they become usable consumption.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

The transaction records a visit or action; the asset record presents the current view of a physical meter. A work instruction can be issued, accepted or completed independently of the meter’s physical connection status. An unsuccessful visit may produce valid evidence without the intended physical transition. Historical submissions support traceability and financial review; the future QA correction process is still undecided.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Open the assigned or permitted reading task for the correct conventional meter.
2. Confirm the premise, meter serial, service and instruction.
3. Record access; if access or a usable reading is unavailable, use the appropriate reason with evidence.
4. Read the actual register, record capture time and GPS and take the required photograph.
5. Review a reading lower than the previous one; record the available exception reason rather than changing the value to make it look plausible.
6. Submit, verify the transaction and current reading information, and let the authorised web workflow prepare the billing export.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Instruction | Reason for this reading visit. | Server requires a reading instruction; office context must match the accepted instruction. |
| Reading | Observed conventional register value. | Numeric when supplied; missing value needs a no-reading reason. Preserve display precision; do not assume currency. |
| Reading time | When the register was observed. | Required for a successful reading; late transmission does not change observation time. |
| Reading GPS | Device position at capture. | Known meter GPS and reading GPS required; inspected server rejects distance greater than 5 metres (or an uncomputable distance). Confirm location accuracy and release behaviour. |
| Lower-reading reason | Explains a value below the prior register reading. | Use the source options; investigate rollover/replacement/context rather than assuming negative consumption. |
| No-reading reason | Why no usable register value was captured. | Alternative to a reading; not a zero reading. |
| Evidence | Visible register or access/reading exception proof. | meterReadingEvidence for a successful read; follow No Access evidence requirements. |

The [field catalogue](meter-reading-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](meter-reading-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

Last month’s electricity reading was 12400.0 and this month’s is 12540.6 in the same verified unit. The arithmetic difference is 140.6 units; billing still requires the correct period, account, tariff and exception review. A blank display is an exception, not a zero reading.

## Exceptions, maturity and unresolved decisions

Production readiness remains open by owner direction. Do not teach prepaid token capture as accepted MREAD. Validate exact proximity threshold, units, register multipliers and export acceptance on the relevant release.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-026:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/meter-reading.js#L1) | `ireps-mobile/app/(tabs)/asts/meter-reading.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-076:1](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L1) | `ireps-web-normalisation/functions/meterLifecycle/callables.js` | feature/meter-normalisation-v1 / `d14992ce4ab6` | clean |
| [FS-077:1](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L1) | `ireps-web-normalisation/functions/meterLifecycle/helpers.js` | feature/meter-normalisation-v1 / `d14992ce4ab6` | clean |
| [FS-058:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L1) | `ireps-mobile/src/utils/submissionQueue.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-061:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/logic-rules/meter-normalisation-rules.md#L1) | `ireps-rules/logic-rules/meter-normalisation-rules.md` | main / `f5dc84e44c9f` | clean |
| [FS-062:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/ui-rules/field-form-dropdowns.md#L1) | `ireps-rules/ui-rules/field-form-dropdowns.md` | main / `f5dc84e44c9f` | clean |
