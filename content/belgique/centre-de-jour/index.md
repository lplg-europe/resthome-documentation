---
modules: [resthome_day_care, resthome_day_care_ehealth]
sectors: [csj]
---

# Day care centre (CSJ)

:::{rh-description}
The WideCare day care centre (CSJ): its own app, day places, attendance register, CSJ agreement, forfait and day price, staffing norm, care on attendance days.
:::

:::{rh-faq}
What is a day care centre in WideCare?
: A centre whose users live at home: they come for the day and go home at night. They hold a place in a day room, not a bed, and what they owe is decided by the days recorded in the attendance register.

Does a day care centre need the rest home application?
: No. A day care centre runs on its own, with its own approval and its own INAMI number. A house that runs both sectors has both, and a person moves from one to the other with an internal transfer.

Where do I find the day care screens?
: In the **Day care centre** app on the home screen: today's attendance, the register, the users, the stays, the figures and the centre's configuration.

What does the health insurer pay for a day care user?
: A daily forfait for each day that earns it: six hours at the centre with an arrival by noon, or a day cut short by a hospitalisation or a death. The amount is the same for every CSJ category, and the insurer must have agreed to the user's care.

What does the user pay?
: The centre's own day price, for every day recorded — a day that earns no forfait is still a day spent at the centre.
:::

:::{toctree}
:hidden:

configuration
admission
accord
presences
absences
facturation
norme-personnel
soins
rapports
:::

A **day care centre** (CSJ, *centre de soins de jour*) welcomes people who live
at home: they come for the day — two or three days a week, or every day — and
go home at night. WideCare runs it as a sector of its own, next to the rest
home or without it.

## The Day care centre app

The centre has its own tile on the home screen, **Day care centre**. Its menus
follow the day of the team at the door:

| Menu | What it opens |
| --- | --- |
| **Today's attendance** | The screen at the door: one card per user, one tap on arrival, one on departure. |
| **Register** | The **Day care register** (the days recorded), the **Unannounced absences** and **Print the day care register**. |
| **Day care users** | The files of the people who have, or had, a day care stay. |
| **Day care stays** | The CSJ stays: day place, start, end, transport. |
| **Reporting** | **Day care statistics** and **Places occupancy**. |
| **Configuration** | **Approval and opening days**, **Closures and public holidays**. |

**Reporting** and **Configuration** are shown to managers and to whoever may
amend a closed register day. The billing and the staffing norm stay in the
**Billing** app; when the centre runs without a rest home, that app is named
**Day Care Billing**.

### Who does what

Two access rights split the register:

- **Day care / Keep the register** ticks who came and when, at the door or on
  the list. Care assistants and the activity team hold it.
- **Day care / Amend a closed register day** corrects a past day, or an
  arrival after 13:00. The head nurse, the billing managers and the managers
  hold it. Every change is kept in the audit log.

## What changes compared with a rest home

| | Rest home (MR/MRS) | Day care centre (CSJ) |
| --- | --- | --- |
| Where the person is | A licensed **bed** | A shared **day place** |
| What counts the days | The stay, day after day | The **attendance register** |
| The forfait | Every day of presence | Each day that **earns** it |
| What the person pays | The accommodation price | The centre's **day price** |
| The agreement | Annexe 7, then Annexe 10 | **Annexe 14**, renewed every year |
| Absences | Declared, with their rebates | Declared or unannounced; a day not recorded is not billed |
| Categories | The rest home Katz categories | **F**, **Fp**, **Fd** or **D**, read from the same Katz evaluation |

## A day at the centre

1. In the morning, the users arrive: tap their card on **Today's attendance**
   before **13:00**, when the register closes to arrivals.
2. Care, tasks and medication are planned only for the users **expected**
   that day.
3. In the evening, tap their card again when they leave: the register says
   whether the day earns the forfait.
4. At the end of the month, the billing counts the days recorded: the
   **forfait** to the health insurer, the **day price** to the user.
5. Once a year, the **agreement** of each user is renewed, and the
   **staffing norm** says whether the forfait of the billing year is due in
   full.

## What's next

- [Setting up a day care centre](configuration.md) — the approval, the opening days, the day room, the rates and the day price.
- [Admitting a day care user](admission.md) — the stay, the days expected, the category, the move-in steps.
- [The day care agreement](accord.md) — the Annexe 14, the insurer's answer, the yearly renewal, the end of care.
- [Recording attendance](presences.md) — the screen at the door, the register, one day at a time, the 13:00 closure.
- [Absences and hospitalisation](absences.md) — a holiday, a day in hospital, a day nobody announced.
- [Billing a day care month](facturation.md) — the forfait, the day price, the supplements, the month nobody ticked.
- [The staffing norm](norme-personnel.md) — the yearly check and what it does to the forfait.
- [Care for a day care user](soins.md) — care plans, tasks and medication on the days the user comes.
- [Day care figures](rapports.md) — the billing board, the statistics, the places, the printed register.
