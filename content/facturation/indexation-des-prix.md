---
modules: [healthcare_accommodation_billing]
howto_auto: true
sectors: [mr, rs]
---

# Price indexation

:::{rh-description}
Raise the selling prices of supplements by a percentage from a given date, keep the history of every price, and bill each month at the price in force.
:::

:::{rh-faq}
How do I index the prices of the supplements?
: In Billing → Facturation → Products, select the products, then Actions → Index prices. Enter the percentage, the date it applies from and a note, then click Apply.

Can I record an indexation before it applies?
: Yes. The new price starts on the date you enter; the product's sales price changes on its own that morning.

Does an indexation change the price of residents' conventions?
: Yes, for every line that follows the official price. A line with Negotiated price ticked keeps its own price.

Which price is used when an old month is billed again?
: The price in force that month. A period regenerated in September bills July at July's price.

Can I delete the price history?
: No. The master pricelist holds every price already charged to residents: it cannot be deleted, only archived.
:::

Selling prices move every year: an index is published with a date, and every
supplement price follows. WideCare records each indexation as a new price
starting on its date, and keeps the previous ones. Each month is then billed at
the price in force during that month.

## 1. Select the products

1. Open the **Billing** app → **Facturation → Products**.
2. Tick the products to index (filter or group the list first if needed).
3. Click **Actions → Index prices**.

The action is shown to billing managers and to the home's managers only.

## 2. Enter the indexation

The **Index prices** window opens.

- **Indexation (%)** — how much every selected price moves: 2 means +2 %.
- **Applies from** — the first day the new prices are charged.
- **Note** — where the number comes from (the reference of the publication).
  It is required: it is the whole audit trail.

The table lists each product with its **Current** and **Indexed** price.
Untick **Index** on a product to leave its price alone. **Products selected**
and **To be indexed** count them.

## 3. Apply

Click **Apply**. For each product, the price in force is closed the day before
the date, and the new one starts on that date, so no day is priced twice. The
list of the **Indexed prices** just created opens.

<!-- screenshot to add: the Index prices window with the percentage, the date and the products -->

## Where the new price applies

- **The product's sales price** — on the date itself, by a job that runs every
  morning. An indexation can therefore be recorded weeks in advance.
- **Supplement conventions** — every line that follows the official price.
  A line with **Negotiated price** ticked keeps its own **Unit Price**.
- **One-time supplements** — at the price in force for the month of the
  envelope.

:::{admonition} The master pricelist
:class: note

The price history lives in a pricelist flagged **Master pricelist**, named
**Official prices** and created at the first indexation. A company has only
one, and it cannot be deleted: it explains every price already invoiced. Each
of its rules carries the **Note** of the indexation that created it.
:::

## Going further

- [Supplements](supplements.md)
- [The Supplements app](application-supplements.md)
- [Billing overview](index.md)
