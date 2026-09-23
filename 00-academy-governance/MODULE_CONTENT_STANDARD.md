# Academy module content standard

Owner direction: 23 September 2026. First application: **Meter Discover**, module ID **MDIS**. Status: working content standard established from the owner's request; individual lessons still require review.

Every module has two connected legs. Its **Body of Knowledge** explains the subject comprehensively to field staff, supervisors, managers, administrators, technical contributors, utilities and prospective customers. Its **User Manual** explains how a person performs and checks a task in a specified application release. Neither leg substitutes for the other.

## Required outputs

| Output | Required content | Primary home |
| --- | --- | --- |
| Module entry document | Definition, purpose, scope, audiences, prerequisites, navigation and maturity | Body of Knowledge |
| Subject explanation | Physical and business context, vocabulary, relationships, boundaries, examples and misconceptions | Body of Knowledge |
| Workflow and decision diagrams | Every entry route, normal outcome, exception, handoff and return route | Body of Knowledge; referenced by manual |
| Field catalogue | Each field's label, meaning, path, type, source, visibility, prerequisites, requirement, default, allowed values, validation, evidence, transformation and example | Body of Knowledge reference |
| Controlled values and evidence matrix | Enumerations, reasons, dependencies, required photographs and their purpose | Body of Knowledge reference |
| Error register | Real code where one exists, exact message or identified variable template, trigger, stage, data state, remedy, escalation and source | Body of Knowledge reference; task remedies in manual |
| Rules and data lifecycle | Permissions, identities, outputs, integrations, offline states, acknowledgement, duplicate handling, audit and corrections | Body of Knowledge |
| User task guides | Start point, actor, steps, decisions, examples, expected result, result verification, exceptions and recovery | User Manual |
| Role and organisation matrix | Operational responsibilities separated from implemented permission checks; unresolved permissions visible | Body of Knowledge and manual |
| Worked scenarios | Electricity/water and relevant variants; ordinary, exceptional and failure cases | Both, with different emphasis |
| Review and acceptance pack | Source baseline, decision gaps, test scenarios, expected evidence and publication gates | Governance / assessments |
| Reusable derivatives | Video scripts, demonstrations, quick cards, FAQ and assessments derived from reviewed material | Existing Academy subject folders |

## Field-record requirements

Each field gets a stable Academy ID. A display label, storage key and business term can differ; record all three. A numeric-looking serial number remains text when leading zeros matter. Specify whether a value is observed, selected, inherited, calculated or supplied by the server. Distinguish a blank, zero, false, unknown and not applicable. State units only where defined; record an unresolved unit as a gap.

Describe validation at the relevant layer: input control, form schema, canonical payload, server and downstream processing. Do not label a field optional simply because the screen does not show an asterisk, or claim that a dropdown restriction is also enforced by the server without checking. Explain what switching a parent field clears or makes inapplicable. A helper input such as Other text may be folded into another field and never stored under its on-screen key.

## Error-record requirements

Academy reference IDs are navigation aids, never invented runtime error codes. Distinguish a local validation message, a structured server refusal, a timeout with an uncertain outcome, a storage/upload failure and a failure after server acceptance. A remedy must preserve evidence and avoid creating a second transaction merely to retry an uncertain first one. An error register cannot promise that nothing was saved unless the stage and implementation justify it.

## Evidence and status

Use four separate labels: **owner direction**, **documented rule**, **observed source behaviour**, and **verified behaviour in a named environment**. Each module names repository, branch, commit and relevant file hashes, plus any uncommitted source. Feature code and a test plan do not prove deployment or test completion. Record discrepancies instead of silently choosing a convenient version.

For publication, a reviewer must be able to trace each workflow, field and error to evidence, reproduce the instructions on the named release, inspect representative screens, and see which product questions are still open. Use synthetic examples in training. The master dictionary remains the single terminology authority; a module may explain terms but must link proposed dictionary changes for review.

## Meter Discover implementation

Begin at [Meter Discover — Body of Knowledge](../01-body-of-knowledge/meter-discover-body-of-knowledge.md). Its field catalogue, error register, data lifecycle, manual and acceptance scenarios form the first worked module package. This standard defines required outputs; it does not declare every output published or every future module complete.
