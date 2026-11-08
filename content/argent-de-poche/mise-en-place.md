---
howto_auto: true
modules: [resthome_pocket_money]
---

# Setting up pocket money

:::{rh-description}
Setting up pocket money in Resthome: the journals in the billing settings, the product that pays in, and the pocket money account of each resident.
:::

:::{rh-faq}
Do I need one accounting account per resident?
: No. Several residents can share the same pocket money account: Resthome reads each resident's share from the entries that name them.

What if I leave the pocket money journal empty?
: The resident keeps a single invoice a month, as before. The balance still rises with the provision.

What if I leave the settlement journal empty?
: The second invoice is not paid automatically out of the balance: pass the settlement entry by hand, as before.

Does the provision have to be billed to the resident?
: No. It may be billed to whoever pays it — a billing contact or a debtor of a split. It still credits the resident's own balance.
:::

Setting up pocket money takes three things: the **journals**, the **product**
that pays in, and the **resident**. Ask your accountant for the accounts and
journals to use.

## 1. The billing journals

In **Settings → Billing**, block **Billing Journals**:

- **Pocket money journal** — a **sales** journal for the **second invoice** of
  pocket money residents, the one carrying what the home bought for them. Left
  empty, everything stays on a single invoice.
- **Pocket money settlement journal** — a **miscellaneous** journal. Filled in,
  the second invoice is **paid automatically** out of the balance when it is
  posted. Left empty, you pass that entry by hand and the balance only records
  what is paid in.

:::{admonition} Settling automatically is an accounting decision
:class: note

That is why the settlement journal is empty by default: Resthome never draws on
money held for someone else unless the home has asked for it.
:::

## 2. The product that pays in

Open the product billed as the monthly provision and tick **Pays into pocket
money** (next to the internal reference). Its invoice line is then booked on
the resident's pocket money account instead of a revenue account, so the
balance rises with it — whoever the invoice is addressed to.

A home may pay in through more than one product (a public provision and a
family top-up, for instance): tick each of them.

:::{admonition} In Belgium
:class: rh-country rh-country-be

The Belgian billing provides a **Pocket money** monthly supplement for the
amount paid by the CPAS. Tick **Pays into pocket money** on it. See
[CPAS support](../belgique/cpas.md).
:::

## 3. The resident

1. On the resident's record, click **Contact** under their name to open their
   contact record.
2. Open the **Invoicing** tab, group **Pocket Money**.
3. Tick **Pocket money**.
4. Choose the **Pocket money account**, the accounting account that holds the
   money — required once the box is ticked.
5. Save.

Then add the provision to the resident: on their record, **Stay Agreement**
tab, add the product to the **Recurring supplements** list, with the amount
granted if it differs from the product's price.

:::{admonition} Not in the supplement envelope
:class: warning

Add the provision to the **Recurring supplements** of the stay agreement, not to
the monthly supplement envelope. The envelope holds the purchases of the month,
which go on the second invoice; the provision belongs on the ordinary invoice,
which is what brings the money in. See [Supplements](../facturation/supplements.md).
:::

The **Pocket money** button appears on the resident's record as soon as the box
is ticked and the account chosen.

:::{admonition} A choice of its own
:class: tip

Pocket money is ticked per resident, never deduced from who funds the stay: a
resident supported by a public body does not automatically receive pocket
money, and a resident funded by their family may.
:::

## What's next

- [Purchases and settlement](achats-reglement.md)
- [Pocket money](index.md)
- [Billing settings](../configuration/reglages-facturation.md)
