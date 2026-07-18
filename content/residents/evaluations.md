# Geriatric assessments (beyond Katz)

:::{rh-description}
Geriatric scales beyond Katz in the nursing home (MR/MRS) with Resthome: MMSE, Braden, MNA, OHAT and Tinetti — entry, score, interpretation and follow-up.
:::

:::{rh-faq}
Which geriatric scales does Resthome offer beyond Katz?
: Five standard scales on the resident's « Evaluation Tools » tab: MMSE (cognition), Braden (pressure ulcer risk), MNA (nutritional status), OHAT (oral health) and Tinetti (balance, gait and fall risk).

Where do you enter a geriatric assessment in Resthome?
: From the resident's record, « Evaluation Tools » tab, or via the Healthcare > Evaluation Tools menu. Each scale has its own list and its own guided form.

Who can validate an assessment?
: Any user can enter and confirm it, but only the head nurse or the physician can validate it. A validated assessment is locked: you have to reset it to draft to correct it.

How do you interpret a low Braden score?
: On the Braden scale, the lower the score, the higher the pressure ulcer risk: 19-23 no risk, 15-18 mild risk, 13-14 moderate, 10-12 high, 9 or less very high.

How do you reassess a resident?
: Enter a new assessment on a new date (one per day and per scale); the full history is kept. For a periodic reassessment cycle with a due date, use the clinical registers.

Is the Morse scale (fall risk) available?
: The « Evaluation Tools » tab offers Tinetti for balance and gait. The Morse scale and the falls register are found in the clinical registers of the care module.
:::

Beyond the [Katz scale](katz.md), Resthome brings together the main
**geriatric scales** used in the nursing home (MR/MRS) to objectively measure
cognition, pressure ulcer risk, nutritional status, oral health and fall risk.
You will find them in two places:

- on the **resident's record**, the **« Evaluation Tools »** tab, where each
  scale shows the resident's history and allows direct entry;
- via the **Healthcare > Evaluation Tools** menu, which lists all the
  assessments in the facility, scale by scale.

<!-- screenshot to add: « Evaluation Tools » tab on the resident record -->

## Available scales

| Scale | What it measures | Score | Meaning |
|---|---|---|---|
| **MMSE** | Cognitive function | /30 | Higher = better |
| **Braden** | Pressure ulcer risk | /23 | Lower = more at risk |
| **MNA** | Nutritional status | /14 | Lower = more at risk |
| **OHAT** | Oral health | /16 | Higher = more at risk |
| **Tinetti** | Balance and gait (falls) | /28 | Lower = more at risk |

:::{admonition} The Katz category stays separate
:class: info

The Katz scale determines the **dependency category** and the **flat-rate fee**; it
has its own page and its own renewal cycle. See [The Katz assessment](katz.md).
:::

## MMSE — cognitive function

The **MMSE** (Mini Mental State Examination) is a standard cognitive screening test
out of **30 points**. You tick each successful item, spread across 7 domains:

| Domain | Points |
|---|---|
| Orientation in time | 5 |
| Orientation in space | 5 |
| Registration (3 words) | 3 |
| Attention and calculation | 5 |
| Recall (3 words) | 3 |
| Language | 8 |
| Visuo-constructive praxis | 1 |

Resthome adds up the ticked items and displays the interpretation:

| Score | Interpretation |
|---|---|
| 27-30 | Normal |
| 21-26 | Mild cognitive impairment |
| 11-20 | Moderate cognitive impairment |
| 0-10 | Severe cognitive impairment |

## Braden — pressure ulcer risk

The **Braden** scale predicts **pressure ulcer risk**. You score **6 subscales**
(radio buttons):

- Sensory perception (1-4)
- Skin moisture (1-4)
- Activity (1-4)
- Mobility (1-4)
- Nutrition (1-4)
- Friction and shear (1-3)

The total ranges from 6 to 23. **Warning: the lower the score, the higher the risk.**

| Score | Risk level |
|---|---|
| 19-23 | No risk |
| 15-18 | Mild risk |
| 13-14 | Moderate risk |
| 10-12 | High risk |
| 9 or less | Very high risk |

<!-- screenshot to add: Braden form with radio scoring and risk badge -->

## MNA — nutritional status

The **MNA** (Mini Nutritional Assessment, short form) screens for **malnutrition
risk** out of **14 points**, from 6 questions:

- Reduced food intake over the past 3 months (0-2)
- Recent weight loss (0-3)
- Mobility (0-2)
- Acute illness / psychological stress (0 or 2)
- Neuropsychological problems (0-2)
- Body mass index — BMI (0-3)

| Score | Nutritional status |
|---|---|
| 12-14 | Normal |
| 8-11 | At risk of malnutrition |
| 0-7 | Malnourished |

:::{admonition} Nutritional follow-up
:class: tip

Malnutrition follow-up (MNA re-scoring reminders, intake vs needs, hydration)
relies on the clinical registers and the care module. See [The clinical
registers](../soins/registres.md).
:::

## OHAT — oral health

The **OHAT** (Oral Health Assessment Tool) assesses **oral health** across
**8 categories**, scored from 0 (healthy) to 2 (needs treatment): lips, tongue,
gums and tissues, saliva, natural teeth, dentures, oral cleanliness and dental
pain.

The total ranges from 0 to 16. **Here, the higher the score, the more concerning
the situation.**

| Score | Oral health status |
|---|---|
| 0-3 | Healthy |
| 4-8 | Changes needed (refer to a dental professional) |
| 9-16 | Unhealthy (urgent referral) |

:::{admonition} « N/A » options
:class: note

The **Natural teeth** and **Dentures** categories have an **N/A** (not applicable)
option: it is excluded from the total score calculation.
:::

## Tinetti — balance, gait and fall risk

The **Tinetti** scale (POMA) assesses **balance** and **gait** to estimate
**fall risk**:

- Balance section: 9 items, /16
- Gait section: /12
- Total: /28

Resthome calculates the two subscores and the total.

| Score | Fall risk |
|---|---|
| 25-28 | Low risk |
| 19-24 | Moderate risk |
| Under 19 | High risk |

:::{admonition} Tinetti, Morse and the falls register
:class: note

The « Evaluation Tools » tab offers **Tinetti**. For the **Morse** scale and the
**falls register** (incidents, preventive measures, reassessments), use the
[clinical registers](../soins/registres.md).
:::

## Entering and validating an assessment

All scales follow the same flow:

1. Open the scale: from the resident's **« Evaluation Tools »** tab, or via
   **Healthcare > Evaluation Tools**.
2. **New**: the resident, the **date** (today by default) and the **assessor**
   (you) are pre-filled. Score the items.
3. **Confirm**: the assessment moves from **Draft** to **Confirmed**.
4. **Validate**: the head nurse or the physician validates; the assessment moves to
   **Validated**, with the validator and the validation date recorded.

The status bar follows these steps: **Draft → Confirmed → Validated** (plus
**Cancelled**). The available buttons are **Confirm**, **Validate**, **Cancel** and
**Reset to draft**.

:::{admonition} Locking and retention
:class: warning

A **validated** assessment is **locked**: its scores can no longer be edited. To
correct it, click **Reset to draft** (restricted to the head nurse). Validated
assessments **cannot be deleted**: health data must be retained (GDPR + INAMI).
:::

:::{admonition} One assessment per day
:class: note

There can only be **one assessment per resident, per date and per scale**. The date
cannot be in the future, and no assessment can be created for a deceased resident.
:::

## Follow-up and reassessment

- The « Evaluation Tools » tab keeps the **dated history** of each scale: to
  reassess, enter a **new assessment** on a new date.
- The **Katz** scale has its own **renewal cycle** (validity due date, reminders).
  See [The Katz assessment](katz.md).
- For a structured **periodic reassessment cycle** (calculated due date, keep /
  change / stop decision, follow-up log), use the [clinical
  registers](../soins/registres.md).

## Key points to remember

- Five scales beyond Katz: MMSE, Braden, MNA, OHAT and Tinetti, on the resident's
  « Evaluation Tools » tab.
- Score meaning: MMSE and Tinetti, a **high** score = favorable situation; Braden
  and MNA, a **low** score = more at risk; OHAT, a **high** score = more at risk.
- Common flow: **Draft → Confirmed → Validated**; validation is restricted to the
  head nurse or the physician.
- Validated = **locked and retained**; reset to draft to correct.
- One assessment per resident, per date and per scale.

## Learn more

- [The Katz assessment](katz.md) — dependency category and flat-rate fee.
- [The clinical registers](../soins/registres.md) — falls (Morse), restraint, pain, wounds, periodic reassessments.
- [Care plans](../soins/plans-de-soins.md)
- [Managing a resident](gerer-un-resident.md)
