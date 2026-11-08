---
modules: [resthome_billing_medication, resthome_supplements_pmi]
sectors: [mr, csj]
---

# Billing medicines in Belgium

:::{rh-description}
Pass the cost of medicines on to the residents in WideCare: the doses given of a billable medicine on the monthly invoice, and the pharmacy's invoice recharged resident by resident.
:::

:::{rh-faq}
How do I bill a medicine the house provides?
: In the medicine's **Billing** tab, tick **Billable** and give its **Sale Price**. At the generation of the billing period, each dose given that month is billed to the resident.

Is a refused or missed dose billed?
: No. Only the doses recorded as **Given** are billed, and each one only once.

How do I pass the pharmacy's invoice on to the residents?
: Make the vendor bill from the pharmacy invoice and post it, then click **Recharge to residents**: WideCare proposes one line per resident, with the amount the pharmacy states for them.

Why is there no VAT on the recharged medicines?
: The medicines are bought in the resident's name, under their pharmacy mandate, and passed on as they are: the amount the pharmacy states already includes its VAT.
:::

Two ways bring the cost of medicines to the resident's invoice: a medicine the
**house** provides and bills per dose, and the **pharmacy's** invoice passed on
resident by resident.

## Medicines billed per dose

### Set the medicine up

Open the medicine in the [catalogue](../medicaments/catalogue.md), **Billing**
tab:

- tick **Billable** — the doses given of this medicine are billed to the
  resident;
- enter the **Sale Price**, the price of one dose.

### At the generation of the period

When the billing period is generated (see [Billing a month in
Belgium](facturation.md)), WideCare gathers, for each resident, the doses of
billable medicines recorded as **Given** during the period and not billed yet:

- **one billing line per medicine**, of the type **Medication**, paid by the
  resident, with the name of the medicine and the number of doses (*Paracetamol
  x 28*), the quantity of doses and the sale price;
- the line's **Administrations** tab lists the doses it bills;
- each dose is billed only once.

In the billing lines, the **Medications** filter shows these lines.

<!-- screenshot to add: billing line of type Medication with its Administrations tab -->

## The pharmacy's invoice, recharged

When the pharmacy sends its invoice by eHealthBox with one block per resident
(see [The pharmacy link](medicaments-lien-pharmacie.md)):

1. On the **Pharmacy Invoice**, check the residents, then click **Make the
   Vendor Bill**.
2. Post the vendor bill.
3. Click **Recharge to residents**. WideCare proposes **one line per resident**
   the invoice names, with the amount the pharmacy states for them, on the
   product **Medicines (pharmacy invoice)**, which carries no VAT. The house's
   own block and a resident the house does not know are left out.
4. Validate the recharge: each resident's part becomes a supplement on their
   invoice.

The recharge itself works as for any vendor bill: see [Recharging a vendor
bill](../facturation/refacturation-fournisseur.md).

## Going further

- [The medicine catalogue](../medicaments/catalogue.md)
- [The pharmacy link](medicaments-lien-pharmacie.md)
- [Billing a month in Belgium](facturation.md)
- [Supplements](../facturation/supplements.md)
