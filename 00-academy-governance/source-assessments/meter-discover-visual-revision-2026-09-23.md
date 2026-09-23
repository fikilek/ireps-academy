# Meter Discover visual and terminology revision — 23 September 2026

Status: **version 0.2 review draft**. This supplements the original [source baseline](meter-discover-source-baseline-2026-09-23.md); it does not claim an application release or new runtime behaviour.

## Owner corrections implemented

- Show the municipality, ward and ERF, then the Property Type grouping, individual premises and their meters. Flats show Flat 1 through Flat 4, each with electricity and water where present. The Complex example includes separate named complexes and their units.
- Provide separate examples for all 12 current Property Type values. Distinguish conceptual type/name grouping from persisted Premise records; do not add a database parent by drawing a box.
- Replace the ambiguous outside-ERF chart with a spatial site plan: two bounded ERFs, houses, roadside verge, shared kiosk, two individual meters and explicit serves arrows. Record meter GPS at the equipment.
- Add eight paired, explicitly AI-generated placement plates beneath the placement table, with recognition cues, confusions and sample comments. The plates are teaching illustrations, not actual field photographs. Retain the prompt and file checksum in the media register.
- Use **Normal Path** and **Sales Path** consistently. Add both terms to the master dictionary, retaining every pre-existing term. Verbatim technical codes and error messages remain unchanged.

## Additional source evidence

- **MD-VS01**: `C:/dev/ireps-mobile/src/features/premises/formPremise.js`; branch `feature/meter-normalisation-v1`; commit `c8a5dbcaa041a1546235a27e15e3e5f1c65d3a21`; SHA-256 `1abc8b3d0d2409afa0fd37e7109f8071a391f5a4446d76ec2ef2e979a56d8cfa`.
- **MD-VS02**: `C:/dev/ireps-mobile/src/features/premises/premiseRepeatability.js`; branch `feature/meter-normalisation-v1`; commit `c8a5dbcaa041a1546235a27e15e3e5f1c65d3a21`; SHA-256 `76d81986b4e0644a88be084e28e38a6f437b714db18ae2364ac43b318b09c63f`.

The form lists Residential, Commercial, Industrial, Sectional Title, Townhouse Complex, Vacant Land, Flats, Estate, Church, School, Government and Backroom. Select... is excluded as a placeholder. The helper defines Flats, Townhouse Complex, Sectional Title, Backroom, Commercial, Industrial and Estate as repeatable; the other five choices are not repeatable through Duplicate Premise. Property Name and Unit Number are attributes, not new intermediate collections.

## Remaining interpretation and review boundaries

The owner requested property-type grouping in the teaching diagrams. The inspected storage model still attaches each individual premise directly to its ERF. No application hierarchy or validation has been changed. The diagrams include types and illustrative property names as visual groupings only.

Inside Property can overlap Kiosk, Wall Indoors and other more specific mounting descriptions. This revision explains that overlap instead of inventing a mutually exclusive runtime rule. A shared/bulk meter is not duplicated onto every unit to match a simplified diagram. Water placement, permission inheritance, offline handling and QA questions remain open.

Actual South African field photographs with appropriate provenance are still needed for a field-photo collection. The included realistic illustrations are clearly identified as generated. No production customer data or externally sourced photograph was imported.

## Verification

All 16 Mermaid diagrams in the revised module were rendered in a local browser preview. The revised flats and complex hierarchies and the outside-ERF SVG were visually inspected. Placement plates are reviewed for placement recognition and visible generated-image labelling. Link/anchor, media-checksum, register coverage, field/error catalogue and exact Git-change checks accompany integration. These are documentation/media checks; no application deployment or live-data test was performed.
