# BGO Planning — Body of Knowledge

Module **FRM-031** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](bgo-planning-body-of-knowledge.md) · [User Manual](../02-user-manual/web/bgo-planning-user-manual.md) · [Field catalogue](bgo-planning-field-catalogue.md) · [Error register](bgo-planning-error-register.md) · [Practical examples](../10-assessments/bgo-planning-scenarios.md)

## Meaning and purpose

BGO planning creates and manages the batch work objects exposed by the current operational screens.

BMD and TC planning screens have create/delete actions. Preserve the actual screen labels and keep prototype or legacy variants marked; do not infer a universal batch lifecycle from their similar names.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

Administrative actions can affect many people or records. Their scope, actor and result need explicit verification. A filter changing what is visible is different from a mutation changing stored information. Do not infer completion from a modal closing or a row disappearing from a filtered list.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Select the appropriate BMD or TC planning route.
2. Review source rows, geography and target context.
3. Create the proposed work object and inspect the returned result.
4. Track acceptance through My Work Orders.
5. Use deletion only where the source permits an unaccepted object to be removed.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Source population | Records from which the BGO is created. | Check the specific BMD/TC route and source eligibility. |
| Batch context | Workbase/area and available targeting values. | Use the exact implementation variant; no invented global schema. |
| Delete action | Removal of an eligible unaccepted BGO. | Source names DeleteUnacceptedBgo; acceptance changes eligibility. |

The [field catalogue](bgo-planning-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](bgo-planning-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

An office user tries to delete work after acceptance. The relevant rule is the BGO action’s guard, not whether the row is currently visible in a filtered table.

## Exceptions, maturity and unresolved decisions

This family needs route-by-route release review. Do not treat every historical BGO screen as a current recommended workflow.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-158:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/BmdBgoPage.jsx#L1) | `ireps-web/src/pages/operations/BmdBgoPage.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-165:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TcBgoPage.jsx#L1) | `ireps-web/src/pages/operations/TcBgoPage.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-161:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L1) | `ireps-web/src/pages/operations/MdBgoRowsPage.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
