# Premise Account Data — User Manual

Module **FRM-011** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/premise-account-data-body-of-knowledge.md) · [User Manual](premise-account-data-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/premise-account-data-field-catalogue.md) · [Error register](../../01-body-of-knowledge/premise-account-data-error-register.md) · [Practical examples](../../10-assessments/premise-account-data-scenarios.md)

## Before you start

One premise may need several account references. The owner may be a natural or juristic person; the occupant may be the owner or someone else. These records do not establish legal ownership, a billing invoice or payment.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Open Account Data for the verified premise.
2. Inspect existing account information before starting a new capture.
3. Add account numbers without duplicates and select owner type.
4. Capture the corresponding owner name and contact fields; describe the occupant separately when appropriate.
5. Attach requested evidence, review the association and submit.
6. Confirm server acknowledgement or inspect the Data Cleansing local queue; a saved queue item is not a completed server update.

## What to check in the result

A company owns Unit 03B and a person occupies it. Record the company under juristic owner and the person under occupant; do not put the tenant’s name in the registered-company field.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Blank-to-NAv transformations exist in source. Unknown, not applicable and unavailable need precise interpretation rather than guessed values. A network-unavailable submit can enter a separate account-data queue.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/premise-account-data-error-register.md) and [field catalogue](../../01-body-of-knowledge/premise-account-data-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/premise-account-data-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
