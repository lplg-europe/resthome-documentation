---
modules: [healthcare_medication, healthcare_medical]
sectors: [mr, csj]
---

# Prescriptions

:::{rh-description}
Receive, read and confirm the physicians' prescriptions in WideCare: by e-mail or typed in, lines read off the PDF, a batch of several patients, confirmation into treatments, expiry and renewal.
:::

:::{rh-faq}
How does a prescription arrive in WideCare?
: Each e-mail sent to the house's prescriptions address becomes a draft prescription, its PDF beside the form. You can also create one with **New Prescription** on the Medicines workstation, or drop the PDF on a draft.

What happens when I confirm a prescription?
: Each line becomes a treatment of the resident, placed on the round from its start date. The prescription moves to **In Force**.

Can WideCare read the lines of the PDF for me?
: Yes, when **Read the lines off the PDF** is set to local OCR. The lines are filled in from the PDF and shown in yellow until checked: a nurse checks each one against the PDF before confirming.

What happens when a prescription expires?
: Nothing stops by itself. The prescription shows an **Expired** ribbon, the head nurse is asked to renew it, and **Ask for a Renewal** sends the physician the lines to renew.

Who can confirm a prescription?
: Nurses and physicians. A care assistant sees the treatments on the round, not the prescriptions to read.
:::

A **prescription** is the physician's document. WideCare receives it, lets a
nurse check its lines, and on confirmation turns each line into a **treatment**
of the resident — what the round gives every day. Prescriptions are handled on
the [Medicines workstation](../medicaments/index.md) (**Nursing Care →
Medicines**), **Prescriptions** tab, and its **To Read** counter.

## Before you start

Two settings, in **Nursing Care → Configuration → Settings**, block
**Prescriptions**:

- **Receive prescriptions by e-mail** — give the address (alias and domain):
  each e-mail sent to it becomes a draft prescription, its PDF beside the form.
  The sender is matched to the physician.
- **Read the lines off the PDF** — **Typed by hand**, or **Local OCR
  (Tesseract)** to fill in the lines from the PDF. With OCR, set **Create a
  missing medicine from the reference catalogue from this certainty (%)**: a
  medicine read that is not in the catalogue is created when the reading is
  that sure (0 = never created, only proposed in the line's notes).

:::{admonition} In Belgium
:class: rh-country rh-country-be

A prescription sent from a physician's eHealthBox becomes a draft the same way,
and the renewal can be asked there: see [Prescriptions through the
eHealthBox](../belgique/medicaments-ehealthbox.md).
:::

## 1. Receive the prescription

A prescription arrives as a **Draft**:

- by **e-mail** to the prescriptions address — the PDF shows beside the form,
  and the message says how the resident was found, or why not;
- with **New Prescription** on the workstation, typed in;
- by dropping the PDF on a draft's discussion: with OCR reading on, its lines
  are read and the form reloads.

The resident is the one the PDF names when the name, and the birth date where
one is read, point to a single resident. Otherwise choose the **Resident** by
hand. The **Physician** is the resident's attending physician until another is
said (the sender of the e-mail, or the one you pick).

### A PDF of several patients

From the list of prescriptions, **Batch of Prescriptions** reads a PDF holding
several prescriptions, one patient or more per page:

1. Choose the file and click **Read the File**.
2. Check the resident proposed for each patient read — a resident is proposed
   only when the name and the birth date point to one person. Pick the others by
   hand, or untick them.
3. Click **Create the Prescriptions**: one draft per patient, with its lines.

Nothing is created before you have checked the residents.

## 2. Check the lines

On the draft, the **Lines** tab lists what the physician prescribed. When the
lines are read off the PDF, a banner reminds you to check each one against it,
and a line still missing its medicine or its dose is shown in yellow. **Read
the PDF** reads the attached PDF again when the draft has no line yet.

Open a line to set:

- **Medication** — picked from the catalogue; **Read As** shows the name read
  when no medicine was matched;
- **Dosage** — picked from the list of dosages (**Dosage Read** shows what the
  PDF said);
- **Dosage Form**, **Meal Timing**, **End Date**;
- **Schedule** — **Frequency**, and the moments **Morning**, **Noon**,
  **Afternoon**, **Evening**, **Night** or **Specific Times**;
- **Notes**.

At the top of the form: **Prescription Date**, **Expiry Date** and
**Physician**.

<!-- screenshot to add: draft prescription with its lines and the PDF beside the form -->

## 3. Confirm

Click **Confirm**. WideCare asks for what is missing — the resident, the
physician, at least one line, a medicine and a dose on each line. Then each
line becomes a **treatment** of the resident, on the round from its start
date, and the prescription moves to **In Force**. The **Treatments** smart
button and tab show the treatments it started.

A line that renews a treatment ended less than a month ago (same resident, same
medicine) keeps what the team had set on it: the intake, *not together with*,
the pharmacy's sachets and the box.

Each confirmed prescription read off its PDF teaches WideCare the medicines
and the letterheads it recognised. See [The medicine
catalogue](../medicaments/catalogue.md).

## The life of a prescription

The states are **Draft**, **In Force**, **Closed** and **Discarded**.

- **Cancel** discards a draft (a prescription received twice, a wrong file);
  **Reset to Draft** brings it back.
- **Close** ends a prescription in force: the treatments it started stop today.
- **Expiry Date** — past this day, the **Expired** ribbon shows, the date turns
  red in the list and the head nurse is asked to renew it. Nothing stops by
  itself.

### Ask for a renewal

**Ask for a Renewal** (in force, highlighted once expired) e-mails the physician
the resident and each line to renew. The physician's answer arrives as a new
draft at the prescriptions address, never on the old prescription. The request
is shown on the form (to whom, when), in the list (**Renewal Asked On**) and
under **Waiting, nothing to do** on the workstation; a new expiry date clears
it.

## Finding a prescription

**All the Prescriptions**, on the workstation, opens the list: number,
resident, physician, prescription date, expiry date, treatments and state.
Filters **Open** (default), **Draft**, **In Force**, **Closed**, **Expired**
and **Renewal Asked**; groupings **By Resident**, **By Physician** and **By
State**.

## Going further

- [Treatments](../medicaments/traitements.md)
- [Medicines](../medicaments/index.md)
- [The medicine catalogue](../medicaments/catalogue.md)
- [Care plans](plans-de-soins.md)
