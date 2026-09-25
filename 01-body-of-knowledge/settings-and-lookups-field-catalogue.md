# Settings and Lookup Administration — Field Catalogue

Module **FRM-034** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](settings-and-lookups-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/settings-and-lookups-user-manual.md) · [Field catalogue](settings-and-lookups-field-catalogue.md) · [Error register](settings-and-lookups-error-register.md) · [Practical examples](../10-assessments/settings-and-lookups-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Lookup key/domain/field key | Text identifiers | Identifies the configuration and intended consumer. | Normalised keys in UI; do not rename established codes without migration review. | TRAINING_REASON |
| Title/description | Text | Human-readable explanation of the list. | Describe its actual use. | Training reasons |
| Allow Other/Other label | Boolean and text | Whether a list supports additional explanation. | A flag alone does not create a companion form field. | Other |
| Option code/label | Text identifiers | Stable stored code and displayed wording. | Code can be non-editable on existing options; preserve historical meaning. | DISPLAY_BLANK / Display blank |
| Sort order/status/system | Number/controlled flags | Ordering and administrative behaviour. | Do not equate inactive with deleted; verify consumer treatment. | 10 |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-034-C001 — Add new item...

- **Meaning:** Source control for Add new item...; interpret in the business definitions and its enclosing section.
- **UI binding:** `newItemText`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `setNewItemText`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-014:155](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/index.js#L155).

### FRM-034-C002 — placeholder

- **Meaning:** Source control for placeholder; interpret in the business definitions and its enclosing section.
- **UI binding:** `value`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `onChangeText`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-016:115](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/create.js#L115).

### FRM-034-C003 — Lookup key

- **Meaning:** Source control for Lookup key; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.lookupKey`; component `Field`; input hint `Field`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) =><br>              updateField("lookupKey", normalizeLookupKey(text))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-016:285](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/create.js#L285).

### FRM-034-C004 — Title

- **Meaning:** Source control for Title; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.title`; component `Field`; input hint `Field`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) => updateField("title", text)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-016:297](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/create.js#L297).

### FRM-034-C005 — Description

- **Meaning:** Source control for Description; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.description`; component `Field`; input hint `Field`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) => updateField("description", text)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-016:306](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/create.js#L306).

### FRM-034-C006 — Domain

- **Meaning:** Source control for Domain; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.domain`; component `Field`; input hint `Field`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) =><br>              updateField("domain", normalizeDomain(text))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-016:315](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/create.js#L315).

### FRM-034-C007 — Field key

- **Meaning:** Source control for Field key; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.fieldKey`; component `Field`; input hint `Field`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) => updateField("fieldKey", text)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-016:327](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/create.js#L327).

### FRM-034-C008 — form.allowOther

- **Meaning:** Source control for form.allowOther; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.allowOther`; component `Switch`; input hint `Switch`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateField("allowOther", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-016:348](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/create.js#L348).

### FRM-034-C009 — Other label

- **Meaning:** Source control for Other label; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.otherLabel`; component `Field`; input hint `Field`.
- **Visibility/prerequisites:** `conditional branch: form.allowOther`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) => updateField("otherLabel", text)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-016:355](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/create.js#L355).

### FRM-034-C010 — form.system

- **Meaning:** Source control for form.system; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.system`; component `Switch`; input hint `Switch`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateField("system", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-016:373](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/create.js#L373).

### FRM-034-C011 — placeholder

- **Meaning:** Source control for placeholder; interpret in the business definitions and its enclosing section.
- **UI binding:** `value`; component `TextInput`; input hint `keyboardType`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `editable`.
- **Change handling:** `onChangeText`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-017:86](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/option.js#L86).

### FRM-034-C012 — Code

- **Meaning:** Source control for Code; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.code`; component `Field`; input hint `Field`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!isEditMode`.
- **Change handling:** `(text) =><br>              updateField("code", normalizeOptionCode(text))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-017:343](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/option.js#L343).

### FRM-034-C013 — Label

- **Meaning:** Source control for Label; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.label`; component `Field`; input hint `Field`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) => updateField("label", text)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-017:360](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/option.js#L360).

### FRM-034-C014 — Description

- **Meaning:** Source control for Description; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.description`; component `Field`; input hint `Field`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) => updateField("description", text)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-017:370](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/option.js#L370).

### FRM-034-C015 — Sort order

- **Meaning:** Source control for Sort order; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.sortOrder`; component `Field`; input hint `numeric`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) =><br>              updateField("sortOrder", text.replace(/[^0-9.]/g, ""))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-017:379](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/option.js#L379).

### FRM-034-C016 — form.system

- **Meaning:** Source control for form.system; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.system`; component `Switch`; input hint `Switch`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateField("system", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-017:403](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/option.js#L403).

### FRM-034-C017 — Lookup title

- **Meaning:** Source control for Lookup title; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.title`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) => updateField("title", text)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-015:182](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/[lookupKey].js#L182).

### FRM-034-C018 — Description

- **Meaning:** Source control for Description; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.description`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) => updateField("description", text)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-015:191](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/[lookupKey].js#L191).

### FRM-034-C019 — METER_REMOVAL

- **Meaning:** Source control for METER_REMOVAL; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.domain`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) =><br>                updateField(<br>                  "domain",<br>                  String(text &#124;&#124; "")<br>                    .toUpperCase()<br>                    .replace(/[^A-Z0-9_]/g, "_"),<br>                )`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-015:202](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/[lookupKey].js#L202).

### FRM-034-C020 — removal.finalReading.noReadingReason

- **Meaning:** Source control for removal.finalReading.noReadingReason; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.fieldKey`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) => updateField("fieldKey", text)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-015:219](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/[lookupKey].js#L219).

### FRM-034-C021 — form.allowOther

- **Meaning:** Source control for form.allowOther; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.allowOther`; component `Switch`; input hint `Switch`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateField("allowOther", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-015:236](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/[lookupKey].js#L236).

### FRM-034-C022 — Other

- **Meaning:** Source control for Other; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.otherLabel`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `conditional branch: form.allowOther`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) => updateField("otherLabel", text)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-015:245](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/[lookupKey].js#L245).

### FRM-034-C023 — form.system

- **Meaning:** Source control for form.system; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.system`; component `Switch`; input hint `Switch`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateField("system", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-015:263](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/[lookupKey].js#L263).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Map every lookup consumer before changing or retiring options. Common form standards must reference engineering rules rather than create a competing list authority.

[Download the detailed control inventory (CSV)](settings-and-lookups-field-catalogue.csv).

[Inspect the extracted client validation expressions (CSV)](settings-and-lookups-validation-evidence.csv). Expressions preserve nested conditions; extraction is not a claim that every backend check is mapped.
