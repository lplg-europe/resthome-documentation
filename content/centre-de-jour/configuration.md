---
howto_auto: true
---

# Setting up a day care centre

:::{rh-description}
Setting up a day care centre (CSJ) in Resthome: the approval and opening hours, day places, CSJ forfait rates and the day price.
:::

:::{rh-faq}
Where do I enter the days the centre opens?
: On the CSJ approval of the establishment: Settings, Approvals, Manage establishments and approvals. Monday to Friday, 8:00 to 18:00, by default.

Why is a bedroom refused to a day care user?
: Because a bedroom is a licensed bed. A day care stay only goes in a day place, and a residential stay never does: tick Day Place on the room type of the day room.

Does the capacity of the day room limit the admissions?
: No. A centre enrols more people than it has places, and they share them day by day. The capacity is the number of places the room offers.

What if the day price is still 0.00 EUR when a user starts?
: Nothing is subscribed, and the user's file says so. Set the price on the product: every user who started in the meantime is subscribed at once, from their admission day.
:::

A day care centre needs five things before its first user: its approval, its
opening days, a day room, the amounts of the CSJ forfait and its own day price.

## 1. Record the CSJ approval

Go to **Settings → Approvals → Manage establishments and approvals**, open the
establishment of the day care centre and add its **CSJ** approval, with the
number of places it covers.

A day care centre has **its own INAMI number**: it is recorded on its
establishment, with its eHealth certificate — see
[eHealth and eFact settings](../configuration/reglages-ehealth.md).

## 2. Set the opening days and hours

On the CSJ approval, the **Opening days and hours** section says when the
centre opens: the days from **Monday** to **Sunday**, **Opens at** and
**Closes at**. It starts from Monday to Friday, 8:00 to 18:00 — the legal
floor.

- **Open Days / Week** counts the days ticked.
- **Below the Norm** lights up under five days a week, or with a window
  narrower than 8:00–18:00. It is said, never blocked: what the centre opens
  is its own to declare.

These days are read everywhere else: a day recorded in the register on a day
the centre is closed is flagged **Centre closed that day**, and a user with no
agreed days is expected on every day the centre opens.

:::{note}
Public holidays are not known yet: a holiday still reads as an open day.
:::

## 3. Create the day room

A day care user holds a **day place**, never a licensed bed.

1. Under **Configuration → Rooms → Room Types**, create the type of the day
   room and tick **Day Place**.
2. Under **Accommodation → Rooms**, create the room with that type, and the
   number of places as its **capacity**.

From then on:

- a day care stay only goes in a day place, and a residential stay never does;
- every room picker offers day places to a day care stay, and beds to the
  others;
- a day room reads « 15 day places » in the pickers, never « free beds »: the
  places are shared, and a centre enrols more users than it has places.

<!-- screenshot to add: the room type form with Day Place ticked -->

## 4. Fill in the CSJ rates

The health insurer pays a **daily forfait** per CSJ category. Under
**Billing → Configuration → INAMI Rates**, the grid carries one row per CSJ
category, each with its own **pseudo-code**:

| Category | Pseudo-code |
| --- | --- |
| F | 126036 |
| Fp | 126073 |
| D | 126095 |
| Fd | 126117 |

Enter the amount in force from its start date. The amount is the **same for
every category**: the category declares the user's profile to the insurer.

:::{warning}
A rate left at 0.00 EUR bills no forfait. Resthome never sends a claim at zero:
the month's generation says which users were left without one, and why.
:::

## 5. Set the centre's day price

What the user pays is the centre's **day price**: the product **CSJ Stay
Supplement** (SUPP-CSJ-STAY). Set its sales price.

- Each user is **subscribed automatically** when their stay starts, from the
  admission day.
- A user who follows the tariff follows its yearly **indexation** too.
- A price agreed with one user goes on their convention, with **Negotiated
  price** ticked: the indexation then leaves it alone. See
  [Supplements](../facturation/supplements.md).

## What's next

- [Admitting a day care user](admission.md) — the stay, the days expected, the category, the agreement.
- [Recording attendance](presences.md) — the register of the day, and one day at a time.
