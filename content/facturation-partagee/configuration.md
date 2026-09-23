---
modules: [resthome_split_billing]
---

# Setting up a split

:::{rh-description}
Setting up split billing in Resthome: the accounting settings, the debtors on the resident's record, capture at admission, and the terms frozen on the stay.
:::

:::{rh-faq}
Where do I set the debtors?
: On the resident's record, Billing tab: choose a split **Invoice Type**, then fill in the **Split Billing Partners** list.

What must be configured before the first split invoice?
: A dedicated split billing journal and a suspense account, in the settings of the **Nursing Home** app. Without them, generation stops before anything is produced.

I changed the debtors and the current month did not change. Why?
: Because a stay bills under the terms it was opened with. New debtors apply to the next stay.
:::

## 1. The accounting settings

In the **Settings** of the **Nursing Home** app, under the optional features:

- **Split Billing Journal** — a journal of its own, separate from the resident
  journal.
- **Split Billing Suspense Account** — the account that carries the resident
  statement.

:::{admonition} Required before generating
:class: warning

Without these two settings, the generation of split invoices stops **before**
touching anything. Nothing is produced, nothing is deleted.
:::

## 2. The debtors on the resident

On the **resident's record**, **Billing** tab:

1. Set **Invoice Type** to **Split Billing — Anticipatory** or
   **Split Billing — Arrears**, depending on whether the month is billed in
   advance or in arrears.
2. Fill in the **Split Billing Partners** list: the **debtor**, the
   **intervention type** (**Percentage**, **Fixed amount** or **Variable**), and
   the percentage or the amount.
3. Save.

The order of the lines matters: the **last** line absorbs the rounding.

:::{admonition} Percentages balance themselves
:class: tip

On saving, lines left at zero share what remains; otherwise the last untouched
line absorbs the difference. Deleting a line frees its share to the last one.
Fixed amounts are never rebalanced automatically.
:::

A few rules worth knowing:

- a resident cannot be their own debtor, and each debtor appears once;
- a fixed amount must be positive;
- **an archived debtor blocks generation**, naming the person concerned;
- a resident set to split billing **without any debtor** is refused.

## 3. At admission

The [admission wizard](../admissions/admettre.md) carries the same list: the
debtors can be recorded straight away. If the resident already has some, the
wizard shows them for reference only, with a note saying to change them on the
resident's record rather than in the dialog.

## 4. The terms are frozen on the stay

A stay bills under the terms it was **opened** with: the invoice type and the
debtors are copied onto it. Changing the debtors on the resident today affects
the **next** stay, not the one in progress.

## What's next

- [The documents produced](factures.md)
- [Invoicing a month, step by step](../facturation/facturer-un-mois.md)
