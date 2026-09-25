# Report Generation and Delivery — User Manual

Module **FRM-033** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/report-generation-body-of-knowledge.md) · [User Manual](report-generation-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/report-generation-field-catalogue.md) · [Error register](../../01-body-of-knowledge/report-generation-error-register.md) · [Practical examples](../../10-assessments/report-generation-scenarios.md)

## Before you start

General Monthly Report generation and a transaction-report preview/email interface are different actions. Report filters are view controls. A visible Send interface does not prove a configured delivery service; authentication reset email also does not prove that report email works.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Select the report and its intended scope/period.
2. Review the underlying transactions and exceptions.
3. Generate or preview the report using the supported action.
4. Check content and recipients before any delivery action.
5. Verify generation/download/delivery separately and preserve the report’s source period and identity.

## What to check in the result

A monthly report shows higher vending revenue after inspections. It is an observed change; it does not by itself prove that the inspections caused the increase.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Verify email delivery implementation/configuration and recipient controls before teaching Send as operational. No report was sent during this documentation work. A backend report-email delivery module exists, including recipient, subject and body validation. Its existence does not verify delivery configuration or successful delivery; the older auth-rule statement that iREPS cannot send email must not be applied as a platform-wide claim.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/report-generation-error-register.md) and [field catalogue](../../01-body-of-knowledge/report-generation-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/report-generation-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
