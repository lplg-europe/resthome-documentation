# The documents produced

:::{rh-description}
What split billing produces in Resthome: a resident statement totalling zero, one invoice per debtor with its own VAT, the debtor PDF, rounding and safeguards.
:::

:::{rh-faq}
Why does the resident's statement total 0.00 €?
: Because it shows the whole month and then deducts each debtor's participation. It is a statement, not a demand for payment.

Does a debtor see what the others pay?
: No. Their PDF repeats the month's detail, without the deduction lines.

Why is a debtor missing an invoice?
: Because their share rounds to zero everywhere. No invoice is produced for an amount of zero.
:::

Generating the invoices of a month produces, for a resident in split billing,
**one statement and one invoice per debtor**.

## The resident's statement

- It is addressed to the **resident**, in the dedicated journal.
- It lists the whole month — accommodation, supplements — **without VAT**, on
  the suspense account.
- A **Down Payments** section then deducts **each debtor's participation**.
- Total: **0.00 €**.

:::{admonition} A statement marked "Paid"
:class: note

A document totalling zero is considered settled: the statement shows as
**Paid**. It is normal, and means nothing about what the debtors have actually
paid.
:::

## The debtors' invoices

Each debtor receives a real invoice, in the usual resident journal:

- a note at the top recalls the month, the resident, the total of the statement
  and **their** share (a percentage, a fixed amount, or the part not covered by
  the others);
- each line of the month is repeated with the wording **Full amount: … — Your
  participation = x %**;
- income accounts and **VAT are normal**, following the **debtor's** fiscal
  position.

The PDF carries a second page, **Resident Invoice**, which repeats the whole
month — without the deduction lines, so nobody reads what the others pay.

## Rounding

An agreed **fixed amount** is invoiced to the cent; what remains falls on the
**variable** debtor. A debtor whose share rounds to zero everywhere receives
**no invoice**.

## Safeguards

- A **posted** deposit blocks regeneration: Resthome names the invoices to reset
  to draft first.
- **Draft** deposits are replaced, never stacked.
- Resetting the period to draft deletes the statement **and** its deposits
  together.

## What's next

- [Setting up a split](configuration.md)
- [Invoicing a month, step by step](../facturation/facturer-un-mois.md)
- [Departure and death](../facturation/depart-deces.md)
