# Report Generation and Delivery — Field Catalogue

Module **FRM-033** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](report-generation-body-of-knowledge.md) · [User Manual](../02-user-manual/web/report-generation-user-manual.md) · [Field catalogue](report-generation-field-catalogue.md) · [Error register](report-generation-error-register.md) · [Practical examples](../10-assessments/report-generation-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Scope and dates | References/date range | Population summarised by the report. | Confirm filters before generation; avoid comparing unlike periods. | Training month |
| Recipient | Email text | Address entered for the report-delivery interface. | Required email input; delivery integration must be verified. | reviewer@example.org |
| Subject | Text | Report email subject. | Required in the displayed form. | Training report |
| Message | Text | Optional accompanying context. | Does not replace the report or its provenance. | Synthetic review note |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-033-C001 — reportMonthTooltip(reportMonth)

- **Meaning:** Source control for reportMonthTooltip(reportMonth); interpret in the business definitions and its enclosing section.
- **UI binding:** `reportMonth`; component `input`; input hint `month`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `isGenerating`.
- **Change handling:** `(event) => setReportMonth(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-179:287](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/reports/GeneralMonthlyReportPage.jsx#L287).

### FRM-033-C002 — recipient@example.com

- **Meaning:** Address entered for the report-delivery interface.
- **UI binding:** `emailForm.to`; component `input`; input hint `email`.
- **Visibility/prerequisites:** `conditional branch: emailOpen`.
- **Requirement/options:** `true`; `See schema / owning shared component`.
- **Editability:** `emailState.status === "sending" &#124;&#124; emailState.status === "sent"`.
- **Change handling:** `(event) =><br>                    setEmailForm((current) => ({ ...current, to: event.target.value }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-178:517](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/components/TrnReportPreviewModal.jsx#L517).

### FRM-033-C003 — emailForm.subject

- **Meaning:** Report email subject.
- **UI binding:** `emailForm.subject`; component `input`; input hint `text`.
- **Visibility/prerequisites:** `conditional branch: emailOpen`.
- **Requirement/options:** `true`; `See schema / owning shared component`.
- **Editability:** `emailState.status === "sending" &#124;&#124; emailState.status === "sent"`.
- **Change handling:** `(event) =><br>                    setEmailForm((current) => ({ ...current, subject: event.target.value }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-178:533](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/components/TrnReportPreviewModal.jsx#L533).

### FRM-033-C004 — emailForm.message

- **Meaning:** Optional accompanying context.
- **UI binding:** `emailForm.message`; component `textarea`; input hint `textarea`.
- **Visibility/prerequisites:** `conditional branch: emailOpen`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `emailState.status === "sending" &#124;&#124; emailState.status === "sent"`.
- **Change handling:** `(event) =><br>                    setEmailForm((current) => ({ ...current, message: event.target.value }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-178:548](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/components/TrnReportPreviewModal.jsx#L548).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Verify email delivery implementation/configuration and recipient controls before teaching Send as operational. No report was sent during this documentation work. A backend report-email delivery module exists, including recipient, subject and body validation. Its existence does not verify delivery configuration or successful delivery; the older auth-rule statement that iREPS cannot send email must not be applied as a platform-wide claim.

[Download the detailed control inventory (CSV)](report-generation-field-catalogue.csv).

[Inspect the extracted client validation expressions (CSV)](report-generation-validation-evidence.csv). Expressions preserve nested conditions; extraction is not a claim that every backend check is mapped.
