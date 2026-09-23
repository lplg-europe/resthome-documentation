---
modules: [healthcare_accommodation_billing, healthcare_accommodation, l10n_health_be_perdiem_ehealth]
---

# Departure and death

:::{rh-description}
Close a stay (departure or death) in Resthome — billing stops on the correct date, automatic credit note for prepaid accommodation, notification to the health insurer.
:::

:::{rh-faq}
How do I close a stay on departure or death?
: Open the resident's record and their stay, enter the departure date and time with the reason (departure, death, transfer...), then validate the closure.

Does Resthome issue a credit note automatically?
: Yes. Since accommodation is billed one month in advance, a departure partway through an already-billed month automatically prepares a credit note for the unoccupied period, and you are notified when it is created.

Why is there a refund when a resident leaves?
: Because accommodation is billed the previous month (anticipatory billing). The care allowance and the supplements, by contrast, are billed on the month actually served.

Is the health insurer notified of the departure?
: Where the country requires it, yes: the closure prepares the departure notification to the resident's health insurer.

Can I reopen a stay closed by mistake?
: Yes. Resthome restores billing and cancels the adjustments, as long as they are not yet final. If the month is already posted, go through a reset to draft or a credit note first.
:::

When a resident leaves the facility or passes away, all you need to do is **close their stay**: Resthome stops billing on the correct date, prepares the **adjustment** for what was billed in advance, and notifies the health insurer of the departure where the country requires it.

## Close the stay

1. Open the resident's record → their **stay**.
2. Enter the **departure date** (and the time), with the **reason** (departure, death, transfer…).
3. **Validate** the closure.

## What Resthome does automatically

- **Billing stops** on the correct date: nothing is billed after the departure.
- **Credit note for prepaid accommodation**: since accommodation is billed **one month in advance** (anticipatory billing), if the resident leaves partway through an already-billed month, Resthome **automatically prepares a credit note** to refund the unoccupied period. You are **notified** when it is created.
- **Notification to the health insurer**: where the country requires it, the departure prepares the departure notification to the resident's health insurer, through the electronic exchanges with the health insurer.

:::{admonition} In Belgium
:class: rh-country rh-country-be

The closure prepares the Annexe 11 departure notification to the mutuality, and
the INAMI allowance stops at the end of the INAMI intervention. See
[Billing a month in Belgium](../belgique/facturation.md) and
[Agreements (eAgreement)](../belgique/ehealth/eagreement.md).
:::

:::{admonition} Anticipatory billing, in plain terms
:class: note

One month of accommodation is billed **the previous month**. That is why a departure partway through a month gives rise to a **refund** (credit note): it had been billed in advance, and it is adjusted upon departure. The care allowance and the supplements, however, are billed on the month actually served.
:::

## Reopen a stay closed by mistake

If you closed a stay in error (or in the case of a death recorded by mistake), you can **reopen** it: Resthome restores billing and cancels the adjustments as long as they are not yet final.

:::{admonition} If the month is already posted
:class: warning

As everywhere, if the invoice in question is already **posted**, the correction goes first through a **reset to draft** or a **credit note**, then a **refresh**. Other residents are not affected.
:::

## Further reading

- [Absences and hospitalizations](absences.md)
- [Split billing](../facturation-partagee/index.md)
- [Billing overview](index.md)
