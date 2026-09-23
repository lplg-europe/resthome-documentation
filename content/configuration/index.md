---
modules: [healthcare_accommodation, healthcare_accommodation_billing, healthcare_base, l10n_health_be]
---

# Configuration

:::{rh-description}
Configure Resthome — rooms and sectors, billing rates, supplement types, health insurers, facility and multi-company.
:::

:::{toctree}
:hidden:

reglages-generaux
reglages-facturation
reglages-repas
reglages-documents
:::

Before day-to-day use, a few basic settings give Resthome its structure. They are set up once, then only change at the margins.

## Application settings

The **Settings** menu brings together all the parameters, organized by tab. For a nursing home, follow these guides — each one details **every field** and its **recommended value**:

- [General settings (residents, rooms)](reglages-generaux.md)
- [Billing settings](reglages-facturation.md)
- [Meals and nutrition settings](reglages-repas.md)
- [Document settings](reglages-documents.md)

:::{admonition} In Belgium
:class: rh-country rh-country-be

The Belgian pack adds its own settings: the INAMI numbers and approvals of the establishment, the INAMI rates and pseudo-codes, and the eHealth and eFact credentials. See [Belgian settings](../belgique/reglages.md) and [eHealth and eFact settings](../belgique/reglages-ehealth.md).
:::

## Rooms and sectors

- **Rooms**: create your rooms, with their **type** (single or double room, the sector it belongs to…) and their **amenities**.
- **Sectors / units**: group rooms by living unit.
- A room can be set to **maintenance**, **reserved**, or switched back to **automatic** assignment based on occupancy.

## Rates and packages

- **Billing Rates**: the dated amounts Resthome bills — the accommodation price (resident's share) and, where the country has one, the care allowance paid by the health insurer.
- **Supplement types**: the catalog of billable services (see [Supplements](../facturation/supplements.md)).
- **Absence discount rules**: the fine-tuning of billing when a resident is away.

:::{admonition} In Belgium
:class: rh-country rh-country-be

The rate menu is called **INAMI Rates** and carries the dependency allowance per Katz category and sector, next to the **Billing Codes** (pseudo-codes). See [Belgian settings](../belgique/reglages.md).
:::

## Health insurers and reference data

- **Health insurers**: the list of the residents' health insurers, used for insurability checks and the electronic exchanges with the health insurer, where the country has them.
- **Facility**: your home's information (identifiers, contact details) used in documents and in those exchanges.

## Multi-company

Resthome handles **multiple companies** in a single database: each company has its own residents, rooms and billing, kept separate. Useful for a group that operates several facilities.

:::{admonition} The activity log
:class: note

An **activity log** tracks access to sensitive data (GDPR). It can be viewed from the configuration — useful for compliance.
:::

## Learn more

- [Getting started](../premiers-pas.md)
- [Managing a resident](../residents/gerer-un-resident.md)
