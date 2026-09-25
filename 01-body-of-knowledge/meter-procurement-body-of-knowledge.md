# Meter Procurement — Body of Knowledge

Module **FRM-035** · Baseline **25 September 2026** · Application: **Planned; no implemented form found**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](meter-procurement-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/meter-procurement-user-manual.md) · [Field catalogue](meter-procurement-field-catalogue.md) · [Error register](meter-procurement-error-register.md) · [Practical examples](../10-assessments/meter-procurement-scenarios.md)

## Meaning and purpose

Procurement establishes the planned purchase and traceable acquisition of meters before operational use.

Owner-directed lifecycle requirement. No implemented iREPS form for this stage was found in the inspected application source. The fields below are a discussion specification, not existing controls or storage keys.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

This stage extends the owner’s intended lifecycle beyond the currently demonstrated operational forms. Proposed records below are discussion requirements. Their identifiers, statuses and permissions need product agreement before an implementation or a production manual can be approved.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Record the approved requirement and technical/service need.
2. Link the purchase order, supplier and agreed quantities.
3. Record invoice, payment and delivery documentation as separate events.
4. Reconcile what was ordered with what was delivered and accepted.
5. Hand the accepted meter population to store receiving with serial identities where available.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Purchase order | Authorised order context. | Proposed requirement; approval policy and numbering need agreement. |
| Supplier and line items | What was bought and from whom. | Proposed; distinguish ordered, delivered, accepted and rejected quantities. |
| Commercial documents | Invoice, payment reference and delivery note. | Proposed; actual document order follows the contract, not a fixed software assumption. |

The [field catalogue](meter-procurement-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](meter-procurement-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

Ten meters are ordered and nine arrive. Receipt records nine physical units and the discrepancy; it must not turn the order quantity into a ten-meter stock balance.

## Exceptions, maturity and unresolved decisions

Agree record ownership, roles, approval, financial consequences, serial timing and integration. No production transaction type, runtime error codes or button sequence is claimed.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

No implemented UI/backend source was found for this proposed stage. Evidence is the owner’s lifecycle briefing and the repository search scope.
