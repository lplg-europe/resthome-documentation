---
modules: [healthcare_accommodation_billing, resthome_split_billing]
sectors: [mr, csj]
---

# Invoice type: in advance or in arrears

:::{rh-description}
Choose whether a resident's accommodation is billed in advance or for the elapsed month, change it during a stay, and give a single month a different invoice type.
:::

:::{rh-faq}
What is the difference between anticipatory and arrears billing?
: With Anticipatory Billing, the accommodation is billed one month in advance, and the care allowance and the supplements for the elapsed month. With Arrears Billing, everything is billed for the elapsed month.

Where do I set a resident's invoice type?
: On the resident's contact record: open the resident, click the Contact link under their name, and choose the Invoice Type at the top of the form.

What happens when I change the invoice type of a resident who is already staying?
: The new type applies from today to their running stay. Moving from advance to arrears creates a credit note for the accommodation already billed ahead; moving from arrears to advance creates the catch-up invoice of the current month.

Can I change the invoice type for one month only?
: Yes. Open the month's billing period, click the resident in the Residents tab and choose an Invoice Type (this period). It applies to that month only.

Why is a resident's row yellow in the billing period?
: Their invoice type for the month changed after the billing lines were built. Open the row and click Apply the Invoice Type: until then, WideCare refuses to create or post their invoices.
:::

Each resident is billed under an **invoice type**. It answers two questions:
**when** the accommodation is billed (one month in advance, or once the month
is over), and **who** receives the invoice (the resident alone, or several
debtors when [split billing](../facturation-partagee/index.md) is installed).

## The invoice types

| Invoice type | Accommodation | Care allowance and supplements | Invoice sent to |
|---|---|---|---|
| **Anticipatory Billing** (default) | One month in advance | For the elapsed month | The resident, or their billing contact |
| **Arrears Billing** | For the elapsed month | For the elapsed month | The resident, or their billing contact |
| **Split Billing — Anticipatory** | One month in advance | For the elapsed month | One invoice per debtor |
| **Split Billing — Arrears** | For the elapsed month | For the elapsed month | One invoice per debtor |

The two **Split Billing** types only appear once split billing is turned on in
the [billing settings](../configuration/reglages-facturation.md).

:::{admonition} A day place is never billed in advance
:class: note

For someone who lives at home and only comes during the day, the invoice type
is hidden: there is no room to bill ahead.
:::

## Set the invoice type of a resident

1. Open the resident's record.
2. Click the **Contact** link under the resident's name.
3. At the top of the contact form, choose the **Invoice Type**.
4. Save.

The type can also be chosen in the [admission wizard](../admissions/admettre.md),
which writes it back to the resident.

### The first invoice of an admission

For a resident billed in advance, the month of admission cannot wait for the
next billing period. When the stay is **confirmed** or **started**, WideCare
creates the **first accommodation invoice** on its own: from the admission date
to the end of the month.

If it cannot be created (no resident journal set, room without a price…), a
notification says why, and the same message is written on the stay. Fix the
cause, then click **Create First Invoice** on the stay.

## Change the invoice type during a stay

Change the **Invoice Type** on the contact as above. WideCare applies it **from
today** to the resident's confirmed or running stay:

- **a stay already billed** is closed the day before and continued on a new
  stay, same room, under the new type;
- **a stay not started yet**, or on its arrival day, simply changes type.

The money left hanging by the switch is settled at the same time:

| Switch | What WideCare creates |
|---|---|
| **Anticipatory → Arrears** | A **credit note** for the accommodation already billed ahead from today — the posted admission invoice included. Otherwise the resident would pay those days twice. |
| **Arrears → Anticipatory** | A **catch-up invoice** for the current month, which neither type would otherwise bill. |
| **Anticipatory ↔ Split Billing — Anticipatory** (same timing) | Nothing to settle: the same days are billed, to other people. |

The stay records the change in its discussion thread. On the stay, the
**Invoice Type** field shows the type the stay is billed under; it can only be
edited while the stay is still a draft.

:::{admonition} Dating the change yourself
:class: tip

To apply a new invoice type from another date, use **Change Room** on the stay,
keep the same room and fill in the **New invoice type** next to the change
date. See [Room change and transfer](../residents/changement-chambre.md).
:::

:::{admonition} When the month is already closed
:class: warning

If the billing period covering the change date is **closed**, the type changes
but nothing is billed or credited for it. Reopen the period first if the change
has to reach the invoice.
:::

## Change the invoice type for one month

Sometimes a single month must be billed differently — a family that pays one
month in arrears, for instance — without changing the resident's type.

1. Open the month's billing period (**Billing → Facturation → Billing Periods**).
2. In the **Residents** tab, click the resident: their **Resident Billing**
   detail opens.
3. Choose the **Invoice Type (this period)**. Left empty, the month follows the
   stay ("As the stay").
4. Save.

:::{admonition} In split billing
:class: note

When the month is given a split invoice type, **Debtors (this period)** lets you
pick which of the resident's debtors share this month. By default, the month is
split between the debtors of the stay. Their shares are checked with the same
rules as on the resident's record.
:::

The choice is kept for this month only, even when the period is generated
again or refreshed.

### Apply the new type

If the month's billing lines or invoice were already built, the change is not
applied at once:

- the resident's row turns **yellow** in the **Residents** tab of the period;
- the detail shows a warning and an **Apply the Invoice Type** button.

Click **Apply the Invoice Type**: the month's lines are rebuilt, and its draft
invoice with them.

:::{admonition} Invoices are refused until the type is applied
:class: warning

While a row is yellow, **Create Invoices** on the period and posting that
resident's invoice are both refused, with a message naming the residents to
open.
:::

### When the type can no longer change

The field is locked, and a line under it says why, when:

- the period is **closed**;
- the period is not **generated** yet;
- the resident already has a **posted** invoice for the month — reset it to
  draft first.

A change that moves the accommodation between advance and arrears is also
refused when a **later** period is already generated for the resident, because
that period measured what it bills on the old timing. Remove the resident from
the later period, or reset it to draft, first.

## Going further

- [Billing a month, step by step](facturer-un-mois.md)
- [Departure and death](depart-deces.md)
- [Split billing](../facturation-partagee/index.md)
- [Billing settings](../configuration/reglages-facturation.md)
