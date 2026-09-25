# Report Generation and Delivery — Error Register

Module **FRM-033** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](report-generation-body-of-knowledge.md) · [User Manual](../02-user-manual/web/report-generation-user-manual.md) · [Field catalogue](report-generation-field-catalogue.md) · [Error register](report-generation-error-register.md) · [Practical examples](../10-assessments/report-generation-scenarios.md)

## How to interpret this register

Academy IDs identify documentation entries; they are not runtime codes. Source messages can be dynamic templates. Informational or success notifications found beside errors are labelled source messages and must not be counted as failures. A refusal before the business commit differs from an unknown outcome after a network timeout.

| Situation | Meaning / data state | User response |
| --- | --- | --- |
| Local validation | The current attempt has not passed the form validator; a prior draft or prior attempt can still exist. | Correct the named field and recheck dependent fields/evidence. |
| Server permission/state refusal | The request was refused at a checked condition; inspect the code-specific stage before asserting that nothing at all was saved. | Retain the reference and resolve authority, subject or state; do not bypass the check with another identity. |
| Timeout or dropped connection | Outcome can be uncertain; late processing may succeed. | Reconcile the original attempt and use the workflow’s duplicate-safe recovery path when verified. |
| Local save or media failure | The intended evidence or draft may not be durable yet. | Retain the screen/context and verify storage/upload before leaving. |
| Partial success | One system step may have succeeded while a later write failed. | Follow the effective credential/record state and escalate the incomplete step with identifiers. |

## Source error and message evidence

[Complete extracted register with trigger expressions (CSV)](report-generation-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-033-E001 | `LOCAL_MESSAGE` |  | Client source: handleGenerate · [FS-179:143](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/reports/GeneralMonthlyReportPage.jsx#L143) |
| FRM-033-E002 | `LOCAL_MESSAGE` | errorMessage(generationError) | Client source: handleGenerate · [FS-179:190](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/reports/GeneralMonthlyReportPage.jsx#L190) |
| FRM-033-E003 | `dynamic code` | error.message | Server source: toHttpsError · [FS-110:30](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/emailDeliveryCallable.js#L30) |
| FRM-033-E004 | `internal` | Report email delivery failed. | Server source: toHttpsError · [FS-110:33](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/emailDeliveryCallable.js#L33) |
| FRM-033-E005 | `dynamic code` | error | Server source: sendGeneratedReportEmailCallable · [FS-110:82](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/emailDeliveryCallable.js#L82) |
| FRM-033-E006 | `dynamic code` | error.message | Server source: toHttpsError · [FS-112:25](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/generatedReportsCallables.js#L25) |
| FRM-033-E007 | `internal` | Generated Reports operation failed. | Server source: toHttpsError · [FS-112:28](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/generatedReportsCallables.js#L28) |
| FRM-033-E008 | `dynamic code` | error | Server source: listGeneratedReportsCallable · [FS-112:41](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/generatedReportsCallables.js#L41) |
| FRM-033-E009 | `dynamic code` | error | Server source: getGeneratedReportDownloadCallable · [FS-112:56](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/generatedReportsCallables.js#L56) |
| FRM-033-E010 | `dynamic code` | error | Server source: deleteGeneratedReportCallable · [FS-112:70](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/generatedReportsCallables.js#L70) |
| FRM-033-E011 | `dynamic code` | error.message | Server source: toHttpsError · [FS-114:24](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/persistenceCallables.js#L24) |
| FRM-033-E012 | `internal` | Report persistence failed. | Server source: toHttpsError · [FS-114:27](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/persistenceCallables.js#L27) |
| FRM-033-E013 | `dynamic code` | error | Server source: prepareGeneratedReportCallable · [FS-114:38](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/persistenceCallables.js#L38) |
| FRM-033-E014 | `dynamic code` | error | Server source: finalizeGeneratedReportCallable · [FS-114:52](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/persistenceCallables.js#L52) |
| FRM-033-E015 | `unauthenticated` | Authentication required. | Server source: assertTrnReadAccess · [FS-117:39](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/trnMediaCallables.js#L39) |
| FRM-033-E016 | `permission-denied` | This user may not read TRN Registry media. | Server source: assertTrnReadAccess · [FS-117:48](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/trnMediaCallables.js#L48) |
| FRM-033-E017 | `permission-denied` | This TRN is outside the user's assigned workbases. | Server source: assertTrnReadAccess · [FS-117:60](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/trnMediaCallables.js#L60) |
| FRM-033-E018 | `failed-precondition` | The selected TRN media URL is invalid. | Server source: assertTrustedMediaUrl · [FS-117:100](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/trnMediaCallables.js#L100) |
| FRM-033-E019 | `failed-precondition` | The selected TRN media is not stored in an approved Firebase Storage URL. | Server source: assertTrustedMediaUrl · [FS-117:110](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/trnMediaCallables.js#L110) |
| FRM-033-E020 | `permission-denied` | The selected TRN media belongs to an unexpected Storage bucket. | Server source: assertTrustedMediaUrl · [FS-117:121](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/trnMediaCallables.js#L121) |
| FRM-033-E021 | `unavailable` | `TRN media download failed with HTTP ${response.status}.` | Server source: fetchImageBytes · [FS-117:156](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/trnMediaCallables.js#L156) |
| FRM-033-E022 | `resource-exhausted` | The selected TRN image is too large for Quick TRN PDF embedding. | Server source: fetchImageBytes · [FS-117:164](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/trnMediaCallables.js#L164) |
| FRM-033-E023 | `failed-precondition` | The selected TRN media is not a supported JPG or PNG image. | Server source: fetchImageBytes · [FS-117:176](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/trnMediaCallables.js#L176) |
| FRM-033-E024 | `unavailable` | The selected TRN image is empty. | Server source: fetchImageBytes · [FS-117:184](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/trnMediaCallables.js#L184) |
| FRM-033-E025 | `resource-exhausted` | The selected TRN image is too large for Quick TRN PDF embedding. | Server source: fetchImageBytes · [FS-117:187](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/trnMediaCallables.js#L187) |
| FRM-033-E026 | `deadline-exceeded` | TRN media download timed out. | Server source: fetchImageBytes · [FS-117:198](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/trnMediaCallables.js#L198) |
| FRM-033-E027 | `unavailable` | error?.message &#124;&#124; "TRN media could not be downloaded." | Server source: fetchImageBytes · [FS-117:201](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/trnMediaCallables.js#L201) |
| FRM-033-E028 | `invalid-argument` | mediaIndex must be a non-negative integer. | Server source: assertMediaIndex · [FS-117:315](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/trnMediaCallables.js#L315) |
| FRM-033-E029 | `not-found` | `The requested ${source.toLowerCase()} media item does not exist.` | Server source: loadMediaResult · [FS-117:332](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/trnMediaCallables.js#L332) |
| FRM-033-E030 | `unauthenticated` | Authentication required. | Server source: getQuickTrnMediaCallable · [FS-117:364](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/trnMediaCallables.js#L364) |
| FRM-033-E031 | `invalid-argument` | trnId is required. | Server source: getQuickTrnMediaCallable · [FS-117:371](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/trnMediaCallables.js#L371) |
| FRM-033-E032 | `invalid-argument` | Unsupported Quick TRN media action. | Server source: getQuickTrnMediaCallable · [FS-117:375](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/trnMediaCallables.js#L375) |
| FRM-033-E033 | `not-found` | The exact TRN was not found. | Server source: getQuickTrnMediaCallable · [FS-117:385](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/trnMediaCallables.js#L385) |
| FRM-033-E034 | `not-found` | The TRN-linked authoritative premise was not found. | Server source: getQuickTrnMediaCallable · [FS-117:420](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reportPlatform/trnMediaCallables.js#L420) |
| FRM-033-E035 | `unauthenticated` | Authentication required. | Server source: assertGmrAccess · [FS-119:273](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reports/generalMonthlyReport.js#L273) |
| FRM-033-E036 | `permission-denied` | This user may not generate the General Monthly Report. | Server source: assertGmrAccess · [FS-119:281](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reports/generalMonthlyReport.js#L281) |
| FRM-033-E037 | `permission-denied` | The General Monthly Report is outside the user's assigned workbases. | Server source: assertGmrAccess · [FS-119:293](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reports/generalMonthlyReport.js#L293) |
| FRM-033-E038 | `invalid-argument` | `GMR Builder v0.1 is locked to ${GMR_LM_NAME} (${GMR_LM_PCODE}).` | Server source: generateGeneralMonthlyReportCallable · [FS-119:1402](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reports/generalMonthlyReport.js#L1402) |
| FRM-033-E039 | `invalid-argument` | GMR Builder v0.1 requires MONTHLY_GMR generation mode. | Server source: generateGeneralMonthlyReportCallable · [FS-119:1408](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reports/generalMonthlyReport.js#L1408) |
| FRM-033-E040 | `invalid-argument` | error.message | Server source: generateGeneralMonthlyReportCallable · [FS-119:1419](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reports/generalMonthlyReport.js#L1419) |
| FRM-033-E041 | `failed-precondition` | error.message | Server source: generateGeneralMonthlyReportCallable · [FS-119:1469](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reports/generalMonthlyReport.js#L1469) |
| FRM-033-E042 | `internal` | The General Monthly Report dataset could not be generated. | Server source: generateGeneralMonthlyReportCallable · [FS-119:1471](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/reports/generalMonthlyReport.js#L1471) |

## Module-specific recovery and unresolved cases

Verify email delivery implementation/configuration and recipient controls before teaching Send as operational. No report was sent during this documentation work. A backend report-email delivery module exists, including recipient, subject and body validation. Its existence does not verify delivery configuration or successful delivery; the older auth-rule statement that iREPS cannot send email must not be applied as a platform-wide claim.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.
