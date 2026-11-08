---
modules: [healthcare_consultation, healthcare_billing_core]
sectors: [gp]
---

# Practice settings

:::{rh-description}
Who can do what in a WideCare general practice: the Consultations and Per-Act Billing accesses of each user, and the product the acts are booked on.
:::

:::{rh-faq}
Which access does a colleague need to see the diary and write consultations?
: **Consultations**, set to **User**. **Manager** can also delete consultations.

Which access does the secretary need to invoice the acts?
: **Per-Act Billing**, set to **User**: it records the acts and issues the customer invoices. **Manager** can also delete acts.

Who has these accesses at the start?
: The administrator of the practice has both, as **Manager**.
:::

Each user of the practice gets the accesses of their role. The administrator of
the practice gives them in the user's record.

## Give a user access

1. Open **Settings**, then **Users & Companies → Users**, and the user.
2. In the access rights, set:
   - **Consultations**: **User** to book appointments, see the patients and
     write consultations; **Manager** to also delete consultations;
   - **Per-Act Billing**: **User** to record the acts and invoice them;
     **Manager** to also delete acts.
3. Save.

A user with the **Consultations** access sees the **Practice** app and can
create and edit the patient cards.

<!-- screenshot to add: the access rights of a user with Consultations and Per-Act Billing -->

## What each access shows

| Access | What it opens |
| --- | --- |
| **Consultations** | The **Practice** app: **Patients**, **Appointments**, **Consultations**; the patient and the reason of every appointment. |
| **Per-Act Billing** | **Billable Acts**, the **Acts** tab of the consultations, **Create Invoice**, and the customer invoices. |

A colleague who shares the calendar without the **Consultations** access sees
the time slots, not the patients nor the reasons.

## The product of the acts

Every invoice line of an act is booked on the **Healthcare Act** product: a
service, without tax. Your accountant sets its income account in the
**Invoicing** app.

:::{admonition} In Belgium
:class: rh-country rh-country-be

A doctor whose eHealth certificate has the quality **Doctor (natural person)**
gets the **Practice** app with it: see
[eHealth identity and eID sign-in](../belgique/medecins/identite-ehealth.md).
:::

## What's next

- [General practice](index.md)
- [Per-act billing](facturation-a-l-acte.md)
