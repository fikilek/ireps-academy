# Meter Reading Staging and Export — Body of Knowledge

Module **FRM-032** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](reading-staging-body-of-knowledge.md) · [User Manual](../02-user-manual/web/reading-staging-user-manual.md) · [Field catalogue](reading-staging-field-catalogue.md) · [Error register](reading-staging-error-register.md) · [Practical examples](../10-assessments/reading-staging-scenarios.md)

## Meaning and purpose

Meter Reading Staging prepares captured conventional readings for review and delivery to an external billing system.

Reading capture, staging generation, review and download are separate events. The web source has a staging-generation action, a controller and staging/registry views. A downloaded file is not proof that the receiving billing system imported it.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

Administrative actions can affect many people or records. Their scope, actor and result need explicit verification. A filter changing what is visible is different from a mutation changing stored information. Do not infer completion from a modal closing or a row disappearing from a filtered list.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Choose the correct municipality and billing period/session.
2. Review available reading population and exceptions.
3. Run the authorised staging action where offered.
4. Inspect the session’s counts, excluded/invalid readings and individual meter history.
5. Download the reviewed output in the supported format.
6. Record the handoff and receiving-system acknowledgement through the agreed process; reconcile rejected rows.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Municipality/workbase | Scope of the readings prepared. | Check the active workbase and explicit municipality code. |
| Billing period/session | Period and generation context. | A session is not simply the month displayed by a filter. |
| Generation controls | Initiates supported staging preparation. | Role and backend eligibility must be checked. |
| Export | Prepared readings for downstream use. | Verify counts/identity/units and receiving-system format; download is not import. |

The [field catalogue](reading-staging-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](reading-staging-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

The office generates 98 usable readings from 100 planned visits; two are No Access. The export contains reviewed readings, while the exceptions remain visible and the external billing team acknowledges its import.

## Exceptions, maturity and unresolved decisions

Owner states this module needs strengthening before production readiness. Automated billing-system integration and full customer billing remain future work. Do not invent an approval button where the page only filters or downloads.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-157:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/admin/MreadStagingControllerPage.jsx#L1) | `ireps-web/src/pages/admin/MreadStagingControllerPage.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-176:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L1) | `ireps-web/src/pages/registries/MreadRegistryPage.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-177:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadStagingPage.jsx#L1) | `ireps-web/src/pages/registries/MreadStagingPage.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-097:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/constants.js#L1) | `ireps-web/functions/registry/mread/constants.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-098:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/generateMreadStaging.js#L1) | `ireps-web/functions/registry/mread/generateMreadStaging.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-099:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/index.js#L1) | `ireps-web/functions/registry/mread/index.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-100:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/listMreadStagingCycles.js#L1) | `ireps-web/functions/registry/mread/listMreadStagingCycles.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-101:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/listMreadStagingRows.js#L1) | `ireps-web/functions/registry/mread/listMreadStagingRows.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-102:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/listMreadStagingSessions.js#L1) | `ireps-web/functions/registry/mread/listMreadStagingSessions.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-103:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/mapTrnMreadToRegistryMread.js#L1) | `ireps-web/functions/registry/mread/mapTrnMreadToRegistryMread.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-104:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/mreadStagingCycleController.v2.js#L1) | `ireps-web/functions/registry/mread/mreadStagingCycleController.v2.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-105:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/rebuildRegistryMread.js#L1) | `ireps-web/functions/registry/mread/rebuildRegistryMread.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-106:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/registry/mread/writeRegistryMreadFromTrn.js#L1) | `ireps-web/functions/registry/mread/writeRegistryMreadFromTrn.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
