# Workbase Selection and Account Settings — Field Catalogue

Module **FRM-008** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](workbase-selection-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/workbase-selection-user-manual.md) · [Field catalogue](workbase-selection-field-catalogue.md) · [Error register](workbase-selection-error-register.md) · [Practical examples](../10-assessments/workbase-selection-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Workbase | Reference | Assigned operational area selected as active. | Use an offered authorised reference; do not infer access from a place name. | Training Workbase A |
| Profile/contact values | Text | User profile details supported by the settings variant. | Inspect the per-control evidence; sign-in email must use the dedicated account flow. | Synthetic details |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-008-C001 — `Enter ${label}`

- **Meaning:** Source control for `Enter ${label}`; interpret in the business definitions and its enclosing section.
- **UI binding:** `value`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `conditional branch: isEditing`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `onChangeText`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-018:223](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/user/user-settings.js#L223).

### FRM-008-C002 — selectedWorkbaseId

- **Meaning:** Assigned operational area selected as active.
- **UI binding:** `selectedWorkbaseId`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `saving`.
- **Change handling:** `(event) => setSelectedWorkbaseId(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-175:140](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/profile/ProfilePage.jsx#L140).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Primary select-workbase code clears mustChangePassword without changing a password, contrary to AU-R001. Keep this discrepancy visible. No blanket role inheritance is accepted.

[Download the detailed control inventory (CSV)](workbase-selection-field-catalogue.csv).
