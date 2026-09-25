# Store Check-in — Field Catalogue

Module **FRM-036** · Baseline **25 September 2026** · Application: **Planned; no implemented form found**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](store-receipt-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/store-receipt-user-manual.md) · [Field catalogue](store-receipt-field-catalogue.md) · [Error register](store-receipt-error-register.md) · [Practical examples](../10-assessments/store-receipt-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Store/bin | References | Actual receiving store and storage position. | Proposed; multi-store identity must be explicit. | TRAIN-STORE-A |
| Meter identities | Serial/reference list | Physical units received. | Proposed uniqueness and scan reconciliation; preserve leading zeros. | 00123456789 |
| Condition/discrepancy | Controlled assessment plus text | Damage, short delivery or identity mismatch. | Proposed; quarantine/release decisions need owners. | One damaged enclosure |
| Receipt document | Reference | Goods-received record linked to delivery note/order. | Proposed; document terminology and approval open. | TRAIN-GRN01 |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

No literal input controls were extracted from the selected UI sources. This can mean an action/list-driven screen, a shared component boundary or a planned form; it is not proof that the workflow has no information requirements. See business definitions and source scope.

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Agree record ownership, roles, approval, financial consequences, serial timing and integration. No production transaction type, runtime error codes or button sequence is claimed.
