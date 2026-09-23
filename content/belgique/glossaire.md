---
modules: []
---

# Glossary — Belgium

:::{rh-description}
Glossary of the Belgian terms and acronyms used in Resthome and in Belgian nursing-home billing: INAMI, Katz, NISS, OA, MDA, eFact, eAgreement, annexes, AViQ, CPAS.
:::

The terms and acronyms that come from **Belgian** rules and institutions,
explained simply. Each entry links, where useful, to the page that covers it in
detail. The terms valid in every country are in the
[Glossary](../glossaire.md).

---

## Annexe 7

eHealth **admission agreement** document (coverage) sent to the health insurance fund
at the start of a stay or on a **readmission** after an absence.
See: [Agreements (eAgreement)](ehealth/eagreement.md)

## Annexe 10

**Care-agreement update** document, prepared upon a validated **Katz aggravation** (the
aggravation reason is carried over into it; the clinician's signature completes it).
See: [The Katz assessment](katz.md)

## Annexe 11

**Discharge notification** sent to the health insurance fund on an absence of more than
72 h, a hospitalisation, or an end of stay / a death.
See: [Agreements (eAgreement)](ehealth/eagreement.md)

## Annexe 12

The **expense note**: an individual note per resident for the expenses advanced, and a
summary note per insurance organisation.
See: [The Expense Note (Annexe 12)](note-de-frais-annexe12.md)

## AViQ

The Walloon agency that sets the rates of the dependency allowance and funds the
facility through the **institutional allowance**. Under the AViQ rates, the
dependency allowance is the **same amount for every Katz category**.
See: [Institutional allowance](forfait/index.md)

## BIM (status)

**Increased-reimbursement beneficiary**: a social status granting the right to better
reimbursement. The MDA pulls it automatically onto the resident's record.
See: [Insurability (MDA)](ehealth/mda.md)

## CPAS

**Public Centre for Social Welfare** of the resident's municipality. It can cover all or
part of the resident's personal share (accommodation and supplements) — never the
dependency allowance, which goes to the health insurance fund.
See: [CPAS coverage](cpas.md)

## CSJ (day care centre)

**Day care centre** (*centre de soins de jour*): a centre whose users live at home and
come for the day. Its forfait is paid per day that earns it — six hours, an arrival by
noon — for the CSJ categories **F**, **Fd** and **D**.
See: [Day care centre (CSJ)](centre-de-jour/index.md)

## Day place

A **place in a day room**, shared by the day care users who come on different days —
never a licensed bed. A day care stay only goes in a day place, and a residential stay
never does.
See: [Setting up a day care centre](centre-de-jour/configuration.md)

## eAgreement

**Care coverage agreement** (linked to the Katz category and the package), exchanged
electronically with the health insurance fund via eHealth.
See: [Agreements (eAgreement)](ehealth/eagreement.md)

## eAgreement Light

The **simple notifications** tied to the resident's **movements** (admission, absence,
departure, return) that Resthome generates automatically as you work.
See: [Agreements (eAgreement)](ehealth/eagreement.md)

## eFact

**Electronic** transmission of the **insurer's share** (the INAMI package) to the health
insurers over the eHealth / MyCareNet network, with tracking of acknowledgements,
statements, acceptances and rejections.
See: [Electronic invoicing (eFact)](ehealth/efact.md)

## eFact batch

An **electronic file** grouping the packages of one eFact transmission. Resthome builds
**one batch per insurer union**.
See: [Electronic invoicing (eFact)](ehealth/efact.md)

## eFact Cockpit

**Monitoring** view for electronic billing: the status of all batches and transmissions
at a glance (transmitted, accepted, rejected, pending).
See: [Electronic invoicing (eFact)](ehealth/efact.md)

## eHealth

Belgian platform for **secure electronic exchanges** in healthcare. Resthome uses it for
the MDA, the eAgreement and eFact (via MyCareNet / WalCareNet).
See: [eHealth](ehealth/index.md)

## INAMI

**National Institute for Health and Disability Insurance** (in Dutch: RIZIV). The federal
body that sets the rules and the packages for health-care insurance.

## INAMI package

**Daily** amount covered by the health insurance fund for care, determined by the
resident's **Katz category** and calculated on their **days of presence**.
See: [The INAMI dependency allowance](forfait-inami.md)

## Institutional allowance

What the facility receives per day and per resident for a funding year, computed from
the days billed to the health insurers and the staff present over the reference period.
See: [Institutional allowance](forfait/index.md)

## Insurer (OA)

The resident's **health insurance fund** (*mutualité*, *organisme assureur*), recipient
of the INAMI share via eFact. Insurers are grouped into large **unions**.
See: [Insurability (MDA)](ehealth/mda.md)

## Insurer union

The large **families of insurers** used to group eFact transmissions: **100** (Alliance
nationale), **300** (Solidaris), **500** (Union nationale), **600** (CAAMI), **900** (HR
Rail)…
See: [Electronic invoicing (eFact)](ehealth/efact.md)

## Katz (scale)

Scale measuring a resident's **degree of dependency** across 6 criteria (washing,
dressing, transfer and mobility, using the toilet, continence, eating), each rated from
1 to 4. It determines the **category** (**O**, **A**, **B**, **C**, **Cd / Cc**) and
therefore the package.
See: [The Katz assessment](katz.md)

## MDA (insurability)

*Member Data* — the **check of a resident's insurability** and of their **exact health
insurance fund** with MyCareNet / WalCareNet for a given period. An essential
prerequisite for eFact.
See: [Insurability (MDA)](ehealth/mda.md)

## MR / MRS

**Rest home** (MR) and **rest and care home** (MRS) — the two types of residential
facility for the elderly, with distinct care levels and packages. In Dutch: ROB / RVT
(grouped under the term *woonzorgcentrum*).
See: [Admitting a resident in Belgium](admission.md)

## MyCareNet / WalCareNet

The health insurance funds' **electronic gateways** (via eHealth) that Resthome queries
for the MDA, the eAgreement and eFact. WalCareNet is the Walloon counterpart.

## NISS

**Social Security Identification Number** (the national register number). Essential for
sending a resident's MDA and eAgreement agreements.
See: [Admitting a resident in Belgium](admission.md)

## Noon rule

Day-counting convention: it is **presence at noon** (Brussels time) that determines
whether a day counts toward the package, hence the importance of departure and return
dates and times.
See: [Billing a month in Belgium](facturation.md)

## Pseudo-code

The code under which the allowance is billed to the health insurance fund: each Katz
category (for example **770501** for category **O**) and each CSJ category carries its
own on the INAMI rates, and the same code appears on the Annexe 12. A supplement
declared to the insurer carries its declaration pseudo-code too. Always say
**pseudo-code**, never "INAMI code".
See: [Billing a month in Belgium](facturation.md)

## Reintegration

Shifting lines **from the resident to the health insurance fund** (or the reverse) when
insurability changes between two MDA checks (loss then return of insurability, for
example).
See: [Insurability (MDA)](ehealth/mda.md)

## SAM

The Belgian **authentic-source medication database**, with the ATC code, the BCFI class,
the Black Triangle and the SmPC / leaflet, searched with the **Search SAM** wizard.
See: [The SAM medication database](sam-base-medicaments.md)

## Third-party payer

In Belgium, the **health insurance fund pays its share directly** to the facility via
eFact, the resident settling only their own share. In Dutch: *derdebetaler*.
See: [Electronic invoicing (eFact)](ehealth/efact.md)

---

## Further reading

- [Glossary](../glossaire.md) — the terms valid in every country.
- [FAQ — Belgium](faq.md)
- [The billing journey](parcours-facturation.md)
