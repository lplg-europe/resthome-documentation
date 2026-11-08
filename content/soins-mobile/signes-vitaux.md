---
modules: [healthcare_mobile_care]
---

# Vital signs

:::{rh-description}
Taking the vital signs from the WideCare app: temperature, blood pressure, pulse, oxygen, breathing, weight and blood sugar, with the usual range and the last value.
:::

:::{rh-faq}
Must I fill in every measure?
: No. Fill in only the measures taken. An empty field is a measure not taken, never a zero.

Can I type 37,4 with a comma?
: Yes. The comma and the point are both accepted.

Why is a field orange or red?
: Orange means the value is outside the usual range. Red means the value is impossible: correct it, **Save** stays locked until then.

Why must I enter the weight?
: Because the form was opened from a weighing care: the weight comes first and is required, and saving ticks the care.
:::

The **Vital signs** button of the resident's sheet opens the form of measures.
A care that asks for a weighing opens it too.

![The Vital signs form on the phone: one field per measure with its unit, the usual range and the last value below](../assets/screenshots/soins-mobile/phone-10-signes-vitaux.png)
<!-- screenshot to update: the Vital signs form with the new look -->

## Measures

- **Temperature** (°C)
- **Blood pressure** — the two figures, systolic and diastolic, in mmHg
- **Pulse** (bpm)
- **Oxygen** (%)
- **Breathing** (per minute)
- **Weight** (kg)
- **Blood sugar** (mg/dL)

The **Next** key of the phone keyboard goes to the next field.

## Taking the measures

1. Fill in the measures taken — only those.
2. Read the line under each field: the usual range and the last value, with its
   date.
3. Add a remark under **Anything to add** if useful: taken while resting,
   resident agitated…
4. Tap **Save**.

## A weighing asked for

When the form is opened from a care that asks for a weighing, the **Weight**
field comes first and is required: **Enter the weight asked for** shows until
it is filled in. Saving ticks the care.

## Colours and short forms

- **Orange** — the value is outside the usual range: check it.
- **Red** — the value is impossible, or the diastolic is not lower than the
  systolic. **Save** stays locked until it is corrected.

The short forms used on the floor are understood: **13** is read as 130 mmHg,
**374** as 37.4 °C. The line under the field then says what will be recorded.

A reading out of range is saved with a warning, and appears in the bell of the
colleagues who must read it.

The measures are recorded as a vital signs observation on the resident. They
feed the same history and the same curves as in the back office. See
[Observations and vital signs](../soins/observations.md).
