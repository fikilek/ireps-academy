# Informal ERF Capture — Body of Knowledge

Module **FRM-012** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](informal-erf-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/informal-erf-user-manual.md) · [Field catalogue](informal-erf-field-catalogue.md) · [Error register](informal-erf-error-register.md) · [Practical examples](../10-assessments/informal-erf-scenarios.md)

## Meaning and purpose

Informal ERF Capture records an operational geographic context where a usable formal ERF cannot be identified.

The drawn boundary and reason explain why the record exists. It does not establish a legal cadastral parcel or legal ownership, and a roadside meter by itself does not prove that a new ERF is necessary.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

An ERF supplies land context; an individual premise identifies the served unit; accounts identify billing relationships; meters identify equipment. A shared kiosk can contain meters for different premises. Never infer the served unit solely from proximity to the meter or a shared address.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Inspect the mapped and nearby ERFs first.
2. Choose the informal ERF route only where the operational context warrants it.
3. Draw and confirm the boundary and review its position.
4. Select the creation reason; explain Other.
5. Capture the requested evidence, review and submit.
6. Verify the returned record and subsequently register the individual premise in that context.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Boundary points | Drawn operational boundary. | At least 3 valid unique latitude/longitude points; source rounds comparison to 7 decimal places. |
| Reason | Why a usable formal ERF was not selected. | One of the listed creation reasons; Other needs text. |
| Other reason | Explanation for an unlisted reason. | Required when reason is OTHER. |
| Evidence | Context supporting the capture. | Follow the current form/controller evidence requirements. |

The [field catalogue](informal-erf-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](informal-erf-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

A meter is outside a mapped boundary but serves an already known flat. Keep the served premise association; do not automatically create an informal ERF around the kiosk.

## Exceptions, maturity and unresolved decisions

Operational geometry must not be described as cadastral proof. Confirm overlap handling, queue recovery and server validation on the intended release.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-041:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/erfs/FormInformalErf.js#L1) | `ireps-mobile/src/features/erfs/FormInformalErf.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-055:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/services/informalErfSubmissionController.js#L1) | `ireps-mobile/src/services/informalErfSubmissionController.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-089:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/informal-erfs/helpers.js#L1) | `ireps-web/functions/informal-erfs/helpers.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-090:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/informal-erfs/submitInformalErfCallable.js#L1) | `ireps-web/functions/informal-erfs/submitInformalErfCallable.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
