# Report Generation and Delivery — Body of Knowledge

Module **FRM-033** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](report-generation-body-of-knowledge.md) · [User Manual](../02-user-manual/web/report-generation-user-manual.md) · [Field catalogue](report-generation-field-catalogue.md) · [Error register](report-generation-error-register.md) · [Practical examples](../10-assessments/report-generation-scenarios.md)

## Meaning and purpose

Report forms select reporting scope and, where implemented, generate or deliver a report derived from existing operational evidence.

General Monthly Report generation and a transaction-report preview/email interface are different actions. Report filters are view controls. A visible Send interface does not prove a configured delivery service; authentication reset email also does not prove that report email works.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

Administrative actions can affect many people or records. Their scope, actor and result need explicit verification. A filter changing what is visible is different from a mutation changing stored information. Do not infer completion from a modal closing or a row disappearing from a filtered list.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Select the report and its intended scope/period.
2. Review the underlying transactions and exceptions.
3. Generate or preview the report using the supported action.
4. Check content and recipients before any delivery action.
5. Verify generation/download/delivery separately and preserve the report’s source period and identity.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Scope and dates | Population summarised by the report. | Confirm filters before generation; avoid comparing unlike periods. |
| Recipient | Address entered for the report-delivery interface. | Required email input; delivery integration must be verified. |
| Subject | Report email subject. | Required in the displayed form. |
| Message | Optional accompanying context. | Does not replace the report or its provenance. |

The [field catalogue](report-generation-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](report-generation-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

A monthly report shows higher vending revenue after inspections. It is an observed change; it does not by itself prove that the inspections caused the increase.

## Exceptions, maturity and unresolved decisions

Verify email delivery implementation/configuration and recipient controls before teaching Send as operational. No report was sent during this documentation work. A backend report-email delivery module exists, including recipient, subject and body validation. Its existence does not verify delivery configuration or successful delivery; the older auth-rule statement that iREPS cannot send email must not be applied as a platform-wide claim.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-179:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/reports/GeneralMonthlyReportPage.jsx#L1) | `ireps-web/src/pages/reports/GeneralMonthlyReportPage.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-178:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/components/TrnReportPreviewModal.jsx#L1) | `ireps-web/src/pages/registries/components/TrnReportPreviewModal.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-107:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/config.js#L1) | `ireps-web/functions/reportPlatform/config.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-108:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/contract.js#L1) | `ireps-web/functions/reportPlatform/contract.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-109:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/emailDelivery.js#L1) | `ireps-web/functions/reportPlatform/emailDelivery.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-110:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/emailDeliveryCallable.js#L1) | `ireps-web/functions/reportPlatform/emailDeliveryCallable.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-111:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/generatedReports.js#L1) | `ireps-web/functions/reportPlatform/generatedReports.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-112:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/generatedReportsCallables.js#L1) | `ireps-web/functions/reportPlatform/generatedReportsCallables.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-113:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/persistence.js#L1) | `ireps-web/functions/reportPlatform/persistence.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-114:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/persistenceCallables.js#L1) | `ireps-web/functions/reportPlatform/persistenceCallables.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-115:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/retentionCleanup.js#L1) | `ireps-web/functions/reportPlatform/retentionCleanup.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-116:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/retentionCleanupSchedule.js#L1) | `ireps-web/functions/reportPlatform/retentionCleanupSchedule.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-117:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/trnMediaCallables.js#L1) | `ireps-web/functions/reportPlatform/trnMediaCallables.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-118:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/validateGeneratedReport.js#L1) | `ireps-web/functions/reportPlatform/validateGeneratedReport.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-119:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reports/generalMonthlyReport.js#L1) | `ireps-web/functions/reports/generalMonthlyReport.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
