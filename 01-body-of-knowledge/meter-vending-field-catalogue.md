# Meter Vending — Field Catalogue

Module **FRM-040** · Baseline **25 September 2026** · Application: **Planned; no implemented form found**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](meter-vending-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/meter-vending-user-manual.md) · [Field catalogue](meter-vending-field-catalogue.md) · [Error register](meter-vending-error-register.md) · [Practical examples](../10-assessments/meter-vending-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Meter/account | References | Destination of the prepaid purchase. | Proposed; validate eligibility and identity. | Training prepaid meter |
| Purchase/payment | Amount and references | Customer purchase and financial transaction. | Proposed; currency, tariff, tax and payment integration are not defined here. | Synthetic amount |
| Vending result | Reference/status | Token-generation and delivery outcome. | Proposed; no real token or runtime schema exists in this package. | Synthetic transaction reference |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

No literal input controls were extracted from the selected UI sources. This can mean an action/list-driven screen, a shared component boundary or a planned form; it is not proof that the workflow has no information requirements. See business definitions and source scope.

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Agree state transitions, permissions, custody/financial audit, duplicate handling and evidence requirements. METER_VENDING is recognised by name but is excluded from the implemented generic lifecycle list; it returns LCT_TYPE_NOT_IMPLEMENTED there.
