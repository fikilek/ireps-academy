# Targeted Batch Planning and Allocation — Body of Knowledge

Module **FRM-029** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](targeted-batches-body-of-knowledge.md) · [User Manual](../02-user-manual/web/targeted-batches-user-manual.md) · [Field catalogue](targeted-batches-field-catalogue.md) · [Error register](targeted-batches-error-register.md) · [Practical examples](../10-assessments/targeted-batches-scenarios.md)

## Meaning and purpose

Targeted batches group selected records into accountable fieldwork and assign them to eligible people or teams.

The web family contains upload, draft selection, confirmation, allocation targets, grouped allocation, unallocation, deletion and row take-out actions. These are separate actions with different guards. Search, sorting and map filters alter the view and do not alone mutate a batch.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

Administrative actions can affect many people or records. Their scope, actor and result need explicit verification. A filter changing what is visible is different from a mutation changing stored information. Do not infer completion from a modal closing or a row disappearing from a filtered list.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Choose the correct source population and geographic scope.
2. Review draft rows and exceptions before confirmation.
3. Confirm the intended batch content.
4. Select the eligible allocation target and inspect affected rows/team members.
5. Submit the specific allocation action and check its result.
6. Use unallocation, take-out or deletion only through the supported action with its own confirmation; verify downstream work ownership.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Source/upload | Population from which work is prepared. | Validate format and context; do not treat an uploaded row as a discovered meter. |
| Selected rows | Exact work population. | Check counts, eligibility and exceptions before confirmation. |
| Target | Responsibility for the batch. | Server scope and allocation checks apply. |
| Management action | Confirm/allocate/unallocate/delete/take out. | Each action has distinct guards and must be verified separately. |

The [field catalogue](targeted-batches-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](targeted-batches-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

A shared ERF contains three expected meter rows. Assign and later complete the appropriate row based on actual meter/premise evidence; the ERF itself is not a licence to close all three.

## Exceptions, maturity and unresolved decisions

Eight multi-meter capture permutations remain deferred in the source rule’s release plan; ambiguous Test 15 still needs an agreed association rule. Reported DEV fixes are not a published acceptance certificate.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-164:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TargetedBatchesPage.jsx#L1) | `ireps-web/src/pages/operations/TargetedBatchesPage.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-163:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TargetedBatchAllocationMapPage.jsx#L1) | `ireps-web/src/pages/operations/TargetedBatchAllocationMapPage.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-169:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/targeted-batches/TargetedBatchUploadModal.jsx#L1) | `ireps-web/src/pages/operations/targeted-batches/TargetedBatchUploadModal.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-168:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/targeted-batches/TargetedBatchUnallocateModal.jsx#L1) | `ireps-web/src/pages/operations/targeted-batches/TargetedBatchUnallocateModal.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-171:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/targeted-batches/allocation/TargetedBatchAllocationTargetPanel.jsx#L1) | `ireps-web/src/pages/operations/targeted-batches/allocation/TargetedBatchAllocationTargetPanel.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-172:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/targeted-batches/draft/TargetedBatchDraftTable.jsx#L1) | `ireps-web/src/pages/operations/targeted-batches/draft/TargetedBatchDraftTable.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-174:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/targeted-batches/rows/TargetedBatchTakeOutWindows.jsx#L1) | `ireps-web/src/pages/operations/targeted-batches/rows/TargetedBatchTakeOutWindows.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-180:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/sales/NonGpsBatchPlanningPage.jsx#L1) | `ireps-web/src/pages/sales/NonGpsBatchPlanningPage.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-181:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/sales/components/NonGpsQuickSelect.jsx#L1) | `ireps-web/src/pages/sales/components/NonGpsQuickSelect.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-182:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/sales/components/NonGpsStreetPlanning.jsx#L1) | `ireps-web/src/pages/sales/components/NonGpsStreetPlanning.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-170:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/targeted-batches/allocation/TargetedBatchAllocationRowsPanel.jsx#L1) | `ireps-web/src/pages/operations/targeted-batches/allocation/TargetedBatchAllocationRowsPanel.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-173:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/targeted-batches/rows/TargetedBatchRowsTable.jsx#L1) | `ireps-web/src/pages/operations/targeted-batches/rows/TargetedBatchRowsTable.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-120:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/acceptanceCallable.js#L1) | `ireps-web/functions/targetedBatches/acceptanceCallable.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-121:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/allocationCallable.js#L1) | `ireps-web/functions/targetedBatches/allocationCallable.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-122:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/batch-stats.js#L1) | `ireps-web/functions/targetedBatches/batch-stats.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-123:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/batch-work-guard.js#L1) | `ireps-web/functions/targetedBatches/batch-work-guard.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-124:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/batchStatsCallable.js#L1) | `ireps-web/functions/targetedBatches/batchStatsCallable.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-125:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/callables.js#L1) | `ireps-web/functions/targetedBatches/callables.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-126:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/deleteCallable.js#L1) | `ireps-web/functions/targetedBatches/deleteCallable.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-127:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/differentMeterAtErf.js#L1) | `ireps-web/functions/targetedBatches/differentMeterAtErf.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-128:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/documentFactory.js#L1) | `ireps-web/functions/targetedBatches/documentFactory.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-129:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/execution-evidence.js#L1) | `ireps-web/functions/targetedBatches/execution-evidence.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-130:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/getTargetedBatchRowsCallable.js#L1) | `ireps-web/functions/targetedBatches/getTargetedBatchRowsCallable.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-131:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/helpers.js#L1) | `ireps-web/functions/targetedBatches/helpers.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-132:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/lifecycle.js#L1) | `ireps-web/functions/targetedBatches/lifecycle.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-133:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/premiseLink.js#L1) | `ireps-web/functions/targetedBatches/premiseLink.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-134:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/recordTargetedBatchNoAccessCallable.js#L1) | `ireps-web/functions/targetedBatches/recordTargetedBatchNoAccessCallable.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-135:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/rowFollowsSales.js#L1) | `ireps-web/functions/targetedBatches/rowFollowsSales.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-136:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/rowFollowsSalesTrigger.js#L1) | `ireps-web/functions/targetedBatches/rowFollowsSalesTrigger.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-137:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/sales-batch-creation.js#L1) | `ireps-web/functions/targetedBatches/sales-batch-creation.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-138:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/sales-batch-geocoding.js#L1) | `ireps-web/functions/targetedBatches/sales-batch-geocoding.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-139:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/sales-batch-geofence.js#L1) | `ireps-web/functions/targetedBatches/sales-batch-geofence.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-140:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/sales-batch-history.js#L1) | `ireps-web/functions/targetedBatches/sales-batch-history.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-141:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/sales-batch-resolution.js#L1) | `ireps-web/functions/targetedBatches/sales-batch-resolution.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-142:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/sales-map-fence.js#L1) | `ireps-web/functions/targetedBatches/sales-map-fence.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-143:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/takeOutOfBatch.js#L1) | `ireps-web/functions/targetedBatches/takeOutOfBatch.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-144:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/takeOutOfBatchCallable.js#L1) | `ireps-web/functions/targetedBatches/takeOutOfBatchCallable.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-145:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/targetedBatches/unallocateCallable.js#L1) | `ireps-web/functions/targetedBatches/unallocateCallable.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-060:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/logic-rules/meter-capture-permutations.md#L1) | `ireps-rules/logic-rules/meter-capture-permutations.md` | main / `f5dc84e44c9f` | clean |
