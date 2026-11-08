---
modules: [resthome_split_billing]
---

# Setting up a split

:::{rh-description}
Setting up split billing in Resthome: the accounting settings, the debtors on the resident's contact, capture at admission, and what happens to a stay when the debtors change.
:::

:::{rh-faq}
Where do I set the debtors?
: On the resident's contact (the Contact link under their name): choose a split Invoice Type at the top, then fill in the Split Billing Partners list in the Invoicing tab. The same list can be edited from the stay.

What must be configured before the first split invoice?
: A dedicated split billing journal and a suspense account, in the billing settings, Optional features block. Without them, generation stops before anything is produced.

I changed the debtors. Which months does it affect?
: The running stay follows the new debtors from the next generation of a month not invoiced yet. A stay that has ended keeps the debtors it was billed with.

Can the debtors differ for one month only?
: Yes. In the resident's detail of a billing period, Debtors (this period) picks among the resident's debtors for that month alone.
:::

## 1. The accounting settings

In the [billing settings](../configuration/reglages-facturation.md), block
**Optional features**:

1. Tick **Split Billing (food debtors)**. The split billing feature is
   installed.
2. Fill in **Split Billing Journal** — a journal of its own, separate from the
   resident journal.
3. Fill in **Split Billing Suspense Account** — the account that carries the
   resident statement.

:::{admonition} Required before generating
:class: warning

Without these two settings, the generation of split invoices stops **before**
touching anything. Nothing is produced, nothing is deleted.
:::

## 2. The debtors on the resident

1. Open the resident's contact: the **Contact** link under their name.
2. At the top of the form, set **Invoice Type** to **Split Billing —
   Anticipatory** or **Split Billing — Arrears**, depending on whether the
   month is billed in advance or in arrears. See
   [Invoice type](../facturation/type-de-facture.md).
3. In the **Invoicing** tab, fill in the **Split Billing Partners** list: the
   **Debtor**, the **Intervention Type** (**Percentage**, **Fixed amount** or
   **Variable**), and the **Invoice %** or the **Fixed Amount**.
4. Save.

While the percentages do not reach 100, a red **Remaining to allocate** line
shows what is left. The order of the lines matters: the **last** line absorbs
the rounding.

With fixed amounts, they are invoiced first and the **Variable** debtor takes
what is left. When the resident's share is smaller than the fixed amounts, each
is invoiced pro rata and the variable debtor gets nothing.

<!-- screenshot to update: the contact's Invoicing tab with the Split Billing Partners list -->

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

## 4. When the debtors or the type change

- **A running stay follows the resident's debtors.** A debtor added, changed
  or removed applies from the next generation of a month not invoiced yet. The
  stay form shows the same **Split Billing Partners** list and lets you edit it:
  the change is written to the resident.
- **An ended stay keeps its debtors.** Its **Split Billing Partners as Billed**
  stay as they were, so a month regenerated later is split as it was billed.
- **For one month only**, open the resident's detail in the billing period:
  **Debtors (this period)** picks among the resident's debtors, the stay's by
  default, and checks that the shares still add up.
- **Changing the invoice type** (to or from split billing, or in advance ↔ in
  arrears) applies from today to the running stay. See
  [Invoice type](../facturation/type-de-facture.md).

## What's next

- [The documents produced](factures.md)
- [Invoice type](../facturation/type-de-facture.md)
- [Billing settings](../configuration/reglages-facturation.md)
- [Invoicing a month, step by step](../facturation/facturer-un-mois.md)
