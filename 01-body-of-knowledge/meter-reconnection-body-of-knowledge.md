# Meter Reconnection — Body of Knowledge

Module **FRM-018** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](meter-reconnection-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/meter-reconnection-user-manual.md) · [Field catalogue](meter-reconnection-field-catalogue.md) · [Error register](meter-reconnection-error-register.md) · [Practical examples](../10-assessments/meter-reconnection-scenarios.md)

## Meaning and purpose

Meter Reconnection records restoration of supply to an existing disconnected meter, together with confirmation and proof.

The observed server transition is DISCONNECTED to CONNECTED after the required instruction, positive supply-reconnected confirmation and evidence. The instruction label is Reconnect meter. Reconnection is not registration, commissioning of a new meter, or proof that an account balance was settled.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

The transaction records a visit or action; the asset record presents the current view of a physical meter. A work instruction can be issued, accepted or completed independently of the meter’s physical connection status. An unsuccessful visit may produce valid evidence without the intended physical transition. Historical submissions support traceability and financial review; the future QA correction process is still undecided.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Open the accepted instruction or permitted field route and verify the meter is the intended one.
2. Read Reconnect meter and its context.
3. Record access; use No Access if the work cannot be reached.
4. After authorised work, confirm supply was reconnected and capture the required proof.
5. Submit and read the server result.
6. Verify CONNECTED and the linked transaction; report a refusal or uncertain result without pretending the supply changed.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Instruction | Requested reconnection. | Required; canonical wording Reconnect meter. |
| Supply reconnected | Explicit completion confirmation. | Server requires yes for successful execution; a negative answer is not a completed reconnection. |
| Reconnection evidence | Proof of the completed reconnection. | reconnectionEvidence required for success. |
| Access and reason | Whether the work could be reached. | No Access keeps the prior asset state under the inspected helper. |

The [field catalogue](meter-reconnection-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](meter-reconnection-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

An instruction was accepted but the worker cannot access the meter. The work record can document No Access while the meter remains DISCONNECTED.

## Exceptions, maturity and unresolved decisions

Do not infer debt clearance, safety clearance or authority solely from the form’s existence. Document the utility-approved prerequisite separately when agreed.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-027:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/reconnection.jsx#L1) | `ireps-mobile/app/(tabs)/asts/reconnection.jsx` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-076:1](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L1) | `ireps-web-normalisation/functions/meterLifecycle/callables.js` | feature/meter-normalisation-v1 / `d14992ce4ab6` | clean |
| [FS-077:1](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L1) | `ireps-web-normalisation/functions/meterLifecycle/helpers.js` | feature/meter-normalisation-v1 / `d14992ce4ab6` | clean |
| [FS-058:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/submissionQueue.js#L1) | `ireps-mobile/src/utils/submissionQueue.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-061:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/logic-rules/meter-normalisation-rules.md#L1) | `ireps-rules/logic-rules/meter-normalisation-rules.md` | main / `f5dc84e44c9f` | clean |
| [FS-062:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/ui-rules/field-form-dropdowns.md#L1) | `ireps-rules/ui-rules/field-form-dropdowns.md` | main / `f5dc84e44c9f` | clean |
