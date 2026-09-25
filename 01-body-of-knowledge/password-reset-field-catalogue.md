# Password Reset — Field Catalogue

Module **FRM-003** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](password-reset-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/password-reset.md) · [Field catalogue](password-reset-field-catalogue.md) · [Error register](password-reset-error-register.md) · [Practical examples](../10-assessments/password-reset-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Email | Text | Destination associated with the sign-in account. | Valid email required; acknowledgement does not reveal account existence. | worker@example.org |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-003-C001 — you@example.com

- **Meaning:** Source control for you@example.com; interpret in the business definitions and its enclosing section.
- **UI binding:** `email`; component `input`; input hint `email`.
- **Visibility/prerequisites:** `conditional branch: step === "confirm"`.
- **Requirement/options:** `true`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => setEmail(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-156:98](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/PasswordResetPage.jsx#L98).

### FRM-003-C002 — Email address

- **Meaning:** Destination associated with the sign-in account.
- **UI binding:** `values.email`; component `TextInput`; input hint `email-address`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!isLoading`.
- **Change handling:** `handleChange("email")`.
- **Validation:** `string()<br>    .email("That does not look like an email address")<br>    .required("Email is required")<br>string()<br>    .email("That does not look like an email address")`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-006:149](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(auth)/signin.jsx#L149).

### FRM-003-C003 — Password

- **Meaning:** Source control for Password; interpret in the business definitions and its enclosing section.
- **UI binding:** `values.password`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!isLoading`.
- **Change handling:** `handleChange("password")`.
- **Validation:** `string().required("Password is required")`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-006:171](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(auth)/signin.jsx#L171).

### FRM-003-C004 — Email address

- **Meaning:** Destination associated with the sign-in account.
- **UI binding:** `values.email`; component `TextInput`; input hint `email-address`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!busy`.
- **Change handling:** `handleChange("email")`.
- **Validation:** `string()<br>    .email("That does not look like an email address")<br>    .required("Email is required")<br>string()<br>    .email("That does not look like an email address")`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-001:129](https://github.com/fikilek/ireps-mobile/blob/7bc9884325ff3db9bfe4493062f2450d8a7c83c0/app/(auth)/pwdReset.jsx#L129).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

The hosted link expiry and provider error conditions require release testing. Never promise delivery time or expose whether another person has an account. The primary mobile tree links to /pwdReset but that screen is absent there; it exists in the mobile-auth worktree. The feature must be integrated and verified before the primary mobile guide can be treated as executable.

[Download the detailed control inventory (CSV)](password-reset-field-catalogue.csv).

[Inspect the extracted client validation expressions (CSV)](password-reset-validation-evidence.csv). Expressions preserve nested conditions; extraction is not a claim that every backend check is mapped.
