# Sign Up — User Manual

Module **FRM-002** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/sign-up-body-of-knowledge.md) · [User Manual](signup.md) · [Field catalogue](../../01-body-of-knowledge/sign-up-field-catalogue.md) · [Error register](../../01-body-of-knowledge/sign-up-error-register.md) · [Practical examples](../../10-assessments/sign-up-scenarios.md)

## Before you start

The current documented journey is mobile signup followed by approval. The web sign-in interface does not establish a web self-registration journey. Utility/main-contractor/subcontractor governance and permission inheritance remain separate decisions.

Use a named, verified build in the intended environment. Confirm identity, workbase and action-specific access. Check the subject before editing or submitting; similarly named people, premises, meters and batches are not interchangeable.

## Procedure

1. Open Sign Up on mobile.
2. Enter your surname, name, email, password and matching confirmation.
3. Load and select the correct active service provider; do not choose a different employer just to bypass a failure.
4. Review the email and service provider in the confirmation.
5. Submit once, retain the result, then use Sign In and await the responsible manager’s authorisation.

## What to check in the result

Lebo chooses the correct provider, submits and receives a pending outcome. A manager must authorise the fieldworker; registration is not permission to start Meter Discovery.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Confirm backend/UI parity on the target release and whether account creation succeeded before retrying a network failure. Do not promise an invitation email for self-signup.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/sign-up-error-register.md) and [field catalogue](../../01-body-of-knowledge/sign-up-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/sign-up-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
