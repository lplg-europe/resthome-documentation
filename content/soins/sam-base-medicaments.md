---
howto_auto: true
---

# The SAM medication database

:::{rh-description}
The Belgian SAM authentic-source database in Resthome: ATC reference, BCFI class, Black Triangle, SmPC/leaflet and the Search SAM wizard for the nursing home (MR/MRS).
:::

:::{rh-faq}
What is the SAM database?
: SAM (Source Authentique des Médicaments, the authentic source of medicines) is the official Belgian medication reference database. Resthome ships a copy of it to feed your nursing home (MR/MRS) catalog with reliable data: CNK code, active ingredient, ATC code, BCFI class, leaflets.

Where can I find the SAM database in Resthome?
: Two entry points. Browsing, through the Care app → Configuration → SAM Database. And the "Search SAM" import wizard, through the MR/MRS app → Configuration → eHealth Configuration → Search SAM.

How do I add a SAM medication to my catalog?
: Open the Search SAM wizard, search by name or by CNK code, check the rows you want and click Import Selected. The medications are created in your catalog with their SAM data.

What does "Black Triangle" mean?
: The black triangle flags a medication under additional monitoring (additional pharmacovigilance). The information is taken from SAM, for guidance, on the reference record.

Does the search work without an eHealth connection?
: Yes. The search relies first on the local copy of SAM, available offline and instantly. The live DICS v5 service is used only as a fallback and requires a certified eHealth connection.

How do I update a medication that is already present?
: Run the search again and re-import the row. If the CNK code already exists in the catalog, Resthome updates the existing record instead of creating a second one.
:::

**SAM** (Source Authentique des Médicaments, the authentic source of medicines) is
the official Belgian medication reference database. Resthome uses it as the
foundation of its **medication catalog**: rather than entering a medication by
hand, you search for it in SAM and import it, with its reliable data (CNK code,
active ingredient, classification, leaflets).

Two entry points:

- **Browse** the reference database — **Care** app → **Configuration** →
  **SAM Database** (read-only).
- **Search and import** — the **Search SAM** wizard, in the **MR/MRS** app →
  **Configuration** → **eHealth Configuration** → **Search SAM**.

:::{admonition} A feature of the eHealth integration
:class: info

The **Search SAM** wizard is part of Resthome's Belgian eHealth layer. It installs
automatically as soon as the medical module and the eHealth module are present,
and access is reserved for the **eHealth manager**. Browsing the database
(Care → Configuration) remains accessible without that role.
:::

## What the SAM database provides

Every medication in the reference database carries authentic data, useful both
for care and for traceability:

| Data | What it is used for |
| --- | --- |
| **CNK code** | Belgian pharmacy code (7 digits) that identifies the package. |
| **Active ingredient (INN)** | The active substance, in French and Dutch. |
| **ATC code** | Anatomical Therapeutic Chemical classification (WHO), with its description. |
| **BCFI class** | Pharmacotherapeutic classification from the Belgian Centre for Pharmacotherapeutic Information. |
| **Black Triangle** | Flags a medication under additional monitoring (additional pharmacovigilance). |
| **Form and route** | Pharmaceutical form and route of administration, in French and Dutch. |
| **SmPC and leaflet** | Links to the Summary of Product Characteristics and the patient leaflet (FR and NL). |
| **BCFI link** | Direct link to the medication's page on the BCFI website. |
| **Prescription and manufacturer** | Dispensing status (prescription required) and marketing authorization holder. |

:::{admonition} A reference copy, not an order
:class: note

Resthome's SAM database is a **local copy** loaded at installation. It helps you
identify and document a medication; it manages neither stock nor prices. Those
live on the catalog record, once the medication is imported.
:::

## Browsing the SAM database

From **Care → Configuration → SAM Database**, you browse the reference database in
read-only mode. The list shows the CNK code, the name, the active ingredient, the
ATC code, the form and the manufacturer.

Use the search bar and filters to narrow down:

- **search** by name (FR/NL), CNK code, ATC code, active ingredient or manufacturer;
- **filters** — **Prescription Required**, **Black Triangle** and **With CNK**;
- **groupings** by ATC code, by form or by manufacturer.

A medication's record details its identification, its classification, its
pharmaceutical form, its active ingredient and the links to its official
documents (SmPC and leaflet, FR and NL).

<!-- screenshot to add: a medication record in the SAM Database, identification / classification / official documents tabs -->

## The Search SAM wizard

The **Search SAM** wizard finds a medication in SAM and adds it to your catalog in
one step. Open it through **MR/MRS → Configuration → eHealth Configuration →
Search SAM**.

### 1. Run a search

Choose the **search type**:

- **By Name** — by brand name or active ingredient (e.g. *Dafalgan*, *Rilatine*);
- **By CNK Code** — by CNK code.

Enter your term in the search field then click **Search**. The search is
**accent-insensitive** and handles multiple words (e.g. *Amlodipine 5mg*).

:::{admonition} Local search first
:class: tip

The wizard first queries the local copy of SAM: the response is immediate, even
without a connection. If that copy is empty, Resthome can switch to the live
**DICS v5** service — but that path requires a certified eHealth connection.
:::

### 2. Choose from the results

Results are shown in a table. Each row shows the **CNK** code, the **name**, the
**active ingredient (INN)**, the **strength**, the **form** and — in optional
columns — the manufacturer, the ATC code, the BCFI class and the SmPC / leaflet
links.

The **In Catalog** column indicates whether the medication is already in your
catalog. Those rows appear **in blue**: no need to recreate them.

Check the **Select** box at the start of the row for each medication to import.

<!-- screenshot to add: Search SAM results with Select boxes checked and the In Catalog column -->

### 3. Import to the catalog

Click **Import Selected**. Resthome creates one record in your catalog per checked
medication, carrying over the SAM data:

| SAM data | Catalog field |
| --- | --- |
| Name | Medication name |
| CNK | CNK code |
| INN (active ingredient) | Active ingredient |
| Strength | Dosage |
| Form | Form (converted to a Resthome category) |
| Manufacturer | Manufacturer |
| ATC | ATC code |
| SmPC / leaflet / BCFI link | **Official documents** tab of the record |

A notification confirms the number of medications **created** (and **updated**,
where applicable).

### 4. Update an existing medication

To refresh a record that is already present, run the search again (**Search
Again** button) and re-import the row. Resthome **matches by CNK code**: if the
medication already exists, it **updates** the record instead of creating a
duplicate.

:::{admonition} An import does not replace the prescription
:class: warning

Importing a medication adds it to the facility's **catalog**. You still have to
**prescribe** it to the resident afterwards, with its dosage and period. See
[Prescriptions and medications](prescriptions.md).
:::

## Key takeaways

- **SAM = the official Belgian medication reference database**, embedded in
  Resthome as the foundation of the catalog.
- **Two entry points**: browsing (Care → Configuration → SAM Database) and the
  **Search SAM** import wizard (MR/MRS → Configuration → eHealth Configuration).
- The search accepts the **name**, the **CNK code** or the **active ingredient**,
  and works **offline** on the local copy.
- **Import Selected** creates the records; a re-import **updates** medications
  already present (matching by CNK).
- SAM provides **ATC, BCFI class, Black Triangle, SmPC and leaflet (FR/NL)** —
  reliable data, for reference.

## Further reading

- [Prescriptions and medications](prescriptions.md)
- [Care plans and vital signs](plans-de-soins.md)
- [The eHealth integration](../ehealth/index.md)
