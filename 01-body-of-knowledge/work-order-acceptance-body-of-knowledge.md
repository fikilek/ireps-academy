# My Work Orders and Acceptance — Body of Knowledge

Module **FRM-028** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](work-order-acceptance-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/work-order-acceptance-user-manual.md) · [Field catalogue](work-order-acceptance-field-catalogue.md) · [Error register](work-order-acceptance-error-register.md) · [Practical examples](../10-assessments/work-order-acceptance-scenarios.md)

## Meaning and purpose

My Work Orders is the worker’s entry to assigned lifecycle instructions and batch work, with acceptance/refusal actions.

Lifecycle instructions, BGO batches and targeted batches use different mutations. Their status words may look similar but their permissions and reversal rules differ. The Premise Picker on a Sales row is a navigation/association step, not a new meter registration form.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

Administrative actions can affect many people or records. Their scope, actor and result need explicit verification. A filter changing what is visible is different from a mutation changing stored information. Do not infer completion from a modal closing or a row disappearing from a filtered list.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Open My Work Orders in the correct workbase.
2. Inspect assignment identity, area and requested work.
3. Accept or reject the specific instruction/batch using the offered action and required reason.
4. Verify the returned workflow state.
5. Open the accepted task. On the Sales Path choose the correct row and premise; record the actual field outcome through its own form.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Work item | The instruction or batch being accepted. | Check type as well as identifier. |
| Decision | Acceptance or refusal. | Do not accept an unrelated item to bypass a lock. |
| Reason | Explanation where refusal/reversal requires it. | Follow the specific mutation’s validation. |
| Premise selection | Individual premise associated with a Sales row. | Same-batch row locks and server cross-batch checks apply. |

The [field catalogue](work-order-acceptance-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](work-order-acceptance-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

Two flats share an ERF. A worker accepts the targeted batch and chooses Flat 2 in the Premise Picker for its row. Acceptance does not justify completing every Sales row on the ERF.

## Exceptions, maturity and unresolved decisions

A wrong association has backend capabilities but may lack a phone correction interface. Cross-batch Not joined labels may be misleading; server refusal remains authoritative.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-010:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/my-workorders.js#L1) | `ireps-mobile/app/(tabs)/admin/operations/my-workorders.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-075:1](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/acceptRejectCallable.js#L1) | `ireps-web-normalisation/functions/meterLifecycle/acceptRejectCallable.js` | feature/meter-normalisation-v1 / `d14992ce4ab6` | clean |
| [FS-060:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/logic-rules/meter-capture-permutations.md#L1) | `ireps-rules/logic-rules/meter-capture-permutations.md` | main / `f5dc84e44c9f` | clean |
