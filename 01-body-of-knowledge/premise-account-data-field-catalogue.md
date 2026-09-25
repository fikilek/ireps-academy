# Premise Account Data — Field Catalogue

Module **FRM-011** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](premise-account-data-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/premise-account-data-user-manual.md) · [Field catalogue](premise-account-data-field-catalogue.md) · [Error register](premise-account-data-error-register.md) · [Practical examples](../10-assessments/premise-account-data-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Accounts | Array of text identifiers | Municipal account numbers associated with the premise. | At least one; trim values and reject duplicates; preserve leading zeros. | 000123456 |
| Owner type | Controlled text | Determines which owner identity fields apply. | NATURAL_PERSON or JURISTIC_PERSON. | NATURAL_PERSON |
| Natural person | Structured text | Owner name, surname and optional identity data supported by the form. | Name and surname required in this branch; do not fabricate an ID. | Lebo Dlamini |
| Juristic person | Structured text | Registered name, registration number and trading name. | Registered name required; other requirements must follow the inspected schema. | Example Utility Services |
| Contacts | Text fields | Phone, WhatsApp and email for the represented person. | Treat these as contact data, not authentication credentials. | contact@example.org |
| Occupant is owner | Yes/no | Whether the occupant and owner represent the same person. | Conditional occupant section; do not overwrite owner facts to record a tenant. | no |
| Evidence | Media list | Supporting account/premise evidence. | Record only needed information; synthetic data in Academy examples. | Training account image |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-011-C001 — value

- **Meaning:** Source control for value; interpret in the business definitions and its enclosing section.
- **UI binding:** `value`; component `TextInputProxy`; input hint `keyboardType`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `onChangeText`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-047:544](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L544).

### FRM-011-C002 — NAv

- **Meaning:** Source control for NAv; interpret in the business definitions and its enclosing section.
- **UI binding:** `value &#124;&#124; ""`; component `TextInput`; input hint `keyboardType`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `onChangeText`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-047:559](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L559).

### FRM-011-C003 — Municipal Account Number

- **Meaning:** Source control for Municipal Account Number; interpret in the business definitions and its enclosing section.
- **UI binding:** ``accounts.${index}.accountNo``; component `FormInputAccountNo`; input hint `FormInputAccountNo`.
- **Visibility/prerequisites:** `isFormOpen; conditional branch: isEditingExistingAccount`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-047:1411](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L1411).

### FRM-011-C004 — Registered Name

- **Meaning:** Source control for Registered Name; interpret in the business definitions and its enclosing section.
- **UI binding:** `values.owner.juristicPerson.registeredName`; component `TextField`; input hint `TextField`.
- **Visibility/prerequisites:** `isFormOpen; conditional branch: values.owner.ownerType === "JURISTIC_PERSON"`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => setFieldValue("owner.juristicPerson.registeredName", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-047:1491](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L1491).

### FRM-011-C005 — Registration Number

- **Meaning:** Source control for Registration Number; interpret in the business definitions and its enclosing section.
- **UI binding:** `values.owner.juristicPerson.registrationNumber`; component `TextField`; input hint `TextField`.
- **Visibility/prerequisites:** `isFormOpen; conditional branch: values.owner.ownerType === "JURISTIC_PERSON"`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => setFieldValue("owner.juristicPerson.registrationNumber", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-047:1497](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L1497).

### FRM-011-C006 — Trading Name

- **Meaning:** Source control for Trading Name; interpret in the business definitions and its enclosing section.
- **UI binding:** `values.owner.juristicPerson.tradingName`; component `TextField`; input hint `TextField`.
- **Visibility/prerequisites:** `isFormOpen; conditional branch: values.owner.ownerType === "JURISTIC_PERSON"`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => setFieldValue("owner.juristicPerson.tradingName", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-047:1502](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L1502).

### FRM-011-C007 — Name

- **Meaning:** Source control for Name; interpret in the business definitions and its enclosing section.
- **UI binding:** `values.owner.naturalPerson.name`; component `TextField`; input hint `TextField`.
- **Visibility/prerequisites:** `isFormOpen; conditional branch: values.owner.ownerType === "JURISTIC_PERSON"`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => setFieldValue("owner.naturalPerson.name", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-047:1510](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L1510).

### FRM-011-C008 — Surname

- **Meaning:** Source control for Surname; interpret in the business definitions and its enclosing section.
- **UI binding:** `values.owner.naturalPerson.surname`; component `TextField`; input hint `TextField`.
- **Visibility/prerequisites:** `isFormOpen; conditional branch: values.owner.ownerType === "JURISTIC_PERSON"`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => setFieldValue("owner.naturalPerson.surname", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-047:1516](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L1516).

### FRM-011-C009 — ID Number

- **Meaning:** Source control for ID Number; interpret in the business definitions and its enclosing section.
- **UI binding:** `values.owner.naturalPerson.idNumber`; component `TextField`; input hint `TextField`.
- **Visibility/prerequisites:** `isFormOpen; conditional branch: values.owner.ownerType === "JURISTIC_PERSON"`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => setFieldValue("owner.naturalPerson.idNumber", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-047:1522](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L1522).

### FRM-011-C010 — Phone

- **Meaning:** Source control for Phone; interpret in the business definitions and its enclosing section.
- **UI binding:** `values.owner.contact.phone`; component `TextField`; input hint `phone-pad`.
- **Visibility/prerequisites:** `isFormOpen`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => setFieldValue("owner.contact.phone", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-047:1531](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L1531).

### FRM-011-C011 — WhatsApp

- **Meaning:** Source control for WhatsApp; interpret in the business definitions and its enclosing section.
- **UI binding:** `values.owner.contact.whatsapp`; component `TextField`; input hint `phone-pad`.
- **Visibility/prerequisites:** `isFormOpen`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => setFieldValue("owner.contact.whatsapp", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-047:1537](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L1537).

### FRM-011-C012 — Email

- **Meaning:** Source control for Email; interpret in the business definitions and its enclosing section.
- **UI binding:** `values.owner.contact.email`; component `TextField`; input hint `email-address`.
- **Visibility/prerequisites:** `isFormOpen`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => setFieldValue("owner.contact.email", value)`.
- **Validation:** `string().email("Invalid email")`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-047:1543](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L1543).

### FRM-011-C013 — Name

- **Meaning:** Source control for Name; interpret in the business definitions and its enclosing section.
- **UI binding:** `values.occupant.name`; component `TextField`; input hint `TextField`.
- **Visibility/prerequisites:** `isFormOpen`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => setFieldValue("occupant.name", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-047:1591](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L1591).

### FRM-011-C014 — Surname

- **Meaning:** Source control for Surname; interpret in the business definitions and its enclosing section.
- **UI binding:** `values.occupant.surname`; component `TextField`; input hint `TextField`.
- **Visibility/prerequisites:** `isFormOpen`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => setFieldValue("occupant.surname", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-047:1596](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L1596).

### FRM-011-C015 — ID Number

- **Meaning:** Source control for ID Number; interpret in the business definitions and its enclosing section.
- **UI binding:** `values.occupant.idNumber`; component `TextField`; input hint `TextField`.
- **Visibility/prerequisites:** `isFormOpen`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => setFieldValue("occupant.idNumber", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-047:1601](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L1601).

### FRM-011-C016 — Relationship to Owner

- **Meaning:** Source control for Relationship to Owner; interpret in the business definitions and its enclosing section.
- **UI binding:** `values.occupant.relationshipToOwner`; component `TextField`; input hint `TextField`.
- **Visibility/prerequisites:** `isFormOpen`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => setFieldValue("occupant.relationshipToOwner", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-047:1606](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L1606).

### FRM-011-C017 — Phone

- **Meaning:** Source control for Phone; interpret in the business definitions and its enclosing section.
- **UI binding:** `values.occupant.contact.phone`; component `TextField`; input hint `phone-pad`.
- **Visibility/prerequisites:** `isFormOpen`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => setFieldValue("occupant.contact.phone", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-047:1613](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L1613).

### FRM-011-C018 — WhatsApp

- **Meaning:** Source control for WhatsApp; interpret in the business definitions and its enclosing section.
- **UI binding:** `values.occupant.contact.whatsapp`; component `TextField`; input hint `phone-pad`.
- **Visibility/prerequisites:** `isFormOpen`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => setFieldValue("occupant.contact.whatsapp", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-047:1619](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L1619).

### FRM-011-C019 — Email

- **Meaning:** Source control for Email; interpret in the business definitions and its enclosing section.
- **UI binding:** `values.occupant.contact.email`; component `TextField`; input hint `email-address`.
- **Visibility/prerequisites:** `isFormOpen`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => setFieldValue("occupant.contact.email", value)`.
- **Validation:** `string().email("Invalid email")`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-047:1625](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/FormAccountData.js#L1625).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Blank-to-NAv transformations exist in source. Unknown, not applicable and unavailable need precise interpretation rather than guessed values. A network-unavailable submit can enter a separate account-data queue.

[Download the detailed control inventory (CSV)](premise-account-data-field-catalogue.csv).

[Inspect the extracted client validation expressions (CSV)](premise-account-data-validation-evidence.csv). Expressions preserve nested conditions; extraction is not a claim that every backend check is mapped.
