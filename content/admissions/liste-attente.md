---
modules: [healthcare_accommodation]
sectors: [mr, csj, rs]
---

# The waiting list

:::{rh-description}
The waiting list in WideCare: the open admission requests, the rooms that free up on a known date, and the waiting-list rooms that hold a family's place until a bed is free.
:::

:::{rh-faq}
Which requests are on the waiting list?
: Every admission request still open: not admitted, not refused or withdrawn, not given up. The **Waiting list** filter of the pipeline shows them.

Can I admit someone into a room that is still occupied?
: Yes, when the room frees up on a known date. The admission offers it with that date, and moves the stay start to the first free day.

What is a waiting-list room?
: A placeholder room, one per room type, that holds the families who accepted a price before any bed of that type is free. It never fills up and nobody moves into it.

How do I create the waiting-list rooms?
: In **Nursing Home → Accommodation → Rooms**, list view, click **Create waiting-list rooms**. A manager creates one per room type in one click; pressing it again only adds the missing ones.

How does the person leave the waiting-list room?
: When a real bed frees up, open their stay and use **Change Room** to move them into it.
:::

A family asks for a place months before a bed is free. WideCare keeps those
requests in the pipeline, shows which rooms free up and when, and lets you
record an admission before the bed exists.

## The open requests

In **Admissions**, the **Waiting list** filter shows the requests still open —
not admitted, not refused or withdrawn, not given up. Group them by **Room
type** to see who waits for which price.

A request leaves the waiting list on its own when the person is admitted, or
when you click **Give up** — see [Admissions](index.md).

:::{admonition} In Belgium
:class: rh-country rh-country-be

The insurability of the whole waiting list can be checked with the mutualities
in one go (**Check insurability (MDA)** on the selected requests); a death
reported by the mutuality closes the request. See [Admitting a resident in
Belgium](../belgique/admission.md).
:::

## Rooms that free up on a known date

A room is full today, but its resident leaves on a known date — a planned
departure, a planned room change. That room is exactly what a waiting family
asks about:

- in **Nursing Home → Accommodation → Rooms**, the **Frees up (date known)**
  filter lists those rooms, and **Planned Departure** groups them by date;
- the list shows the **Planned Departure** column, and the room record its date;
- in every room picker (admission, room change), such a room reads **frees up**
  followed by the first free day.

When you choose such a room in the admission wizard, the **Stay start date**
moves forward to the first free day. A room whose next departure is already
taken by another admission is no longer offered.

## Waiting-list rooms

A waiting-list room is a **placeholder**: one per room type, because what a
family accepts in advance is the price, not a room number. It never fills up,
and its record shows **People waiting** instead of a capacity.

### Creating them

1. Open **Nursing Home → Accommodation → Rooms** and switch to the **list**
   view.
2. Click **Create waiting-list rooms** (managers only).

WideCare creates one waiting-list room per room type that has real rooms behind
it. Pressing the button again, after creating a new price, adds only the
missing ones.

:::{note}
A waiting-list room is never put **to prepare** or **to clean** on the
housekeeping board, and it is never offered as the target of a room change:
nobody lives there.
:::

### Admitting onto the waiting list

1. In the admission wizard, choose the **waiting-list room** of the room type
   the family accepted — see [Admitting a candidate](admettre.md).
2. Use the **Notes** of the wizard for what was agreed — for example the floor
   or the type of room the family wants. They are copied into the stay's
   admission reason, where the team reads them.
3. Click **Admit**.

The person becomes a resident, **Expected**, with a confirmed stay on the
waiting-list room.

### Moving into a real room

When a bed of the right type frees up:

1. Open the person's stay.
2. Click **Change Room** and choose the real room.
3. Confirm.

The stay moves into the room — see [Room change and
transfer](../residents/changement-chambre.md).

## What's next

- [Admitting a candidate](admettre.md)
- [Rooms and occupancy](../residents/chambres.md)
- [Room change and transfer](../residents/changement-chambre.md)
