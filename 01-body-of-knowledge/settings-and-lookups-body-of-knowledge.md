# Settings and Lookup Administration — Body of Knowledge

Module **FRM-034** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](settings-and-lookups-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/settings-and-lookups-user-manual.md) · [Field catalogue](settings-and-lookups-field-catalogue.md) · [Error register](settings-and-lookups-error-register.md) · [Practical examples](../10-assessments/settings-and-lookups-scenarios.md)

## Meaning and purpose

Settings and lookup administration maintain supported configuration records and their controlled options.

The source includes legacy settings arrays, lookup creation/editing, option creation/editing and status actions. UI-R003 now requires field-form choice lists to live in the phone’s formOptions module. Editing a database lookup is therefore not evidence that a current field-form dropdown will change.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

Administrative actions can affect many people or records. Their scope, actor and result need explicit verification. A filter changing what is visible is different from a mutation changing stored information. Do not infer completion from a modal closing or a row disappearing from a filtered list.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Identify the setting or lookup and the application component that actually consumes it.
2. Inspect existing codes and historical use.
3. Create/edit the supported metadata or option deliberately.
4. Review label, code, sort order and status implications before saving.
5. Verify the consumer’s behaviour on the relevant release; coordinate code-owned list changes with engineering.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Lookup key/domain/field key | Identifies the configuration and intended consumer. | Normalised keys in UI; do not rename established codes without migration review. |
| Title/description | Human-readable explanation of the list. | Describe its actual use. |
| Allow Other/Other label | Whether a list supports additional explanation. | A flag alone does not create a companion form field. |
| Option code/label | Stable stored code and displayed wording. | Code can be non-editable on existing options; preserve historical meaning. |
| Sort order/status/system | Ordering and administrative behaviour. | Do not equate inactive with deleted; verify consumer treatment. |

The [field catalogue](settings-and-lookups-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](settings-and-lookups-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

An administrator adds a database reason but the current Meter Reading form uses its local shared list. The absence on the phone is a source-of-list mismatch, not a sync failure to be fixed by repeated edits.

## Exceptions, maturity and unresolved decisions

Map every lookup consumer before changing or retiring options. Common form standards must reference engineering rules rather than create a competing list authority.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-014:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/index.js#L1) | `ireps-mobile/app/(tabs)/admin/settings/index.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-016:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/create.js#L1) | `ireps-mobile/app/(tabs)/admin/settings/select-lookups/create.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-017:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/option.js#L1) | `ireps-mobile/app/(tabs)/admin/settings/select-lookups/option.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-015:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/settings/select-lookups/[lookupKey].js#L1) | `ireps-mobile/app/(tabs)/admin/settings/select-lookups/[lookupKey].js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-091:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/lookups/constants.js#L1) | `ireps-web/functions/lookups/constants.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-092:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/lookups/index.js#L1) | `ireps-web/functions/lookups/index.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-093:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/lookups/onIrepsSelectLookupAdminCallable.js#L1) | `ireps-web/functions/lookups/onIrepsSelectLookupAdminCallable.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-094:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/lookups/onIrepsSelectOptionsCallable.js#L1) | `ireps-web/functions/lookups/onIrepsSelectOptionsCallable.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-095:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/lookups/serializers.js#L1) | `ireps-web/functions/lookups/serializers.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-096:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/lookups/validators.js#L1) | `ireps-web/functions/lookups/validators.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-062:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/ui-rules/field-form-dropdowns.md#L1) | `ireps-rules/ui-rules/field-form-dropdowns.md` | main / `f5dc84e44c9f` | clean |
