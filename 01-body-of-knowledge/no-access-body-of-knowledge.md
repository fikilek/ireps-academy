# No Access — Body of Knowledge

Module **FRM-020** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](no-access-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/no-access-user-manual.md) · [Field catalogue](no-access-field-catalogue.md) · [Error register](no-access-error-register.md) · [Practical examples](../10-assessments/no-access-scenarios.md)

## Meaning and purpose

No Access records that a worker could not reach or inspect the required equipment or premise for the intended task.

No Access is shared across registration and lifecycle capture and also has a targeted-batch visit route. It is an outcome of an attempted visit, not a meter state or evidence that an installation, reading, removal or disconnection succeeded. Lack of access and an unreadable display are different facts.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

The transaction records a visit or action; the asset record presents the current view of a physical meter. A work instruction can be issued, accepted or completed independently of the meter’s physical connection status. An unsuccessful visit may produce valid evidence without the intended physical transition. Historical submissions support traceability and financial review; the future QA correction process is still undecided.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Identify the intended task, premise/meter or targeted-batch row.
2. Select the No Access outcome in that workflow.
3. Choose the actual reason and provide Other details when required.
4. Capture the required contextual evidence without inventing a meter serial or register value.
5. Review the result and submit through the parent workflow.
6. Verify the visit/transaction result and the work-order follow-up; do not assume the asset state changed.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Has access | Whether the worker can reach the task’s subject. | No changes which task-specific fields apply. |
| Reason | Observed obstacle to access. | Use complete reason; Other requires explanatory text where implemented. |
| Evidence | Context for the failed access attempt. | noAccessPhoto appears in lifecycle validators. |
| Work context | Task or batch row to which the failed visit belongs. | Do not close an unrelated row or meter task. |

The [field catalogue](no-access-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](no-access-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

The display is blank but the meter is reachable: use the form’s no-reading reason. A locked gate preventing access is No Access. Neither should be represented by a reading of zero.

## Exceptions, maturity and unresolved decisions

Reason lists and evidence rules must be checked per workflow. Row completion and reallocation after No Access are workflow-specific; a generic automatic revisit policy is not approved.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-037:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/IrepsNoAccessSection.js#L1) | `ireps-mobile/components/forms/IrepsNoAccessSection.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-011:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/targeted-batch-no-access.js#L1) | `ireps-mobile/app/(tabs)/admin/operations/targeted-batch-no-access.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-077:1](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L1) | `ireps-web-normalisation/functions/meterLifecycle/helpers.js` | feature/meter-normalisation-v1 / `d14992ce4ab6` | clean |
| [FS-046:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/meters/noAccessReasons.js#L1) | `ireps-mobile/src/features/meters/noAccessReasons.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
