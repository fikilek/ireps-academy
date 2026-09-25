# Service Provider Registration and Editing — Body of Knowledge

Module **FRM-023** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](service-provider-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/service-provider-user-manual.md) · [Field catalogue](service-provider-field-catalogue.md) · [Error register](service-provider-error-register.md) · [Practical examples](../10-assessments/service-provider-scenarios.md)

## Meaning and purpose

A service provider record identifies an organisation that participates in delivery and employment relationships.

The source has create and edit wrappers around a shared provider form. Trading identity, registered identity, ownership contact, manager and geographic coverage are distinct facts. Utility/main contractor/subcontractor hierarchy is owner context and must not be inferred solely from a provider name.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

Administrative actions can affect many people or records. Their scope, actor and result need explicit verification. A filter changing what is visible is different from a mutation changing stored information. Do not infer completion from a modal closing or a row disappearing from a filtered list.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Check that the organisation is not already registered.
2. Open Create or Edit deliberately.
3. Record trading and registered details, ownership fields and the available responsible-manager/workbase selections.
4. Review the relationships before submitting.
5. Verify the saved provider and its intended availability for signup and assignments.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Trading name | Operational name shown to users. | Required details follow the provider form; do not use a person’s name as a substitute organisation. |
| Registered identity | Registered name and registration number. | Keep number as text and use verified source data. |
| Owner | Ownership/contact fields in this provider form. | Synthetic examples only; this record is not proof of legal ownership. |
| Manager and workbases | Responsibility and operating scope. | Select existing authorised identities/areas; absent manager affects signup. |

The [field catalogue](service-provider-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](service-provider-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

A provider exists but has no responsible manager. Fieldworker signup can be blocked even when the trading name appears correct.

## Exceptions, maturity and unresolved decisions

Review hierarchy and status changes with the responsible product workstream. Provider deactivation, existing users and outstanding assignments require explicit transition rules.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-051:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/serviceProviders/FormCreateServiceProvider.js#L1) | `ireps-mobile/src/features/serviceProviders/FormCreateServiceProvider.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-052:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/serviceProviders/FormEditServiceProvider.js#L1) | `ireps-mobile/src/features/serviceProviders/FormEditServiceProvider.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-053:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/serviceProviders/FormServiceProvider.js#L1) | `ireps-mobile/src/features/serviceProviders/FormServiceProvider.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-088:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L1) | `ireps-web/functions/index.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
