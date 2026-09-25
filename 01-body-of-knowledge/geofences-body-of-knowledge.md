# Geofence Planning — Body of Knowledge

Module **FRM-025** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](geofences-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/geofences-user-manual.md) · [Field catalogue](geofences-field-catalogue.md) · [Error register](geofences-error-register.md) · [Practical examples](../10-assessments/geofences-scenarios.md)

## Meaning and purpose

Geofence planning defines an operational geographic boundary used to select or organise work.

A geofence is a work-planning object. It does not replace a municipal boundary, ward, legal ERF, premise or asset location. Mobile creation and web drawing/planning interfaces must be distinguished from read-only map filters.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

Administrative actions can affect many people or records. Their scope, actor and result need explicit verification. A filter changing what is visible is different from a mutation changing stored information. Do not infer completion from a modal closing or a row disappearing from a filtered list.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Choose the workbase and intended planning context.
2. Draw or select the supported boundary.
3. Enter its name and description and inspect included work.
4. Review geometry and overlapping operational areas.
5. Save and verify the stored boundary before using it in allocation.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Name | Operational name of the planning area. | Required where shown; use a meaningful local identifier. |
| Description | Reason/scope of the boundary. | Explain work-planning purpose, not legal ownership. |
| Geometry | Boundary used for planning. | Valid geometry and scope checks; inspect the rendered shape. |

The [field catalogue](geofences-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](geofences-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

A geofence crosses several ERFs for a reading route. Each meter retains its own premise and ERF identity even while assigned to that route.

## Exceptions, maturity and unresolved decisions

Geometry validation and role scope are release-specific. Do not interpret a boundary selection as allocation or acceptance of work.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-009:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/geo-fences.js#L1) | `ireps-mobile/app/(tabs)/admin/operations/geo-fences.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-159:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/GeoFencesPage.jsx#L1) | `ireps-web/src/pages/operations/GeoFencesPage.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-167:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/geofence-shared-ui.jsx#L1) | `ireps-web/src/pages/operations/geofence-shared-ui.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-160:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/GeofencePlanningLayers.jsx#L1) | `ireps-web/src/pages/operations/GeofencePlanningLayers.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-081:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/geofences/callables.js#L1) | `ireps-web/functions/geofences/callables.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-082:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/geofences/geofence-name.js#L1) | `ireps-web/functions/geofences/geofence-name.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-083:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/geofences/helpers.js#L1) | `ireps-web/functions/geofences/helpers.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-084:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/geofences/membership.js#L1) | `ireps-web/functions/geofences/membership.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-085:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/geofences/sales-batch-geometry.js#L1) | `ireps-web/functions/geofences/sales-batch-geometry.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-086:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/geofences/salesMembership.js#L1) | `ireps-web/functions/geofences/salesMembership.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-087:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/geofences/triggers.js#L1) | `ireps-web/functions/geofences/triggers.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
