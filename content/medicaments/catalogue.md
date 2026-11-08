---
modules: [healthcare_medication, healthcare_medical]
---

# The medicine catalogue

:::{rh-description}
The house's medicine catalogue in Resthome: the medicine record and what the round reads from it, allergens, drug interactions, the list of dosages and what the reading of prescriptions has learned.
:::

:::{rh-faq}
Where is the medicine catalogue?
: On the Medicines workstation (**Nursing Care → Medicines**), **Catalogue** tab: **The Medicines** opens the whole catalogue, **Interactions** the house's drug interactions. The tab itself lists the medicines in use.

Who can add a medicine to the catalogue?
: The medication manager. A nurse picks a medicine from the catalogue; a medicine missing from it is added by the manager, or created from the reference catalogue when the reading of a prescription is sure enough.

Where are the allergens and dosages?
: In **Nursing Care → Configuration → Clinical Catalogues**: **Allergens**, **Dosages**, **Pathologies (ICD-10)** and, for the head nurse, **Prescription Reading Memory**.

Does the catalogue hold clinical information automatically?
: No. Indications, contraindications, side effects and allergens are what the house records on the medicine, or reads in the official documents linked to it.

Can a medicine be billed to the resident?
: Yes, where the country's billing provides it: tick **Billable** in the medicine's **Billing** tab and give its **Sale Price**.
:::

The **catalogue** lists the medicines the house uses. Every treatment points at
one of its medicines, and the round, the pillboxes and the pharmacy's sachets
read what the medicine record says.

Open it from the [Medicines workstation](index.md), **Catalogue** tab: the tab
lists the **Medicines in Use**; **The Medicines** opens the whole catalogue and
**Interactions** the house's list of drug interactions.

## The medicine record

At the top: the name, the **Active Ingredient**, the **Form** (*Tablet*,
*Capsule*, *Liquid/Syrup*, *Injectable*, *Cream/Ointment*, *Patch*, *Drops*,
*Inhaler*, *Suppository*, *Other*), the **Strength**, the **Category**
(*Analgesic*, *Antibiotic*, *Anxiolytic*, *Antipsychotic*, *Hypnotic/Sedative*…)
and the **Manufacturer**.

What the round and the pillboxes read:

- **Prescription Required** and **Controlled Substance**;
- **Do Not Crush** — the treatment refuses a crushed intake;
- **Glucose Before Giving** — the care app asks the blood glucose before the
  dose (an insulin);
- **Discard After Opening (days)** — sets the discard date of an opened box;
- **Never in the Pharmacy's Sachets** — the pharmacist leaves it out of the
  sachets prepared per moment;
- **Food Supplement**.

The tabs:

- **Information** — **Contains Allergens** (used by the allergy check),
  **Indications**, **Contraindications**, **Side Effects**, **Storage
  Instructions**;
- **Official Documents** — **SPC URL** and **Leaflet URL**;
- **Billing** — **Billable** and **Sale Price**;
- **Notes**.

The **Create Product** smart button makes the stock product of the medicine,
for a house that keeps a stock in Inventory; once made, it shows the quantity
**In Stock**.

Filters: **Controlled Substances**, **Prescription Required**, **Billable**,
**Archived**; groupings by **Category** and **Form**.

:::{admonition} In Belgium
:class: rh-country rh-country-be

A new medicine starts with a search in SAM, the Belgian medicines database,
which fills the whole record and its national product code: see [The SAM
medication database](../belgique/sam-base-medicaments.md). A billable medicine
is billed on the resident's monthly invoice: see [Billing medicines in
Belgium](../belgique/medicaments-facturation.md).
:::

## Allergens

**Nursing Care → Configuration → Clinical Catalogues → Allergens** lists the
allergens: name, **Category** (*Drug*, *Food*, *Environmental*, *Contact*,
*Insect/Venom*), **ImmunoCAP Class**, **Allergen Type** for a drug, and the
**Default Severity**:

- *Low - Monitor*;
- *Medium - Warning*;
- *High - Strong Warning*;
- *Critical - Block Prescription*.

The **Cross-Reactivity** tab names the allergens that react together. The
**Residents** and **Medications** smart buttons show who is allergic and which
medicines contain the allergen. A resident's allergies are recorded on their
medical record (see [The resident's medical record](../soins/dossier-medical.md)).

## Drug interactions

**Interactions**, in the **Catalogue** tab, opens the house's list of drug
interactions. An interaction names two medicines (**Medication 1**,
**Medication 2**) or two active ingredients, with:

- the **Severity** — *Minor*, *Moderate*, *Major*, *Contraindicated*;
- the **Interaction Type** and the **Evidence Level**;
- the tabs **Clinical Information** (clinical effect, mechanism, management),
  **Active Ingredients** and **References**.

Each treatment is checked against this list: a major interaction warns, a
contraindicated pair refuses the treatment. See [Treatments](traitements.md).

## Dosages

**Nursing Care → Configuration → Clinical Catalogues → Dosages** is the list
the treatments and prescription lines pick their dose from: a quantity and its
unit (*1 tablet*, *500 mg*, *5 ml*). Drag the lines to order them; archive one
you no longer use. A dosage typed elsewhere joins the list by itself.

## What the reading of prescriptions learns

When the lines of prescriptions are read off their PDF:

- **Nursing Care → Configuration → Clinical Catalogues → Prescription Reading
  Memory** keeps what each confirmed prescription taught: the medicine each
  name read was matched to, and the physician behind a letterhead (filters
  **Medicines Read**, **Letterheads**). Delete a line to forget it.
- **Nursing Care → Reports → Prescription Reading** measures, field by field,
  what was kept as read and what was corrected (filters **Not Kept**, **PDF
  Text**, **OCR**).

Both are for the head nurse and the medication manager. See
[Prescriptions](../soins/prescriptions.md).

## Going further

- [Treatments](traitements.md)
- [Prescriptions](../soins/prescriptions.md)
- [Medicines](index.md)
