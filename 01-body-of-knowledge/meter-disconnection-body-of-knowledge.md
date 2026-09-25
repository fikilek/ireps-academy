# Meter Disconnection — Body of Knowledge

Module **FRM-017** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](meter-disconnection-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/meter-disconnection-user-manual.md) · [Field catalogue](meter-disconnection-field-catalogue.md) · [Error register](meter-disconnection-error-register.md) · [Practical examples](../10-assessments/meter-disconnection-scenarios.md)

## Meaning and purpose

Meter Disconnection records an authorised interruption of supply to an existing meter and the evidence of the completed action.

The usual source transition is CONNECTED to DISCONNECTED. There is a finding-linked exception allowing some disconnection follow-on work when the recorded state is already DISCONNECTED. That exception must not be taught as general permission to repeat any transaction. This manual records the digital workflow, not an electrical or water isolation procedure.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

The transaction records a visit or action; the asset record presents the current view of a physical meter. A work instruction can be issued, accepted or completed independently of the meter’s physical connection status. An unsuccessful visit may produce valid evidence without the intended physical transition. Historical submissions support traceability and financial review; the future QA correction process is still undecided.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Open the correct accepted instruction or permitted finding-linked/field route.
2. Verify the meter, premise, instruction and source finding where present.
3. Record access; if access fails, record No Access and supporting evidence without claiming completion.
4. For completed work, select the actual disconnection level and capture its evidence.
5. Review and submit the transaction once.
6. Verify the completed outcome and DISCONNECTED state; distinguish an instruction being issued from supply actually being disconnected.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Instruction | The requested disconnection work. | Required; current local instruction list applies. |
| Access | Whether the meter could be reached for this work. | No requires the appropriate reason and noAccessPhoto. |
| Disconnection level | What level of disconnection was actually carried out. | Server validates one of three source codes; service-specific applicability needs review. |
| Level evidence | Proof corresponding to the recorded action. | disconnectionLevelEvidence is the current tag; older draft tag also appears in helper. |
| Origin | Links execution to instruction or prior finding. | Must remain consistent with the authorised source and meter. |

The [field catalogue](meter-disconnection-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](meter-disconnection-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

A worker reaches a locked enclosure and cannot do the disconnection. The No Access submission records the failed visit; it must not cause the learner to report successful disconnection or manually change the asset state.

## Exceptions, maturity and unresolved decisions

The generic validator accepts water and electricity while its disconnection levels describe circuit-breaker actions. Water-specific teaching and product rules need resolution. Physical work instructions require the utility’s authorised procedure.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-024:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/disconnection.jsx#L1) | `ireps-mobile/app/(tabs)/asts/disconnection.jsx` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-076:1](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L1) | `ireps-web-normalisation/functions/meterLifecycle/callables.js` | feature/meter-normalisation-v1 / `d14992ce4ab6` | clean |
| [FS-077:1](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L1) | `ireps-web-normalisation/functions/meterLifecycle/helpers.js` | feature/meter-normalisation-v1 / `d14992ce4ab6` | clean |
| [FS-058:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L1) | `ireps-mobile/src/utils/submissionQueue.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-061:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/logic-rules/meter-normalisation-rules.md#L1) | `ireps-rules/logic-rules/meter-normalisation-rules.md` | main / `f5dc84e44c9f` | clean |
| [FS-062:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/ui-rules/field-form-dropdowns.md#L1) | `ireps-rules/ui-rules/field-form-dropdowns.md` | main / `f5dc84e44c9f` | clean |
