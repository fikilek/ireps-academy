# Operational Teams — Body of Knowledge

Module **FRM-024** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](operational-teams-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/operational-teams-user-manual.md) · [Field catalogue](operational-teams-field-catalogue.md) · [Error register](operational-teams-error-register.md) · [Practical examples](../10-assessments/operational-teams-scenarios.md)

## Meaning and purpose

Operational Teams organises eligible people for assignment and work management.

Create, rename, add member, remove member and delete are distinct operations on the same team family. Team membership does not itself prove permission to execute every transaction or erase existing task assignments.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

Administrative actions can affect many people or records. Their scope, actor and result need explicit verification. A filter changing what is visible is different from a mutation changing stored information. Do not infer completion from a modal closing or a row disappearing from a filtered list.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Select the correct provider/workbase context.
2. Create or choose a team and verify its members.
3. Use the intended membership or naming action.
4. Review any dependencies before a destructive team action.
5. Confirm the result and inspect relevant allocations separately.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Team name | Human-readable team identifier. | Client/server naming rules apply; do not assume globally unique display names. |
| Member | Eligible person to add or remove. | Use actual permitted user options; do not substitute free text. |
| Team/action | Team and mutation being requested. | Check the exact action and outstanding assignments before deletion. |

The [field catalogue](operational-teams-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](operational-teams-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

Removing a fieldworker from a team does not prove every previously accepted job was reassigned. Check the affected allocations through their own workflow.

## Exceptions, maturity and unresolved decisions

Verify eligibility, deletion guards and assignment effects in the target release. The form inventory records both mobile and web implementations.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-012:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/teams.js#L1) | `ireps-mobile/app/(tabs)/admin/operations/teams.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-162:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/OperationalTeamsPage.jsx#L1) | `ireps-web/src/pages/operations/OperationalTeamsPage.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-146:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/callables.js#L1) | `ireps-web/functions/teams/callables.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-147:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/field-work-summary.js#L1) | `ireps-web/functions/teams/field-work-summary.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-148:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/fieldWorkSummaryCallable.js#L1) | `ireps-web/functions/teams/fieldWorkSummaryCallable.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-149:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/helpers.js#L1) | `ireps-web/functions/teams/helpers.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-150:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/teams/member-history.js#L1) | `ireps-web/functions/teams/member-history.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
