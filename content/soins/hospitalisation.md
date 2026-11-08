---
modules: [resthome_geriatric, healthcare_medical_absences]
sectors: [mr]
---

# Hospital departure and return

:::{rh-description}
Record a resident's hospital departure and return in WideCare in one step: prescriptions suspended and resumed, care cancelled and planned again, the absence for billing, the liaison pack for the hospital and a record review at the return.
:::

:::{rh-faq}
Where do I record a hospital departure?
: On the resident's form, **Hospital departure**; or **New → Hospital departure or return** on the care dashboard.

What happens to the medicines and the care while the resident is in hospital?
: The running prescriptions are suspended and the planned care tasks cancelled. At the return, the prescriptions resume and the care of the day is planned again.

Does it change the bill?
: When billing is installed, the departure opens a hospital absence and the return closes it. See [Absences and hospitalisations](../facturation/absences.md).

What does the hospital receive?
: The liaison pack: treatments, allergies, advance directives and the resident's wishes for a hospitalisation. It prints when you confirm, or with **Print Liaison Pack**.
:::

When a resident leaves for hospital, several things must happen at once: stop
the medicines, cancel the care, tell billing, give the hospital what it needs.
WideCare does it in one step.

## 1. Record the departure

1. On the resident's form, click **Hospital departure** — or **New → Hospital
   departure or return** on the [care dashboard](tableau-de-bord.md).
2. Check the **Date and time**.
3. Pick the **Hospital** (required).
4. Write the **Reason**: why the resident leaves — the hospital will ask.
5. Read what will happen:
   - the running prescriptions suspended;
   - the planned care tasks cancelled;
   - a hospital absence opened for billing, when billing is installed;
   - the liaison pack printed on confirmation.
6. Click **Confirm**.

For a day-centre user, the sheet also asks where they left from (**The day
centre** or **Home**).

<!-- screenshot to add: the Hospitalization sheet for a departure, with the summary of what will be suspended and cancelled -->

## 2. While the resident is in hospital

- The resident counts as **In hospital** on the care dashboard's presence
  strip.
- The care tasks of those days are cancelled, with a note saying the resident
  is in hospital.
- **Return from hospital** becomes the first button on the resident's form.

## 3. Record the return

1. Click **Return from hospital**.
2. Check the **Date and time** and the hospital.
3. Read what will happen:
   - the prescriptions resumed;
   - today's care planned again;
   - the hospital absence closed;
   - the record put up for review.
4. Click **Confirm**.

:::{admonition} The record is reviewed after a return
:class: note

A return from hospital creates a record review: the team re-reads the record
— treatments may have changed. It shows in the next
[multidisciplinary meeting](reunion-pluridisciplinaire.md).
:::

## The liaison pack

The liaison pack gathers what the hospital needs: treatments, allergies,
advance directives, and the wishes for a hospitalisation (preferred and refused
hospitals, room type, complementary insurance). It prints when you confirm the
departure, with **Print Liaison Pack**, or from the **Documents** tab of the
resident's form.

## The absences

**Nursing Care → Residents → Absences** lists the residents' absences,
hospitalisations included.

## Going further

- [Absences and hospitalisations](../facturation/absences.md)
- [The resident's medical record](dossier-medical.md)
- [Prescriptions and medicines](prescriptions.md)
