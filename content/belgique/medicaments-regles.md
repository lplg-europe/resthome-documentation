---
modules: [l10n_health_be_medication]
---

# Medication rules in Belgium

:::{rh-description}
What Belgian law adds to the medication circuit in Resthome: the CNK code, what a care assistant may give, the fourteen days of the pharmacy's sachets (PMI) and the split tablet left to the house.
:::

:::{rh-faq}
Can a care assistant give medicines in Belgium?
: Yes, under a nurse's delegation, the medicines a nurse or a pharmacist prepared: by mouth, rectally, as eye or ear drops, on the skin, and under the skin for fractionated heparin only. Never a narcotic, and never a dose prepared at the moment.

Where do I say which list a care assistant follows?
: On the employee's record, the **Medication Acts** field: the list of 2019 (150 h of training, the default) or the list of 2006 (help with the oral intake only).

How long can the pharmacy's sachets be used?
: Fourteen days from the delivery. When the last day falls on a weekend or a legal public holiday, it moves to the next working day. Past that date, the doses still to give are blocked.

Why is a medicine left out of the pharmacy's sachets?
: The treatment says why under **Out of the Sachets Because**: a split tablet, a liquid, an as-needed medicine, a dose prepared at the moment, or a product the pharmacist leaves out.

Do these rules only apply to nursing homes?
: No. They come from federal law and apply to every Belgian sector that uses the medication circuit.
:::

The medication circuit of Resthome — [treatments](../medicaments/traitements.md),
[pillboxes](../medicaments/piluliers.md), [the round](../medicaments/tour.md) —
asks a few questions that each country answers. In Belgium, the answers come
from federal law and install themselves with the Belgian pack and the
medication circuit.

## The CNK code

The **CNK Code** is the national code of a medicine package, the one a Belgian
pharmacy finds a medicine by.

- It appears on the medicine record, after the strength, in the catalogue list
  and in its search, with the **With CNK** filter.
- The **BCFI URL** sits next to the SmPC and the leaflet, in the **Official
  Documents** tab.
- The stock product made from a medicine carries its CNK as internal
  reference.

The CNK is filled in from SAM: see [The SAM medication
database](sam-base-medicaments.md).

## Who may give what

Giving a medicine is a nursing act (royal decree of 18 June 1990). A nurse or
a physician gives everything. A **care assistant** gives, under a nurse's
delegation, the medicines a nurse or a pharmacist prepared (royal decree of
12 January 2006 as amended on 27 February 2019):

- by mouth (sublingual and inhalation included), rectally, as eye or ear drops,
  on the skin;
- under the skin **only** for a medicine ticked **SC Injection Open to Care
  Assistants** in the catalogue (fractionated heparin);
- **never a narcotic** (a medicine marked **Controlled Substance**);
- **never a dose prepared at the moment** (**Prepared at the Moment** on the
  treatment: a syrup measured, a powder dissolved) — it is a preparation, so a
  nurse's.

On the employee's record, **Medication Acts** says which list a care assistant
follows:

- *Prepared medicines, every route of the list of 2019 (150 h)* — the default;
- *Help with the oral intake only (list of 2006)* — by mouth only.

When a care assistant may not give a dose, the care app shows the reason in
place of the buttons (*A nurse gives it: a narcotic is never given by a care
assistant*, for instance), and Resthome refuses the record, even sent later
from the phone.

:::{admonition} With the pillboxes tracked
:class: note

When **Track the pillboxes** is on, a care assistant gives only a dose that was
prepared and checked without an issue. See [Pillboxes and the pharmacy's
sachets](../medicaments/piluliers.md).
:::

## The pharmacy's sachets (PMI)

The individual preparation of medication (PMI) is the pharmacist's act: the
pharmacy prepares the medicines in a sachet per resident and per moment (royal
decree of 24 September 2012, FAMHP guideline of October 2013).

### Fourteen days from the delivery

The sachets are used within **fourteen days** of the delivery (art. 6). The
delivery's **Use By** date is computed so: when the last day falls on a
weekend or on one of the ten **legal public holidays**, it moves to the next
working day. The care app shows the same date when the sachets are received.

Past that date, the delivery shows a red banner, its doses still to give are
**blocked**, and the **Past the Use-By Date** filter finds it. A nurse prepares
the doses again, or a new delivery takes them; the old sachets go back to the
pharmacy and are listed on the return slip.

### What stays with the house

The pharmacy's sachets leave out what the guideline keeps out of them (2.1):
a **split tablet** — written as *½ tablet*, *1/2*, *half*, or as a part of a
tablet such as *0.5 tablet* — stays the house's to prepare. The treatment says
so under **Out of the Sachets Because**. What goes back to the pharmacy is
never given again (annex 2.6).

## Going further

- [The SAM medication database](sam-base-medicaments.md)
- [The pharmacy link](medicaments-lien-pharmacie.md)
- [Pillboxes and the pharmacy's sachets](../medicaments/piluliers.md)
- [Treatments](../medicaments/traitements.md)
