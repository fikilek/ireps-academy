# TC Upload and Validation — Field Catalogue

Module **FRM-030** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](tc-upload-body-of-knowledge.md) · [User Manual](../02-user-manual/web/tc-upload-user-manual.md) · [Field catalogue](tc-upload-field-catalogue.md) · [Error register](tc-upload-error-register.md) · [Practical examples](../10-assessments/tc-upload-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Transaction type | Controlled value | Kind of work represented by the input. | Use supported types; check the file agrees. | Synthetic supported type |
| Municipality code | Text/reference | Scope of the uploaded work. | Must match intended workbase/municipality. | Training municipality |
| File | File input | Operational source data. | Extension alone is not validation; inspect server row results. | training-input.csv |
| Notes | Text | Upload context. | Optional in the displayed form. | Training example |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-030-C001 — form.trnType

- **Meaning:** Source control for form.trnType; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.trnType`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) =><br>                    updateField("trnType", event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-166:1932](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TcUploadsPage.jsx#L1932).

### FRM-030-C002 — form.lmPcode

- **Meaning:** Source control for form.lmPcode; interpret in the business definitions and its enclosing section.
- **UI binding:** `form.lmPcode`; component `input`; input hint `input`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) =><br>                    updateField("lmPcode", event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-166:1949](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TcUploadsPage.jsx#L1949).

### FRM-030-C003 — input

- **Meaning:** Source control for input; interpret in the business definitions and its enclosing section.
- **UI binding:** ``; component `input`; input hint `file`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `handleFileChange`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-166:1961](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TcUploadsPage.jsx#L1961).

### FRM-030-C004 — Optional upload notes

- **Meaning:** Upload context.
- **UI binding:** `form.notes`; component `textarea`; input hint `textarea`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => updateField("notes", event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-166:1987](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TcUploadsPage.jsx#L1987).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Exact file schema, row validation and delete guards require the corresponding backend/source-data review before publication. This task did not upload files or inspect customer exports.

[Download the detailed control inventory (CSV)](tc-upload-field-catalogue.csv).

[Inspect the extracted client validation expressions (CSV)](tc-upload-validation-evidence.csv). Expressions preserve nested conditions; extraction is not a claim that every backend check is mapped.
