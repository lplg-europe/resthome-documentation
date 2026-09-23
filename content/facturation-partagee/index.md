---
modules: [resthome_split_billing]
---

# Split billing

:::{rh-description}
Split billing in Resthome: the resident's share divided among several debtors, by percentage or by fixed amount, with a neutral resident statement and one invoice per debtor.
:::

:::{rh-faq}
What part of the invoice is split?
: Only the resident's share — accommodation and supplements. The care allowance paid by the health insurer is not split: it goes to the health insurer in full.

Can I mix percentages and fixed amounts?
: Not freely. Either every debtor has a percentage and the total is exactly 100, or some debtors have a fixed amount and exactly one is **Variable** and takes what is left.

Who can be a debtor?
: Anyone: the maintenance debtors (children, relatives), a public welfare body, a notary, an outside payer.
:::

:::{toctree}
:hidden:

configuration
factures
:::

When the **resident's share** must be paid by **several people** — typically the
maintenance debtors — Resthome splits it automatically, and produces one invoice
per debtor.

## The principle

- The **resident's share** (accommodation + supplements) is divided among the
  debtors, according to a key you set on the resident's record.
- Each debtor receives **their own invoice**, with their own VAT treatment.
- The resident receives a **statement** of the whole month, which totals
  **0.00 €**: it shows everything, and charges nothing.

:::{admonition} The insurer's share is not concerned
:class: note

The care allowance goes to the health insurer, as usual. Split billing only
touches what the resident owes.
:::

:::{admonition} In Belgium
:class: rh-country rh-country-be

The INAMI allowance goes to the mutuality through eFact and is never split. A
CPAS that pays part of the resident's share is added here as a debtor. See
[Billing a month in Belgium](../belgique/facturation.md) and
[CPAS coverage](../belgique/cpas.md).
:::

## Two ways of splitting

- **By percentage** — every debtor has a share; the total must be **exactly
  100 %**. A message shows what is **left to allocate**.
- **By fixed amount** — one or several debtors owe an agreed amount, and
  **exactly one** debtor is **Variable**: they take what is left.

:::{admonition} When the amounts do not fit
:class: warning

Fixed amounts are invoiced first. If the resident's share is **smaller** than
the sum of the fixed amounts, each of them is invoiced pro rata and the variable
debtor gets nothing.
:::

## What's next

- [Setting up a split](configuration.md) — the settings, the debtors, the admission.
- [The documents produced](factures.md) — the statement, the invoices, the PDF.
