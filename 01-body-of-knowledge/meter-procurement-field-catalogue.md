# Meter Procurement — Field Catalogue

Module **FRM-035** · Baseline **25 September 2026** · Application: **Planned; no implemented form found**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](meter-procurement-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/meter-procurement-user-manual.md) · [Field catalogue](meter-procurement-field-catalogue.md) · [Error register](meter-procurement-error-register.md) · [Practical examples](../10-assessments/meter-procurement-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Purchase order | Reference | Authorised order context. | Proposed requirement; approval policy and numbering need agreement. | TRAIN-PO01 |
| Supplier and line items | References/quantities | What was bought and from whom. | Proposed; distinguish ordered, delivered, accepted and rejected quantities. | 10 conventional water meters |
| Commercial documents | Reference set | Invoice, payment reference and delivery note. | Proposed; actual document order follows the contract, not a fixed software assumption. | TRAIN-DN01 |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

No literal input controls were extracted from the selected UI sources. This can mean an action/list-driven screen, a shared component boundary or a planned form; it is not proof that the workflow has no information requirements. See business definitions and source scope.

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Agree record ownership, roles, approval, financial consequences, serial timing and integration. No production transaction type, runtime error codes or button sequence is claimed.
