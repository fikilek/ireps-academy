# Meter Retirement and Disposal — User Manual

Module **FRM-039** · Baseline **25 September 2026** · Application: **Planned; no implemented form found**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/meter-disposal-body-of-knowledge.md) · [User Manual](meter-disposal-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/meter-disposal-field-catalogue.md) · [Error register](../../01-body-of-knowledge/meter-disposal-error-register.md) · [Practical examples](../../10-assessments/meter-disposal-scenarios.md)

## Before you start

This is an owner-directed future module. The source inventory did not establish an implemented capture form for this stage. Teaching focuses on business meaning, evidence and design questions, not invented app steps.

No operational iREPS screen has been established for this planned stage. The following is a proposed business procedure for discussion, not button-by-button app instructions.

## Procedure

1. Review identity, history, condition and any unresolved investigation.
2. Record retirement/disposition authority and its reason.
3. Select the approved disposal route and preserve evidence of handover or destruction.
4. Reconcile stock, asset and commercial records through their owners.
5. Retain the meter identity and history after physical disposal.

## What to check in the result

The meter is removed in September but held for investigation until November. Its removal date, retirement decision and disposal date are three different events.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Agree state transitions, permissions, custody/financial audit, duplicate handling and evidence requirements. METER_VENDING is recognised by name but is excluded from the implemented generic lifecycle list; it returns LCT_TYPE_NOT_IMPLEMENTED there.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/meter-disposal-error-register.md) and [field catalogue](../../01-body-of-knowledge/meter-disposal-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/meter-disposal-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
