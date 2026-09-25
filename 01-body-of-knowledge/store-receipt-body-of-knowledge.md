# Store Check-in — Body of Knowledge

Module **FRM-036** · Baseline **25 September 2026** · Application: **Planned; no implemented form found**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](store-receipt-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/store-receipt-user-manual.md) · [Field catalogue](store-receipt-field-catalogue.md) · [Error register](store-receipt-error-register.md) · [Practical examples](../10-assessments/store-receipt-scenarios.md)

## Meaning and purpose

Store Check-in records physical receipt of identified meters into a named store and transfers accountable custody.

Owner-directed lifecycle requirement. No implemented iREPS form for this stage was found in the inspected application source. The fields below are a discussion specification, not existing controls or storage keys.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

This stage extends the owner’s intended lifecycle beyond the currently demonstrated operational forms. Proposed records below are discussion requirements. Their identifiers, statuses and permissions need product agreement before an implementation or a production manual can be approved.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Identify the delivery and store.
2. Count and match physical serials to the delivery/transfer record.
3. Record condition and discrepancies; separate accepted stock from items held for review.
4. Record receiver, time and storage location.
5. Confirm the receipt and reconcile the inventory movement.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Store/bin | Actual receiving store and storage position. | Proposed; multi-store identity must be explicit. |
| Meter identities | Physical units received. | Proposed uniqueness and scan reconciliation; preserve leading zeros. |
| Condition/discrepancy | Damage, short delivery or identity mismatch. | Proposed; quarantine/release decisions need owners. |
| Receipt document | Goods-received record linked to delivery note/order. | Proposed; document terminology and approval open. |

The [field catalogue](store-receipt-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](store-receipt-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

A store receives one damaged meter among nine delivered. It records all nine arrivals but only the accepted population is available for issue; the damaged one remains traceable in a review holding area.

## Exceptions, maturity and unresolved decisions

Agree record ownership, roles, approval, financial consequences, serial timing and integration. No production transaction type, runtime error codes or button sequence is claimed.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

No implemented UI/backend source was found for this proposed stage. Evidence is the owner’s lifecycle briefing and the repository search scope.
