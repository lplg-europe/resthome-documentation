---
modules: [healthcare_medical_planning]
sectors: [mr, csj]
---

# Automatic assignment of care tasks

:::{rh-description}
Automatic assignment in WideCare: each night the care tasks of the coming day go to the care staff on the planning at their hour and in their sector, evenly, with warnings when nobody of the right role is planned.
:::

:::{rh-faq}
How do I switch on automatic assignment?
: In **Nursing Care → Configuration → Settings**, block **Care Tasks**, tick **Assign care tasks automatically**. Switched off, nothing of it shows: no button, no column, no warning, no ribbon.

Who receives a care task?
: A member of staff on a confirmed shift at the hour of the care, in the resident's sector, whose role may do this care. The care is shared evenly among them.

Does the staff get a notification?
: No. The assignment is silent: each person finds their care under **My Assigned Care**.

Why does a care show "No staff planned"?
: Nobody of the role this care needs is on a confirmed shift at its hour. Plan someone, or assign the care by hand.

Does it replace an assignment done by hand?
: No. Only care tasks still unassigned are shared.
:::

When the house plans its staff in the **Planning** app, WideCare can share the
care tasks among the people at work: each care goes to someone of the right
role, on duty at its hour, in the resident's sector.

## Switch it on

1. Open **Nursing Care → Configuration → Settings**.
2. In the **Care Tasks** block, tick **Assign care tasks automatically**.
3. Save.

Each night, the care tasks of the coming day are then assigned. Switched off,
none of what follows shows on screen.

## Who may do which care

Each care type and each care activity says who it is **Done by** — one or
more care roles. The activity wins over the care type; left empty, any care
staff may do it.

The defaults:

| Care | Done by |
|---|---|
| Hygiene, elimination, nutrition, vital signs, medication | Nurses and care assistants |
| Wounds, examinations, injections, preparing medicines, urinary catheter | Nurses |
| Mobility | Nurses, care assistants and physiotherapists |
| Physiotherapy, occupational therapy, speech therapy | Their therapist |

Change them under **Nursing Care → Configuration → Care Catalogues → Care
Types** and **Care Activities**. See [Care configuration](configuration-soins.md).

## Assign now

On **Today's Care** and **To Assign**, the **Assign automatically** button
shares the open care tasks at once (planning administrators). It answers with
the number of care tasks shared and of staff members who received them, or
says why nothing could be assigned.

## Warnings

When a care cannot be given to anyone, the **Planning** column of the list and
a yellow banner on the care task say why:

- nobody on the planning at this hour;
- nobody of its role on the planning at this hour (in the sector);
- the person assigned is not on the planning at this hour;
- people are on the planning but without access to the care tasks, or to the
  resident's sector.

A planned care task whose role nobody covers at its hour carries the yellow
ribbon **No staff planned**, on its card and its form.

:::{admonition} Check the shifts too
:class: tip

On a shift, the Planning app warns when its person will receive no care task:
their user has no care role, or the sector of the shift is not among the
sectors of their employee file. Fix it there, then click **Assign
automatically** again.
:::

## Going further

- [Care tasks](taches-de-soins.md)
- [Staff planning](../planning/index.md)
- [Shifts for the staff](../planning/postes-du-personnel.md)
