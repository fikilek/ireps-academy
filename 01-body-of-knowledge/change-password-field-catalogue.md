# Change Password — Field Catalogue

Module **FRM-004** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](change-password-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/change-password.md) · [Field catalogue](change-password-field-catalogue.md) · [Error register](change-password-error-register.md) · [Practical examples](../10-assessments/change-password-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| New password | Secret text | Replacement credential. | At least 8 characters under AU-R001; current session may need fresh sign-in. | [redacted] |
| Confirm password | Secret text | Typing check. | Must equal the new password. | [redacted] |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-004-C001 — Enter new password

- **Meaning:** Replacement credential.
- **UI binding:** `newPassword`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!isSaving`.
- **Change handling:** `setNewPassword`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-029:187](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/change-password.js#L187).

### FRM-004-C002 — Confirm new password

- **Meaning:** Replacement credential.
- **UI binding:** `confirmPassword`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!isSaving`.
- **Change handling:** `setConfirmPassword`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-029:213](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/change-password.js#L213).

### FRM-004-C003 — `At least ${PASSWORD_MIN_LENGTH} characters`

- **Meaning:** Source control for `At least ${PASSWORD_MIN_LENGTH} characters`; interpret in the business definitions and its enclosing section.
- **UI binding:** `password`; component `input`; input hint `password`.
- **Visibility/prerequisites:** `conditional branch: step === "confirm"`.
- **Requirement/options:** `true`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => setPassword(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-154:153](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/ChangePasswordPage.jsx#L153).

### FRM-004-C004 — Type it again

- **Meaning:** Source control for Type it again; interpret in the business definitions and its enclosing section.
- **UI binding:** `confirmPassword`; component `input`; input hint `password`.
- **Visibility/prerequisites:** `conditional branch: step === "confirm"`.
- **Requirement/options:** `true`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => setConfirmPassword(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-154:166](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/ChangePasswordPage.jsx#L166).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

The rule records no voluntary signed-in password-change route at present. The primary select-workbase screen still clears mustChangePassword: this conflicts with the rule that only an actual password change clears it. Flag for engineering review; Academy does not patch it.

[Download the detailed control inventory (CSV)](change-password-field-catalogue.csv).
