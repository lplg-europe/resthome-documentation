---
modules: [healthcare_accommodation_billing, healthcare_accommodation]
---

# Departure and death

:::{rh-description}
Close a stay (departure or death) in Resthome — billing stops on the correct date, automatic credit note for prepaid accommodation.
:::

:::{rh-faq}
How do I close a stay on departure or death?
: Open the resident's stay and click End Stay. Enter the End Date & Time and the Departure Reason (deceased, external transfer, return to family or home…), then confirm with End Stay.

Does Resthome issue a credit note automatically?
: Yes. For a resident billed in advance, a departure partway through an already-billed month prepares a credit note for the unoccupied days.

Why is there a refund when a resident leaves?
: Because accommodation is billed the previous month (anticipatory billing). The care allowance and the supplements, by contrast, are billed on the month actually served.

Is a hospitalisation an end of stay?
: No. The bed is kept and the resident comes back: record an absence instead.

Can I reopen a stay closed by mistake?
: Yes, with Undo end of stay (reopen) on the ended stay. Billing resumes; a month already posted is corrected with a supplementary invoice or a credit note.
:::

When a resident leaves the facility or passes away, all you need to do is
**close their stay**: Resthome stops billing on the correct date and prepares
the **adjustment** for what was billed in advance.

## Close the stay

1. Open the resident's record → their **stay**.
2. Click **End Stay**.
3. Enter the **End Date & Time** and the **Departure Reason** (**Deceased**,
   **External transfer**, **Return to family / home**, **Other**), with
   optional notes.
4. Click **End Stay** to confirm.

:::{admonition} A hospitalisation is not a departure
:class: warning

The bed is kept and the resident returns: record an
[absence](absences.md), not an end of stay. The window reminds you of it.
:::

## What Resthome does automatically

- **Billing stops** on the correct date: nothing is billed after the departure.
- **Credit note for prepaid accommodation**: for a resident billed **one month
  in advance**, if they leave partway through an already-billed month, Resthome
  **prepares a credit note** for the unoccupied days.
- **Supplements**: recurring supplements are not billed after the departure
  date either. The resident
  stays in the [Supplements app](application-supplements.md) until the month
  they left is invoiced, so the last one-time supplements can still be entered.

:::{admonition} In Belgium
:class: rh-country rh-country-be

The closure also prepares the Annexe 11 departure notification to the
mutuality, and the INAMI allowance stops at the end of the INAMI intervention.
The first **End Stay** can then leave the room billed until it is freed: a
second click, **Close Stay (stop billing)**, closes it. See
[Billing a month in Belgium](../belgique/facturation.md) and
[Agreements (eAgreement)](../belgique/ehealth/eagreement.md).
:::

:::{admonition} Anticipatory billing, in plain terms
:class: note

One month of accommodation is billed **the previous month**. That is why a
departure partway through a month gives rise to a **refund** (credit note): it
had been billed in advance, and it is adjusted upon departure. The care
allowance and the supplements, however, are billed on the month actually
served. See [Invoice type: in advance or in arrears](type-de-facture.md).
:::

## Reopen a stay closed by mistake

If you closed a stay in error, click **Undo end of stay (reopen)** on the ended
stay and confirm: the stay becomes active again, the departure is cleared and
billing resumes.

:::{admonition} If the month is already posted
:class: warning

A posted invoice is never rewritten. The billing period shows **Corrections
pending**: click **Refresh** to create the supplementary invoice or credit
note. Other residents are not affected.
:::

## Further reading

- [Absences and hospitalisations](absences.md)
- [Split billing](../facturation-partagee/index.md)
- [Billing overview](index.md)
