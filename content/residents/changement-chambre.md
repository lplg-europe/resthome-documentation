# Room change and transfer

:::{rh-description}
Move a resident to another room or transfer them between MR and MRS in Resthome — billing is split automatically, with no new admission.
:::

A resident can **change room** or move from **MR to MRS** (or the other way
around) during their stay. Resthome handles the **transition** cleanly: billing
is **split** at the right date, without you having to redo an admission.

## Changing room

For a simple room change (same type of care):

1. On the resident's **stay**, use the **Change room** action.
2. Enter the **new room** and the **date/time** of the change.
3. **Validate.**

Resthome **closes** billing for the old room on that date and **opens** billing
for the new one, at the corresponding rate.

:::{admonition} No new admission
:class: note

A room change is **not** a new admission: the INAMI intervention (the flat rate)
stays **continuous**, there is no new agreement to request. Only the
**accommodation portion** is split across the two rates.
:::

## MR ↔ MRS transfer

Moving from one type of care to the other (MR ↔ MRS) is an **internal transfer**:

1. On the stay, use the **Internal transfer** action.
2. Enter the **date/time** of the transfer and the **new type of care**.
3. **Validate.**

Resthome splits billing at the transfer date and **updates the flat rate**
according to the new type. Where applicable, it prepares the corresponding
**eHealth notification**.

:::{admonition} Billing follows automatically
:class: tip

After a room change or a transfer, you have nothing to recalculate by hand: each
segment is billed at its own rate, and the flat rate continues without
interruption.
:::

## Learn more

- [Manage a resident](gerer-un-resident.md)
- [Billing overview](../facturation/index.md)
