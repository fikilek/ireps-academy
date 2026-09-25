# Email Verification — Field Catalogue

Module **FRM-006** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](email-verification-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/email-verification-user-manual.md) · [Field catalogue](email-verification-field-catalogue.md) · [Error register](email-verification-error-register.md) · [Practical examples](../10-assessments/email-verification-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Email | Displayed account text | Address being verified. | Inherited from authenticated account; not editable on this screen. | worker@example.org |
| Resend/check actions | Action | Request a link or refresh verified state. | Source has a 30-second resend cooldown; backend limits may also apply. | Check verification |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

No literal input controls were extracted from the selected UI sources. This can mean an action/list-driven screen, a shared component boundary or a planned form; it is not proof that the workflow has no information requirements. See business definitions and source scope.

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Routing and mutation connectivity require release verification. Do not merge this with Password Reset or Change Sign-in Email.
