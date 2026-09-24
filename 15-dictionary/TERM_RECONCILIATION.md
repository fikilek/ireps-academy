# Dictionary reconciliation

Status: approved SPU correction applied; other comparisons remain review evidence.

- **SPU:** use the owner's exact name, **Super User**. All existing `Superuser` occurrences in the master were changed to that spelling.
- **Guest/GST:** not part of the current role catalogue. Historical source assessments may retain it as evidence of an old description.
- **Permissions:** the mobile glossary's numeric hierarchy does not establish inheritance; do not merge its authority claims as policy.
- **Offline terms:** definitions name concepts; common retry, acknowledgement and deletion rules remain undecided.
- **QA:** a planned module, not an available supervisor capability.
- **Technical glossary entries:** review against engineering sources before adoption. Do not automatically import assertions merely because they appeared in the older glossary.

The source-pack dictionary has one term heading absent from the current master: **Legacy Informal ERF ID**. Its source excerpt is retained below for review only; inclusion here does not approve its meaning or migrate live identifiers.

## Historical candidate — not an approved addition

### Term: Legacy Informal ERF ID

- **Acronym:** None

- **Simple meaning:** The older Informal ERF ID format retained only for retry compatibility.

- **Detailed explanation:** The legacy format is `IE-YYYYMMDD-hhmmss-XXXX` and does not contain a ward pCode. The callable may accept it only to preserve idempotent retries for pilot submissions created before Ward-Scoped Identity was introduced. New mobile submissions must use the current ward-scoped format.

- **Example:** `IE-20260724-225238-8629` may be accepted for a safe retry but must not be generated for a new Informal ERF.

- **Related terms:** Ward-Scoped Identity, Informal ERF Full ID, Idempotent Retry, Legacy Data

## Contribution rule

Propose additions and revisions against the one master dictionary, citing the owning rule or product decision. Preserve existing approved meanings unless the owner has agreed to change them. Application glossaries should link to the master; historical source packs remain provenance, not competing authorities.


## Confirmed entry-path terminology — 23 September 2026

Added **Normal Path** and **Sales Path** from the owner's direct correction. The Meter Discovery Body of Knowledge, user manual, field catalogue, scenarios and explanatory data guide use these names. The 412 pre-existing term headings are preserved; the master now contains 414. Existing runtime identifiers and quoted error messages are not renamed.


## Confirmed module name — 24 September 2026

The owner confirmed **Meter Discovery** as the canonical module name. Academy titles, references and the existing Meter Discovery dictionary entry use that name. Existing file paths, links, source fingerprints and runtime identifiers remain unchanged.
