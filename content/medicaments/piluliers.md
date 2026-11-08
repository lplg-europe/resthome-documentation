---
modules: [healthcare_medication, healthcare_medical]
---

# Pillboxes and the pharmacy's sachets

:::{rh-description}
Prepare and check the residents' pillboxes in Resthome with four eyes, report an issue, take out what changed, and follow the pharmacy's sachets: delivery, recalled lot and return.
:::

:::{rh-faq}
How do I turn on pillbox tracking?
: In **Nursing Care → Configuration → Settings**, tick **Track the pillboxes**. Switched off, the Pillboxes tab, its buttons and its counters do not show.

Can the nurse who filled a pillbox also check it?
: No. **Checked** is refused to the hand that prepared the dose: another nurse or a physician checks it. Only the pharmacy's sachets can be checked by whoever received them.

What happens when a treatment changes after the pillbox was prepared?
: A dose whose medicine, dose or route changed is flagged **Changed after preparation** and blocked until it is prepared again. A dose that moved or stopped is flagged to take out of the box.

Who may give a dose when pillboxes are tracked?
: A care assistant gives only a dose that was prepared and has no issue. A nurse who gives a dose that was not prepared prepares it on the spot.

What do I do when the pharmacy recalls a lot?
: Open the delivery and click **Lot Recalled**. Every delivery of that lot in the house is recalled: its doses are blocked and its sachets go back. The pharmacy's new sachets take the doses, or a nurse prepares them.
:::

When the house prepares the residents' medicines in advance, each dose is
**prepared** by a nurse and **checked** by another, before the round
distributes it. When the pharmacy prepares them in a sachet per moment, the
sachets are **received** in the house and followed until they are used or go
back.

## Turning it on

Pillbox tracking is a setting: **Nursing Care → Configuration → Settings**,
**Track the pillboxes**. Once it is on:

- each dose records who prepared it and who checked it;
- a care assistant gives only a dose that was prepared and has no issue; a
  nurse who gives an unprepared dose prepares it on the spot;
- a dose with an issue, or missing, is blocked for everybody until it is
  prepared again.

Switched off, nothing of this page shows: no **Pillboxes** tab, no **Pillbox
Issues** counter, no **Tomorrow's Pillboxes** link.

## Preparing and checking at the desk

From the [Medicines workstation](index.md), **Tomorrow's Pillboxes** (or **The
Pillboxes** in the **Pillboxes** tab) opens tomorrow's doses, resident by
resident, in the order of the day. Opening it places tomorrow's doses when they
were not yet. The filters **Today**, **Tomorrow**, **To Prepare**, **To
Check**, **Issues** and **To Take Out** narrow the list.

1. Select the doses you put in the box and click **Prepared**: they are
   prepared now, by you.
2. Another nurse selects the doses checked against the treatments and clicks
   **Checked**. The doses you prepared yourself are left aside, and the message
   says what remains and why.
3. A dose that does not match: **Report an Issue** — *Wrong medicine*, *Wrong
   dose*, *Wrong moment*, *Dose missing*, *Dose in excess*. The dose is blocked.
4. Put it right, then click **Prepared Again** on the line: the check is to be
   done again.

The **Filled In** column says who filled the box: *The house* or *The
pharmacy*. A line is red when it has an issue or must be taken out, green once
checked. Nurses and physicians do these gestures; a care assistant sees no
pillbox button.

<!-- screenshot to add: the Pillboxes list with the Prepared, Checked and Report an Issue buttons -->

:::{admonition} On the phone too
:class: tip

The same preparation and check are done in the care app, on the Pillboxes
screen of the round. A dose prepared on the phone shows here, and the other
way round.
:::

## When a treatment changes after the preparation

- The medicine, the dose or the route changed: the dose gets the issue
  **Changed after preparation** and is blocked until it is prepared again.
- The moment moved, the dates or the frequency changed, or the treatment was
  stopped or suspended: the prepared dose is **To Take Out of the Box**. Take it
  out, then click **Taken Out**. The workstation lists these doses under **To
  take out of the pillboxes**.

A medicine missing when filling the box (**Missing From Stock**) enters the
pharmacy's basket. See [Pharmacy orders](pharmacie.md).

## The pharmacy's sachets

When the pharmacy prepares the medicines in a sachet per moment:

- **In the Pharmacy's Sachets** on the treatment says which medicines the
  sachets hold. A liquid, an *as needed* medicine, a dose prepared at the
  moment or a medicine marked **Never in the Pharmacy's Sachets** stay with the
  house.
- The sachets are **received in the care app**, on the Pillboxes screen: the
  delivery date, the days covered, the lot or series number printed on the
  sachet and the number of sachets. The doses they hold are marked as prepared
  by the pharmacy.

### The deliveries

From the workstation, **Pharmacy's Deliveries** (in the **Pharmacy** tab) or
the **Pharmacy's Deliveries** smart button of a resident lists the deliveries:
resident, pharmacy, **Delivered On**, **Sachets Until**, **Use By**, **Lot /
Series**, **Still to Give**, **To Return** and the state **Received**,
**Recalled** or **Returned**. Filters: **Received**, **Past the Use-By Date**,
**Recalled**, **Returned**. A delivery is never created by hand at the desk.

- **Lot Recalled** — every delivery of the same lot in the house is recalled:
  the doses they still hold are blocked and their sachets go back.
- **Returned to the Pharmacy** — choose the reason (*Treatment stopped*,
  *Resident in hospital*, *Resident deceased or gone*, *Past the use-by date*,
  *Lot recalled*, *Other*). The tab **Sachets Going Back** lists the sachets
  that leave, with what **replaced** them.
- **Return Slip** — the PDF to hand over with the sachets: resident, pharmacy,
  lot, reason, the sachets returned, and the signatures.

A returned sachet is never given again: it is the **dose** that returns to
prepare. The pharmacy's new sachets take it, in whatever order they arrive, or
a nurse prepares it with **Prepared Again**. The workstation shows **Sachets
to give back to the pharmacy** as a line to do.

:::{admonition} In Belgium
:class: rh-country rh-country-be

The pharmacy's sachets must be used within fourteen days of the delivery,
weekends and public holidays pushed to the next working day, and a split tablet
stays with the house: see [Medication rules in Belgium](../belgique/medicaments-regles.md).
:::

## Going further

- [The medication round at the desk](tour.md)
- [Treatments](traitements.md)
- [Pharmacy orders](pharmacie.md)
- [Medication round on the care app](../soins-mobile/tour-medicaments.md)
