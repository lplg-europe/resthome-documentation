---
modules: [healthcare_accommodation, healthcare_accommodation_billing, l10n_health_be_perdiem_ehealth, resthome_mr_billing]
---

# Room change and transfer

:::{rh-description}
Move a resident to another room or transfer them between the sectors the home is licensed for in Resthome — billing is split automatically, with no new admission.
:::

:::{rh-faq}
How do I change a resident's room?
: On the resident's stay, use the Change Room action, enter the new room and the date and time of the change, then validate.

Does a room change require a new admission?
: No. The care allowance paid by the health insurer stays continuous and there is nothing new to request from the insurer - only the accommodation portion is split across the two rates.

How do I transfer a resident to another sector?
: On the stay, use the Internal Transfer action, enter the date and time and the new type of care, then validate. Resthome updates the care allowance and, where the country requires it, prepares the notification to the health insurer.

Do I have to recalculate billing after a room change?
: No. Resthome closes billing for the old room on the chosen date and opens it for the new one, each segment at its own rate.
:::

A resident can **change room** or move to **another sector** the home is
licensed for during their stay. Resthome handles the **transition** cleanly:
billing is **split** at the right date, without you having to redo an admission.

## Changing room

For a simple room change (same type of care):

1. On the resident's **stay**, use the **Change Room** action.
2. Enter the **new room** and the **date/time** of the change.
3. **Validate.**

Resthome **closes** billing for the old room on that date and **opens** billing
for the new one, at the corresponding rate.

:::{admonition} No new admission
:class: note

A room change is **not** a new admission: the care allowance paid by the health
insurer stays **continuous**, and there is nothing new to request from the
insurer. Only the **accommodation portion** is split across the two rates.
:::

## Transfer between sectors

When the home is licensed for several sectors, moving from one to another is an
**internal transfer**. The **stay type** can no longer be edited once the stay is
confirmed: the change goes through the **Internal Transfer** action, which the
country pack provides where the country regulates sectors.

1. On the stay, use the **Internal Transfer** action.
2. Enter the **date/time** of the transfer and the **new type of care**.
3. **Validate.**

Resthome splits billing at the transfer date and **updates the care allowance**
according to the new type. Where the country requires it, it prepares the
**notification to the health insurer**.

:::{admonition} A sector can require a minimum dependency category
:class: warning

When a sector only takes residents above a given dependency category, Resthome
refuses to **put or keep a stay** in it for a resident assessed below — at
admission and at transfer time.

A **room change is not blocked**, though: a resident whose category no longer
matches their bed can still be moved from one room to another. A banner on their
record flags the situation until the transfer is entered.
:::

:::{admonition} In Belgium
:class: rh-country rh-country-be

The sectors are **MR** and **MRS**: an MRS bed only takes Katz categories **B
and above**, and the transfer produces the Annexe 11 + Annexe 7 pair for the
mutualité — see [Internal transfer (MR ↔ MRS)](../belgique/ehealth/eagreement-transfert.md)
and [The Katz assessment](../belgique/katz.md).
:::

:::{admonition} Billing follows automatically
:class: tip

After a room change or a transfer, you have nothing to recalculate by hand: each
segment is billed at its own rate, and the care allowance continues without
interruption.
:::

## Learn more

- [Manage a resident](gerer-un-resident.md)
- [Billing overview](../facturation/index.md)
