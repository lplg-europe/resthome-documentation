# eHealth

:::{rh-description}
MDA insurability, eFact electronic invoicing and eAgreement agreements in Resthome.
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
:::

Resthome is connected to the Belgian e-health ecosystem (eHealth, MyCareNet,
WalCareNet) to exchange directly with the mutualities.

## The services

- **MDA — Insurability**

  Checks that a resident is **insured** and retrieves their mutuality and BIM
  status, individually or in batch.

  → [Insurability in detail](mda.md)

- **eFact — Electronic invoicing**

  Sends the **mutuality share** (message 920000) to the insurance organisations
  and follows the acknowledgements and settlements.

  → [eFact invoicing in detail](efact.md) · [Rejections](efact-rejets.md)
  · [Corrections and credit notes](efact-corrections.md) · [Settlements](efact-paiements.md)

- **eAgreement — Agreements**

  Notifies the OA on an **admission**, an **end of stay** or an **absence**
  (Annexes 7, 10, 11…).

  → [Agreements in detail](eagreement.md) · [Signing the annexes](eagreement-signature.md)
  · [Following a request](eagreement-suivi.md) · [Internal transfer](eagreement-transfert.md)

## Prerequisites

:::{admonition} To check before sending
:class: warning
- The resident has a valid **NISS**.
- Their **mutuality** is filled in.
- An **insurability (MDA)** has been checked for the period.
- The establishment's **eHealth certificate** is active.
:::

## Good to know

- An **absence** of more than 72 h (or any hospitalisation) triggers an
  end-of-accommodation **Annexe 11**; the **return** generates a readmission
  **Annexe 7**.
- An invoice that is already **posted** "freezes" the month's billing for that
  resident: to change it, reset it to draft (or issue a credit note), then
  refresh.

## What's next

- [Agreements (eAgreement)](eagreement.md) — admission, absence, return,
  discharge (Annexes 7, 10, 11).
- [The billing journey](../parcours-facturation.md) — from admission to payment.
- [Absences and hospitalisations](../facturation/absences.md)
- [Billing](../facturation/index.md)
- [FAQ](../faq.md) · [Glossary](../glossaire.md)
