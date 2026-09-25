# Meter Inspection — Body of Knowledge

Module **FRM-016** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](meter-inspection-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/meter-inspection-user-manual.md) · [Field catalogue](meter-inspection-field-catalogue.md) · [Error register](meter-inspection-error-register.md) · [Practical examples](../10-assessments/meter-inspection-scenarios.md)

## Meaning and purpose

Meter Inspection records the meter as found, compares it with the existing iREPS asset information and records anomalies, evidence and permitted follow-on work.

Inspection is a later observation of an existing asset. It does not silently rewrite the original discovery transaction. Current source supports confirming differences and updating the current asset view; observed Connected/Disconnected status can change that view in either direction. This is distinct from the future QA rejection/correction module.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

The transaction records a visit or action; the asset record presents the current view of a physical meter. A work instruction can be issued, accepted or completed independently of the meter’s physical connection status. An unsuccessful visit may produce valid evidence without the intended physical transition. Historical submissions support traceability and financial review; the future QA correction process is still undecided.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Open the accepted office instruction or a permitted field-origin inspection for the intended meter.
2. Read Existing iREPS values, then inspect the actual equipment.
3. Use SAME only when the observed value genuinely matches; capture changed values and their required proof.
4. Record access, reading/context, anomalies, any work actually performed and observed connection state.
5. Review and explicitly confirm the comparison when differences exist.
6. Choose SAVE to keep an unfinished phone draft or SUBMIT to transmit; follow-on work waits for the inspection to be sent.
7. After acknowledgement verify the inspection transaction, asset changes and any linked disconnection/removal/installation task.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Captured asset values | The current field observation, distinct from baseline. | Service-specific fields and confirmed comparison govern changes. |
| SAME / changed controls | Indicate whether each fact matches Existing iREPS. | SAME copies the baseline, including NAv where present; it is not evidence that an unknown fact was observed. |
| Anomalies | As-found conditions requiring attention. | Shared lists and conditional photographs apply. |
| Normalisation/action | What was actually corrected or which follow-on is required. | Do not mark a future action as already completed. |
| Observed state | Connection state found during inspection. | Current source supports Connected/Disconnected; reconcile against prior state with evidence. |
| Comparison confirmation | Acknowledgement of changed facts. | Required when detected differences need confirmation. |
| Reading and evidence | Reading or a supported reason plus relevant media. | Do not confuse inspection reading with a final billing export. |

The [field catalogue](meter-inspection-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](meter-inspection-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

The asset says Connected, but the inspector finds it disconnected. Record the observed state with evidence and confirm the comparison. The new inspection updates the current asset view while the earlier discovery remains historical evidence.

## Exceptions, maturity and unresolved decisions

The screen may say a timed-out inspection was NOT sent. A timeout does not prove the server received nothing; this wording is a release-review concern. Current saved-form success is retained with SUCCESS, unlike screens that remove successful queue items. QA corrections and financial effects remain open.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-025:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/inspection.js#L1) | `ireps-mobile/app/(tabs)/asts/inspection.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-076:1](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L1) | `ireps-web-normalisation/functions/meterLifecycle/callables.js` | feature/meter-normalisation-v1 / `d14992ce4ab6` | clean |
| [FS-077:1](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L1) | `ireps-web-normalisation/functions/meterLifecycle/helpers.js` | feature/meter-normalisation-v1 / `d14992ce4ab6` | clean |
| [FS-058:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L1) | `ireps-mobile/src/utils/submissionQueue.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-061:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/logic-rules/meter-normalisation-rules.md#L1) | `ireps-rules/logic-rules/meter-normalisation-rules.md` | main / `f5dc84e44c9f` | clean |
| [FS-062:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/ui-rules/field-form-dropdowns.md#L1) | `ireps-rules/ui-rules/field-form-dropdowns.md` | main / `f5dc84e44c9f` | clean |
