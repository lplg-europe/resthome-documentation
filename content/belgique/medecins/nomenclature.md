---
modules: [l10n_health_be_nomenclature]
sectors: [gp]
---

# The INAMI nomenclature

:::{rh-description}
The INAMI nomenclature in a WideCare general practice: the codes, their fees and personal shares (ordinary or BIM), the NomenSoft import, and the pricing of the billed acts.
:::

:::{rh-faq}
Why does a code have no fee?
: WideCare ships the general practitioners' consultation codes with their labels only: fees and personal shares change with every indexation. Import the NomenSoft files of the INAMI to fill them in.

How is the personal share chosen?
: From the patient's **BIM Status**: the BIM share when the patient benefits from increased intervention, the ordinary one otherwise.

Which version of a code prices an act?
: The one in force on the day of the act, from its **Valid From** and **Valid Until** dates.

Who can import the nomenclature?
: The users with the **Per-Act Billing** access as **Manager**.
:::

The **INAMI nomenclature** gives each act its code, its official fee and the
**personal share** the patient pays, ordinary or BIM. WideCare reads it to price
the billed acts and the eAttest.

## The catalogue

**Invoicing → Customers → INAMI Nomenclature** lists the codes:

- **Code**: the 6-digit INAMI number;
- **Label (French)** and **Label (Dutch)**;
- **Profession**: **General Practitioner**, **Specialist Physician**…;
- **Fee**, **Patient Share (Ordinary)** and **Patient Share (BIM)**;
- **Valid From** and **Valid Until**: one line per version of the code.

The filter **Without Fee** lists the codes still waiting for their amounts.

<!-- screenshot to add: the INAMI nomenclature filtered on the general practitioner -->

## Import the NomenSoft files

The INAMI publishes the nomenclature as **NomenSoft** tables: the tariffs
(NOMEN_CODE_FEE_LIM) and the labels (NOMEN_CODE_DESC_HIST).

1. Open **Invoicing → Customers → Import INAMI Nomenclature**.
2. Choose the **File** (CSV or XLSX). Leave **Layout** on **Detect from the
   header**.
3. Set the **Profession**, and the codes to keep in **Only These Codes**
   (separated by commas) to import only those.
4. Click **Import**.

The **Result** says how many codes were created and updated. Import the labels
file the same way.

For the tariffs file, three fee codes say which lines of the table carry the
fee and the insurer's intervention: **Fee Code: Fee** (0) and **Fee Code: BIM
Intervention** (1300) come filled in; type the **Fee Code: Ordinary
Intervention**, read in the NomenSoft table of fee codes (NOMEN_FEECODES),
before importing.

## Price an act

- On a billable act, pick the **INAMI Code**: the code, the description, the
  unit fee and the patient share fill in.
- On the **Acts** tab of a consultation, type the **Code**: **Create Invoice**
  finds the version in force on the day of the act and prices it.

A code without a fee keeps the amounts you typed: WideCare never guesses an
amount.

## What's next

- [Per-act billing](../../medecins/facturation-a-l-acte.md) — the acts and their
  invoice.
- [eAttest](eattest.md)
- [eFact per act](efact-a-l-acte.md)
