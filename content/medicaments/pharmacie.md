---
modules: [healthcare_medication, healthcare_medical, healthcare_medication_accommodation]
sectors: [mr, csj]
---

# Pharmacy orders

:::{rh-description}
Order the residents' medicines from their pharmacy in WideCare: the resident's pharmacist, the pharmacy mandate, the basket that fills itself, and the delivery followed like a parcel.
:::

:::{rh-faq}
Which pharmacy does an order go to?
: To the pharmacist the resident chose, on their record; otherwise to the house's pharmacy set in the Care settings. One order per pharmacy.

Why is a line of my order red?
: Its resident has no pharmacy mandate in force. Nobody may order their medicines until the mandate is signed: have it signed, or take the line off, before sending.

Do I have to create the orders myself?
: No. What is missing enters the basket by itself — the first box of a new treatment, a dose not available on the round, a medicine missing from a pillbox, a box running low. Where a secure channel to the pharmacy exists, the basket also leaves by itself every morning.

How do I order something urgently?
: Open the basket and send it yourself. The order shows the pharmacy's phone number.

What do I do when the delivery arrives?
: Tick **Not in the Delivery** on what did not come, then click **Everything Arrived**. What is missing goes back into the basket.
:::

The residents' medicines come from a pharmacy. WideCare keeps one **basket**
per pharmacy that fills itself with what is missing, and follows each order
like a parcel until it arrives.

## Before you start

### The pharmacies

A pharmacy is a company contact with **Is a Pharmacy** ticked, next to the
hospital and social-service tick boxes of the contact form. Only those
contacts are proposed as a resident's pharmacist, the house's pharmacy or the
pharmacy of an order.

### The resident's pharmacist

On the resident's record, the **Pharmacy** field (next to the physicians) names
the pharmacist the resident chose. Leave it empty and **the house's pharmacy**
serves the resident: set it in **Nursing Care → Configuration → Settings**,
**The house's pharmacy**.

### The pharmacy mandate

The resident, or their representative, signs that a staff member may **order
and receive** their medicines at the pharmacy. Without a mandate in force,
nobody may order for them.

- At admission, the resident's admission guide asks **Have the pharmacy mandate
  signed** while none is in force, and opens a pre-filled mandate.
- On the resident's record, the **Documents** tab shows a pharmacy mandate tile:
  *signed on …, mandatary …*, or what is still to be signed.
- On the [Medicines workstation](index.md), **Mandates to Sign** lists the
  residents without one, with **Have the Mandate Signed**.

The mandate form holds the resident, **Signed On**, **Signed By** (*The
resident* or *Their representative*), the **Signatory**, the **Mandatary** (the
staff member who orders and receives) and the **Signed Copy**. Its states are
**In force** and **Ended**.

- Only **one** mandate is in force per resident: a new signature replaces the
  previous one.
- **End the Mandate** ends it (*Ended by the signatory*); the end of the stay
  ends it too, and a stay reopened puts it back in force.

Nurses and physicians create and change mandates; the administrative staff can
record one from the admission guide.

## The basket fills itself

The basket (an order **To Order**) receives a line, with **Why** and **Said
By**, whenever:

- a **new treatment** needs its first box (not a renewal, and not what the
  pharmacy's sachets already bring);
- a dose is **not available** on the round;
- a medicine is **missing** from a pillbox;
- someone clicks **Missing: Tell the Pharmacy** or **Order From the Pharmacy**
  on a treatment;
- a box the house counts runs **low**, is **expired** or was **opened too
  long**.

From the workstation, **Prepare the Orders** puts the boxes to order into one
basket per pharmacy at once. A box already on an open order is not proposed
again.

:::{admonition} No pharmacy chosen
:class: warning

A resident with no pharmacist and no house's pharmacy cannot be ordered for:
the **Pharmacy** tab of the workstation shows **No pharmacy chosen**, with the
number of residents, and opens the settings.
:::

## The order, step by step

An order goes through four steps, shown at its top: **To Order** → **Sent** →
**Seen by the Pharmacy** → **Arrived** (or **Withdrawn**).

<!-- screenshot to add: pharmacy order form with its step bar, the basket banner and the lines -->

### 1. Check the basket

Open the basket from the workstation (**Baskets** or the **Pharmacy** tab). Each
line shows the resident, the medicine, the dose, **Why** (*First box*,
*Missing*, *Missing from a delivery*, *Running low*, *Expired*, *Opened too
long*), **Said By**, the number of **Boxes** and **Mandate Signed**.

A red line has no mandate: the **Mandates To Sign** smart button lists the
residents concerned. Add a **note** for the pharmacist if needed (a delivery
hour, a substitution refused…).

### 2. Send it

Where a secure channel to the pharmacy takes the basket without a hand, the
banner says when it **leaves for the pharmacy by itself**: every morning from
the hour set in **The pharmacy's basket leaves at**, the lines without a mandate
waiting apart. An e-mail never leaves by itself. To send the order yourself:

- **Send by E-mail** — when the pharmacy has an e-mail address; the order is
  attached as a PDF;
- **Mark as Sent** — the order was phoned, faxed or handed over.

**Print** gives the order; **Medication Sheets** prints the medication sheet of
the residents on the order. **Cancel** withdraws it.

### 3. Follow it

The order is **Sent**; where the channel returns a read receipt, it becomes
**Seen by the Pharmacy** once the pharmacy has opened it. The treatment says
where its box is (**At the Pharmacy**).

### 4. Receive the delivery

At the delivery, tick **Not in the Delivery** on what did not come, then click
**Everything Arrived**. What did not come goes back into the basket as
*Missing from a delivery*. For a box the house counts, type the **Units
Received** first: they fill the resident's box.

:::{admonition} In Belgium
:class: rh-country rh-country-be

The order leaves sealed by eHealthBox to the pharmacy, with the medication
schedule, and the pharmacy's answer is attached to it; the pharmacy can also
send its stock and its invoice: see [The pharmacy link](../belgique/medicaments-lien-pharmacie.md).
:::

## The pharmacy's sachets

When the pharmacy prepares the medicines in a sachet per moment, the sachets
are received and followed per resident. See [Pillboxes and the pharmacy's
sachets](piluliers.md).

## Going further

- [Treatments](traitements.md)
- [Pillboxes and the pharmacy's sachets](piluliers.md)
- [Medicines](index.md)
