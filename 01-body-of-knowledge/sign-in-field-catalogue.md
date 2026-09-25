# Sign In — Field Catalogue

Module **FRM-001** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](sign-in-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/signin.md) · [Field catalogue](sign-in-field-catalogue.md) · [Error register](sign-in-error-register.md) · [Practical examples](../10-assessments/sign-in-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Email | Text | Account identifier; use the sign-in email, not a separately edited contact address. | Required; valid email syntax; rule normalises whitespace/case. | worker@example.org |
| Password | Secret text | Authenticates the account; never include in a training screenshot or support report. | Required; entered by the person. Eight-character creation rule is not an instruction to alter an existing password. | [redacted] |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-001-C001 — Email address

- **Meaning:** Account identifier; use the sign-in email, not a separately edited contact address.
- **UI binding:** `values.email`; component `TextInput`; input hint `email-address`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!isLoading`.
- **Change handling:** `handleChange("email")`.
- **Validation:** `string()<br>    .email("That does not look like an email address")<br>    .required("Email is required")<br>string()<br>    .email("That does not look like an email address")`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-006:149](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(auth)/signin.jsx#L149).

### FRM-001-C002 — Password

- **Meaning:** Authenticates the account; never include in a training screenshot or support report.
- **UI binding:** `values.password`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!isLoading`.
- **Change handling:** `handleChange("password")`.
- **Validation:** `string().required("Password is required")`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-006:171](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(auth)/signin.jsx#L171).

### FRM-001-C003 — you@example.com

- **Meaning:** Source control for you@example.com; interpret in the business definitions and its enclosing section.
- **UI binding:** `email`; component `input`; input hint `email`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `true`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => setEmail(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-155:79](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/LoginPage.jsx#L79).

### FRM-001-C004 — Enter your password

- **Meaning:** Authenticates the account; never include in a training screenshot or support report.
- **UI binding:** `password`; component `input`; input hint `password`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `true`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => setPassword(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-155:92](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/LoginPage.jsx#L92).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Verify the actual post-login route on each release. A successful Firebase sign-in followed by a missing user record is a partial result. Do not describe it as an incorrect password.

[Download the detailed control inventory (CSV)](sign-in-field-catalogue.csv).

[Inspect the extracted client validation expressions (CSV)](sign-in-validation-evidence.csv). Expressions preserve nested conditions; extraction is not a claim that every backend check is mapped.
