---
modules: [resthome_mr_billing]
sectors: [mr]
---

# Occupancy MR / CS / MRS

:::{rh-description}
The occupancy board of a Belgian nursing home in WideCare: residents by sector and Katz category against the approved beds, the quarter's occupancy rate and the MR residents an MRS bed admits.
:::

:::{rh-faq}
Where is the occupancy board?
: In **Billing → Facturation → Occupancy MR / CS / MRS**, and on the billing dashboard.

What does "% end of quarter (projection)" mean?
: The occupancy rate the quarter would reach if today's occupancy held until its last day.

Which residents are "transferable to MRS"?
: The MR residents whose validated Katz category an MRS bed admits (B, C, Cd or D), and whose end of stay is not announced. Ccoma is left out: it depends on the home's accreditation.

How is a transfer day counted?
: In the incoming sector. A bed is held from the day of entry to the day of departure.

Is the board stored anywhere?
: No. It is computed when you open it, from the stays, the absences, the validated Katz assessments and the approvals, so it never disagrees with them.
:::

An **MRS** bed is funded as MRS only while it is occupied, and the home is
approved for a fixed number of them. The occupancy board answers the morning
question: where does the home stand against its approved beds this quarter, and
who could move up to MRS?

Open **Billing → Facturation → Occupancy MR / CS / MRS**. The board shows
**today**; pick another date in the date field, and **Today** brings you back.

<!-- screenshot to add: the occupancy board with the MR, CS and MRS columns, the Katz rows and the quarter figures -->

## The grid

One column per sector — **MR**, **CS** (short stay, an MR bed with its own
approval and codes) and **MRS** — and a **Total**. One row per Katz category the
sector may carry: MRS starts at B.

Every figure is a link: click it to open the residents behind it.

Under the categories:

| Row | What it says |
|---|---|
| **Total** | The residents of the sector. |
| **Approved beds** | The beds of the sector's approval — see [Belgian settings](reglages.md). |
| **Free beds** | Approved beds minus residents; negative when the sector is above its approval. |
| **% quarter to date** | The occupancy of the quarter so far. |
| **% end of quarter (projection)** | The occupancy the quarter reaches if today's holds until its end. |

**Among them**, the residents in a particular situation:

- **Hospitalised** and **Absent** at the end of the day;
- **Without OA intervention**: no mutuality pays the allowance — the end of the
  intervention is declared while the room is not freed yet, or the resident is
  outside the INAMI financing;
- **Without category**: no validated Katz;
- **Non-beneficiaries**: residents whose days are encoded as non-beneficiary
  days.

A bed is held from the day of entry to the day of departure; a transfer day
counts in the incoming sector.

## What to do now

Two banners above the grid say what needs action:

- in red, the **MRS residents above the approved MRS beds**: a bed beyond the
  approval is not funded as MRS;
- in orange, the **free MRS beds** while MR residents an MRS bed admits are
  waiting, with **See the residents transferable to MRS**.

In the **MR** column, a blue badge next to a category counts the residents of
that category an MRS bed admits; click it to see them.

## Transferring a resident to MRS

The list **MR residents transferable to MRS** shows each resident with their
category, room and stay start. **Transfer to MRS** on a row opens the internal
transfer with the destination already set to MRS: WideCare prepares the end of
stay (Annexe 11) and the new request (Annexe 7, with the Katz scale) for the
mutuality.

See [Internal transfer (MR ↔ MRS)](ehealth/eagreement-transfert.md).

## What's next

- [The Katz assessment](katz.md) — the category decides who an MRS bed admits.
- [Internal transfer (MR ↔ MRS)](ehealth/eagreement-transfert.md)
- [Belgian settings](reglages.md) — the approvals and their beds.
- [Billing a month in Belgium](facturation.md)
- [Management reports](rapports-gestion.md) — occupancy by approval and the KAPPA control.
