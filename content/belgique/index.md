---
modules: []
---

# Belgium

:::{rh-description}
Everything Resthome does that comes from Belgian rules: the Katz assessment, the INAMI allowance and billing, the eHealth exchanges (MDA, eAgreement, eFact), the institutional allowance, the day care centre and the Belgian settings.
:::

:::{rh-faq}
Why is there a Belgium space?
: Because everything in it comes from Belgian law or from Belgian institutions: the INAMI, the AViQ, the mutualities, the eHealth platform. The rest of the documentation — residents, admissions, care, meals, accommodation billing — works the same way in every country.

What does Belgium add to the common applications?
: The Katz scale and its categories, the NISS on the resident's file, the INAMI dependency allowance billed to the mutuality, the eHealth exchanges (MDA, eAgreement, eFact), the Belgian annexes, the CPAS, the institutional allowance and the day care centre (CSJ).

Where do I find the general billing?
: Under [Billing](../facturation/index.md): periods, supplements, absences and invoices work the same way in every country. [Billing a month in Belgium](facturation.md) adds what is Belgian.

How do I see only the Belgian pages in the navigation?
: Choose **Belgium** in the country selector at the top of the page: the side bar then shows the common applications and this space.
:::

:::{toctree}
:hidden:
:::

This space gathers everything that comes from **Belgian** rules: the scale that
measures dependency, the allowance paid by the mutualities, the electronic
exchanges with them over eHealth, the funding of the facility and the day care
centre.

The common pages — [Residents](../residents/index.md),
[Admissions](../admissions/index.md), [Billing](../facturation/index.md),
[Care](../soins/index.md), [Meals](../repas/index.md) — describe the journey in
every country. Where Belgium adds something, they show an **In Belgium** box
that links here.

## Start here

- [The billing journey](parcours-facturation.md) — the big picture: admission →
  MDA → eAgreement → Katz → eFact → payment.
- [FAQ — Belgium](faq.md) — short answers on the Katz, the MDA, the eAgreement,
  the eFact and Belgian billing.
- [Glossary — Belgium](glossaire.md) — INAMI, NISS, OA, annexes, pseudo-codes
  and the other Belgian terms.

## The resident and their assessment

- [The resident's file in Belgium](dossier-resident.md) — the NISS and the
  eID reading, the mutuality (OA), the MR, MRS and short-stay sectors, the Katz
  category.
- [Admitting a resident in Belgium](admission.md) — the MR, MRS or day care
  stay type, the NISS, the MDA before admission, the admission agreement.
- [The Katz assessment](katz.md) — the 6 criteria, the category (O, A, B, C,
  Cd) and the allowance it gives.
- [Internal transfer (MR ↔ MRS)](ehealth/eagreement-transfert.md) — moving a
  resident between sectors and the two annexes the insurer expects.

## Billing and the INAMI

- [Billing a month in Belgium](facturation.md) — the INAMI allowance and its
  pseudo-codes, the mutuality and resident shares, the month-end checklist.
- [The INAMI dependency allowance](forfait-inami.md) — from the Katz category
  to the amount billed to the mutuality.
- [The Expense Note (Annexe 12)](note-de-frais-annexe12.md) — the individual
  note per resident and the summary note per insurance organisation.
- [CPAS coverage](cpas.md) — when a CPAS pays all or part of the resident
  share.

## eHealth

- [eHealth](ehealth/index.md) — the overview of the exchanges with the
  mutualities.
- Insurability: [Insurability (MDA)](ehealth/mda.md) and
  [MDA errors — causes and solutions](ehealth/mda-erreurs.md).
- Agreements: [Agreements (eAgreement)](ehealth/eagreement.md),
  [Following a request: deadlines and decision](ehealth/eagreement-suivi.md),
  [Refused agreement (eAgreement) — causes and solutions](ehealth/eagreement-refus.md),
  [Responsible practitioner and annex signatures](ehealth/eagreement-signature.md)
  and [Collective holidays](ehealth/vacances-collectives.md).
- Electronic invoicing: [Electronic invoicing (eFact)](ehealth/efact.md),
  [eFact rejections — causes and solutions](ehealth/efact-rejets.md),
  [Correcting an already-settled sending](ehealth/efact-corrections.md) and
  [Payment tracking and settlement reconciliation](ehealth/efact-paiements.md).

## The institutional allowance

- [Institutional allowance](forfait/index.md) — the AViQ allowance of the
  facility, from the days billed and the staff present.
- [Computing the allowance](forfait/calcul.md) — step by step, from the days
  billed to the INAMI rates.
- [Simulations and live tracking](forfait/suivi-simulations.md) — trying a
  change and following the year in progress.

## The day care centre

- [Day care centre (CSJ)](centre-de-jour/index.md) — day places, the
  attendance register, the CSJ forfait and the staffing norm.
- [Setting up a day care centre](centre-de-jour/configuration.md),
  [Admitting a day care user](centre-de-jour/admission.md) and
  [Recording attendance](centre-de-jour/presences.md).
- [Billing a day care month](centre-de-jour/facturation.md),
  [Care for a day care user](centre-de-jour/soins.md) and
  [The staffing norm](centre-de-jour/norme-personnel.md).

## Care and medication

- [Care in Belgium](soins.md) — the Katz scale in the medical record, the INAMI
  number of care staff, the AViQ undernutrition screening.
- [The SAM medication database](sam-base-medicaments.md) — the Belgian
  authentic source: ATC, BCFI class, SmPC and leaflet.

## Settings

- [Belgian settings](reglages.md) — INAMI numbers and MR/MRS approvals, the
  Cc accreditation, INAMI rates and pseudo-codes, health insurers and CPAS.
- [eHealth and eFact Settings](reglages-ehealth.md) — certificate, platform,
  Walloon Account C, CIN licence and invoicing header.

## The same software elsewhere

Resthome separates the **question** from the **answer**: the engine asks for a
dependency category, a national identification number, a stay type; the
Belgian pack answers with the Katz, the NISS, MR/MRS. Another country brings
its own pack, and the common pages do not change. See
[France](../france/index.md) and [Luxembourg](../luxembourg/index.md).
