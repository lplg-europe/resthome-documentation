---
modules: [healthcare_medical, healthcare_medication, healthcare_medication_accommodation]
---

# Medicines

:::{rh-description}
The Medicines workstation of the Care app: the whole medication circuit on one screen, from the prescription to the pharmacy, the pillboxes, the round and the follow-up.
:::

:::{toctree}
:hidden:

traitements
pharmacie
piluliers
tour
suivi
catalogue
:::

:::{rh-faq}
Where do I manage medicines in Resthome?
: Open **Nursing Care → Medicines**. One screen, the Medicines workstation, gathers the prescriptions to read, the treatments, the pharmacy orders, the pillboxes, the round, the follow-up and the catalogue, each in its own tab.

What does the To Do Now tab show?
: Everything that waits for someone now: a prescription to read, a resident back from hospital, a pillbox to prepare again, missed doses, a basket for the pharmacy, mandates to have signed. Each line has a button that opens the right record.

Why does a care assistant see fewer things than a nurse?
: Each line and each tab is shown only to whoever may act on it. A care assistant sees the doses and treatments of their sectors; reading prescriptions, ordering and the pillbox gestures are for nurses and physicians.

How do I see one wing only?
: Choose the sector in the drop-down at the right of the header. The counters, the lists and the buttons then count that sector only; the Care dashboard keeps the same choice.

Which settings act on the medication circuit?
: In **Nursing Care → Configuration → Settings**, the **Prescriptions** block: receiving prescriptions by e-mail, reading their lines off the PDF, tracking the pillboxes, the house's pharmacy and the hour the pharmacy's basket leaves.
:::

Everything about medicines sits behind **one** entry of the Care app:
**Nursing Care → Medicines**. It opens the **Medicines workstation**, a single
screen that follows the circuit in the order things happen: the physician's
prescription, the treatments it starts, the pharmacy that supplies them, the
pillboxes prepared then checked, the round that gives the doses, and the
follow-up of what did not go as planned. The **Medicines** card of the Care
dashboard opens the same screen.

<!-- screenshot to add: the Medicines workstation with its header, smart buttons and the To Do Now tab -->

## Settings of the medication circuit

The settings live in **Nursing Care → Configuration → Settings**, block
**Prescriptions** (managers):

- **Receive prescriptions by e-mail** — each e-mail sent to the address you set
  becomes a draft prescription, its PDF beside the form. See
  [Prescriptions](../soins/prescriptions.md).
- **Read the lines off the PDF** — **Typed by hand** or **Local OCR (Tesseract)**: the lines
  of a received prescription are filled in from its PDF, for a nurse to check.
  The same setting holds the certainty from which a medicine missing from the
  catalogue is created from the reference catalogue (0 = never created, only
  proposed in the line's notes).
- **Track the pillboxes** — each dose records who prepared it and who checked
  it. Switched off, the **Pillboxes** tab, its buttons and its counters do not
  show at all. See [Pillboxes and the pharmacy's sachets](piluliers.md).
- **The house's pharmacy** — the pharmacy that serves the residents who chose no
  pharmacist of their own: their orders go to it.
- **The pharmacy's basket leaves at** — every morning from this hour, the
  basket leaves for the pharmacy by itself, where a secure channel to the
  pharmacy exists. See [Pharmacy orders](pharmacie.md).

:::{admonition} Sectors
:class: note

A nurse or a care assistant assigned to one or more **sectors** sees the
prescriptions, treatments, doses, allergies and pathologies of the residents
whose room is in those sectors. An employee with no sector assigned sees the
whole house.
:::

## The header

- **Prepare the Orders** — shown when boxes run low, are expired or opened too
  long: puts them into one basket per pharmacy (nurses and physicians).
- The **sector** drop-down, at the right — **The whole house** or one of your
  sectors. The choice applies at once and is shared with the Care dashboard.

Under the title, the day's gestures: **The Round** (today's doses still to
give, by moment), **Tomorrow's Pillboxes** (when the pillboxes are tracked),
**New Prescription** and **New Treatment**.

Below, the day's figures: the round of the moment (or the next moment that has
doses), tomorrow's pillboxes, the **If Needed** doses given since midnight and
the pharmacy's basket.

## The smart buttons

Each counter opens the list it counts, for the chosen sector. A button with
nothing to count stays hidden when it is optional.

| Button | What it opens |
| --- | --- |
| **To Read** | The prescriptions still in draft. |
| **To Order** | The boxes running low, expired or opened too long, not yet on an order. |
| **Baskets** | The pharmacy orders. |
| **Mandates to Sign** | The residents without a pharmacy mandate in force. |
| **Doses to Give** | The round. |
| **Pillbox Issues** | The pillbox doses with an issue found at the check (pillboxes tracked). |
| **Back From Hospital** | The residents whose treatments wait to be reconciled. |
| **Repeated Refusals** | The treatments refused several times in a row. |
| **To Review** | The residents whose medication deserves a review. |

## The tabs

| Tab | What it holds |
| --- | --- |
| **To Do Now** | One line per thing waiting for a hand, with **Open**; then **Waiting, nothing to do**, greyed out (a renewal asked, an order on its way, the week's sachets). |
| **Prescriptions** | The prescriptions to read; **All the Prescriptions**, **New Prescription**. |
| **Treatments** | The running treatments with their box; **All the Treatments**, **If Needed**, **New Treatment**. |
| **Pharmacy** | Boxes to order, orders, the pharmacy's deliveries, residents without a mandate; **Prepare the Orders**, **All the Orders**, **Pharmacy Mandates**, **Pharmacy's Deliveries**. |
| **Pillboxes** | Tomorrow's doses with **Prepared** and **Checked** on each line (pillboxes tracked). |
| **Round** | The doses of the round with **Distributed**, **Given** and **Given Earlier**; **The Whole Round**, **Administrations**. |
| **Follow-up** | Back from hospital, repeated refusals, medication review; **Incidents**, **Corrections**. |
| **Catalogue** | The medicines in use; **The Medicines**, **Interactions**. |

:::{admonition} Who sees what
:class: tip

A line appears only to whoever can handle it. Nurses and physicians read
prescriptions, reconcile, order and prepare pillboxes; a care assistant sees
the doses and the treatments of their sectors, without the prescriptions to
read or the pillbox buttons. **Incidents** is for the medication manager and
the head nurse.
:::

:::{admonition} In Belgium
:class: rh-country rh-country-be

The workstation adds the medicines without a national product code, the SAM
database and, with the pharmacy link, the schedules sent, the pharmacy's stock
and invoices: see [The SAM medication database](../belgique/sam-base-medicaments.md)
and [The pharmacy link](../belgique/medicaments-lien-pharmacie.md).
:::

## Going further

- [Prescriptions](../soins/prescriptions.md)
- [Treatments](traitements.md)
- [Pharmacy orders](pharmacie.md)
- [Pillboxes and the pharmacy's sachets](piluliers.md)
- [The medication round at the desk](tour.md)
- [Medication follow-up](suivi.md)
- [The medicine catalogue](catalogue.md)
- [Medication round on the care app](../soins-mobile/tour-medicaments.md)
