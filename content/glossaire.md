# Glossary

:::{rh-description}
Glossary of Resthome terms and acronyms and of nursing-home billing: MDA, eFact, eAgreement, Katz, INAMI package, OA, third-party payer, Annexes.
:::

The terms and acronyms used in Resthome and in Belgian nursing-home billing, explained
simply. Each entry links, where useful, to the page that covers it in detail.

---

## Annexe 7

eHealth **admission agreement** document (coverage) sent to the health insurance fund
at the start of a stay or on a **readmission** after an absence.
See: [Agreements (eAgreement)](ehealth/eagreement.md)

## Annexe 10

**Care-agreement update** document, prepared upon a validated **Katz aggravation** (the
aggravation reason is carried over into it; the clinician's signature completes it).
See: [The Katz assessment](residents/katz.md)

## Annexe 11

**Discharge notification** sent to the health insurance fund on an absence of more than
72 h, a hospitalisation, or an end of stay / a death.
See: [Absences and hospitalisations](facturation/absences.md)

## BIM (status)

**Increased-reimbursement beneficiary**: a social status granting the right to better
reimbursement. The MDA pulls it automatically onto the resident's record.
See: [Insurability (MDA)](ehealth/mda.md)

## eFact Cockpit

**Monitoring** view for electronic billing: the status of all batches and transmissions
at a glance (transmitted, accepted, rejected, pending).
See: [Electronic billing (eFact)](ehealth/efact.md)

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
See: [Electronic billing (eFact)](ehealth/efact.md)

## eHealth

Belgian platform for **secure electronic exchanges** in healthcare. Resthome uses it for
the MDA, the eAgreement and eFact (via MyCareNet / WalCareNet).

## Supplements envelope

The **monthly grouping of a resident's supplements** (products and services outside the
package). Any change automatically updates their invoice.
See: [Supplements](facturation/supplements.md)

## Anticipatory billing

A billing mode where a month's **accommodation** is invoiced **the previous month**,
while the **INAMI package** and the **supplements** are invoiced in the month they are
provided.
See: [Billing overview](facturation/index.md)

## INAMI package

**Daily** amount covered by the health insurance fund for care, determined by the
resident's **Katz category** and calculated on their **days of presence**.
See: [The Katz assessment](residents/katz.md)

## INAMI

**National Institute for Health and Disability Insurance** (in Dutch: RIZIV). The federal
body that sets the rules and the packages for health-care insurance.

## Katz (scale)

Scale measuring a resident's **degree of dependency** across 6 criteria (washing,
dressing, transfer and mobility, using the toilet, continence, eating), each rated from
1 to 4. It determines the **category** (**O**, **A**, **B**, **C**, **Cd / Cc**) and
therefore the package.
See: [The Katz assessment](residents/katz.md)

## eFact batch

An **electronic file** grouping the packages of one eFact transmission. Resthome builds
**one batch per insurer union**.
See: [Electronic billing (eFact)](ehealth/efact.md)

## MDA (insurability)

*Member Data* — the **check of a resident's insurability** and of their **exact health
insurance fund** with MyCareNet / WalCareNet for a given period. An essential
prerequisite for eFact.
See: [Insurability (MDA)](ehealth/mda.md)

## MR / MRS

**Rest home** (MR) and **rest and care home** (MRS) — the two types of residential
facility for the elderly, with distinct care levels and packages. In Dutch: ROB / RVT
(grouped under the term *woonzorgcentrum*).

## MyCareNet / WalCareNet

The health insurance funds' **electronic gateways** (via eHealth) that Resthome queries
for the MDA, the eAgreement and eFact. WalCareNet is the Walloon counterpart.

## NISS

**Social Security Identification Number** (the national register number). Essential for
sending a resident's MDA and eAgreement agreements.
See: [Managing a resident](residents/gerer-un-resident.md)

## Credit note

Document that **cancels or refunds** all or part of an invoice. Resthome prepares one
automatically, for example on a departure partway through a month that has already been
invoiced (accommodation billed in advance).
See: [Departure and death](facturation/depart-deces.md)

## Insurer (OA)

The resident's **health insurance fund**, recipient of the INAMI share via eFact.
Insurers are grouped into large **unions**.
See: [Insurability (MDA)](ehealth/mda.md)

## Billing period

The **billing month** in Resthome, which moves through four states: **Draft**,
**Generated** (calculated), **Invoiced** and **Closed**.
See: [Billing a month, step by step](facturation/facturer-un-mois.md)

## Reintegration

Shifting lines **from the resident to the health insurance fund** (or the reverse) when
insurability changes between two MDA checks (loss then return of insurability, for
example).
See: [Insurability (MDA)](ehealth/mda.md)

## Noon rule

Day-counting convention: it is **presence at noon** (Brussels time) that determines
whether a day counts toward the package, hence the importance of departure and return
dates and times.
See: [Absences and hospitalisations](facturation/absences.md)

## Third-party payer

Mechanism where the **health insurance fund pays its share directly** to the facility
(via eFact), the resident settling only their own share. In Dutch: *derdebetaler*.

## Insurer union

The large **families of insurers** used to group eFact transmissions: **100** (Alliance
nationale), **300** (Solidaris), **500** (Union nationale), **600** (CAAMI), **900** (HR
Rail)…
See: [Electronic billing (eFact)](ehealth/efact.md)

---

## Further reading

- [FAQ — Frequently asked questions](faq.md)
- [The billing journey](parcours-facturation.md)
- [Billing overview](facturation/index.md)
