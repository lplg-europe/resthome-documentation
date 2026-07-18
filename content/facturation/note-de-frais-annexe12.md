# The Expense Note (Annexe 12)

:::{rh-description}
Produce the Annexe 12 expense notes in a nursing home (MR/MRS) with Resthome: an individual note per resident and a summary note per insurance organisation.
:::

:::{rh-faq}
What is Annexe 12 used for in a nursing home (MR/MRS)?
: It is the official AViQ document that justifies a month's expenses: an individual expense note per resident and a summary note per insurance organisation.

Where do you generate Annexe 12 in Resthome?
: Via the Print button: on a billing period for the summary note, on a per-resident billing record for the individual note.

What is the difference between an individual note and a summary note?
: The individual note details the expenses of a single resident over three pages; the summary note lists all residents of the same insurance organisation with the totals.

Which amounts appear on Annexe 12?
: The three mandatory amounts: payable by the insurance organisation (O.A.), payable by the patient and the total, together with the number of days of presence for the month.

Do you have to give Annexe 12 to the resident?
: Yes: a copy of the individual expense note must be given to the beneficiary; the summary note accompanies the billing sent to the insurance organisation.
:::

**Annexe 12** is the official document that justifies, month by month, the
accommodation and care expenses of a nursing home (MR/MRS) resident. Resthome
produces it in two complementary forms:

- the **Individual Expense Note** — a detailed supporting document **per resident**;
- the **Summary Expense Note** — a table **per insurance organisation (O.A.)**
  that groups all residents of the same insurance fund.

Both are generated from the **Print** button, from a **billing period** or a
**per-resident billing record**.

:::{admonition} An official AViQ document
:class: info

Annexe 12 targets the "institutions referred to in Article 43/7, 4° of the
Walloon Code of Social Action and Health". Resthome automatically fills in the
official form with your period's data: you have nothing to copy out by hand.
:::

## Two documents, two scopes

| Document | Scope | Printed template | Generated from |
|---|---|---|---|
| **Individual Expense Note** | One resident | `Annexe12_<resident>_<period>` | **Billing per resident** record → **Print** |
| **Summary Expense Note** | One insurance organisation | `NoteRecap_<period>` | **Billing period** → **Print** |

:::{admonition} The link between the two
:class: tip

Each line of the summary note carries an **individual note number** that refers
back to the individual note of the corresponding resident. So you generally
produce **both documents for the same month**: the summary for the O.A., the
individual notes for the residents.
:::

## The Individual Expense Note (per resident)

This is the complete supporting document for **a single resident** for the month.
Resthome generates it on the **official form** across three pages.

| Page | Content |
|---|---|
| **1. Resident summary** | Identification of the institution (name, address, INAMI number) and of the insurance fund, period, the resident's line (name, NISS registration number, days of presence) and the **three mandatory amounts**: payable by O.A., payable by patient, total. |
| **2. Fixed costs** | The **care flat-rate** (insurance-organisation share), with its **AViQ pseudo-code**, the daily price, the number of days and the amount — broken down by sub-period where applicable — as well as the **incontinence rebate**. |
| **3. Supplements** | The **accommodation** (the room), the **supplements** (television, telephone, laundry, pedicure, single room…), the (para)pharmaceutical **medication** and the **supplements total**. |

:::{admonition} The three mandatory amounts
:class: note

The first page carries the **three amounts** required by electronic billing:
**payable by the O.A.** (the reimbursed flat-rate, incontinence rebate included),
**payable by the patient** (accommodation + supplements) and the **total**. These
are the amounts that justify, to the resident, what the insurance fund covers and
what remains for them to pay.
:::

:::{admonition} The flat-rate does not depend on the Katz category
:class: info

The amount of the **care flat-rate** is the **same for all Katz categories**
(AViQ tariffs): the category serves to **declare the dependency profile** to the
insurance fund, not to set a different amount. See
[The INAMI flat-rate](forfait-inami.md).
:::

### Generating an individual note

1. Open the month's **billing period** (**MR/MRS → Billing → Billing periods**
   application).
2. Open the relevant **resident's billing record** ("Billing per resident").
3. Click **Print → Annexe 12 — Individual Expense Note**.
4. The PDF is generated in the name of the resident and the period.

<!-- screenshot to add: the Print button opened on a per-resident billing record, showing the "Annexe 12 — Individual Expense Note" entry -->

:::{admonition} Give a copy to the resident
:class: warning

The summary note certifies that "a copy of the individual expense note has been
given to the beneficiary". So remember to **give the individual note** (or a copy
of it) to each resident or their representative.
:::

## The Summary Expense Note (per insurance organisation)

The summary note groups, for a month, **all residents of the same insurance
organisation** in a single table. Resthome produces **one page per O.A.**: if your
period includes residents affiliated with several insurance funds, the document
contains as many pages as there are organisations.

Header of each page:

- the **institution identification**: name, address, telephone, **INAMI number**;
- the **insurance-fund identification**: number (O.A. code) and name;
- the **period** covered ("Summary note from … to … — issued on …").

The residents table has the following columns:

| Column | Content |
|---|---|
| **Individual note no.** | Reference of the resident's individual note |
| **Beneficiary surname and first name** | The resident |
| **Registration number** | The resident's NISS |
| **Number of days** | Billed days of presence |
| **Payable by O.A.** | Share reimbursed by the insurance organisation |
| **Payable by patient** | Share payable by the resident |
| **Total** | Sum of the two |

The last line totals the **Grand total for the O.A.**, payable by patient and
total. The document ends with a **certification** signed by the **Institution
Manager** (date, name and signature).

### Generating a summary note

1. Open the month's **billing period** (or select it in the **Billing periods**
   list).
2. Click **Print → Annexe 12 — Summary Note**.
3. Resthome generates the PDF, **one page per insurance organisation**.

<!-- screenshot to add: the generated summary note, with the institution/insurance-fund header and the table of residents grouped by O.A. -->

## When to generate Annexe 12

Generate Annexe 12 **once the month has been billed**: the amounts pick up the
billing lines calculated by Resthome (flat-rate, accommodation, supplements,
medication, absences). If you change an invoice afterwards, **refresh** the period
then regenerate the document so that it reflects the new amounts.

:::{admonition} It accompanies the eFact
:class: tip

The summary note is the "paper" supporting document that **accompanies the billing
sent** to each insurance organisation. For the complete electronic flow (sending
the flat-rate to the insurance fund), see
[Billing a month, step by step](facturer-un-mois.md).
:::

:::{admonition} Departure or death during the month
:class: note

The amounts take into account the **actual days of presence**: a departure or
death during the month is already reflected in the billing lines, and therefore in
Annexe 12. See [Departure and death](depart-deces.md).
:::

## Key points to remember

- Annexe 12 exists in **two forms**: the **individual note** (per resident) and the
  **summary note** (per insurance organisation).
- Both are generated from the **Print** button: the summary on the **period**, the
  individual one on the **per-resident billing record**.
- The individual note carries the **three mandatory amounts**: payable by O.A.,
  payable by patient and total.
- The summary produces **one page per insurance organisation** and totals the
  **Grand total for the O.A.**.
- A **copy of the individual note** must be **given to the resident**.
- The institution's INAMI number and the tariffs are **specific to your
  establishment**: check that they are configured correctly.

## Further reading

- [Billing a month, step by step](facturer-un-mois.md)
- [Supplements](supplements.md)
- [Billing overview](index.md)
- [Departure and death](depart-deces.md)
