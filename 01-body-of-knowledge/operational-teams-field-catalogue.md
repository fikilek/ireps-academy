# Operational Teams — Field Catalogue

Module **FRM-024** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](operational-teams-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/operational-teams-user-manual.md) · [Field catalogue](operational-teams-field-catalogue.md) · [Error register](operational-teams-error-register.md) · [Practical examples](../10-assessments/operational-teams-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Team name | Text | Human-readable team identifier. | Client/server naming rules apply; do not assume globally unique display names. | Training Team A |
| Member | User reference | Eligible person to add or remove. | Use actual permitted user options; do not substitute free text. | Synthetic UID |
| Team/action | Reference and operation | Team and mutation being requested. | Check the exact action and outstanding assignments before deletion. | Rename |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-024-C001 — Enter team name

- **Meaning:** Human-readable team identifier.
- **UI binding:** `newTeamName`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!isCreatingTeam`.
- **Change handling:** `setNewTeamName`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-012:712](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/teams.js#L712).

### FRM-024-C002 — Enter team name

- **Meaning:** Human-readable team identifier.
- **UI binding:** `teamName`; component `input`; input hint `input`.
- **Visibility/prerequisites:** `conditional branch: modalMode`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `isSavingTeam`.
- **Change handling:** `(event) => setTeamName(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-162:689](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/OperationalTeamsPage.jsx#L689).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Verify eligibility, deletion guards and assignment effects in the target release. The form inventory records both mobile and web implementations.

[Download the detailed control inventory (CSV)](operational-teams-field-catalogue.csv).
