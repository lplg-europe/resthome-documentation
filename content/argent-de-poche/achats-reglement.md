---
modules: [resthome_pocket_money]
sectors: [mr]
---

# Purchases and settlement

:::{rh-description}
How Resthome bills the purchases of a pocket money resident on a second invoice each month, and pays it automatically out of their balance.
:::

:::{rh-faq}
Why does a pocket money resident receive two invoices?
: The ordinary invoice carries the accommodation, the agreed supplements and the pocket money provision. The second one carries what the home bought for the resident during the month, and is paid out of their pocket money.

Which purchases go on the second invoice?
: The supplements of the resident's monthly envelope — the hairdresser, the pedicure, a newspaper. The recurring supplements of the stay agreement stay on the ordinary invoice.

Can I put the second invoice back to draft?
: Yes. The automatic settlement is undone at the same time, and the balance goes back up.

What if the balance is not enough?
: The invoice is settled all the same and the balance becomes negative: the resident's record shows **Pocket money overdrawn**.
:::

For a resident with pocket money, the monthly billing produces **two
invoices**, once the **Pocket money journal** is set (see
[Setting up pocket money](mise-en-place.md)).

## Two invoices a month

| Invoice | What it carries | Journal |
| --- | --- | --- |
| **Ordinary invoice** | Accommodation, the recurring supplements of the stay agreement, and the pocket money **provision** | The resident journal |
| **Second invoice** | The supplements of the monthly envelope: what the home bought for the resident | **Pocket money journal** |

The second invoice exists only when the month holds envelope supplements. In
every other case — no pocket money, no journal set, nothing bought this month —
the resident receives the single invoice they always received.

:::{admonition} Split billing
:class: note

When the resident share is split between several debtors, the split concerns
the ordinary invoice. The second invoice is paid out of money the home already
holds for the resident, and is not split. The provision billed to a debtor
still credits the resident's own balance.
:::

## The automatic settlement

When the **Pocket money settlement journal** is set, posting the second invoice
**pays it** out of the balance: Resthome passes an entry in that journal which
draws the amount from the resident's pocket money account and settles the
invoice, which shows as paid. The balance on the resident's record goes down by
the same amount.

- **Back to draft** — putting the second invoice back to draft undoes the
  settlement, and the balance goes back up.
- **Not enough money** — the settlement is passed anyway; the balance becomes
  negative and the record shows **Pocket money overdrawn**.
- **No settlement journal** — nothing happens on posting: pass the settlement
  by hand. The balance then only records what is paid in.

<!-- screenshot to add: second invoice of a pocket money resident, paid by the settlement entry -->

## Check a balance

On the resident's record, the **Pocket money** button opens the entries behind
the balance: the provisions paid in, the settlements drawn from it. The list
adds up to the figure on the button. See [Pocket money](index.md).

## What's next

- [Pocket money](index.md)
- [Supplements](../facturation/supplements.md)
- [Invoice a month, step by step](../facturation/facturer-un-mois.md)
