# Premise Account Data — Body of Knowledge

Module **FRM-011** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](premise-account-data-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/premise-account-data-user-manual.md) · [Field catalogue](premise-account-data-field-catalogue.md) · [Error register](premise-account-data-error-register.md) · [Practical examples](../10-assessments/premise-account-data-scenarios.md)

## Meaning and purpose

Premise Account Data captures the municipal account association and owner/occupant information used for data cleansing.

One premise may need several account references. The owner may be a natural or juristic person; the occupant may be the owner or someone else. These records do not establish legal ownership, a billing invoice or payment.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

An ERF supplies land context; an individual premise identifies the served unit; accounts identify billing relationships; meters identify equipment. A shared kiosk can contain meters for different premises. Never infer the served unit solely from proximity to the meter or a shared address.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Open Account Data for the verified premise.
2. Inspect existing account information before starting a new capture.
3. Add account numbers without duplicates and select owner type.
4. Capture the corresponding owner name and contact fields; describe the occupant separately when appropriate.
5. Attach requested evidence, review the association and submit.
6. Confirm server acknowledgement or inspect the Data Cleansing local queue; a saved queue item is not a completed server update.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Accounts | Municipal account numbers associated with the premise. | At least one; trim values and reject duplicates; preserve leading zeros. |
| Owner type | Determines which owner identity fields apply. | NATURAL_PERSON or JURISTIC_PERSON. |
| Natural person | Owner name, surname and optional identity data supported by the form. | Name and surname required in this branch; do not fabricate an ID. |
| Juristic person | Registered name, registration number and trading name. | Registered name required; other requirements must follow the inspected schema. |
| Contacts | Phone, WhatsApp and email for the represented person. | Treat these as contact data, not authentication credentials. |
| Occupant is owner | Whether the occupant and owner represent the same person. | Conditional occupant section; do not overwrite owner facts to record a tenant. |
| Evidence | Supporting account/premise evidence. | Record only needed information; synthetic data in Academy examples. |

The [field catalogue](premise-account-data-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](premise-account-data-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

A company owns Unit 03B and a person occupies it. Record the company under juristic owner and the person under occupant; do not put the tenant’s name in the registered-company field.

## Exceptions, maturity and unresolved decisions

Blank-to-NAv transformations exist in source. Unknown, not applicable and unavailable need precise interpretation rather than guessed values. A network-unavailable submit can enter a separate account-data queue.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-047:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L1) | `ireps-mobile/src/features/premises/FormAccountData.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-072:1](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/dataCleansing/callables.js#L1) | `ireps-web-normalisation/functions/dataCleansing/callables.js` | feature/meter-normalisation-v1 / `d14992ce4ab6` | clean |
| [FS-056:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/utils/accountDataSubmissionQueue.js#L1) | `ireps-mobile/src/utils/accountDataSubmissionQueue.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
