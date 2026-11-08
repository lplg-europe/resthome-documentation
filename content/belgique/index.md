---
modules: []
sectors: [mr, csj, rs, gp]
---

# Belgium

:::{rh-description}
Everything WideCare does that comes from Belgian rules: the eID, the Katz assessment, the INAMI allowance and billing, occupancy against the approvals, the eHealth exchanges (MDA, eAgreement, eFact, eHealthBox), the institutional allowance, the day care centre and the Belgian settings.
:::

:::{rh-faq}
Why is there a Belgium space?
: Because everything in it comes from Belgian law or from Belgian institutions: the INAMI, the AViQ, the mutualities, the eHealth platform. The rest of the documentation — residents, admissions, care, meals, accommodation billing — works the same way in every country.

What does Belgium add to the common applications?
: The eID reading, the Katz scale and its categories, the NISS on the resident's file, the INAMI approvals and the occupancy of their beds, the INAMI dependency allowance billed to the mutuality, the eHealth exchanges (MDA, eAgreement, eFact, eHealthBox, Health Directory, consent), the Belgian annexes, the CPAS and MediPrima, the institutional allowance and the day care centre (CSJ).

Where do I find the general billing?
: Under [Billing](../facturation/index.md): periods, supplements, absences and invoices work the same way in every country. [Billing a month in Belgium](facturation.md) adds what is Belgian.

Is the eFact still due by the 20th of the following month?
: No. That sending deadline was abolished; what still runs is the insurer's payment deadline, from the day the batch is sent. See [Payment tracking](ehealth/efact-paiements.md).

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

- [The resident's file in Belgium](dossier-resident.md) — the NISS, the
  mutuality (OA), the MR, MRS and short-stay sectors, the Katz category, the
  palliative status and the Belgian buttons of the record.
- [Reading the eID card](lecture-eid.md) — the identity and the NISS read from
  the card, on an admission request, a resident or a contact.
- [Admitting a resident in Belgium](admission.md) — the MR, MRS or day care
  stay type, the free places, the MDA before admission, the waiting list
  checked with the mutualities, the admission agreement.
- [The Katz assessment](katz.md) — the criteria, the category (O, A, B, C, Cd,
  D, Ccoma), signing and validating, and why there is no allowance without a
  validated Katz.
- [Internal transfer (MR ↔ MRS)](ehealth/eagreement-transfert.md) — moving a
  resident between sectors and the two annexes the insurer expects.

## Billing and the INAMI

- [Billing a month in Belgium](facturation.md) — the INAMI allowance and its
  pseudo-codes, the mutuality and resident shares, the month-end checklist.
- [The INAMI dependency allowance](forfait-inami.md) — from the Katz category
  to the amount billed to the mutuality.
- [The Expense Note (Annexe 12)](note-de-frais-annexe12.md) — the individual
  note per resident and the summary note per insurance organisation.
- [Occupancy MR / CS / MRS](occupation-mr-mrs.md) — the beds of each sector
  against the approvals, the quarter's occupancy, and the residents
  transferable to MRS.
- [CPAS coverage](cpas.md) — when a CPAS pays all or part of the resident
  share, and the MediPrima medical card.
- [Management reports](rapports-gestion.md) — KAPPA control, movements,
  occupancy by room and by approval.

## eHealth

- [eHealth](ehealth/index.md) — the overview of the exchanges with the
  mutualities, and what to do when an answer gets lost.
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
- With the other caregivers: [The eHealthBox](ehealth/ehealthbox.md),
  [Health Directory and CoBRHA](ehealth/annuaire-sante.md) and
  [eHealth consent](ehealth/consentement.md).

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
- [The day care agreement](centre-de-jour/accord.md),
  [Absences and hospitalisation](centre-de-jour/absences.md) and
  [Day care figures](centre-de-jour/rapports.md).
- [Billing a day care month](centre-de-jour/facturation.md),
  [Care for a day care user](centre-de-jour/soins.md) and
  [The staffing norm](centre-de-jour/norme-personnel.md).

## Care and medication

- [Care in Belgium](soins.md) — the Katz scale in the medical record, the INAMI
  number of care staff, the AViQ undernutrition screening.
- [The SAM medication database](sam-base-medicaments.md) — the Belgian
  authentic source: ATC, BCFI class, SmPC and leaflet.
- [Medication rules in Belgium](medicaments-regles.md),
  [The pharmacy link](medicaments-lien-pharmacie.md),
  [Prescriptions through the eHealthBox](medicaments-ehealthbox.md) and
  [Billing medicines in Belgium](medicaments-facturation.md).

## Serviced residences

- [Serviced residences in Belgium](residences-services.md) and
  [Moving between a serviced residence and the nursing home](residences-services-maison-de-repos.md).

## General practitioners

- [General practice in Belgium](medecins/index.md) — the practitioner's eHealth
  identity, the patient's insurability, the eAttest, the Global Medical File,
  the INAMI nomenclature and the per-act eFact.

## Settings

- [Belgian settings](reglages.md) — the approvals and their sectors, the
  Cc accreditation, INAMI rates and pseudo-codes, health insurers and CPAS.
- [eHealth and eFact settings](reglages-ehealth.md) — the platform, the
  approval's certificate, the automations, eAgreement Light, the Walloon
  Account C, the CIN licence and the invoicing header.

## The same software elsewhere

WideCare separates the **question** from the **answer**: the engine asks for a
dependency category, a national identification number, a stay type; the
Belgian pack answers with the Katz, the NISS, MR/MRS. Another country brings
its own pack, and the common pages do not change.
