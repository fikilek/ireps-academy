# Invited Profile and Admin Confirmation — Field Catalogue

Module **FRM-005** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](invited-profile-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/invited-profile-user-manual.md) · [Field catalogue](invited-profile-field-catalogue.md) · [Error register](invited-profile-error-register.md) · [Practical examples](../10-assessments/invited-profile-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| New permanent/admin password | Secret text | Permanent replacement credential. | Use the current authentication rule; verify older screen validation against it. | [redacted] |
| Confirm password | Secret text | Password cross-check. | Must match. | [redacted] |
| Cell number | Text | Invited person’s contact number. | Phone keyboard assists entry but does not prove number ownership. | Synthetic training number |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-005-C001 — New Permanent Password

- **Meaning:** Source control for New Permanent Password; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.password`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(t) => setForm({ ...form, password: t })`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-030:121](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/complete-invited-profile.js#L121).

### FRM-005-C002 — Confirm New Password

- **Meaning:** Source control for Confirm New Password; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.confirmPassword`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(t) => setForm({ ...form, confirmPassword: t })`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-030:142](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/complete-invited-profile.js#L142).

### FRM-005-C003 — Cell Phone Number

- **Meaning:** Source control for Cell Phone Number; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.cell`; component `TextInput`; input hint `phone-pad`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(t) => setForm({ ...form, cell: t })`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-030:166](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/complete-invited-profile.js#L166).

### FRM-005-C004 — New Admin Password

- **Meaning:** Source control for New Admin Password; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.password`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(t) => setForm({ ...form, password: t })`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-031:122](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/confirm-admin.js#L122).

### FRM-005-C005 — Confirm Password

- **Meaning:** Password cross-check.
- **UI binding:** `form.confirmPassword`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(t) => setForm({ ...form, confirmPassword: t })`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-031:139](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/confirm-admin.js#L139).

### FRM-005-C006 — Admin Cell Number

- **Meaning:** Invited person’s contact number.
- **UI binding:** `form.cell`; component `TextInput`; input hint `phone-pad`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(t) => setForm({ ...form, cell: t })`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-031:160](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/confirm-admin.js#L160).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Legacy screen validation/routing may differ from the current mandatory-password design. Invitation delivery and account-change sequencing must be tested without exposing real credentials.

[Download the detailed control inventory (CSV)](invited-profile-field-catalogue.csv).
