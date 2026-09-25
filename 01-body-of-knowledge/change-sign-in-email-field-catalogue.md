# Change Sign-in Email — Field Catalogue

Module **FRM-009** · Baseline **25 September 2026** · Application: **Feature-branch source; deployment unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](change-sign-in-email-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/change-sign-in-email.md) · [Field catalogue](change-sign-in-email-field-catalogue.md) · [Error register](change-sign-in-email-error-register.md) · [Practical examples](../10-assessments/change-sign-in-email-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| New email | Text | New sign-in identifier. | Valid and not already in use; own-address equality is a no-op. | new.worker@example.org |
| Current password | Secret text | Fresh authentication for own-account change. | Own-account flow only; do not request another person’s password for an office action. | [redacted] |
| Target user | Reference | Person whose identifier is being corrected. | Office permission and organisational scope are action-specific. | Synthetic UID |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-009-C001 — New email address

- **Meaning:** New sign-in identifier.
- **UI binding:** `newEmail`; component `TextInput`; input hint `email-address`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!isSendingLink`.
- **Change handling:** `setNewEmail`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-003:252](https://github.com/fikilek/ireps-mobile/blob/9a981d1882c388043bae6021a1dd33a3e758dfa8/app/(tabs)/admin/user/user-settings.js#L252).

### FRM-009-C002 — Your password

- **Meaning:** Source control for Your password; interpret in the business definitions and its enclosing section.
- **UI binding:** `currentPassword`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!isSendingLink`.
- **Change handling:** `setCurrentPassword`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-003:265](https://github.com/fikilek/ireps-mobile/blob/9a981d1882c388043bae6021a1dd33a3e758dfa8/app/(tabs)/admin/user/user-settings.js#L265).

### FRM-009-C003 — `Enter ${label}`

- **Meaning:** Source control for `Enter ${label}`; interpret in the business definitions and its enclosing section.
- **UI binding:** `value`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `conditional branch: isEditing`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `onChangeText`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-003:367](https://github.com/fikilek/ireps-mobile/blob/9a981d1882c388043bae6021a1dd33a3e758dfa8/app/(tabs)/admin/user/user-settings.js#L367).

### FRM-009-C004 — newRole

- **Meaning:** Source control for newRole; interpret in the business definitions and its enclosing section.
- **UI binding:** `newRole`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `isSaving &#124;&#124; feedback?.type === "success"`.
- **Change handling:** `(event) => {<br>                setNewRole(event.target.value);<br>                setFeedback(null);<br>              }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-067:470](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/src/pages/users/UsersPage.jsx#L470).

### FRM-009-C005 — newStatus

- **Meaning:** Source control for newStatus; interpret in the business definitions and its enclosing section.
- **UI binding:** `newStatus`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => setNewStatus(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-067:568](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/src/pages/users/UsersPage.jsx#L568).

### FRM-009-C006 — placeholder

- **Meaning:** Source control for placeholder; interpret in the business definitions and its enclosing section.
- **UI binding:** `value`; component `input`; input hint `input`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => onChange(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-067:750](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/src/pages/users/UsersPage.jsx#L750).

### FRM-009-C007 — value

- **Meaning:** Source control for value; interpret in the business definitions and its enclosing section.
- **UI binding:** `value`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => onChange(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-067:761](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/src/pages/users/UsersPage.jsx#L761).

### FRM-009-C008 — pageSize

- **Meaning:** Source control for pageSize; interpret in the business definitions and its enclosing section.
- **UI binding:** `pageSize`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => onPageSizeChange(Number(event.target.value))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-067:813](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/src/pages/users/UsersPage.jsx#L813).

### FRM-009-C009 — Search name or email...

- **Meaning:** Source control for Search name or email...; interpret in the business definitions and its enclosing section.
- **UI binding:** `searchText`; component `input`; input hint `search`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => {<br>            setCurrentPage(1);<br>            setSearchText(event.target.value);<br>          }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-067:1285](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/src/pages/users/UsersPage.jsx#L1285).

### FRM-009-C010 — roleFilter

- **Meaning:** Source control for roleFilter; interpret in the business definitions and its enclosing section.
- **UI binding:** `roleFilter`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => {<br>            setCurrentPage(1);<br>            setRoleFilter(event.target.value);<br>          }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-067:1297](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/src/pages/users/UsersPage.jsx#L1297).

### FRM-009-C011 — statusFilter

- **Meaning:** Source control for statusFilter; interpret in the business definitions and its enclosing section.
- **UI binding:** `statusFilter`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => {<br>            setCurrentPage(1);<br>            setStatusFilter(event.target.value);<br>          }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-067:1314](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/src/pages/users/UsersPage.jsx#L1314).

### FRM-009-C012 — Surname

- **Meaning:** Source control for Surname; interpret in the business definitions and its enclosing section.
- **UI binding:** `columnFilters.surname`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateColumnFilter("surname", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-067:1346](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/src/pages/users/UsersPage.jsx#L1346).

### FRM-009-C013 — Name

- **Meaning:** Source control for Name; interpret in the business definitions and its enclosing section.
- **UI binding:** `columnFilters.name`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateColumnFilter("name", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-067:1359](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/src/pages/users/UsersPage.jsx#L1359).

### FRM-009-C014 — Email

- **Meaning:** Source control for Email; interpret in the business definitions and its enclosing section.
- **UI binding:** `columnFilters.email`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateColumnFilter("email", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-067:1372](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/src/pages/users/UsersPage.jsx#L1372).

### FRM-009-C015 — columnFilters.role

- **Meaning:** Source control for columnFilters.role; interpret in the business definitions and its enclosing section.
- **UI binding:** `columnFilters.role`; component `FilterSelect`; input hint `FilterSelect`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `columnOptions.role`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateColumnFilter("role", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-067:1385](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/src/pages/users/UsersPage.jsx#L1385).

### FRM-009-C016 — columnFilters.serviceProviderName

- **Meaning:** Source control for columnFilters.serviceProviderName; interpret in the business definitions and its enclosing section.
- **UI binding:** `columnFilters.serviceProviderName`; component `FilterSelect`; input hint `FilterSelect`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `columnOptions.serviceProviderName`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                      updateColumnFilter("serviceProviderName", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-067:1399](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/src/pages/users/UsersPage.jsx#L1399).

### FRM-009-C017 — columnFilters.teams

- **Meaning:** Source control for columnFilters.teams; interpret in the business definitions and its enclosing section.
- **UI binding:** `columnFilters.teams`; component `FilterSelect`; input hint `FilterSelect`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `columnOptions.teams`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateColumnFilter("teams", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-067:1415](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/src/pages/users/UsersPage.jsx#L1415).

### FRM-009-C018 — columnFilters.accountStatus

- **Meaning:** Source control for columnFilters.accountStatus; interpret in the business definitions and its enclosing section.
- **UI binding:** `columnFilters.accountStatus`; component `FilterSelect`; input hint `FilterSelect`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `columnOptions.accountStatus`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                      updateColumnFilter("accountStatus", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-067:1429](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/src/pages/users/UsersPage.jsx#L1429).

### FRM-009-C019 — columnFilters.onboardingStatus

- **Meaning:** Source control for columnFilters.onboardingStatus; interpret in the business definitions and its enclosing section.
- **UI binding:** `columnFilters.onboardingStatus`; component `FilterSelect`; input hint `FilterSelect`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `columnOptions.onboardingStatus`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                      updateColumnFilter("onboardingStatus", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-067:1445](https://github.com/fikilek/ireps-web/blob/f9f0a09be4e3d9363a39977f998aeea296613323/src/pages/users/UsersPage.jsx#L1445).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Verify deployment of email branches, permitted actor/target combinations and audit reconciliation. AU-R001 gives specific email-change permissions; it does not settle permission inheritance elsewhere.

[Download the detailed control inventory (CSV)](change-sign-in-email-field-catalogue.csv).

[Inspect the extracted client validation expressions (CSV)](change-sign-in-email-validation-evidence.csv). Expressions preserve nested conditions; extraction is not a claim that every backend check is mapped.
