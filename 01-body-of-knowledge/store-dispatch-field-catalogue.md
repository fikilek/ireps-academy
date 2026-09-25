# Store Check-out — Field Catalogue

Module **FRM-037** · Baseline **25 September 2026** · Application: **Planned; no implemented form found**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](store-dispatch-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/store-dispatch-user-manual.md) · [Field catalogue](store-dispatch-field-catalogue.md) · [Error register](store-dispatch-error-register.md) · [Practical examples](../10-assessments/store-dispatch-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Store and recipient | References | Origin store and receiving provider/person. | Proposed; custody is distinct from employment role. | TRAIN-STORE-A to Training Team A |
| Meter list | References | Exact units handed over. | Proposed available-stock checks; no duplicate issue. | 00123456789 |
| Issue/job reference | Reference | Why stock leaves and where it is intended to go. | Proposed link to intended premise/work order. | TRAIN-ISS01 |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

No literal input controls were extracted from the selected UI sources. This can mean an action/list-driven screen, a shared component boundary or a planned form; it is not proof that the workflow has no information requirements. See business definitions and source scope.

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Agree state transitions, permissions, custody/financial audit, duplicate handling and evidence requirements. METER_VENDING is recognised by name but is excluded from the implemented generic lifecycle list; it returns LCT_TYPE_NOT_IMPLEMENTED there.
