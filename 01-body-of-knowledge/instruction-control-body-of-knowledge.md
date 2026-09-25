# Lifecycle Instruction Control — Body of Knowledge

Module **FRM-027** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](instruction-control-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/instruction-control-user-manual.md) · [Field catalogue](instruction-control-field-catalogue.md) · [Error register](instruction-control-error-register.md) · [Practical examples](../10-assessments/instruction-control-scenarios.md)

## Meaning and purpose

Instruction Control manages an existing lifecycle work instruction, including reassignment and cancellation where permitted.

Work state and meter state must remain separate. Reassigning an instruction changes responsibility; it does not perform the physical job or remove its history.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

Administrative actions can affect many people or records. Their scope, actor and result need explicit verification. A filter changing what is visible is different from a mutation changing stored information. Do not infer completion from a modal closing or a row disappearing from a filtered list.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Find the instruction and inspect its current workflow state.
2. Choose a supported action and check whether it is still executable.
3. For reassignment select the new eligible target and provide the reason.
4. Review and confirm the action.
5. Verify the new instruction state and ownership, then notify through the organisation’s normal process.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Instruction | Existing lifecycle transaction being managed. | Must be in a state that permits the action. |
| Action | Reassign/cancel or other supported management action. | Server enforces transitions; rejected/cancelled instructions cannot execute. |
| Target and reason | New responsibility and explanation. | Reason required where the source requires it; select eligible target. |

The [field catalogue](instruction-control-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](instruction-control-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

An unexecuted job is reassigned from Team A to Team B. The asset’s CONNECTED state stays unchanged, and the instruction records the management event.

## Exceptions, maturity and unresolved decisions

Confirm concurrency and the handling of an offline execution submitted after reassignment. Do not silently discard either party’s evidence.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-008:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/dashboard/control.js#L1) | `ireps-mobile/app/(tabs)/admin/operations/dashboard/control.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-079:1](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/manageInstructionCallable.js#L1) | `ireps-web-normalisation/functions/meterLifecycle/manageInstructionCallable.js` | feature/meter-normalisation-v1 / `d14992ce4ab6` | clean |
