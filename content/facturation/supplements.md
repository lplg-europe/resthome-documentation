---
modules: [resthome_sales, healthcare_accommodation_billing]
sectors: [mr, csj]
---

# Supplements

:::{rh-description}
Bill supplements in WideCare — recurring supplements on the resident's convention, one-time supplements on the monthly envelope, supplement types and automatic synchronisation.
:::

:::{rh-faq}
What is the difference between a one-time and a recurring supplement?
: A one-time supplement is billed once, on the month's envelope (a haircut, for instance). A recurring supplement lives on the resident's supplement convention and is billed every month while it is active (single room, TV).

What is a supplement envelope?
: A per-resident, per-month document that gathers the resident's one-time supplements. The Envelopes button on the resident's record lists them.

Do I need to refresh the invoice after adding a supplement?
: No. With automatic billing refresh turned on, adding, editing or removing a supplement updates the resident's billing of the month on its own.

How do I give a resident a price of their own?
: On the line of their supplement convention, tick Negotiated price and enter the Unit Price. Unticked, the line follows the official price, including its yearly indexation.

What if the resident's invoice is already posted?
: The posted invoice is not rewritten. The billing period shows Corrections pending: click Refresh to create the supplementary invoice or credit note.
:::

Beyond accommodation and the care allowance, a resident may have **supplements**
to pay: single room, television, hairdresser, pedicure, drinks, telephone…
WideCare handles two kinds.

## Supplement types

Each supplement is a product of the **supplements catalog**
(**Billing → Configuration → Supplement Types**), with a **Supplement Type**
that says how it is counted:

| Supplement type | Billed |
|---|---|
| **Monthly** | Once per month. |
| **One-time** | Once, when it is entered. |
| **Daily — accommodation days** | Per day of stay: the bed stays reserved during an absence, so it keeps being billed (a single-room supplement). |
| **Daily — presence days** | Per day the resident is actually there: not billed during an absence (a TV the resident does not watch while in hospital). |

The price on the product is the official price. It can be raised every year
with [price indexation](indexation-des-prix.md).

## Recurring supplements: the convention

A resident's recurring supplements are grouped on **one supplement convention**,
kept on the **resident** rather than on the stay: it survives a room change or a
transfer.

On the resident's record, open the **Stay Agreement** tab: the **Recurring
supplements** section lists them, and the **Supplements** smart button opens
the convention.

1. Add a line: **product**, **Supplement Type**, **start date**, **quantity**.
2. To charge this resident a price of their own, tick **Negotiated price** and
   enter the **Unit Price**.
3. To stop a line, give it an **end date**, or untick **Active**.

Greyed lines are no longer billed. The **Close supplements** button sets an end
date on the whole convention; **Reopen supplements** lifts it.

:::{admonition} Nothing without a stay
:class: note

Recurring supplements start once the resident has a stay. A resident with no
stay gets no line here, and the section says so.
:::

## One-time supplements: the monthly envelope

One-time supplements go on the resident's **envelope** of the month. The
**Envelopes** smart button on the resident's record lists them, one per month.

The quickest way to enter them is the [Supplements app](application-supplements.md):
click a resident, or select several, and add supplements from the catalog.

:::{admonition} A product under a convention
:class: warning

In the catalog, a product already covered by the resident's active convention
cannot be added as a one-time supplement: add it to the convention, or close
that line first.
:::

:::{admonition} Automatic synchronisation
:class: tip

Adding, editing or removing a supplement updates the resident's billing of the
month on its own, as long as automatic billing refresh is turned on in the
[billing settings](../configuration/reglages-facturation.md).
:::

## Envelopes for every resident

Envelopes are opened on their own when the month is generated. To open the
missing ones of a period in advance, use **Create missing supplement envelopes
(SOs)** from the gear menu of the billing period.

## When the month is already invoiced

- On a **draft** invoice, **Refresh** (gear menu of the invoice) rebuilds it
  from the current data, keeping the same invoice.
- On a **posted** invoice, the change becomes a supplementary invoice or a
  credit note: the period shows **Corrections pending**, click **Refresh**.

## Further reading

- [The Supplements app](application-supplements.md)
- [Recharging a vendor bill](refacturation-fournisseur.md)
- [Price indexation](indexation-des-prix.md)
- [Billing overview](index.md)
