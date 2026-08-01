# Room housekeeping

:::{rh-description}
The housekeeping board in Resthome: track the cleaning stage of each room — to prepare, to clean, in progress, ready — independently of who occupies it.
:::

:::{rh-faq}
Where do I see the rooms to be cleaned in Resthome?
: In the Accommodation app, on the Housekeeping board. It shows one column per stage — To prepare, To clean, In progress, Ready — and you move a room from one to the next by drag and drop.

Is the housekeeping stage the same thing as the room being occupied?
: No, and that is deliberate. An occupied room can perfectly well be "to clean", and a free room is not usable until it is "ready". The two states are tracked separately.

Does Resthome set the housekeeping stage automatically?
: It sets the starting point: a room goes to "To prepare" when a resident is due to arrive, and to "To clean" on departure. From there the housekeeping team moves it on its own board.

Why do empty columns still appear on the board?
: Because an empty "To clean" column is the useful signal that nothing is pending. Every stage stays visible, even with no room in it.
:::

A room has **two independent states**: who occupies it, and where it stands in
the **housekeeping** cycle. Resthome tracks them separately, because they answer
two different questions.

Menu: **Accommodation → Housekeeping**.

:::{admonition} Why two separate states
:class: note

An **occupied** room can still be *to clean*, and a **free** room is not usable
until it is *ready*. Merging the two would hide exactly the case that matters:
a room that looks available but is not yet.
:::

## The four stages

| Stage | Meaning |
|---|---|
| **To prepare** | A resident is due to arrive; the room must be made ready. |
| **To clean** | The room has been vacated and awaits cleaning. |
| **In progress** | Cleaning under way. |
| **Ready** | The room can receive a resident. |

## How a room moves through them

Resthome sets the **starting point** automatically:

- an **arrival** puts the room in *To prepare*;
- a **departure** puts it in *To clean*.

From there, the housekeeping team drives the board itself, by **drag and drop**
from one column to the next. A **Mark ready** button closes the cycle in one
click.

:::{admonition} Empty columns stay visible
:class: tip

Every stage keeps its column, even with no room in it. An empty **To clean** is
not noise — it is the signal that nothing is pending.
:::

## Key takeaways

- Housekeeping is **independent of occupancy**: the two are tracked separately.
- Arrivals and departures set the **starting point**; the team moves the rest.
- The board is driven by **drag and drop**, with **Mark ready** as the shortcut.

## Further reading

- [Rooms and occupancy](chambres.md)
- [Move-in procedure](procedure-emmenagement.md)
- [Condition report](etat-des-lieux.md)
