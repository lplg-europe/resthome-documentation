# The Supplements App

:::{rh-description}
The Supplements app of a nursing home (MR/MRS): multi-resident entry via the catalog, one-off or recurring supplements, conventions, catalog and reporting.
:::

:::{rh-faq}
What is the Supplements app for in a nursing home (MR/MRS)?
: It is the screen dedicated to entering supplements: opening a resident's catalog, adding supplements to several residents at once, managing recurring conventions, maintaining the supplements catalog and tracking billed amounts.

How do I add a supplement to several residents at once?
: On the Residents screen, select several residents (Ctrl+click on a computer, long press on a tablet, or the "Multiple selection" button), then click "Supplements (N)". A single catalog opens and every added supplement is applied to the open envelope of each selected resident.

What is the difference between a one-off supplement and a convention?
: A one-off supplement is billed once on the month's envelope (hairdresser, drink…). A convention groups the resident's recurring supplements (single room, TV, phone): it lives on the resident and survives a stay closure, a room change or a transfer.

Where do I define the list of supplements and their prices?
: In Configuration → Catalog. Each supplement has a type (daily, monthly or one-off), a price specific to the facility and, if needed, an AViQ code for the declaration to the insurance body.

Can I track the supplements billed per resident or per month?
: Yes, via the Reporting menu: graph, pivot table and list views break down the billed supplements per resident, per product and per month.
:::

The **Supplements** app is the screen dedicated to entering and managing
residents' supplements. It brings together in one place what would otherwise
be split between the resident record and the billing period: opening a
resident's catalog, adding supplements to several residents at once, managing
recurring conventions, maintaining the catalog and tracking billed amounts.

You will find it in the **main menu → Supplements app**.

:::{admonition} This page complements "Supplements"
:class: info

The basic concepts — the **supplements envelope** per resident and per month,
the **automatic synchronization** of the invoice, the protection when a month
is already posted — are explained in
[Supplements](supplements.md). This page describes the **dedicated
app** and its entry shortcuts. The app does not create any parallel
data: it acts on the same envelopes and the same conventions.
:::

<!-- screenshot to add: the Supplements app opened on the Residents screen (kanban view) -->

## The Residents screen (the starting point)

On opening, the app displays the **Residents** screen: the list of
active residents, in **kanban view** (cards) or **list view**. Each card
shows the photo, the name, the **room** and the **stay type** (MR / MRS), with
a basket icon "Add supplements".

- **Click a resident**: Resthome directly opens the **catalog** of their
  supplements envelope for the current month. You land on the entry
  grid, without going through the record.
- In **list view**, each row carries an **Add supplements** button, and
  the header an **Add via the catalog** button to act on the checked
  residents.

:::{admonition} Filter and group
:class: tip

The search bar filters by **MR** / **MRS** and groups by **room**
or by **stay type** — handy for quickly spotting a wing or a
floor before a bulk entry.
:::

## Adding supplements to several residents

This is the app's central shortcut: applying the same supplement to
several residents without reopening each record.

1. On the **Residents** screen, **select several residents**:
   - **Ctrl+click** (or Cmd+click) on a computer adds/removes a resident;
     **Shift+click** extends the selection to a range;
   - **long press** on a touch tablet;
   - or enable the **Multiple selection** button, which selects on a single
     click.
2. Click the **Supplements (N)** button that appears (N = number of selected
   residents). In list view, use **Add via the catalog**.
3. **A single catalog** opens. Each supplement you add, modify
   or remove there is **applied to the open envelope of each selected
   resident**, for the current month.

In this shared catalog, the left panel shows a
**Residents** section: the residents concerned appear as tags (the
"pilot" resident in grey, the others in green). The **Add** link lets you
add more on the fly; removing a tag takes out the resident (the
last one cannot be removed).

<!-- screenshot to add: the multi-resident catalog with the Residents section (tags) on the left -->

:::{admonition} A supplement already covered by a convention is skipped
:class: note

If one of the selected residents already has this product in an **active
convention**, the line is **not** added for them (it would be discarded
at billing anyway) — the other residents receive it normally.
For entry on a single resident, Resthome blocks the addition outright and
prompts you to go through the convention.
:::

## One-off and recurring supplements

The app distinguishes the two kinds of supplements already presented in
[Supplements](supplements.md).

- **One-off** — added to the month's envelope via the catalog (hairdresser,
  pedicure, drink, phone…). The **One-off supplements** menu gives the
  **list**, grouped by resident, with the period, the product, the quantity, the
  price and the total. This is the place to review everything entered by hand
  over the month.
- **Recurring** — renewed each month via a **convention** (see the next
  section).

<!-- screenshot to add: the One-off supplements menu, list grouped by resident -->

:::{admonition} Where did my supplement go?
:class: tip

On each addition, Resthome shows a notification indicating **which
period(s)** the supplement was billed on — or warns you that **no open
period** yet matches its date (it will then only be billed once the
relevant month is generated). Check the **start date** if the
supplement does not appear where you expected.
:::

## Supplement conventions

A **convention** groups a resident's **recurring** supplements (single
room, TV, phone…). It lives on the **resident**, not on the stay:
it **survives** a stay closure, a room change or an MR ↔ MRS transfer.
Each resident has **one single** convention, which gathers all their
recurring lines.

In the app, the **Conventions** menu lists the recurring supplement
lines (resident, convention, product, type, dates, quantity, active). The
convention itself — with its status and its buttons — is managed from
the **MR/MRS → Billing → Supplement conventions** app.

On the convention:

| Element | Role |
|---|---|
| **Status** | **Open** or **Closed** (at the top of the record). |
| **Close** button | Sets an **end date** and stops billing each line beyond it. |
| **Reopen** button | Clears the end date and reactivates the lines that had been closed. |
| **Lines** | Product, type, price, start date, end date, quantity, active, notes. |

<!-- screenshot to add: a supplement convention with the Close button and the list of lines -->

:::{admonition} A product under a convention cannot be entered as one-off
:class: warning

As long as a product is covered by an **active convention**, it cannot be
added as a one-off supplement for the same resident. Add it **to
the convention**, or **close** that convention first.
:::

## The supplements catalog

The **Configuration → Catalog** menu holds the list of billable **supplement
types** ("Supplement types"). Each supplement has:

| Field | Description |
|---|---|
| **Reference** | Internal code of the supplement. |
| **Name** | Label shown in the catalog. |
| **Supplement type** | **Daily** (billed pro rata over the days), **Monthly** (per month) or **One-off** (once). |
| **Price** | Unit amount — **value specific to the facility**. |
| **AViQ code** | Declaration pseudo-code, when the supplement is declared to the insurance body. |

:::{admonition} Declared to the insurance body or not?
:class: info

Depending on its **category**, a supplement is either **declared to the
insurance body** in the eFact (ET50), or billed **only on the resident's
invoice**. This setting is made on the product category — see
[Billing settings](../configuration/reglages-facturation.md).
:::

## Reporting

The **Reporting** menu opens an analysis view of **billed** supplements:

- a **graph** of amounts per product;
- a **pivot table** (residents × months);
- a detailed **list** of supplement lines.

You can filter between **one-off** and **convention** supplements, and
group by **resident**, **product** or **month**.

<!-- screenshot to add: the supplements reporting (pivot table residents × months) -->

:::{admonition} After generation only
:class: note

Supplements only appear in the reporting once the **billing period is
generated** for the relevant month.
:::

## Key points to remember

- The **Supplements** app is a dedicated entry screen; it acts on the
  **same envelopes and conventions** as billing — no duplicate data.
- The **Residents** screen is the starting point: click a resident to open
  their catalog, or **select several** (Ctrl+click / long press /
  **Multiple selection**) then **Supplements (N)** to serve them all at once.
- **One-off** = once on the envelope; **convention** = recurring, on the
  resident, surviving stay changes.
- A product under an **active convention** cannot be entered as one-off.
- The **catalog** carries the type and the price (value specific to the
  facility); the **reporting** tracks amounts per resident, product and month.

## Further reading

- [Supplements](supplements.md)
- [Billing a month, step by step](facturer-un-mois.md)
- [Billing overview](index.md)
- [Billing settings](../configuration/reglages-facturation.md)
