# User Authorisation and Role Management — Field Catalogue

Module **FRM-022** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](user-administration-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/user-administration-user-manual.md) · [Field catalogue](user-administration-field-catalogue.md) · [Error register](user-administration-error-register.md) · [Practical examples](../10-assessments/user-administration-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Target user | Reference | Existing person being administered. | Verify UID, email and provider; names can duplicate. | Synthetic UID |
| Role | Controlled code | Functional role of this identity. | Use permitted current roles; Super User is SPU; Guest excluded from current catalogue. | FWR |
| Status | Controlled selection | User availability/approval status. | Primary web status save remains disabled; do not teach it as working. | PENDING |
| Workbase | Reference list | Approved operating areas. | Only assign within the administrator’s actual scope. | Training Workbase A |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-022-C001 — newRole

- **Meaning:** Functional role of this identity.
- **UI binding:** `newRole`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `isSaving &#124;&#124; feedback?.type === "success"`.
- **Change handling:** `(event) => {<br>                setNewRole(event.target.value);<br>                setFeedback(null);<br>              }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-183:405](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/users/UsersPage.jsx#L405).

### FRM-022-C002 — newStatus

- **Meaning:** User availability/approval status.
- **UI binding:** `newStatus`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => setNewStatus(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-183:503](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/users/UsersPage.jsx#L503).

### FRM-022-C003 — Search name or email...

- **Meaning:** Source control for Search name or email...; interpret in the business definitions and its enclosing section.
- **UI binding:** `searchText`; component `input`; input hint `search`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => setSearchText(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-183:658](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/users/UsersPage.jsx#L658).

### FRM-022-C004 — roleFilter

- **Meaning:** Functional role of this identity.
- **UI binding:** `roleFilter`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => setRoleFilter(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-183:667](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/users/UsersPage.jsx#L667).

### FRM-022-C005 — statusFilter

- **Meaning:** User availability/approval status.
- **UI binding:** `statusFilter`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => setStatusFilter(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-183:681](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/users/UsersPage.jsx#L681).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Capture action-level permissions in a tested matrix. Role labels alone are not authority. Review the current branch against other user-management feature worktrees.

[Download the detailed control inventory (CSV)](user-administration-field-catalogue.csv).
