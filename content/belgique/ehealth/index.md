---
modules: [l10n_health_be_connector, l10n_health_be_mda, l10n_health_be_efact, l10n_health_be_eagreement_light]
sectors: [mr, csj]
---

# eHealth

:::{rh-description}
The eHealth services of WideCare for Belgian nursing homes: MDA insurability, eFact electronic invoicing, eAgreement agreements, the eHealthBox, the Health Directory, consent and MediPrima.
:::

:::{rh-faq}
Which eHealth services does WideCare use?
: The insurability check (MDA), the electronic invoicing of the INAMI allowance (eFact), the agreements and notifications (eAgreement Light), the eHealthBox secure mailbox, the Health Directory and CoBRHA, the patient consent and MediPrima. Each one is described on its own page.

What do I need before the first exchange?
: An eHealth certificate installed on the home's approval, with a successful connection test. The residents need a NISS and a mutuality.

A sending got no certain answer: will WideCare resend it?
: Never on its own. It lists the sending in eHealth → Configuration → Sends to check, where you say whether MyCareNet received it; only then can it be sent again.

Where do I see what was exchanged with the platform?
: In eHealth → Configuration → Communication logs: every call, with its answer, for the eHealth managers.
:::

:::{toctree}
:hidden:

mda
mda-erreurs
efact
efact-rejets
efact-corrections
efact-paiements
eagreement
eagreement-signature
eagreement-suivi
eagreement-refus
eagreement-transfert
vacances-collectives
ehealthbox
annuaire-sante
consentement
:::

WideCare is connected to the Belgian e-health ecosystem (eHealth, MyCareNet,
WalCareNet) to exchange directly with the mutualities and the other caregivers.
Most of it lives in the **eHealth** application; some services also show up
where you need them, on the resident's record or in the billing period.

## The services

- **MDA — Insurability**

  Checks that a resident is **insured** and retrieves their mutuality and BIM
  status, individually or in batch — the waiting list included.

  → [Insurability in detail](mda.md) · [MDA errors](mda-erreurs.md)

- **eFact — Electronic invoicing**

  Sends the **mutuality share** (message 920000) to the insurance organisations
  and follows the acknowledgements and settlements.

  → [eFact invoicing in detail](efact.md) · [Rejections](efact-rejets.md)
  · [Corrections and credit notes](efact-corrections.md) · [Settlements](efact-paiements.md)

- **eAgreement — Agreements**

  Notifies the OA on an **admission**, an **end of stay** or an **absence**
  (Annexes 7, 10, 11…).

  → [Agreements in detail](eagreement.md) · [Signing the annexes](eagreement-signature.md)
  · [Following a request](eagreement-suivi.md) · [Refusals](eagreement-refus.md)
  · [Internal transfer](eagreement-transfert.md) · [Collective holidays](vacances-collectives.md)

- **eHealthBox — Secure mailbox**

  Reads and sends the home's encrypted messages with doctors, pharmacies and
  hospitals.

  → [The eHealthBox](ehealthbox.md)

- **Health Directory and CoBRHA**

  Looks professionals and institutions up in the national registers and names
  the NIHII numbers the mutuality returns.

  → [Health Directory and CoBRHA](annuaire-sante.md)

- **Consent**

  Checks, registers or revokes a resident's consent to the exchange of their
  health data.

  → [eHealth consent](consentement.md)

- **MediPrima**

  Consults the medical card of a person covered by a CPAS.

  → [CPAS coverage](../cpas.md)

## Prerequisites

:::{admonition} To check before sending
:class: warning
- The resident has a valid **NISS** — the [eID reader](../lecture-eid.md) fills
  it in.
- Their **mutuality** is filled in.
- An **insurability (MDA)** has been checked for the period.
- The approval's **eHealth certificate** is active, and its **Test connection**
  succeeds — see [eHealth and eFact settings](../reglages-ehealth.md).
:::

## When an answer gets lost

A sending to MyCareNet can end without a certain answer: a time-out, an
interruption. WideCare **never resends it on its own**, so that the mutuality
never receives the same request twice. It lists it in **eHealth →
Configuration → Sends to check**, reserved to the eHealth managers: look for
its acknowledgement in the MyCareNet mailbox, then click **Received by
MyCareNet** (the document counts as sent) or **Not received, may be sent
again**.

Every call to the platform, with its answer, is kept in **eHealth →
Configuration → Communication logs** for the eHealth managers.

## Good to know

- An **absence** of more than 72 h (or any hospitalisation) triggers an
  end-of-accommodation **Annexe 11**; the **return** generates a readmission
  **Annexe 7**.
- An invoice that is already **posted** "freezes" the month's billing for that
  resident: to change it, reset it to draft (or issue a credit note), then
  refresh.
- **Consent** and **MediPrima** are practitioner services: their menus show for
  the eHealth practitioners and managers only.

## What's next

- [Agreements (eAgreement)](eagreement.md) — admission, absence, return,
  discharge (Annexes 7, 10, 11).
- [The billing journey](../parcours-facturation.md) — from admission to payment.
- [Absences and hospitalisations](../../facturation/absences.md)
- [Billing](../../facturation/index.md)
- [FAQ](../../faq.md) · [Glossary](../../glossaire.md)
