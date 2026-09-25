# Premise Registration — Body of Knowledge

Module **FRM-010** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](premise-registration-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/premise-registration-user-manual.md) · [Field catalogue](premise-registration-field-catalogue.md) · [Error register](premise-registration-error-register.md) · [Practical examples](../10-assessments/premise-registration-scenarios.md)

## Meaning and purpose

Premise Registration identifies the individual served place on an ERF. A block or complex can contain many premises; a meter’s physical position can be outside the ERF it serves.

Creation, copying a premise, editing a supported premise record and editing an unsent queued draft are different modes. Copying creates another individual unit and must not carry an existing unit identity or an unrelated Sales-row association. A premise is neither an account nor a meter.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

An ERF supplies land context; an individual premise identifies the served unit; accounts identify billing relationships; meters identify equipment. A shared kiosk can contain meters for different premises. Never infer the served unit solely from proximity to the meter or a shared address.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Reach the ERF through the Normal Path or the assigned Sales Path.
2. Check the Premise Picker for the individual unit before creating another.
3. Use New premise, Copy a premise or the supported edit route deliberately; confirm ERF and path context.
4. Record property type, occupancy, address, required name/unit details, confirmed position and evidence.
5. Review and submit; distinguish a saved phone draft from server acceptance.
6. On the Sales Path verify that the intended row joins the intended premise. Open that premise before Meter Discovery or Meter Installation.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Property Type | Kind of premises represented; names and unit requirements depend on it. | Current controlled values and repeatability rules apply; changing type reconciles dependent values. |
| Property name | Name of the block/complex or business where applicable. | Conditional; Commercial and Industrial use Business Name in current work. |
| Unit number | Individual unit, preserving leading zeros and suffixes. | Conditional on type and uniqueness/repeatability rules; copying requires checking it. |
| Property Status | Observed occupancy/status of this premise. | Required; do not substitute connection status. |
| Address | Suburb, street number, street name and type. | Required fields in the client schema; street name is formatted on input. |
| Context | Township or Suburb contextual selection. | Required; explicit yes/no switch maps to these values. |
| Position | Confirmed premise position. | Valid coordinates and location confirmation; ERF association is not inferred only from nearest point. |
| Media | Images supporting premise identification. | Client conditional photo test; use required tags and check upload acknowledgement. |

The [field catalogue](premise-registration-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](premise-registration-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

ERF TRAIN-101 has Example Court flats 1–4. Choose Premise: Flat 2 for its own service, even when its meter is in a shared outside kiosk. A Sales row allocated to Flat 1 must not be completed from Flat 2.

## Exceptions, maturity and unresolved decisions

Current source uses a 10-second premise submit timeout, unlike the proposed universal 15-second policy. Some successful queued submissions remove the local queue item. Cross-batch picker labels can understate server locks; ambiguous multi-meter ERF fallback remains open.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-048:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/formPremise.js#L1) | `ireps-mobile/src/features/premises/formPremise.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-080:1](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/registry/premiseCallable.js#L1) | `ireps-web-normalisation/functions/registry/premiseCallable.js` | feature/meter-normalisation-v1 / `d14992ce4ab6` | clean |
| [FS-049:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/premiseRepeatability.js#L1) | `ireps-mobile/src/features/premises/premiseRepeatability.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-050:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/targetedBatchPremiseContext.js#L1) | `ireps-mobile/src/features/premises/targetedBatchPremiseContext.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-057:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/premiseSubmissionQueue.js#L1) | `ireps-mobile/src/utils/premiseSubmissionQueue.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-060:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/logic-rules/meter-capture-permutations.md#L1) | `ireps-rules/logic-rules/meter-capture-permutations.md` | main / `f5dc84e44c9f` | clean |
