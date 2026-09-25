# Meter Vending — Body of Knowledge

Module **FRM-040** · Baseline **25 September 2026** · Application: **Planned; no implemented form found**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](meter-vending-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/meter-vending-user-manual.md) · [Field catalogue](meter-vending-field-catalogue.md) · [Error register](meter-vending-error-register.md) · [Practical examples](../10-assessments/meter-vending-scenarios.md)

## Meaning and purpose

Meter Vending will record a prepaid purchase and its transaction outcome against the correct meter and customer context.

This is an owner-directed future module. The source inventory did not establish an implemented capture form for this stage. Teaching focuses on business meaning, evidence and design questions, not invented app steps.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

This stage extends the owner’s intended lifecycle beyond the currently demonstrated operational forms. Proposed records below are discussion requirements. Their identifiers, statuses and permissions need product agreement before an implementation or a production manual can be approved.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Define the meter/account identity and eligible prepaid context.
2. Record the proposed purchase and pricing/integration inputs under approved rules.
3. Submit through a future duplicate-safe vending service.
4. Separate payment acceptance, token generation and token delivery outcomes.
5. Reconcile uncertain results before retrying; preserve reversals and audit history.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Meter/account | Destination of the prepaid purchase. | Proposed; validate eligibility and identity. |
| Purchase/payment | Customer purchase and financial transaction. | Proposed; currency, tariff, tax and payment integration are not defined here. |
| Vending result | Token-generation and delivery outcome. | Proposed; no real token or runtime schema exists in this package. |

The [field catalogue](meter-vending-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](meter-vending-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

Payment succeeds but the token response times out. A future design must query/reconcile that purchase rather than charging again or generating a duplicate transaction.

## Exceptions, maturity and unresolved decisions

Agree state transitions, permissions, custody/financial audit, duplicate handling and evidence requirements. METER_VENDING is recognised by name but is excluded from the implemented generic lifecycle list; it returns LCT_TYPE_NOT_IMPLEMENTED there.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-077:1](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/helpers.js#L1) | `ireps-web-normalisation/functions/meterLifecycle/helpers.js` | feature/meter-normalisation-v1 / `d14992ce4ab6` | clean |
| [FS-076:1](https://github.com/fikilek/ireps-web/blob/d14992ce4ab608e7688259b33ac4c3a842bce02d/functions/meterLifecycle/callables.js#L1) | `ireps-web-normalisation/functions/meterLifecycle/callables.js` | feature/meter-normalisation-v1 / `d14992ce4ab6` | clean |
