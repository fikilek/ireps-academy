# User Invitations — Field Catalogue

Module **FRM-021** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](user-invitations-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/invite-a-user.md) · [Field catalogue](user-invitations-field-catalogue.md) · [Error register](user-invitations-error-register.md) · [Practical examples](../10-assessments/user-invitations-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Name and surname | Text | Invited person’s identity. | Required identity fields in the role-specific form. | Lebo Dlamini |
| Email | Text | New account sign-in identifier. | Valid email and server uniqueness; do not invite an existing account to bypass approval. | invited@example.org |
| Service Provider | Reference | Organisation association where required. | Choices depend on inviter and role; server must recheck permission. | Example Field Services |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-021-C001 — Name

- **Meaning:** Source control for Name; interpret in the business definitions and its enclosing section.
- **UI binding:** `name`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `setName`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-022:230](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-supervisor.js#L230).

### FRM-021-C002 — Surname

- **Meaning:** Source control for Surname; interpret in the business definitions and its enclosing section.
- **UI binding:** `surname`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `setSurname`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-022:239](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-supervisor.js#L239).

### FRM-021-C003 — Email

- **Meaning:** New account sign-in identifier.
- **UI binding:** `email`; component `TextInput`; input hint `email-address`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `setEmail`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-022:248](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-supervisor.js#L248).

### FRM-021-C004 — Email Address

- **Meaning:** New account sign-in identifier.
- **UI binding:** `values.email`; component `TextInput`; input hint `email-address`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `handleChange("email")`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-021:120](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-manager.js#L120).

### FRM-021-C005 — First Name

- **Meaning:** Source control for First Name; interpret in the business definitions and its enclosing section.
- **UI binding:** `values.name`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `handleChange("name")`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-021:131](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-manager.js#L131).

### FRM-021-C006 — Surname

- **Meaning:** Source control for Surname; interpret in the business definitions and its enclosing section.
- **UI binding:** `values.surname`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `handleChange("surname")`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-021:138](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-manager.js#L138).

### FRM-021-C007 — Email Address

- **Meaning:** New account sign-in identifier.
- **UI binding:** `values.email`; component `TextInput`; input hint `email-address`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `handleChange("email")`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-020:54](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-admin.js#L54).

### FRM-021-C008 — First Name

- **Meaning:** Source control for First Name; interpret in the business definitions and its enclosing section.
- **UI binding:** `values.name`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `handleChange("name")`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-020:65](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-admin.js#L65).

### FRM-021-C009 — Surname

- **Meaning:** Source control for Surname; interpret in the business definitions and its enclosing section.
- **UI binding:** `values.surname`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `handleChange("surname")`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-020:72](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-admin.js#L72).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Do not publish fixed-password examples from historical code. Verify the once-displayed password behaviour in the target build; invitations and re-invitations can have partial success.

[Download the detailed control inventory (CSV)](user-invitations-field-catalogue.csv).

[Inspect the extracted client validation expressions (CSV)](user-invitations-validation-evidence.csv). Expressions preserve nested conditions; extraction is not a claim that every backend check is mapped.
