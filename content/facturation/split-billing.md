# Maintenance debtors (split billing)

:::{rh-description}
Split the resident's share of an invoice among several maintenance debtors in Resthome, by percentage.
:::

:::{rh-faq}
What is split billing among maintenance debtors?
: A way of splitting the resident's share of the invoice among several people - typically the maintenance debtors (children, relatives) - according to a percentage key.

Which part of the invoice is split?
: Only the resident's share, meaning the room and the supplements. The INAMI package is not split: it goes to the health insurance fund through eFact.

How do I set up a split?
: On the resident record or its billing period, open the split tab, add the debtors and their percentage - the total must be 100% - then save. Subsequent invoices are split automatically.

Does the split add up exactly?
: Yes. The sum of the portions matches the resident's share precisely, with no remainder or rounding difference.
:::

When the **resident's share** (accommodation + supplements) must be paid by
**several people** — typically the **maintenance debtors** (children,
relatives) — Resthome can **split it automatically**.

## The principle

For a resident, you define a **percentage split** among several debtors. On each
monthly invoice, Resthome **splits the resident's share** according to these
percentages and sends each debtor **their portion**.

:::{admonition} What gets split
:class: note

Only the **resident's share** is affected (the room and the supplements). The
**INAMI package** (the insurer's share) is not split: it goes to the health
insurer via [eFact](../ehealth/efact.md).
:::

## Setting up a split

1. On the **resident** record (or its billing period), open the **split** tab.
2. Add the **debtors** and their **percentage** (the total must be 100%).
3. **Save.**

Subsequent invoices are automatically **split** according to this key.

:::{admonition} Balancing to zero
:class: tip

The split is designed to **add up exactly**: the sum of the portions matches the
resident's share precisely, with no remainder or rounding difference.
:::

## Further reading

- [Billing overview](index.md)
- [Supplements](supplements.md)
