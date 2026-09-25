# Phone Verification — Field Catalogue

Module **FRM-007** · Baseline **25 September 2026** · Application: **Partial source foundation; service and release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](phone-verification-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/phone-verification-user-manual.md) · [Field catalogue](phone-verification-field-catalogue.md) · [Error register](phone-verification-error-register.md) · [Practical examples](../10-assessments/phone-verification-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Code | Text | Verification code received for the account phone. | Screen requires length 6 and numeric keyboard; backend verification hooks must exist. | Synthetic code only |
| Phone number | Displayed text | Number to which the code is expected to be sent. | Inherited from user record; not an editable contact form here. | Training fixture |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-007-C001 — Enter 6-digit code

- **Meaning:** Verification code received for the account phone.
- **UI binding:** `code`; component `TextInput`; input hint `number-pad`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `setCode`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-034:73](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/onboarding/verify-phone.js#L73).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

VerifyPhone and resendPhoneCode endpoints are not established by the optional-hook syntax. Delivery, expiry, attempt limits and routing remain acceptance gaps. The primary API exposes sendPhoneOtp and confirmPhoneOtp instead of the verifyPhone/resendPhoneCode names used by this screen.

[Download the detailed control inventory (CSV)](phone-verification-field-catalogue.csv).
