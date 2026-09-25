# TC Upload and Validation — Body of Knowledge

Module **FRM-030** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](tc-upload-body-of-knowledge.md) · [User Manual](../02-user-manual/web/tc-upload-user-manual.md) · [Field catalogue](tc-upload-field-catalogue.md) · [Error register](tc-upload-error-register.md) · [Practical examples](../10-assessments/tc-upload-scenarios.md)

## Meaning and purpose

TC Upload records an uploaded operational source file and its validation outcome before it is used to plan work.

Use the product label TC without inventing an expansion. Transaction type, municipality context, source rows and validation results must stay associated. Upload success is not confirmation that every input row is valid or already executed.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

Administrative actions can affect many people or records. Their scope, actor and result need explicit verification. A filter changing what is visible is different from a mutation changing stored information. Do not infer completion from a modal closing or a row disappearing from a filtered list.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Open the upload form and choose its transaction type.
2. Confirm the municipality code and source file.
3. Add relevant upload notes.
4. Upload and inspect row validation and errors.
5. Use only the reviewed result for subsequent planning; retain the upload identifier when escalating problems.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Transaction type | Kind of work represented by the input. | Use supported types; check the file agrees. |
| Municipality code | Scope of the uploaded work. | Must match intended workbase/municipality. |
| File | Operational source data. | Extension alone is not validation; inspect server row results. |
| Notes | Upload context. | Optional in the displayed form. |

The [field catalogue](tc-upload-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](tc-upload-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

A file is accepted for upload but several rows fail validation. The office resolves the rejected rows rather than claiming that all work was scheduled.

## Exceptions, maturity and unresolved decisions

Exact file schema, row validation and delete guards require the corresponding backend/source-data review before publication. This task did not upload files or inspect customer exports.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-166:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TcUploadsPage.jsx#L1) | `ireps-web/src/pages/operations/TcUploadsPage.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
