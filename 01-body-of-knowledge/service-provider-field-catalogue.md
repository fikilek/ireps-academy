# Service Provider Registration and Editing — Field Catalogue

Module **FRM-023** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](service-provider-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/service-provider-user-manual.md) · [Field catalogue](service-provider-field-catalogue.md) · [Error register](service-provider-error-register.md) · [Practical examples](../10-assessments/service-provider-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Trading name | Text | Operational name shown to users. | Required details follow the provider form; do not use a person’s name as a substitute organisation. | Example Field Services |
| Registered identity | Text fields | Registered name and registration number. | Keep number as text and use verified source data. | Example Field Services Ltd |
| Owner | Name/identifier | Ownership/contact fields in this provider form. | Synthetic examples only; this record is not proof of legal ownership. | Training owner |
| Manager and workbases | References | Responsibility and operating scope. | Select existing authorised identities/areas; absent manager affects signup. | Training manager |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-023-C001 — Trading Name

- **Meaning:** Operational name shown to users.
- **UI binding:** `tradingName`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateProfileField("tradingName", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-053:144](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/serviceProviders/FormServiceProvider.js#L144).

### FRM-023-C002 — Registered Name

- **Meaning:** Source control for Registered Name; interpret in the business definitions and its enclosing section.
- **UI binding:** `registeredName`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `showRegisteredName`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                updateProfileField("registeredName", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-053:154](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/serviceProviders/FormServiceProvider.js#L154).

### FRM-023-C003 — Registration Number

- **Meaning:** Source control for Registration Number; interpret in the business definitions and its enclosing section.
- **UI binding:** `registrationNumber`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `showRegistrationNumber`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                updateProfileField("registrationNumber", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-053:167](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/serviceProviders/FormServiceProvider.js#L167).

### FRM-023-C004 — Owner Name

- **Meaning:** Ownership/contact fields in this provider form.
- **UI binding:** `ownerName`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `showOwner`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateOwnerField("name", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-053:185](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/serviceProviders/FormServiceProvider.js#L185).

### FRM-023-C005 — Owner ID

- **Meaning:** Ownership/contact fields in this provider form.
- **UI binding:** `ownerId`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `showOwner`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateOwnerField("id", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-053:194](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/serviceProviders/FormServiceProvider.js#L194).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Review hierarchy and status changes with the responsible product workstream. Provider deactivation, existing users and outstanding assignments require explicit transition rules.

[Download the detailed control inventory (CSV)](service-provider-field-catalogue.csv).
