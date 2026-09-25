# TC Upload and Validation — User Manual

Module **FRM-030** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/tc-upload-body-of-knowledge.md) · [User Manual](tc-upload-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/tc-upload-field-catalogue.md) · [Error register](../../01-body-of-knowledge/tc-upload-error-register.md) · [Practical examples](../../10-assessments/tc-upload-scenarios.md)

## Before you start

Use the product label TC without inventing an expansion. Transaction type, municipality context, source rows and validation results must stay associated. Upload success is not confirmation that every input row is valid or already executed.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Open the upload form and choose its transaction type.
2. Confirm the municipality code and source file.
3. Add relevant upload notes.
4. Upload and inspect row validation and errors.
5. Use only the reviewed result for subsequent planning; retain the upload identifier when escalating problems.

## What to check in the result

A file is accepted for upload but several rows fail validation. The office resolves the rejected rows rather than claiming that all work was scheduled.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Exact file schema, row validation and delete guards require the corresponding backend/source-data review before publication. This task did not upload files or inspect customer exports.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/tc-upload-error-register.md) and [field catalogue](../../01-body-of-knowledge/tc-upload-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/tc-upload-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
