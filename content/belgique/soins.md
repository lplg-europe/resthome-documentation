---
modules: [resthome_geriatric_be, l10n_health_be, resthome_geriatric, healthcare_medication, resthome_documents]
---

# Care in Belgium

:::{rh-description}
What the Belgian country pack adds to the Care app in a nursing home (MR/MRS): the Katz scale in the medical record and the anamnesis, the SAM medication catalogue, the INAMI number of care staff, the AViQ undernutrition screening and the Belgian document tags.
:::

:::{rh-faq}
Where is the Katz category shown in the resident's medical record?
: In the Dependency section of the Medical Information tab, read-only: the current Katz category (O, A, B, C, Cd), the end of validity of the Katz assessment and the active care plan. A Katz button above the tab opens the resident's assessments.

Where does the medication catalogue come from in Belgium?
: From SAM, the official Belgian medication database. It provides the name, form and dosage of each medication, with its CNK code, active ingredient and ATC code, and serves as the source for prescriptions.

Does the undernutrition status change the INAMI allowance?
: No. The dependency allowance follows the resident's Katz category, not their nutritional status. Undernutrition monitoring triggers assessments (MNA) and alerts, but has no effect on billing.

Where do the undernutrition screening thresholds come from?
: They are the default values of the AViQ screening (PWNS-be-A): weight loss of more than 5% in 1 month or more than 10% in 6 months, a BMI below 23 over 70, or an MNA older than 6 months.

Which document tags are Belgian?
: Katz evaluation, MR/MRS agreement (eAgreement), OA allocation and CPAS. They file the Katz grids, the health insurer's agreements and decisions, and the CPAS coverage documents.
:::

The **Care** app works the same way in every country. In Belgium, the country
pack plugs the Belgian answers into it: the **Katz** scale as the dependency
assessment, **SAM** as the medication reference, the **INAMI number** of the
care staff, the **AViQ** screening thresholds and the tags for Belgian
documents.

The care workflow itself — medical record, anamnesis, prescriptions, care plans,
registers, meals — is described in the neutral pages: see [Care](../soins/index.md).

## The Katz scale in the resident's record

The dependency assessment is the **Katz** scale. It appears wherever the Care
app shows the resident's dependency:

- **Medical record** — above the **Medical Information** tab, a **Katz** stat
  button opens the resident's assessments. The **Dependency** section shows,
  read-only, the current **Katz category** (O, A, B, C, Cd), the **end of
  validity** of the Katz assessment and the **active care plan**.
- **Care plans** — the plan and the list of plans show the resident's Katz
  category and its validity.
- **Anamnesis** — the clinical context it composes includes the resident's
  **Katz** assessments and their current category, never re-entered.
- **Residents list** — the side panel filters residents by Katz category.

You never edit the category from these screens: it comes from the validated
Katz assessment. See [The Katz assessment](katz.md).

:::{admonition} The Katz category is declared, it does not set the amount
:class: info

The category is used to **declare the dependency profile** to the resident's
health insurer (mutuelle). In the **AViQ** rates, the dependency allowance is
the **same amount for all categories**, including O. See [The INAMI
dependency allowance](forfait-inami.md).
:::

## The SAM medication catalogue

The facility's **medication catalogue** is fed from **SAM** (Source Authentique
des Médicaments), the official Belgian medication database. Rather than entering
a medication by hand, you search for it in SAM and import it with its CNK code,
active ingredient, ATC code and leaflets. It then serves as the source for
prescriptions.

In **Care → Configuration**, the **SAM Database** menu gives read-only access to
the reference database. See [The SAM medication
database](sam-base-medicaments.md).

## Physicians and care staff: the INAMI number

The resident's **Attending Physician** and **Medical Contacts** are reused in
the **eHealth** exchanges with the health insurer (see
[eHealth](ehealth/index.md)). The Belgian pack adds an **INAMI Number** field
to identify the care professionals:

- on the **physician**'s record, next to the specialty;
- on the **employee** record, for care roles (nurse, head nurse, physician,
  physiotherapist, occupational therapist, speech therapist).

The INAMI number has 11 digits. On the employee record, it is stored on the
employee's contact, so the same number follows the person everywhere.

## Undernutrition screening: the AViQ thresholds

The undernutrition monitoring of the **Meals** app raises a **Re-screen (MNA)**
signal on thresholds that are the default values of the **AViQ** screening
(**PWNS-be-A**):

- weight loss of more than **5%** over about 1 month;
- weight loss of more than **10%** over about 6 months;
- **BMI below 23** in a resident **over 70**;
- **overdue MNA**: no MNA, or a last MNA more than 6 months old.

This screening has no effect on billing: the INAMI allowance follows the Katz
category, not the nutritional status. See [Nutritional monitoring and
undernutrition](../repas/suivi-nutritionnel.md).

## Belgian document tags

Among the predefined tags of the resident's document folder, four file Belgian
documents:

| Tag | Typical use |
|---|---|
| **Katz evaluation** | Katz dependency assessment grids and reports. |
| **MR/MRS agreement (eAgreement)** | The health insurer's MR/MRS agreements (care convention), exchanged through eAgreement. |
| **OA allocation** | Decisions, statements and letters from the health insurer (OA). |
| **CPAS** | Coverage documents from the CPAS. |

Like the other tags, they can be applied automatically as **Default tags**. See
[Resident documents](../documents/index.md) and [Public welfare centre
(CPAS)](cpas.md).

## What's next

- [The Katz assessment](katz.md)
- [The INAMI dependency allowance](forfait-inami.md)
- [The SAM medication database](sam-base-medicaments.md)
- [eHealth](ehealth/index.md)
- [The resident's medical record](../soins/dossier-medical.md)
