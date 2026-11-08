---
modules: [healthcare_medical]
sectors: [mr, csj]
---

# Care configuration

:::{rh-description}
Configure care in WideCare: the settings, the care types and activities with who may do them, the periods of the day, the tags, the outcome reasons, the observation types and the care plan templates.
:::

:::{rh-faq}
Who can change the care configuration?
: The managers of the care app. Care plan templates and recurring meetings can also be written by head nurses.

Can I change the hours of the moments of the day?
: Yes, under **Periods of the Day**. Each period ends when the next one starts.

Where do I write a care plan template?
: **Nursing Care → Configuration → Care Plan Templates**, or from a care plan with **Actions → Save as template**.
:::

The care configuration lives under **Nursing Care → Configuration**. The same
catalogues are also reachable from **Care Tasks → Configuration**.

## Settings

**Nursing Care → Configuration → Settings**:

| Block | Setting |
|---|---|
| **Falls** | How the head nurses are told of a fall to read: by an activity only, or also by email |
| **Prescriptions** | See [Prescriptions and medicines](prescriptions.md) |
| **Clinical Records** | **Body location entry**: on a body drawing or in a list |
| **Care Tasks** | **Assign care tasks automatically** — see [Automatic assignment of care tasks](assignation-automatique.md) |

## Care catalogues

Under **Nursing Care → Configuration → Care Catalogues**.

### Care types

The families of care: Vital Signs, Wound Care, Medication, Hygiene,
Elimination, Mobility/Transfer, Nutrition, Doctor Visit, Specialist Visit,
Therapy, Examination, Other. Each has a code, a default department, a default
duration, an observation type, a colour, and **Done by** — the care roles who
may do it.

### Care activities

The care themselves, as the plan offers them: a name, a care type, a
department, a criticality, a duration and the **Default Description** the
carer will read. **Done by** on an activity wins over its care type.

### Periods of the day

The moments a care is given: Morning (07:00), Noon (12:00), Afternoon (14:00),
Evening (17:00), Night (22:00) by default. Set **Starts At**; the end is the
start of the next period.

### Care tags, outcome reasons, body zones

- **Care Tags** — a name and a colour, to sort the care.
- **Care Outcome Reasons** — the reasons for a care not done or postponed;
  each says what it is **Used For** and whether it **Requires a Comment**. See
  [Care tasks](taches-de-soins.md).
- **Body Zones** — the zones of the body drawing; they can be renamed or
  hidden, not created.

## Clinical catalogues

Under **Nursing Care → Configuration → Clinical Catalogues**: the pathologies
(ICD-10), the dosages, the allergens and the memory of prescription reading.
See [Prescriptions and medicines](prescriptions.md) and
[The resident's medical record](dossier-medical.md).

## Observation types

**Nursing Care → Configuration → Observation Types**: drag the types into the
order in which the meeting reads them, and tick **Critical** for those that
bring a resident up in the next meeting. Falls and incidents are always
critical.

## Care plan templates

**Nursing Care → Configuration → Care Plan Templates** (head nurses and
managers). A template holds:

- its name and the **Dependency Category** it is written for;
- **Written for**: any stay, a stay overnight or a day-care stay;
- **Builds on**: another template it completes;
- **What this template assumes**, shown before applying it;
- the **Objectives** and the **Cares** it adds to a plan.

WideCare comes with sample templates — falls, undernutrition, pressure sores,
cognitive disorders, end of life, life project — to adapt. Applying a template
is described under [Care plans](plans-de-soins.md).

<!-- screenshot to add: a care plan template with its Objectives and Cares tabs -->

## Recurring meetings and life project methods

- **Recurring Meetings** — see
  [Multidisciplinary meetings](reunion-pluridisciplinaire.md).
- **Life Project Methods** — see [The life project](projet-de-vie.md).

## Going further

- [Care plans](plans-de-soins.md)
- [Care tasks](taches-de-soins.md)
