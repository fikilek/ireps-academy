# Meter Procurement — User Manual

Module **FRM-035** · Baseline **25 September 2026** · Application: **Planned; no implemented form found**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../../01-body-of-knowledge/meter-procurement-body-of-knowledge.md) · [User Manual](meter-procurement-user-manual.md) · [Field catalogue](../../01-body-of-knowledge/meter-procurement-field-catalogue.md) · [Error register](../../01-body-of-knowledge/meter-procurement-error-register.md) · [Practical examples](../../10-assessments/meter-procurement-scenarios.md)

## Before you start

Owner-directed lifecycle requirement. No implemented iREPS form for this stage was found in the inspected application source. The fields below are a discussion specification, not existing controls or storage keys.

No operational iREPS screen has been established for this planned stage. The following is a proposed business procedure for discussion, not button-by-button app instructions.

## Procedure

1. Record the approved requirement and technical/service need.
2. Link the purchase order, supplier and agreed quantities.
3. Record invoice, payment and delivery documentation as separate events.
4. Reconcile what was ordered with what was delivered and accepted.
5. Hand the accepted meter population to store receiving with serial identities where available.

## What to check in the result

Ten meters are ordered and nine arrive. Receipt records nine physical units and the discrepancy; it must not turn the order quantity into a ten-meter stock balance.

Record the returned identifier and actual result for this action. Where the action creates or updates stored information, re-open the intended record and inspect the outcome. A local save, upload progress indicator, confirmation of a request, or downloaded export must be described by its actual meaning.

## When something prevents completion

Agree record ownership, roles, approval, financial consequences, serial timing and integration. No production transaction type, runtime error codes or button sequence is claimed.

For a field validation error, correct the specific input and recheck its dependent evidence. For a permission or state refusal, resolve authority or record state through the responsible workstream. After a timeout or partial success, reconcile the original attempt before making a new one. Preserve identifiers and evidence; never publish credentials in an escalation.

[Consult the module error register](../../01-body-of-knowledge/meter-procurement-error-register.md) and [field catalogue](../../01-body-of-knowledge/meter-procurement-field-catalogue.md).

## Training exercise

[Use the practical scenarios and their expected evidence](../../10-assessments/meter-procurement-scenarios.md). Release-specific screenshots, all conditional branches and permission tests remain publication requirements.
