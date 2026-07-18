# Absences and hospitalisations

:::{rh-description}
Record an absence or a hospitalisation in Resthome — effect on the allowance, the 72-hour rule, automatic eHealth notification, cancellation.
:::

When a resident is away (hospitalisation, holidays, family leave), this affects
**the INAMI allowance** for the period and may trigger a **notification to the
mutuality**. Resthome handles both automatically from the absence you record.

## Record an absence

1. Open the month's **billing period**, or the resident's file.
2. Add an **absence**, specifying:
   - the **resident**;
   - the **type** (hospitalisation, holidays, etc.);
   - the **departure date/time** and the **return date/time** (or leave the
     return blank while the resident has not come back yet).
3. **Save.**

:::{admonition} You don't need to click "Refresh"
:class: tip

Adding, modifying or deleting an absence **automatically synchronises** the
billing of the resident concerned: the allowance is recomputed and, where
applicable, the eHealth notification is prepared. See
[billing](index.md#the-refresh-button).
:::

## Effect on the allowance

The **INAMI allowance** (mutuality share) is computed on the **presence days**.
An absence **reduces** this allowance for the days concerned.

:::{admonition} The "noon rule"
:class: note

The count of absence days follows a presence-at-**noon** rule (Brussels time):
it is the presence at noon that determines whether the day counts. The
**dates and times** of departure and return therefore matter — Resthome relies
on them for an exact count.
:::

The **accommodation share** (the room, paid by the resident) follows its own
rules according to your agreement.

## Notification to the mutuality (eHealth)

Some absences must be reported to the mutuality:

- an absence of **more than 72 hours**, or **any hospitalisation**, prepares an
  **Annex 11** (exit notification);
- the resident's **return** prepares an **Annex 7** (readmission).

Resthome creates these notifications **at the moment you record the absence and
the return**, with no extra handling. You only have to check and send them. See
[Agreements (eAgreement)](../ehealth/eagreement.md).

## Cancel an absence

An absence entered by mistake? **Delete it** or set it back to draft: Resthome
**rolls it back cleanly** — the allowance is recomputed as if the absence had
never happened, and the prepared notifications are withdrawn as long as they
have not been validated on the mutuality side.

:::{admonition} Month already invoiced
:class: warning

If the month's invoice is **already posted** for this resident, Resthome does
not change that month automatically (protection against double invoicing). To
correct it anyway: reset the invoice to **draft** (or create a **credit note**),
then **refresh**. The other residents in the period are not affected.
:::

## Going further

- [Agreements (eAgreement)](../ehealth/eagreement.md)
- [Departure and death](depart-deces.md)
- [Billing overview](index.md)
