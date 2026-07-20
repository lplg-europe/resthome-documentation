# The resident's medical record

:::{rh-description}
The resident's clinical record in a nursing home (MR/MRS) with Resthome: measurements, clinical status, ICD-10 pathologies, allergies, devices, directives.
:::

:::{rh-faq}
Where is a resident's medical record located in Resthome?
: On the resident record, open the Medical Information tab. It brings together the measurements, clinical status, senses and risks, devices, diagnoses (ICD-10), allergies, medical contacts and advance directives. The tab is only visible for residents and reserved for care staff.

How do I record a resident's weight?
: Weight is read-only in the record: it comes from vital signs entry. Use the Enter Vital Signs button (at the top of the record) or the small + next to the Weight field. The BMI is then calculated automatically from height and weight.

How do I record a pathology or a diagnosis?
: In the Diagnoses / Pathologies section, add a line, pick the pathology from the ICD-10 catalog, then set the severity and the status (Active or Resolved) specific to this resident. A given pathology can only be recorded once per resident.

Do allergies really block a prescription?
: Yes for drug allergens. An allergy with Critical severity blocks the prescription of the medication concerned; a High, Medium or Low severity shows a warning. Food and environmental allergies are for documentation.

How do I flag a do-not-resuscitate (DNR) order?
: In the Advance Directives section, tick DNR Order (Do Not Resuscitate). An orange alert banner then appears at the top of the resident record, a DNR badge shows on their kanban card and in the list, and a DNR filter lets you find the residents concerned.

Who can see the medical record?
: Access is reserved for care staff (medical group). Changes to medical data are logged for traceability and GDPR compliance.
:::

The **Medical Information** tab of the resident record is their **clinical
record** in Resthome. On a single page it brings together the **measurements**,
the **clinical status**, the **senses and risks**, the **devices**, the
**diagnoses (ICD-10)**, the **allergies**, the **medical contacts** and the
**advance directives**.

You find it on the **resident record** (**Residents** or **Care** app), in the
**Medical Information** tab. The tab only appears for **residents**.

:::{admonition} Access restricted to care staff
:class: warning

The **Medical Information** tab and the indicators derived from it (DNR badge,
filters) are only visible to **care staff**. Changes to medical data are
**logged** (traceability and **GDPR** compliance).
:::

Above the tab, a set of **stat buttons** opens the other follow-up panels:
**Prescriptions**, **Care Plans**, **Notes**, **Katz**, **Vital Signs** and
**Trends**. The medical record described below, for its part, focuses on the
resident's **clinical profile**.

## Measurements and BMI

The **Measurements** section gathers the basic body data:

| Field | Purpose |
|---|---|
| **Blood Type** | The resident's blood type |
| **Height (cm)** | Height, entered once |
| **Weight (kg)** | Read-only — comes from the vital signs |
| **BMI** | Calculated automatically (weight / height²) |

:::{admonition} Weight goes through the vital signs
:class: tip

The **Weight** field is not entered directly here: it picks up the last value
recorded during a **vital signs entry**. Use the **Enter Vital Signs** button at
the top of the record, or the small **+** next to the Weight field. The **BMI**
then recalculates on its own as soon as height and weight are known.
:::

## Dependency (Katz)

The **Dependency** section shows, read-only, the summary of the resident's
dependency:

- the current **Katz category** (O, A, B, C, Cd);
- the **validity end** of the Katz assessment;
- the **active care plan**, if there is one.

This information comes from the **Katz assessment** and the **care plan**; you do
not edit it from the medical record.

:::{admonition} The Katz category is declared, it does not set the amount
:class: info

The category is used to **declare the dependency profile** to the health
insurance fund. In the **AViQ** rates, the dependency allowance is the **same
amount for all categories** (see [The Katz assessment](../residents/katz.md)).
:::

## Clinical status

The **Clinical Status** section describes the resident's functional autonomy.
Each field offers a list of values:

| Field | Values |
|---|---|
| **Mobility** | Autonomous · Cane · Walker · Wheelchair · Bedridden |
| **Continence** | Continent · Occasional Incontinence · Frequent Incontinence · Incontinent |
| **Cognitive Status** | Normal · Mild Impairment · Moderate Impairment · Severe Impairment |
| **Communication** | Normal · Difficulty · Non-verbal · Aphasia |

<!-- screenshot to add: Medical Information tab, Measurements, Dependency and Clinical Status sections -->

## Senses and risks

The **Senses & Risk Assessment** section completes the profile:

| Field | Values |
|---|---|
| **Vision** | Normal · Corrected (Glasses) · Impaired · Blind |
| **Hearing** | Normal · Hearing Aid · Impaired · Deaf |
| **Fall Risk** | Yes / No |
| **Pressure Sore Risk** | Low · Moderate · High |

These indicators guide daily monitoring and feed into the care plan.

## Medical devices

The **Medical Devices** section lists the devices and permanent conditions:

- **Urinary Catheter** (yes / no);
- **Stoma** (yes / no);
- **Dental Status**: Natural Teeth · Partial Denture · Full Denture ·
  Edentulous.

## Diagnoses (ICD-10 pathologies)

The **Diagnoses / Pathologies** section lists the resident's pathologies, coded
according to **ICD-10** (International Classification of Diseases). Each line
links the resident to a pathology from the **catalog**.

| Column | Purpose |
|---|---|
| **Pathology** | The pathology from the catalog (ICD-10 code) |
| **Category** | Taken from the catalog (circulatory, nervous, endocrine…) |
| **Severity** | Mild · Moderate · Severe — specific to this resident |
| **Status** | **Active** or **Resolved** |
| **Confirmed** | Clinically confirmed diagnosis (yes / no) |
| **Date** | Date of diagnosis |
| **Notes** | Clinical observations |

:::{admonition} Severity and status specific to the resident
:class: note

The catalog carries a **default** severity, but you set the severity and the
status (Active / Resolved) **for this resident**. A *Resolved* status requires a
**resolution date**. A given pathology can only be recorded **once** per
resident.
:::

<!-- screenshot to add: diagnoses list with category, severity as a badge and Active/Resolved status -->

## Allergies

The **Allergies** section lists the allergies **specific to the resident**,
linked to the **allergen catalog**.

| Column | Purpose |
|---|---|
| **Allergen** | The allergen from the catalog |
| **Category** | Drug · Food · Environmental · Contact · Insect/Venom |
| **Severity** | Low · Medium · High · **Critical** — specific to this resident |
| **Confirmed** | Clinically confirmed allergy (yes / no) |
| **Date** | Date identified |
| **Reaction** | Description of the reaction |

:::{admonition} Drug allergens protect prescribing
:class: warning

For a **drug allergen**, the severity drives the behavior when prescribing:
**Critical** **blocks** the prescription of the medication concerned; **High**,
**Medium** or **Low** shows a **warning**. **Food** and **environmental**
allergies are for documentation. See
[Prescriptions and medications](prescriptions.md).
:::

An **Additional Allergy Notes** field lets you record, in free text, the
allergies or remarks that are not in the structured list.

## Medical contacts

The **Medical Contacts** section links the resident to their healthcare
providers:

- **Specialist Doctors** — one or more doctors (tags);
- Reference **Pharmacy**.

The **Attending Physician** (the resident's assigned doctor) is set instead on
the resident's general information. These contacts are reused elsewhere in
Resthome (prescriptions, eHealth exchanges).

## Advance directives and DNR

The **Advance Directives** section records the resident's wishes:

- **Has Advance Directive** (yes / no) — when ticked, a **content** field
  appears to describe what it contains;
- **DNR Order (Do Not Resuscitate)** — the do-not-resuscitate decision.

:::{admonition} The DNR is flagged everywhere in Resthome
:class: warning

As soon as **DNR Order (Do Not Resuscitate)** is ticked, Resthome makes it
visible to care staff:

- an **orange banner** "DNR — Do Not Resuscitate" at the top of the resident
  record;
- a **DNR badge** on the **kanban** card and in the residents **list**;
- a **DNR filter** in the search, to find the residents concerned.
:::

<!-- screenshot to add: resident record with the orange DNR banner and the Advance Directives section -->

## Medical notes

Finally, a free-text **Medical Notes** field lets you record any important
information that does not fit the structured sections.

## Key points to remember

- The medical record is the **Medical Information** tab of the resident record;
  it is **reserved for care staff** and **logged** (GDPR).
- The **weight** comes from the **vital signs** (read-only) and the **BMI** is
  calculated automatically from height and weight.
- The **Katz category** and the **active care plan** are shown there read-only;
  the category **declares** the profile, it does not set the allowance amount.
- The **diagnoses** use **ICD-10**; **severity** and **status** (Active /
  Resolved) are specific to the resident.
- **Drug allergens** protect prescribing: **Critical** blocks, the others warn.
- The **DNR** triggers a **banner**, a **kanban/list badge** and a search
  **filter**.

## Further reading

- [Prescriptions and medications](prescriptions.md) — allergies and interactions when prescribing.
- [Care plans and vital signs](plans-de-soins.md)
- [Clinical registers](registres.md)
- [The Katz assessment](../residents/katz.md) — from dependency to category.
