# Meter Removal — Body of Knowledge

Module **FRM-019** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](meter-removal-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/meter-removal-user-manual.md) · [Field catalogue](meter-removal-field-catalogue.md) · [Error register](meter-removal-error-register.md) · [Practical examples](../10-assessments/meter-removal-scenarios.md)

## Meaning and purpose

Meter Removal records taking a registered physical meter out of its installation and preserves the meter’s identity, readings and evidence.

The observed transition is FIELD, CONNECTED or DISCONNECTED to REMOVED. Remove meter can end the physical job; Replace meter requires a linked installation of a different meter. Removal does not by itself prove return to a store, decommissioning approval, retirement, disposal or a customer refund.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

The transaction records a visit or action; the asset record presents the current view of a physical meter. A work instruction can be issued, accepted or completed independently of the meter’s physical connection status. An unsuccessful visit may produce valid evidence without the intended physical transition. Historical submissions support traceability and financial review; the future QA correction process is still undecided.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Open the appropriate meter and Remove meter or Replace meter instruction/context.
2. Verify the serial and served premise; capture required final reading or prepaid credit evidence before removal.
3. Record No Access if the work cannot be reached.
4. For completed work confirm meter removed and capture removal evidence; do not use a success form to describe a failed attempt.
5. Submit and verify REMOVED on the old asset.
6. If replacement is required, continue the linked Meter Installation for the new serial. Record physical custody/return through the utility’s current process until iREPS stores are defined.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Instruction | Standalone removal or replacement intention. | Current wording distinguishes Remove meter and Replace meter; retired wording must not drive new training. |
| Final reading | Conventional register observed before removal. | Reading or supported no-reading reason; required evidence when captured. |
| Remaining credit | Prepaid credit observation before removal. | Do not call it consumption or promise a refund; photo/reason requirements apply. |
| Removal confirmation | Asserts the meter was actually removed. | Source success requires confirmation and removalEvidence. |
| No-reading reason | Explains unavailable reading/credit observation. | Record actual reason; zero is not a substitute. |
| Origin/follow-on | Links the old meter’s removal to finding and replacement. | Keep old and new AST/TRN identifiers distinct. |

The [field catalogue](meter-removal-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](meter-removal-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

Old meter 00123456789 is removed and replaced by 00987654321. The old meter’s final reading remains attached to its history. A later store return references the old meter; it must not be attached to the new installation.

## Exceptions, maturity and unresolved decisions

Current removal helper retains older answer/notes shapes alongside the updated confirmation UI. Decommissioned is also a legacy state guard. A single retirement/disposal policy and a stores return form are not established.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-028:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/removal.jsx#L1) | `ireps-mobile/app/(tabs)/asts/removal.jsx` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-076:1](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L1) | `ireps-web-normalisation/functions/meterLifecycle/callables.js` | feature/meter-normalisation-v1 / `d14992ce4ab6` | clean |
| [FS-077:1](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L1) | `ireps-web-normalisation/functions/meterLifecycle/helpers.js` | feature/meter-normalisation-v1 / `d14992ce4ab6` | clean |
| [FS-058:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L1) | `ireps-mobile/src/utils/submissionQueue.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-061:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/logic-rules/meter-normalisation-rules.md#L1) | `ireps-rules/logic-rules/meter-normalisation-rules.md` | main / `f5dc84e44c9f` | clean |
| [FS-062:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/ui-rules/field-form-dropdowns.md#L1) | `ireps-rules/ui-rules/field-form-dropdowns.md` | main / `f5dc84e44c9f` | clean |
