---
modules: [resthome_mr_ehealth, resthome_mr_billing]
---

# The billing journey

:::{rh-description}
From admission to payment: the complete billing journey of a nursing home resident with Resthome (MDA, eAgreement, Katz, eFact).
:::

From **admission** to **payment**, a correct invoice always follows the same
steps. This page connects the whole journey; each step links to its detailed
page.

```mermaid
flowchart TD
    A[Admission] --> B[Insurability — MDA]
    B --> C[Admission agreement — eAgreement]
    C --> D[Katz evaluation]
    D --> E[Electronic invoicing — eFact]
    E --> F[Payment / settlement]
```

```text
Admission ─► MDA ─► eAgreement ─► Katz ─► eFact ─► Payment
```

1. **Admission** — Create the resident's file and open their stay.
2. **Insurability (MDA)** — Check the insurability and the exact mutuality with
   MyCareNet / WalCareNet.
3. **Admission agreement (eAgreement)** — The care notification (Annex 7) is
   prepared for the mutuality.
4. **Katz evaluation** — Score the dependency: the Katz category is declared to
   the mutuality for the INAMI allowance.
5. **Electronic invoicing (eFact)** — Generate the period, create the invoices
   and send the mutuality share to the insurance organisations.
   → [Billing a month in Belgium](facturation.md) · [Electronic invoicing (eFact)](ehealth/efact.md)
6. **Payment / settlement** — The resident share is invoiced, the mutuality
   share is followed up to the insurer's settlement (acknowledgement,
   acceptance, rejection).

:::{admonition} In practice
:class: tip
**Insurability (MDA)** at the start of the month and a **validated Katz
evaluation** are the two prerequisites that avoid most eFact rejections. Handle
them before generating the invoices.
:::

## What's next

- [Billing a month in Belgium](facturation.md) — the month on the Belgian side, and its month-end checklist.
- [Insurability (MDA)](ehealth/mda.md) · [Agreements (eAgreement)](ehealth/eagreement.md)
- [The Katz assessment](katz.md) · [The INAMI dependency allowance](forfait-inami.md)
- [Electronic invoicing (eFact)](ehealth/efact.md) · [Settlements and payments](ehealth/efact-paiements.md)
