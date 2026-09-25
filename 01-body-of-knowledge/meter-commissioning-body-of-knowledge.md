# Meter Commissioning — Body of Knowledge

Module **FRM-014** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](meter-commissioning-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/meter-commissioning-user-manual.md) · [Field catalogue](meter-commissioning-field-catalogue.md) · [Error register](meter-commissioning-error-register.md) · [Practical examples](../10-assessments/meter-commissioning-scenarios.md)

## Meaning and purpose

Meter Commissioning records the checks establishing whether an installed meter is ready for service. Recording the form and passing commissioning are different outcomes.

The dedicated commissioning callable requires an existing FIELD meter and electricity or water service. Prepaid electricity has vending confirmation, final switch-on and keypad checks. Conventional electricity has the switch-on check. Water has operational/service and reading/flow checks. The confirmation of vending is not an implemented token-selling module.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

The transaction records a visit or action; the asset record presents the current view of a physical meter. A work instruction can be issued, accepted or completed independently of the meter’s physical connection status. An unsuccessful visit may produce valid evidence without the intended physical transition. Historical submissions support traceability and financial review; the future QA correction process is still undecided.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Open Commissioning for the intended FIELD meter.
2. Check service type and meter kind so the correct questions are shown.
3. Record each applicable yes/no answer honestly; supply notes when the answer is no.
4. Capture evidence for each confirmed check using its required media tag.
5. Submit and read both the transaction result and commissioning outcome.
6. For a pass verify CONNECTED on the asset; for a valid unsuccessful outcome verify that FIELD remains and arrange the outstanding work.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Vending confirmation | Prepaid electricity readiness check. | Required for prepaid electricity; yes needs vendingEvidence, no needs explanatory notes. |
| Final switch-on | Electricity service/energisation confirmation. | Applicable electricity check; yes needs finalSwitchOnEvidence. |
| Keypad issued | Prepaid keypad handover check. | Required for prepaid electricity; yes needs keypadIssuedEvidence. |
| Water operational | Water meter/service operation confirmation. | Water only; yes needs waterOperationalEvidence. |
| Water reading/flow | Confirmation of the applicable water operation check. | Water only; yes needs waterReadingEvidence. |
| Meter identity | Existing asset being commissioned. | Server requires FIELD and recognised service; cannot commission a different asset by editing the caption. |

The [field catalogue](meter-commissioning-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](meter-commissioning-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

A prepaid meter passes vending and switch-on but no keypad was issued. Record no with notes. A valid submitted form does not imply a pass; the meter remains FIELD under the observed validator.

## Exceptions, maturity and unresolved decisions

Current generic lifecycle helper also contains older commissioning logic, but the dedicated callable is the relevant route. Verify the callable/trigger pair and result refresh in the chosen environment.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-023:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/commissioning.jsx#L1) | `ireps-mobile/app/(tabs)/asts/commissioning.jsx` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-069:1](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/callable.js#L1) | `ireps-web-normalisation/functions/commissioning/callable.js` | feature/meter-normalisation-v1 / `d14992ce4ab6` | clean |
| [FS-070:1](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/helpers.js#L1) | `ireps-web-normalisation/functions/commissioning/helpers.js` | feature/meter-normalisation-v1 / `d14992ce4ab6` | clean |
| [FS-071:1](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/commissioning/trigger.js#L1) | `ireps-web-normalisation/functions/commissioning/trigger.js` | feature/meter-normalisation-v1 / `d14992ce4ab6` | clean |
| [FS-058:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L1) | `ireps-mobile/src/utils/submissionQueue.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-061:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/logic-rules/meter-normalisation-rules.md#L1) | `ireps-rules/logic-rules/meter-normalisation-rules.md` | main / `f5dc84e44c9f` | clean |
| [FS-062:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/ui-rules/field-form-dropdowns.md#L1) | `ireps-rules/ui-rules/field-form-dropdowns.md` | main / `f5dc84e44c9f` | clean |
