# Meter Discover — Body of Knowledge

**Module:** MDIS · **Content version:** 0.1 · **Status:** comprehensive first draft for review, 23 September 2026. The owner calls the module **Meter Discover**. Existing screens, rules and transaction records use **Meter Discovery** and `METER_DISCOVERY`; these names refer to the same module in this package. No application labels are renamed here.

This knowledge base explains what is being discovered, why it matters, where the meter belongs, how different routes converge, what evidence is collected and what happens to the resulting records. It serves prospective customers as well as every operational role. Source observations describe the [recorded development snapshots](../00-academy-governance/source-assessments/meter-discover-source-baseline-2026-09-23.md), not a certified production release.

## Read the module

| Part | What it answers |
| --- | --- |
| This document | What Meter Discover means, why it exists and how its physical and business context fits together |
| [Field catalogue](meter-discover-field-catalogue.md) | Every catalogued input and context field: meaning, type, prerequisites, validation and storage |
| [Rules and data lifecycle](meter-discover-rules-and-data.md) | Roles, server processing, record identities, offline states, retries, outputs and integrations |
| [Error register](meter-discover-error-register.md) | Validation messages, server codes, failure stages, remedies and escalation |
| [Mobile user manual](../02-user-manual/mobile/meter-discover-user-manual.md) | How to perform and verify a discovery or No Access visit |
| [Acceptance scenarios](../10-assessments/meter-discover-scenarios.md) | Worked cases, practical assessment and evidence needed before publication |
| [Source baseline and gaps](../00-academy-governance/source-assessments/meter-discover-source-baseline-2026-09-23.md) | Exactly what was inspected and what remains unverified |

## 1. What is being discovered?

Meter Discover records an **existing meter encountered in the field** and its relationship to the service location. It captures identity, electricity or water service, physical position, equipment description, observed connection status, findings and evidence. It creates a field record where one is needed; a meter can already be known in a Sales dataset without having been registered as an iREPS field asset.

Discovery is therefore more than photographing a number. The important questions are: which meter is this; which premise does it serve; which ERF contains that premise; where is the equipment actually mounted; what condition and connection state were observed; what was done or must follow; and what evidence supports those statements?

It is different from **installation**, which records putting a meter in place; **inspection**, which revisits a known asset; and **periodic meter reading**, which collects a reading for a defined operational or billing cycle. A discovery may record a water opening reading and may initiate linked disconnection or replacement work, but those activities have their own records. A completed discovery is not proof that every follow-on job has been completed.

### Audiences and questions

| Audience | Needs to understand |
| --- | --- |
| Prospective utility/customer | Asset-register coverage, evidence, field-to-office traceability and the limits of the current product |
| Field Worker | Correct location and premise, accurate capture, required evidence, truthful findings and the result of submission |
| Supervisor | Allocation, capture quality, conflicts, incomplete follow-on work and cases requiring a return visit |
| Manager | Coverage, exceptions, planned work, operational accountability and reliable inputs to revenue work |
| Administrator / Super User | Consistent organisation, access, reference data and terminology; these titles do not imply every field permission |
| Developer / support contributor | Payload, validation layers, identities, queue states, asynchronous processing and reproducible failures |

## 2. Why utilities need it

An asset register can be incomplete, contain outdated locations, or disagree with the equipment found on site. Commercial records can identify a meter that cannot yet be matched reliably to a field asset. A meter may be connected but damaged, operating with a suspected bypass, or serving a different unit from the one a worker first assumed.

Discovery contributes a documented field observation that can help reconcile those records. Accurate meter identity and location support subsequent visits, maintenance, reading routes and investigations. Evidence of a condition supports a supervisor's review. A reason for not acting makes an unresolved task visible instead of implying it was resolved.

These are inputs to revenue protection and revenue enhancement. A discovery does not by itself calculate consumption charges, prove a quantified loss, create a customer invoice or establish a legal conclusion about a customer. A recorded suspicion must remain distinguishable from a confirmed field finding and from the later outcome of an investigation. Full billing and automatic billing-system exchange remain outside this module's present scope.

## 3. The ERF, premise and meter relationship

In this context the property word is **ERF**, not electrical earth. An ERF identifies a land parcel in the geographical structure. A **premise** identifies the service location/address and property type on that ERF. A **meter** is attached to the premise in the application's record chain. A block of flats can have several premises on one ERF, each with its own service equipment.

```mermaid
flowchart TD
    LM[Local municipality] --> W[Ward]
    W --> E[ERF / land parcel]
    E --> P1[Premise: Flat 1]
    E --> P2[Premise: Flat 2]
    P1 --> E1[Electricity meter]
    P1 --> W1[Water meter]
    P2 --> E2[Electricity meter]
    E1 -. actual position .-> K[Shared kiosk outside the parcel]
```

The relationship is an **administrative/service association**, not a statement of legal ownership of the meter or land. Utility asset ownership, the customer account, the service point, the parcel and the mounting position are different concepts. This draft does not invent an asset-owner field where the inspected form has none.

The current submission path requires a saved parent premise. If that premise exists only as a local unsent draft, the meter capture must wait for its parent to be saved. Choosing the wrong premise is not repaired by placing a correct GPS pin: the association and position each need to be right.

### A meter can be outside the ERF it serves

Consider two houses served from a roadside kiosk. Their meters share a physical enclosure outside both property boundaries. Each meter still needs the correct premise/ERF association, its own identity and its actual position. Capturing both at the kiosk does not mean that both belong to the same premise. Conversely, forcing each pin to the centre of its house would misrepresent the equipment's physical location.

```mermaid
flowchart LR
    subgraph A[ERF A]
      PA[House A / premise A]
    end
    subgraph B[ERF B]
      PB[House B / premise B]
    end
    subgraph R[Roadside enclosure outside both ERFs]
      MA[Meter A]
      MB[Meter B]
    end
    MA -. service association .-> PA
    MB -. service association .-> PB
```

This is a conceptual illustration, not a surveyed layout or electrical connection drawing. The reviewed GPS validator checks coordinates; it does not establish that a pin lies inside its associated parcel. The map can show a boundary for orientation without making that boundary a capture restriction.

## 4. Understanding the physical environment

The electricity form offers the following placement choices. They describe where equipment is located; they do not grant access or authority to work on it.

| Placement | Interpretation for capture | Distinction to preserve |
| --- | --- | --- |
| Kiosk | Meter housed in a kiosk/enclosure, potentially shared | Identify the individual meter and served premise; the enclosure is not the meter identity |
| Pole Top | Equipment mounted high on a pole | Record the mounting context; discovery is not a climbing procedure |
| Pole Bottom | Equipment at the lower part/base area of a pole | Distinguish from nearby cabinets and other service meters |
| Boundary Wall | Mounted on or within a boundary wall | The side of the wall and served premise may need explanation |
| Meter Room | Dedicated room with one or several meters | Room location and the unit served are different facts |
| Wall Indoors | Mounted on an internal wall | Indoor position does not alone identify the correct unit or account |
| Inside Property | Located within the property where a more specific option does not describe it | Use field comments to remove ambiguity |
| Other | None of the listed choices is suitable | The inspected placement control has no separate required Other-description field; explain in Field Comment |

Water meters may be encountered in boxes, chambers or other arrangements. The inspected water discovery form captures GPS but **does not expose the electricity placement selector**. A water-specific placement/enclosure taxonomy remains a product-content gap. Do not teach an electricity-only field as though it appears on water.

A complete site explanation can distinguish the parcel, service address/unit, enclosure, mounting position, accessibility, neighbouring meters, serial-number visibility and the evidence used to associate the equipment with the premise. Some of these are structured inputs; others currently belong in an optional field comment. Record uncertainty rather than guessing an association or a serial number.

## 5. How a worker reaches a discovery

There are two principal business routes, with a local-draft recovery route. Both principal routes ultimately capture a meter **on a premise**.

```mermaid
flowchart TD
    N[Ordinary field discovery] --> E[Select correct ERF]
    S[Sales investigation] --> B[Office prepares and allocates batch]
    B --> A[Assigned team accepts work]
    A --> W[My Work Orders: open row / ERF]
    E --> P[Select or create the correct premise]
    W --> P
    P --> Q{Access available?}
    Q -->|No| NA[No Access reason and evidence]
    Q -->|Yes| T{Service type}
    T --> EL[Electricity capture]
    T --> WA[Water capture]
    EL --> V[Validate and submit]
    WA --> V
    NA --> V
    V --> R[Inspect actual save / submission result]
    D[Existing local draft] --> O[Reopen the same queue item]
    O --> V
```

### Ordinary route

A worker identifies the correct ERF, selects or creates its premise, then records electricity, water or No Access through the discovery action. This route can encounter a meter with or without a Sales record. It is not automatically free of batch restrictions: the backend can check the meter and ERF even when the worker did not enter through My Work Orders.

### Sales / Targeted Batch route

The office uses Sales information and location work to plan a batch; the assigned team accepts it. The worker follows a row to its ERF/premise. The carried context identifies the batch, row, Sales record and expected meter. The current planning rule uses batches of at most 30 meters; this is context for the route, not a limit on how many meters can physically exist on an ERF.

The expected Sales number is a lead. The worker must verify the actual number in the field. Recording the number that was expected when another meter is actually present would destroy the point of discovery. The expected and discovered identifiers must remain distinguishable.

| Situation | Capture and reconciliation meaning |
| --- | --- |
| Expected Sales meter is found | Record its actual identity; matching field/Sales links can make it VISIBLE and complete the applicable work |
| Different meter is found at the expected ERF | Record the meter actually found. The newer batch rules include a specific different-meter outcome; they must not falsely claim the expected serial was physically found |
| Meter is found outside a batch and has a Sales match | Field capture can establish the missing field link; any batch effects remain subject to ownership and correlation checks |
| Meter has no Sales match | It can be a valid field asset with no Sales link; INVISIBLE does not mean nonexistent |
| No Access | Record the attempted visit and its evidence; do not invent an asset identity or count the meter as physically discovered |

The source baseline records differences between application branches. Batch closure, different-meter attribution and replacement handoff must be verified together before this route is taught as an accepted release. The backend's batch-context validator directs a No Access visit to the dedicated Targeted Batch No Access action; the diagram shows the business outcome, not a claim that every route shares one submission endpoint.

## 6. What is observed and captured

The [field catalogue](meter-discover-field-catalogue.md) is the detailed reference. The form combines these families:

1. **Visit and parent context:** access outcome, reason where access failed, ERF, premise, address, geography and provider context.
2. **Identity and description:** meter number, manufacturer, model, service, subtype, category and electricity phase.
3. **Location:** the actual GPS position and, for electricity, placement.
4. **Associated equipment:** electricity seal, prepaid keypad and circuit breaker, with reasons/evidence where applicable.
5. **State and readings:** connected/disconnected state, water creation reading or token reading, and prepaid remaining credit.
6. **Findings and response:** anomaly, detail, additional anomalies, electricity normalisation actions and reasons when expected work is not undertaken.
7. **Evidence and commentary:** tagged photographs plus optional text, photo, voice and video comments.
8. **System record:** transaction identity, authenticated actor/time, route correlation, queue state and server-derived references.

Some controls contain numeric-looking strings. Meter numbers must preserve leading zeros. Remaining credit is stored as a signed decimal string; a zero value is different from a missing value. The form does not establish a universal credit unit, so the lesson must not silently describe every value as rand or kWh. Water token reading and remaining credit are separate inspected inputs whose business distinction needs confirmation.

## 7. Connection state, finding, response and visibility

These are independent dimensions. **Connected/Disconnected** records the observed connection state. **Meter Ok/Faulty/Damaged/Illegally Connected** records the finding. **Normalisation** records on-site actions or the follow-on work requested. **VISIBLE/INVISIBLE** reflects the field/Sales linkage. A connected meter can be faulty; a meter described as Meter Ok can still carry a bridge or bypass suspicion; a VISIBLE meter can still need work.

### Findings

| Finding | Details offered in the inspected list |
| --- | --- |
| Meter Ok | Operationally Ok; Bridge Suspicion; Bypass Suspicion |
| Meter Faulty | Not Accepting Sgc Tokens; Meter Display Blank; Negative Credit Units; Zero Reading - Conventional Meter; Meter Wheel Not Moving; Meter Wheel Running In Reverse |
| Meter Damaged | Meter Number Not Clearly Visible; Meter Burnt; Meter Button(s) Not Working; Meter Broken |
| Illegally Connected | Straight Connection (Meter Bypassed); Bridge Wire On The Meter |

These labels are reproduced as application vocabulary, including spelling. A suspicion remains a suspicion. The common list includes electricity-oriented details in a shared component; water applicability needs review rather than assuming every listed detail makes physical sense for every water meter.

Additional anomalies are independent selections: Meter Blocked (By Munic), Meter Bridged (By Munic), Incomplete Service Points, Meter Not Registered and Keypad Faulty. Their presence does not replace the primary finding/detail.

### Electricity normalisation and follow-on work

```mermaid
flowchart TD
    F{Observed finding} -->|Meter Ok| O[None or on-site fix]
    F -->|Illegally Connected| D[Expected job: Disconnect meter]
    F -->|Faulty or Damaged| X[Expected job: Replace meter]
    D --> Q{Expected job selected?}
    X --> Q
    Q -->|No| R[Record reason for not acting]
    Q -->|Yes| S[Submit discovery first]
    S --> M[Wait for created meter record]
    M -->|Disconnect| DC[Separate disconnection form]
    M -->|Replace| RM[Separate removal form]
    RM --> IN[Separate installation form]
```

In the examined mobile feature, selecting a finding preselects its expected action. A worker must still confirm what will actually be done. None is offered only for Meter Ok. When every action is unticked on another finding, the form can still encode `none` internally together with the required reason; the hidden menu choice and the stored no-action representation are different. On-site fixes are Tamper removed, Keypad normalised, Service point completed and Meter registered. A finding cannot request both Disconnect meter and Replace meter in the same action list.

If the expected job is not selected, a reason is required even when a different action or an on-site fix is selected. Current reasons include threat, refusal, unsafe conditions, inability to reach the meter, lack of a replacement, office instruction and Other with an explanation. These choices document the situation; they do not authorise a physical intervention.

The original finding and the meter's later operational condition can differ. The newer normalisation rules describe a projection reflecting what was left after a fix, while the transaction retains what was found. Discovery, removal, installation and disconnection need linked records so a report can distinguish intention from completed work. QA/correction policy is still open and must not be inferred from these links.

The water form does not offer this electricity normalisation workflow. Do not promise an automatic water replacement chain from this screen.

## 8. Evidence and quality

A photograph must support a specific statement. The serial photograph identifies the meter; an anomaly photograph supports the finding; a seal/keypad/circuit-breaker photograph supports the corresponding captured value or evidence-requiring reason. A general scene photograph cannot automatically substitute for a required tagged photograph.

All anomaly details except Operationally Ok require an anomaly photo in the inspected contract, including Bridge Suspicion and Bypass Suspicion. Selecting only a disconnection or replacement job does not require a normalisation photo in the newer feature: the separate job forms provide their own evidence. An on-site fix does require proof. See the catalogue for the complete evidence matrix and branch compatibility warning.

Evidence presence is not evidence quality. A tagged image can pass a technical presence check while being blurred or showing the wrong meter. The proposed review standard is to check legibility, relevance, consistent identity, location context and the relationship between the finding and its proof. This is a content quality recommendation, not a claim that an automated QA module currently performs these checks.

The actual meter position and a photograph's capture/fallback position need not be the same. A manually confirmed map pin is not proof that the device physically stood there. No GPS accuracy threshold or parcel-containment guarantee was found in the discovery validator.

## 9. What completion means

Use three checkpoints:

| Checkpoint | Meaning |
| --- | --- |
| Saved locally | A device queue record exists; server acceptance is not established |
| Server accepted | The discovery transaction was accepted or the same transaction was already present |
| Derived work available | The asset/master/registry and relevant Sales or batch effects are visible, and any follow-on work can be opened or checked |

The backend uses asynchronous processing after transaction creation. A success response does not guarantee that every derived view has already updated. The phone may wait up to 20 seconds for the meter before opening follow-on work; if the record is not ready it directs the worker to the meter card. A missing derived record should be investigated with the transaction ID rather than creating a second discovery.

The inspected form also reuses a generic success display after some local-save outcomes. Read the specific result message and queue/server state; a green icon alone does not establish server submission. The [rules and data lifecycle](meter-discover-rules-and-data.md) explains the different offline branches and why a timeout does not cancel a request already in flight.

## 10. Examples and boundaries

**Shared roadside kiosk.** Record the serial found, associate it with the correct house/unit, place the pin at the kiosk, choose Kiosk and explain any ambiguity. Nearby ERF geometry is orientation, not proof of the service association.

**A damaged meter with an unreadable number.** The anomaly list allows that finding, but an accessed discovery still requires a valid identifier. Do not manufacture one or type NAv to force the form through. Escalate the identification case; the supported unidentified-meter workflow needs a product decision.

**A different meter at a Sales address.** Keep the expected Sales number in the route context and capture the actual physical number. The different-meter outcome can explain why an expected Sales visit is closed without claiming the expected meter was found. Multi-premise/shared-enclosure cases need careful correlation review.

**Access refused.** Capture No Access, an appropriate reason and required evidence. This is a visit transaction, not an asset discovery or proof of a meter condition that could not be observed.

**Submission takes too long.** Retain the existing queued transaction and check its outcome. The server may have accepted it after the phone stopped waiting. Retrying the same transaction and creating a new transaction are different operations.

## 11. Boundaries and open decisions

The owner's unresolved permissions, common offline model, acknowledgement/local deletion and QA questions remain in the [decision register](../00-academy-governance/OWNER_DECISIONS.md). This module adds concrete cases: unreadable identifiers, water placement, water manufacturer Other, reading/credit units, mixed electricity/water anomaly choices, branch compatibility, ambiguous success messages and resuming follow-on work after background sync.

The first package supplies substantive reference content and tasks. Screen captures, role-by-role walkthroughs, verified device outcomes, recorded demonstrations and completed assessments remain publication work. It is comprehensive in its defined structure; it does not claim that unresolved behaviour or uninspected infrastructure errors have already been settled.

Use the [master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) for shared terminology. Proposed module-specific term changes must go through Academy rather than create a competing glossary.
