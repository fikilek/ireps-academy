# Sign Up — Field Catalogue

Module **FRM-002** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](sign-up-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/signup.md) · [Field catalogue](sign-up-field-catalogue.md) · [Error register](sign-up-error-register.md) · [Practical examples](../10-assessments/sign-up-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Surname | Text | Person’s surname. | Required by signup rule. | Dlamini |
| Name | Text | Person’s given name. | Required by signup rule. | Lebo |
| Email | Text | Unique sign-in identity. | Valid email; server uniqueness check; existing account uses Sign In or reset. | lebo@example.org |
| Password | Secret text | Person’s chosen password. | At least 8 characters in the current rule; no mandatory composition beyond that rule. | [redacted] |
| Confirm Password | Secret text | Typing cross-check, not a second credential. | Must match the password. | [redacted] |
| Service Provider | Reference | Employer/provider association selected from active providers. | Server rechecks active status and responsible manager; list loading may fail. | Example Field Services |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-002-C001 — Surname

- **Meaning:** Person’s surname.
- **UI binding:** `values.surname`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!isLoading`.
- **Change handling:** `handleChange("surname")`.
- **Validation:** `string().trim().required("Surname is required")`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-007:158](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(auth)/signup.jsx#L158).

### FRM-002-C002 — Name

- **Meaning:** Person’s given name.
- **UI binding:** `values.name`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!isLoading`.
- **Change handling:** `handleChange("name")`.
- **Validation:** `string().trim().required("Name is required")`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-007:179](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(auth)/signup.jsx#L179).

### FRM-002-C003 — Email

- **Meaning:** Unique sign-in identity.
- **UI binding:** `values.email`; component `TextInput`; input hint `email-address`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!isLoading`.
- **Change handling:** `handleChange("email")`.
- **Validation:** `string().email("Invalid email address").required("Email is required")<br>string().email("Invalid email address")`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-007:196](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(auth)/signup.jsx#L196).

### FRM-002-C004 — Password

- **Meaning:** Person’s chosen password.
- **UI binding:** `values.password`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!isLoading`.
- **Change handling:** `handleChange("password")`.
- **Validation:** `string()<br>    .min(8, "Password must be at least 8 characters")<br>    .required("Password is required")<br>string()<br>    .min(8, "Password must be at least 8 characters")`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-007:215](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(auth)/signup.jsx#L215).

### FRM-002-C005 — Confirm Password

- **Meaning:** Person’s chosen password.
- **UI binding:** `values.confirmPassword`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!isLoading`.
- **Change handling:** `handleChange("confirmPassword")`.
- **Validation:** `string()<br>    .oneOf([ref("password")], "Passwords do not match")<br>    .required("Confirm your password")<br>string()<br>    .oneOf([ref("password")], "Passwords do not match")`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-007:240](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(auth)/signup.jsx#L240).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Confirm backend/UI parity on the target release and whether account creation succeeded before retrying a network failure. Do not promise an invitation email for self-signup.

[Download the detailed control inventory (CSV)](sign-up-field-catalogue.csv).

[Inspect the extracted client validation expressions (CSV)](sign-up-validation-evidence.csv). Expressions preserve nested conditions; extraction is not a claim that every backend check is mapped.
