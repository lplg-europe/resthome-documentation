---
modules: [healthcare_accommodation_billing]
---

# Absences and hospitalisations

:::{rh-description}
Record an absence or a hospitalisation in Resthome — statuses, effect on the day count and the bill, absence discount rules, cancellation.
:::

:::{rh-faq}
How do I record an absence in Resthome?
: Open Absences (from the Billing app or from the Residents menu), click New, choose the resident, the absence type and the departure date and time, then click Confirm. Fill in the return and click Close (return recorded) when the resident is back.

How does an absence affect the bill?
: The days are counted from the departure and return times. The care allowance follows the presence days, and the accommodation share is reduced only by the absence discount rules set up by the home.

Why do the departure and return times matter?
: Because whether a day counts as a presence day depends on the time the resident left and came back. Resthome relies on the exact times for the count.

Can I cancel an absence entered by mistake?
: Yes. Click Cancel, or step it back with Reset to draft: the billing is recomputed as if the absence had never happened.

What if the month is already invoiced?
: Resthome never rewrites a posted invoice. The period shows "Corrections pending": click Refresh to create the supplementary invoice or credit note. Other residents in the period are unaffected.
:::

When a resident is away (hospitalisation, holidays, family outing), this affects
**the billing** of the period. Resthome adjusts it automatically from the
absence you record.

## Where to record it

The same list is reachable from two places:

- **Billing → Facturation → Absences**, for whoever bills;
- **Nursing Home → Residents → Absences**, for the staff on the floor when the
  resident leaves.

The resident's record (**Absences** smart button), the stay (**Absences** tab)
and the **+** button of the [billing dashboard](tableau-de-bord.md) open it
too.

## Record an absence

1. Click **New**.
2. Fill in:
   - the **resident** (and their **stay**, filled in for you);
   - the **Absence Type**: **Hospitalization**, **Vacation**, **Family Outing**
     or **Other**;
   - for a hospitalisation, the **Destination** hospital; otherwise, the
     **Destination (free text)**;
   - the **Departure** date and time.
3. Click **Confirm**: the absence days start counting.
4. When the resident comes back, fill in the **Return** date and time, then
   click **Close (return recorded)**.

Leave the return empty while the resident is still away. The list shows those
absences in orange, and the **Ongoing (no return)** filter finds them.

:::{admonition} The calendar helps
:class: tip

The date pickers only offer days within the resident's stay, and strike out the
days already taken by another absence. Under the form, **Existing absences for
this resident** lists the others.
:::

## Statuses

| Status | Meaning |
|---|---|
| **Draft** | Entered, not counted yet. |
| **Confirmed** | The resident is away; the days count. |
| **Closed** | The return is recorded. |
| **Cancelled** | Withdrawn; it no longer counts. |

## Effect on the bill

Once the return is known, the absence shows what it costs:

- **Total Absence Days** — the days counted as absent over the whole absence;
- **Billing Days** — the days the home will not collect from the resident,
  under the absence discount rules, and **Discount basis**, which says which
  rule applied and why the result may be 0;
- **Absence Days (return month)** and **Days to Bill (return month)** — the
  share of the month the resident came back in.

Whether a day of departure or return counts as a presence day depends on the
**time**: by default, a departure after noon or a return before noon counts as
a presence day. The country pack can apply its own thresholds.

The **care allowance** (the insurer's share), where the country bills one,
follows the presence days. The **accommodation share** keeps being billed: the
room stays reserved. It is reduced only by the **absence discount rules** below.

:::{admonition} You don't need to click "Refresh"
:class: tip

With automatic billing refresh turned on (the default), confirming, closing or
cancelling an absence updates the billing of the resident concerned on its own.
See [Billing settings](../configuration/reglages-facturation.md).
:::

:::{admonition} In Belgium
:class: rh-country rh-country-be

Days are counted on presence at noon (Brussels time). An absence of more than
72 hours, or any hospitalisation, prepares an Annexe 11 notification for the
mutuality as soon as it is recorded; the return prepares an Annexe 7. Stepping
the absence back withdraws them while they are not sent. See
[Billing a month in Belgium](../belgique/facturation.md) and
[Agreements (eAgreement)](../belgique/ehealth/eagreement.md). For a day care
user, see [Absences and hospitalisation of a day care user](../belgique/centre-de-jour/absences.md).
:::

## Absence discount rules

Managers decide how much of the room an absence takes off the bill, in
**Billing → Configuration → Absence Discount Rules**. Each rule has:

- the **Absence Type** it applies to, and an optional validity (**Start Date**,
  **End Date**);
- a **Days Threshold** — the absence days that must be exceeded before the
  discount starts (0 = from the first day);
- a **Discount Type** — **Percentage of daily room rate** or **Amount per
  day**, with its value;
- the **Discount Product** used on the billing line.

Two active rules for the same absence type cannot overlap in time. Without a
rule, an absence does not reduce the accommodation share.

## Cancel or step back

On the absence, depending on its status:

- **Cancel** — withdraws it; the billing is recomputed as if it had never
  happened;
- **Reset to draft** — steps a confirmed or cancelled absence back to draft;
- **Cancel return** — reopens a closed absence (back to confirmed).

:::{admonition} Month already invoiced
:class: warning

If every month the absence spans is already settled for this resident (closed
period or posted invoice), a warning on the absence says so: it is still
recorded, but it no longer changes the billing. When only some months are
posted, the period shows **Corrections pending**: click **Refresh** to create
the supplementary invoice or credit note. The **Corrective docs** smart button
on the absence lists them.
:::

## Going further

- [Hospital departure and return](../soins/hospitalisation.md) — the care side: prescriptions suspended, care cancelled, liaison pack and record review.
- [Departure and death](depart-deces.md)
- [Month-end checklist](checklist-fin-de-mois.md)
- [Billing overview](index.md)
