# Informal ERF Capture — Practical Examples and Assessment

Module **FRM-012** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../01-body-of-knowledge/informal-erf-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/informal-erf-user-manual.md) · [Field catalogue](../01-body-of-knowledge/informal-erf-field-catalogue.md) · [Error register](../01-body-of-knowledge/informal-erf-error-register.md) · [Practical examples](informal-erf-scenarios.md)

All examples use synthetic identities and are review exercises, not evidence of a passed runtime test.

## Scenario 1 — Explain the business event

A meter is outside a mapped boundary but serves an already known flat. Keep the served premise association; do not automatically create an informal ERF around the kiosk.

**Learner task:** identify the subject, event, evidence and next handoff.

**Expected answer:** Informal ERF Capture records an operational geographic context where a usable formal ERF cannot be identified. Separate the submitted record from any physical, credential, work or billing outcome it does not prove.

## Scenario 2 — Wrong context

The form opens with a similarly named person, premise, meter or work item from the wrong operational context.

**Expected action:** stop before submission, verify the actual reference and authorised workbase, and use the correct route. For premise/meter tasks, inspect the individual unit and service even when the ERF or enclosure is shared. For account tasks, verify the UID and effective sign-in address.

## Scenario 3 — Conditional data

The learner changes a parent selection or attempts to submit with required information missing.

**Expected action:** use the field catalogue to identify the dependent controls, allowed values and evidence. Do not retain a now-inapplicable value simply to satisfy an unrelated validator.

**Module focus:** Boundary points — At least 3 valid unique latitude/longitude points; source rounds comparison to 7 decimal places.

## Scenario 4 — Uncertain outcome

The request starts, then the connection is lost before the result is displayed.

**Expected action:** retain the original identifier and evidence, establish whether the operation reached the server and follow the verified recovery route. Do not create another meter, user, charge or transaction merely because a response was late. For planned forms, specify how this must work before implementation.

## Scenario 5 — Review the implementation boundary

Operational geometry must not be described as cadastral proof. Confirm overlap handling, queue recovery and server validation on the intended release.

**Expected action:** state exactly what is observed source, what is documented policy, what is proposed and what a named-environment test still needs to demonstrate.

## Assessment record

For each scenario record: actor and scope; initial record state; inputs and evidence; expected request/result; actual persisted outcome; source/build; reviewer; unresolved discrepancy. Passing requires correct identity/context, truthful outcomes, no fabricated evidence, safe reconciliation of uncertainty and clear explanation of the module-specific gap. No production pass is recorded by this document.
