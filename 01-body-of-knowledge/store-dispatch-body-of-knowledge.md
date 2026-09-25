# Store Check-out — Body of Knowledge

Module **FRM-037** · Baseline **25 September 2026** · Application: **Planned; no implemented form found**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](store-dispatch-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/store-dispatch-user-manual.md) · [Field catalogue](store-dispatch-field-catalogue.md) · [Error register](store-dispatch-error-register.md) · [Practical examples](../10-assessments/store-dispatch-scenarios.md)

## Meaning and purpose

Store Check-out transfers custody of specified stock to an installation service provider or another authorised recipient.

This is an owner-directed future module. The source inventory did not establish an implemented capture form for this stage. Teaching focuses on business meaning, evidence and design questions, not invented app steps.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

This stage extends the owner’s intended lifecycle beyond the currently demonstrated operational forms. Proposed records below are discussion requirements. Their identifiers, statuses and permissions need product agreement before an implementation or a production manual can be approved.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Identify the authorised job and recipient.
2. Select actual available serials from the named store.
3. Record the issue/dispatch document and receiver acknowledgement.
4. Distinguish physical handover from travel and arrival at site.
5. Reconcile the issued population to installed, unused returned and unresolved meters.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Store and recipient | Origin store and receiving provider/person. | Proposed; custody is distinct from employment role. |
| Meter list | Exact units handed over. | Proposed available-stock checks; no duplicate issue. |
| Issue/job reference | Why stock leaves and where it is intended to go. | Proposed link to intended premise/work order. |

The [field catalogue](store-dispatch-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](store-dispatch-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

Five meters are issued; three are installed and two return unused. The five-unit dispatch must reconcile to those outcomes rather than marking all five installed.

## Exceptions, maturity and unresolved decisions

Agree state transitions, permissions, custody/financial audit, duplicate handling and evidence requirements. METER_VENDING is recognised by name but is excluded from the implemented generic lifecycle list; it returns LCT_TYPE_NOT_IMPLEMENTED there.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

No implemented UI/backend source was found for this proposed stage. Evidence is the owner’s lifecycle briefing and the repository search scope.
