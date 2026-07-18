# Configuration

:::{rh-description}
Configure Resthome — rooms and sectors, INAMI rates and packages, supplement types, health insurers, facility and multi-company.
:::

Before day-to-day use, a few basic settings give Resthome its structure. They are set up once, then only change at the margins.

## Application settings

The **Settings** menu brings together all the parameters, organized by tab. For a nursing home (MR/MRS), follow these guides — each one details **every field** and its **recommended value**:

- [General settings (residents, rooms)](reglages-generaux.md)
- [Billing settings (MR/MRS)](reglages-facturation.md)
- [eHealth and eFact settings](reglages-ehealth.md)
- [Meals and nutrition settings](reglages-repas.md)
- [Document settings](reglages-documents.md)

## Rooms and sectors

- **Rooms**: create your rooms, with their **type** (MR, MRS, single or double room…) and their **amenities**.
- **Sectors / units**: group rooms by living unit.
- A room can be set to **maintenance**, **reserved**, or switched back to **automatic** assignment based on occupancy.

## Rates and packages

- **INAMI rates**: the **package** amounts per **Katz category** — the basis for health-insurer reimbursement.
- **Accommodation rates**: the room price (resident's share).
- **Supplement types**: the catalog of billable services (see [Supplements](../facturation/supplements.md)).
- **Absence discount rules** and **AViQ codes**: the fine-tuning of billing.

## Health insurers and reference data

- **Health insurers (insurance organizations)**: the list used for insurability and eFact.
- **Facility**: your home's information (identifiers, contact details) used in documents and eHealth submissions.

## Multi-company

Resthome handles **multiple companies** in a single database: each company has its own residents, rooms and billing, kept separate. Useful for a group that operates several facilities.

:::{admonition} The activity log
:class: note

An **activity log** tracks access to sensitive data (GDPR). It can be viewed from the configuration — useful for compliance.
:::

## Learn more

- [Getting started](../premiers-pas.md)
- [Managing a resident](../residents/gerer-un-resident.md)
