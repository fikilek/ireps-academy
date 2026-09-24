# Handover to iREPS Academy — the Sales Path and the Normal Path

| | |
| --- | --- |
| From | the Targeted Batches + Meter Normalisation chat |
| Date | 24 September 2026 |
| Owner's instruction | Document this first in the Meter Discovery Body of Knowledge, and second in the user manual: the Normal Path and the Sales Path, the tests, and the rules that were updated. It should feature extensively in both. |
| State of the work | Built, tested, **on DEV**. Not on TEST or LIVE |

## 1. What this is about, in one paragraph

A meter can be captured two ways. On the **Sales Path** the worker starts in **My Work Orders**, on a row of a Targeted Batch, and iREPS knows which Sales meter the work belongs to. On the **Normal Path** the worker starts at the ERF or the premise, and iREPS does not. Everything below follows from that one difference: what the worker is asked, what is filled in for them, and what iREPS can close afterwards. A week of the owner's DEV testing on **ERF 689** — one commercial ERF with thirteen businesses at a single street address — is what shaped it.

## 2. The two words

**There are exactly two names: the Sales Path and the Normal Path.** Nothing in any document, screen, button or message may call either of them anything else — not "other work", not "ordinary premise", not "batch work", not "outside the batch". The owner had to say this three times in one day. Please hold the line in the Academy material too.

## 3. What the worker actually sees

### 3.1 Starting from My Work Orders (the Sales Path)

| Button on the row | What happens |
| --- | --- |
| **Premise**, reading 0 | The **Premise Picker** opens (see 3.2) |
| **Premise**, reading 1 | That premise opens. Nothing is asked. The list opens scrolled to it, with it selected |
| **AST** | The Meter Discovery form opens with the **meter number filled in** |

### 3.2 The Premise Picker

The owner's name for it; use it everywhere. It opens when a row has no premise yet, and lists every premise on that row's ERF:

- each premise by its **unit name and unit number**, and under it either **Not joined** or the meter it is joined to;
- a premise already joined to another meter is **greyed and locked** — one premise belongs to one row;
- **New premise** makes one from scratch; **Copy a premise** copies one at the same address so only the name and number change. Both are joined to the row when submitted;
- with no premises on the ERF at all, the New premise form opens straight away.

**Why it exists:** at ERF 689 the worker made the first premise from row 1 and then duplicated it four times on the Premises screen to save typing. Those duplicates belonged to no row, and row 2's Premise button opened row 1's premise. A premise made or picked from a row now carries its row.

**On the premise form**, the **Unit Name** field reads **Business Name** when the property type is Commercial or Industrial.

### 3.3 Starting from a premise card (the Normal Path)

Tapping **Discover** on a premise card can lead to four different things:

| The premise | What the worker sees | Buttons |
| --- | --- | --- |
| Belongs to no batch row | Nothing — the form opens | — |
| Belongs to a row, and the row checks out | **Batch meter**: "This premise belongs to batch *TB* row *N* (meter *M*). Do this meter on the Sales Path or the Normal Path?" | Sales Path · Normal Path · Cancel |
| Belongs to a row that cannot be worked | **Batch meter**: the reason, the batch and row, then "This meter cannot be done on the Sales Path. Do it on the Normal Path?" | Normal Path · Cancel |
| Belongs to a row, but the check could not be made | **Batch meter**: "Could not check the batch meter. Check your connection." then the same question as the row above | Sales Path · Normal Path · Cancel |

A second tap while a check is running says **"Still checking the previous premise"**. The check gives up after **10 seconds**.

**Choosing the Sales Path** hands the work to the batch row: the form opens with the meter number filled in. **Choosing the Normal Path** does not, and **the meter number is deliberately left empty** — choosing it means *this is not that meter*, and a number filled in for a worker is a number that can be submitted without anyone reading the meter.

The same shape applies to adding a **premise** on an ERF a batch is working: on a good check the form opens with nothing asked, and only a failed check asks which path.

### 3.4 The work order card

The card reads the shop beside the address once the row has its premise — **26 OLDACRE ST, Thisa Fish and Chips, 4** — because thirteen rows at one address were otherwise indistinguishable. The search box matches **everything on the card**: meter number, the number found on site, ERF, the address line including the shop and unit number, the account number and the account holder's name.

## 4. The rules that changed

All in `C:\dev\ireps-rules\targeted-batches\targeted-batches-rules.md` unless stated otherwise.

| Version | What |
| --- | --- |
| **1.3.72** | `TB-R063` narrowed: a capture made from a batch row settles that row's Sales meter and nothing else. One capture at ERF 689 had closed all thirteen rows |
| **1.3.73** | **`TB-R067`** — a batch row and its premise: the Premise Picker, one premise to one row, a wrong join can be changed, Business Name for Commercial and Industrial |
| **1.3.74** | The batch rows search matches everything the card shows. This does not touch `TB-R042`, which is about batching, not about finding a row already batched |
| **1.3.75** | `TB-R063` asks the **batch row, then the premise, then the ERF**. Every form that follows a discovery — disconnection, removal, inspection, commissioning — settles only its own shop |
| **1.3.76** | **`TB-R068`** — what the worker is asked before a Meter Discovery, with an **Error Register** of every refusal |
| **1.3.77** | The **Premise Picker** is named; Premise on a row that has one just opens it; the premise list scrolls to it |
| **1.3.78** | The Sales Path and the Normal Path, in the words the worker reads. No third word for either |
| **1.3.79** | A check that could not be made still offers the Sales Path; the Normal Path never pre-fills the meter number |

Also relevant, from earlier in the same stream: **`MN-R001`** (meter normalisation — the finding, the locked instructions, an inspection correcting the meter record), **`UI-R003`** (local dropdowns, SAME on every field) and **`TB-R066`** (a replaced meter carries its batch row to the new meter).

## 5. The tests

**`MC-R001`** — `C:\dev\ireps-rules\logic-rules\meter-capture-permutations.md`. The owner's own table of **sixteen tests**, from four things that vary:

| Code | | |
| --- | --- | --- |
| **Erf** | `OME` one Sales meter in the ERF | `MME` many Sales meters in the one ERF |
| **Premise Origin** | `PO-SP` made on the Sales Path | `PO-NP` made on the Normal Path |
| **Meter Origin** | `MO-SP` form opened on the Sales Path | `MO-NP` opened on the Normal Path |
| **Meter Context** | `MC-SM` the number Sales expects | `MC-DM` a different number |

Sixteen tests give **four** answers, and a difference inside a group is a defect. Tests 0–7 run on a house ERF, 8–15 on a complex. The document holds the full table and where each test stands.

**`TP-001`** — `C:\dev\ireps-rules\test-plans\meter-discovery-test-plan.md`, the Meter Discovery runs (four squares × four findings, plus offline).

## 6. The Error Register

`TB-R068` carries **thirteen refusals** a worker can meet when starting a discovery from a premise card, each with what it means and what to do. Please fold them into `01-body-of-knowledge/meter-discover-error-register.md` and its CSV, in the worker's own words. In short: not linked to a batch meter · not in your work orders · the row is no longer on the batch · no longer allocated · Completed · the Sales record could not be checked · no longer on this ERF · not the batch meter's premise · this premise has no ERF · on another ERF · a meter is already linked · could not check, check your connection · batch details incomplete.

## 7. Where it goes

| Document | What to add |
| --- | --- |
| `01-body-of-knowledge/meter-discover-body-of-knowledge.md` | Sections 1–4: the two paths and why they differ, the Premise Picker, what iREPS can close and what it cannot, and the rules behind each |
| `01-body-of-knowledge/meter-discover-error-register.md` / `.csv` | Section 6 |
| `01-body-of-knowledge/meter-discover-rules-and-data.md` | Section 4, and the premise-carries-its-row link that everything now rests on |
| `02-user-manual/mobile/meter-discover-user-manual.md` | Section 3, written as steps a worker follows, with the two paths side by side |
| `02-user-manual/mobile/iREPS_Mobile_User_Manual.md` | A pointer to the above from the Meter Discovery section |

## 8. What is **not** settled — please do not document as fact

1. **A capture with no batch row and no premise link, on an ERF with several Sales meters.** iREPS still reads the whole ERF there. Which Sales meter an unlisted number replaced — by address, by account, by customer, or by nobody until the office says — is the owner's to settle. It is test **15** of `MC-R001`.
2. **Changing a wrong join.** The server does it and is tested; the phone does not offer it yet, because the window that asked *open or change* was taken out on the owner's instruction. Where it is offered from is open.
3. **Tests 1–6 and 8–15 of `MC-R001` have not been run.**
4. A premise joined to a row of **another batch** can still read *Not joined* in the Premise Picker; the server refuses the join, so the worker meets a refusal instead of seeing it greyed. A fix is proposed — tell the premise whenever a row takes it — and awaits the owner's go.

## 9. Where the code is

Branch `feature/meter-normalisation-v1`, in `C:\dev\ireps-mobile` and the worktree `C:\dev\ireps-web-normalisation` (Functions). On DEV (`ireps2`); not on TEST or LIVE. 448 phone tests and 672 Functions tests pass.
