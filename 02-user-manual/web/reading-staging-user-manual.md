# Meter Reading Staging and Export — User Manual

Module **FRM-032** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/reading-staging-body-of-knowledge.md) · [User Manual](reading-staging-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/reading-staging-field-catalogue.md) · [Error register](../../01-body-of-knowledge/reading-staging-error-register.md) · [Practical examples](../../10-assessments/reading-staging-scenarios.md)

## Before you start

Reading capture, staging generation, review and download are separate events. The web source has a staging-generation action, a controller and staging/registry views. A downloaded file is not proof that the receiving billing system imported it.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Choose the correct municipality and billing period/session.
2. Review available reading population and exceptions.
3. Run the authorised staging action where offered.
4. Inspect the session’s counts, excluded/invalid readings and individual meter history.
5. Download the reviewed output in the supported format.
6. Record the handoff and receiving-system acknowledgement through the agreed process; reconcile rejected rows.

## What to check in the result

The office generates 98 usable readings from 100 planned visits; two are No Access. The export contains reviewed readings, while the exceptions remain visible and the external billing team acknowledges its import.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Owner states this module needs strengthening before production readiness. Automated billing-system integration and full customer billing remain future work. Do not invent an approval button where the page only filters or downloads.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/reading-staging-error-register.md) and [field catalogue](../../01-body-of-knowledge/reading-staging-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/reading-staging-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
