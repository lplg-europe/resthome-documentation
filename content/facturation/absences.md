---
modules: [healthcare_accommodation_billing, l10n_health_be_perdiem_ehealth]
---

# Absences and hospitalisations

:::{rh-description}
Record an absence or a hospitalisation in Resthome — effect on the care allowance, the day count, the notification to the health insurer, cancellation.
:::

:::{rh-faq}
How do I record an absence in Resthome?
: From the month's billing period or the resident's file, add an absence with the type (hospitalisation, holidays...) and the departure and return date and time. Leave the return blank while the resident is still away.

How does an absence affect the care allowance?
: The care allowance is computed on presence days, so an absence reduces it for the days concerned. The accommodation share follows the rules of your own agreement.

Why do the departure and return times matter?
: Because whether a day counts as a presence day depends on the time the resident left and came back, under the counting rule of the country. Resthome relies on the exact times for the count.

Which absences must be reported to the health insurer?
: It depends on the country. Where a notification is required, Resthome prepares it as soon as you record the absence and the return; you only check and send it.

Can I cancel an absence entered by mistake?
: Yes. Delete it or set it back to draft: the care allowance is recomputed as if the absence had never happened, and prepared notifications are withdrawn as long as the insurer has not validated them.

What if the month is already invoiced?
: Resthome does not change a posted invoice automatically, to prevent double invoicing. Reset the invoice to draft or issue a credit note, then refresh. Other residents in the period are unaffected.
:::

When a resident is away (hospitalisation, holidays, family leave), this affects
**the care allowance** for the period and may trigger a **notification to the
health insurer**. Resthome handles both automatically from the absence you
record.

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
billing of the resident concerned: the care allowance is recomputed and, where
applicable, the notification to the health insurer is prepared. See
[billing](index.md).
:::

## Effect on the allowance

The **care allowance** (the insurer's share) is computed on the **presence
days**. An absence **reduces** this allowance for the days concerned.

Whether a day of departure or return counts as a presence day depends on the
**time**: the **dates and times** of departure and return therefore matter —
Resthome relies on them for an exact count.

The **accommodation share** (the room, paid by the resident) follows its own
rules according to your agreement.

## Notification to the health insurer

Where the country requires it, some absences must be reported to the resident's
health insurer — typically a long absence or a hospitalisation, then the
resident's return.

Resthome creates these notifications **at the moment you record the absence and
the return**, through the electronic exchanges with the health insurer, with no
extra handling. You only have to check and send them.

:::{admonition} In Belgium
:class: rh-country rh-country-be

Days are counted on presence at noon (Brussels time). An absence of more than
72 hours, or any hospitalisation, prepares an Annexe 11 for the mutuality; the
return prepares an Annexe 7. See
[Billing a month in Belgium](../belgique/facturation.md) and
[Agreements (eAgreement)](../belgique/ehealth/eagreement.md).
:::

## Cancel an absence

An absence entered by mistake? **Delete it** or set it back to draft: Resthome
**rolls it back cleanly** — the care allowance is recomputed as if the absence
had never happened, and the prepared notifications are withdrawn as long as
they have not been validated by the health insurer.

:::{admonition} Month already invoiced
:class: warning

If the month's invoice is **already posted** for this resident, Resthome does
not change that month automatically (protection against double invoicing). To
correct it anyway: reset the invoice to **draft** (or create a **credit note**),
then **refresh**. The other residents in the period are not affected.
:::

## Going further

- [Departure and death](depart-deces.md)
- [Month-end checklist](checklist-fin-de-mois.md)
- [Billing overview](index.md)
