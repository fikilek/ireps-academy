# Lifecycle Instruction Creation — Body of Knowledge

Module **FRM-026** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](lifecycle-instructions-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/lifecycle-instructions-user-manual.md) · [Field catalogue](lifecycle-instructions-field-catalogue.md) · [Error register](lifecycle-instructions-error-register.md) · [Practical examples](../10-assessments/lifecycle-instructions-scenarios.md)

## Meaning and purpose

A lifecycle instruction requests a specific action on an existing meter and assigns responsibility before execution.

Inspection, disconnection, reconnection, removal and meter reading have office-origin instruction types. Issuing the instruction changes the work state, not the physical meter state. The assigned actor must accept the instruction before the office-origin execution path can complete it.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

Administrative actions can affect many people or records. Their scope, actor and result need explicit verification. A filter changing what is visible is different from a mutation changing stored information. Do not infer completion from a modal closing or a row disappearing from a filtered list.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Choose the meter and task type in TRN Origin.
2. Check meter eligibility and the intended premise.
3. Select the shared instruction and add relevant notes.
4. Choose the permitted target user/team and review the assignment.
5. Issue once, verify ISSUED, and monitor acceptance through work-order management.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Transaction type | Action requested for the meter. | Only supported office instruction types; vending is not one of them. |
| Instruction | The actual requested work. | Local shared lists under UI-R003; Other handling follows source. |
| Notes | Additional factual instruction context. | Do not replace a required controlled instruction with notes. |
| Target | Assigned eligible user/team. | Assignment validation and organisational scope apply. |
| Meter/premise | Subject of the requested work. | Existing records and eligible state required. |

The [field catalogue](lifecycle-instructions-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](lifecycle-instructions-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

Issuing a disconnection instruction leaves the meter connected until an accepted execution reports a completed disconnection. An office dashboard must not equate ISSUED with DISCONNECTED.

## Exceptions, maturity and unresolved decisions

Role inheritance remains open. Field-origin exceptions have separate checks and do not make office acceptance optional for an office-issued instruction.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-013:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/trn-origin.js#L1) | `ireps-mobile/app/(tabs)/admin/operations/trn-origin.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-078:1](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/instructionCallable.js#L1) | `ireps-web-normalisation/functions/meterLifecycle/instructionCallable.js` | feature/meter-normalisation-v1 / `d14992ce4ab6` | clean |
| [FS-077:1](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L1) | `ireps-web-normalisation/functions/meterLifecycle/helpers.js` | feature/meter-normalisation-v1 / `d14992ce4ab6` | clean |
| [FS-061:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/logic-rules/meter-normalisation-rules.md#L1) | `ireps-rules/logic-rules/meter-normalisation-rules.md` | main / `f5dc84e44c9f` | clean |
| [FS-062:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/ui-rules/field-form-dropdowns.md#L1) | `ireps-rules/ui-rules/field-form-dropdowns.md` | main / `f5dc84e44c9f` | clean |
