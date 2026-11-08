---
modules: [healthcare_accommodation, healthcare_accommodation_billing, l10n_health_be_perdiem_ehealth, resthome_mr_billing]
---

# Room change and transfer

:::{rh-description}
Move a resident to another room, now or on a later date, or transfer them between the sectors the home is licensed for in Resthome — billing follows on its own, with no new admission.
:::

:::{rh-faq}
How do I change a resident's room?
: On the resident's stay, click **Change Room**, choose the **New room** and the **Change date**, then click **Change Room** in the window.

Can I plan a room change for a later date?
: Yes. Choose a date in the future: nothing changes today, the current room shows as freeing up, and the move is applied on its own on the day itself. **Cancel the planned room change** on the stay withdraws it while it is pending.

Can I move a resident into a room that is still occupied?
: Yes, when that room frees up on a known date: it is offered with that date, and the change must be dated on the first free day at the earliest.

Does a room change require a new admission?
: No. The care allowance paid by the health insurer stays continuous and there is nothing new to request from the insurer — only the accommodation is billed at the new rate.

How do I undo a room change entered by mistake?
: On the stay the change opened, click **Cancel Room Change**: the resident goes back to their previous room and stay, with their dates.

How do I transfer a resident to another sector?
: On the stay, use the **Internal Transfer** action, enter the date and time and the new type of care, then validate. Resthome updates the care allowance and, where the country requires it, prepares the notification to the health insurer.
:::

A resident can **change room** or move to **another sector** the home is
licensed for during their stay. Resthome handles the **transition**: billing
follows at the right date, without you having to redo an admission.

## Changing room

1. Open the resident's **stay** (from the **Stay Agreement** tab of their record,
   or **Nursing Home → Accommodation → Stays**). The stay must be **Confirmed**
   or **Active**.
2. Click **Change Room**.
3. Choose the **New room**. The list offers the free rooms and the rooms that
   **free up** on a known date; the current room is pre-filled.
4. Enter the **Change date** — the first day billed on the new room. The current
   room is billed up to the day before.
5. Read the notice at the bottom: it says, with the figures, what the change
   does to the billing.
6. Click **Change Room**.

A notification then says what was done: **Room changed — same daily rate**, or
**Room changed — the daily rate moved** with the old and new rates.

<!-- screenshot to add: the Change Room window, with the current and new room, the change date, the two daily rates and the billing notice -->

### What the change does to the stay

Resthome picks the right shape on its own:

| Case | What happens |
|---|---|
| Both rooms cost the same | The stay simply changes room. Nothing is credited or re-issued. |
| The resident has not moved in yet (change dated on or before the arrival) | A correction: the whole stay is re-priced on the right room, with no split. |
| The rooms are priced differently and the resident is already in | The stay is **split** at the change date: the old room is billed up to the day before, the new room from that day. Documents already issued are corrected — a supplementary invoice or a credit note for what was already billed. |

:::{admonition} No new admission
:class: note

A room change is **not** a new admission: the care allowance paid by the health
insurer stays **continuous**, and there is nothing new to request from the
insurer. Only the **accommodation** follows the new rate.
:::

### Moves that come with it

Each room change also:

- puts the **new room** on the housekeeping board **To prepare** and the room
  being left **To clean**, with a task for the housekeeping team — see [Room
  housekeeping](entretien-chambres.md);
- opens the **move-in tasks** of the resident, due on the change date — see
  [The move-in procedure](procedure-emmenagement.md);
- leaves the **private furniture** list unchanged: it follows the resident — see
  [The resident's private furniture](mobilier.md).

## Scheduling a room change

A move is often planned **because** the target room is not free yet: a resident
takes room 12 when its occupant leaves at the end of the month.

1. Click **Change Room** on the stay.
2. Choose the new room — a room that frees up on a known date is offered with
   that date.
3. Enter a **Change date** in the future. For an occupied room, the date must be
   the day after it frees up at the earliest.
4. Click **Change Room**.

Nothing is billed or credited today. Resthome:

- shows the **Planned Room** and the **Planned Room Change** date on the stay;
- shows the current room as freeing up on the eve of the change, so the
  [waiting list](../admissions/liste-attente.md) can count on it;
- applies the move **on its own** on the day itself, with whatever it bills or
  credits then.

To withdraw a scheduled change, click **Cancel the planned room change** under
the planned date on the stay. The resident stays where they are, and the room
stops being announced as freeing up.

:::{note}
Only the room can be scheduled ahead. A change of the terms of the stay — the
invoice type, for example, when the billing layer adds it to this window —
applies on the day it is decided.
:::

## Changing the terms without moving

Depending on the billing modules installed, the **Change Room** window also
carries the terms the stay is billed under, such as the **New invoice type**.
Leave the **New room** on the current room and change only those terms: the
notification then reads **Stay continued — same room**. The part of the stay
already billed keeps its type; the new type applies from the change date. See
[Invoice type: in advance or in arrears](../facturation/type-de-facture.md).

## Undoing a room change

On the stay opened by a room change, **Cancel Room Change** undoes it: the
resident goes back to their previous room and stay (dates restored), and the
move tasks are removed. A confirmation asks before anything is undone.

## Transfer between sectors

When the home is licensed for several sectors, moving from one to another is an
**internal transfer**. The **stay type** can no longer be edited once the stay is
confirmed: the change goes through the **Internal Transfer** action, which the
country pack provides where the country regulates sectors. On the resident's
record, **Change stay type** next to the stay type opens the active stay.

1. On the stay, use the **Internal Transfer** action.
2. Enter the **date/time** of the transfer and the **new type of care**.
3. **Validate.**

Resthome splits billing at the transfer date and **updates the care allowance**
according to the new type. Where the country requires it, it prepares the
**notification to the health insurer**. **Cancel Transfer**, on the stay the
transfer opened, undoes it: the resident goes back to their previous stay
(sector, room and dates restored) and the move tasks are removed.

:::{admonition} A sector can require a minimum dependency category
:class: warning

When a sector only takes residents above a given dependency category, Resthome
refuses to **put or keep a stay** in it for a resident assessed below — at
admission and at transfer time.

A **room change is not blocked**, though: a resident whose category no longer
matches their bed can still be moved from one room to another. A banner on their
record flags the situation until the transfer is entered.
:::

:::{admonition} In Belgium
:class: rh-country rh-country-be

The sectors are **MR** and **MRS**: an MRS bed only takes Katz categories **B
and above**, and the transfer produces the Annexe 11 + Annexe 7 pair for the
mutualité. A room change creates no eAgreement — see [Internal transfer (MR ↔
MRS)](../belgique/ehealth/eagreement-transfert.md) and [The Katz
assessment](../belgique/katz.md).
:::

## Assigning from the room

The **Assign Resident** button of a free room also moves an already-housed
resident (**Transfer Resident**): it ends the old stay and opens a new one, with
no billing notice and no scheduling. Prefer **Change Room** on the stay — see
[Rooms and occupancy](chambres.md).

## Learn more

- [Manage a resident](gerer-un-resident.md)
- [Rooms and occupancy](chambres.md)
- [Billing overview](../facturation/index.md)
- [Invoice type: in advance or in arrears](../facturation/type-de-facture.md)
