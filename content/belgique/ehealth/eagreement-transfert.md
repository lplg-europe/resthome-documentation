---
howto_auto: true
---

# Internal transfer (MR ↔ MRS)

:::{rh-description}
Move a resident between sectors (MR, MRS, day care) in Resthome: the internal transfer assistant closes the stay, opens the new one and produces the two annexes the insurer expects.
:::

:::{rh-faq}
How do I move a resident from MR to MRS?
: From their current stay, use Internal Transfer. The assistant ends the stay, opens the new one in the destination sector and creates the two eAgreement requests the insurer expects: an end-of-stay notice (Annexe 11) then a new intervention request (Annexe 7).

Why can't I just change the sector on the stay?
: Because a bare edit produces no document for the insurer. The sector field is read-only on purpose: only the transfer assistant generates the Annexe 11 / Annexe 7 pair that makes the change official.

Can I transfer a resident to MRS with any Katz category?
: No. MRS requires category B or higher. If the latest assessment is O or A, the assistant refuses and tells you to record a new Katz assessment or to pick MR as the destination.

Do I have to change room to transfer a resident?
: No. The room defaults to the current one — the same room simply gets reclassified. Change it only if the resident physically moves.
:::

A resident whose condition changes may move from **MR** to **MRS** (or the other
way round, or to day care). For the insurer this is not a detail of internal
organisation: it ends one intervention and starts another, and it takes **two
documents** to make it official.

Resthome does it in one step: from the resident's current stay, open **Internal
Transfer**.

:::{admonition} Why the sector field is read-only on the stay
:class: important

You cannot change the sector by editing the stay directly. A bare edit would
change your records while the insurer still believes the resident is in the old
sector — and would produce **no annexe**. The assistant is the only path that
generates the pair of documents.
:::

## What the assistant asks

| Field | What to do |
|---|---|
| **Destination type** | MR, MRS or day care. Defaults to the opposite of the current sector. |
| **New room** | Defaults to the current room — the same room simply gets reclassified. Change it only if the resident physically moves. |
| **Transfer date** | Ends the current stay and starts the new one, on the same day. |
| **Transfer time** | The moment of the handover. It appears on the end-of-stay annexe (*"at … hours"*). |
| **With Katz category change** | Tick this when the transfer comes with a new assessment, then pick or create it. |

## What it produces

In a single operation the assistant:

1. **ends** the current stay, with *transfer* as the departure reason, the time
   you entered, and the destination sector;
2. **opens** the new stay in the destination sector, starting at that same
   moment;
3. creates the **two eAgreement requests**, in order: an **end-of-stay notice**
   (Annexe 11) for the sector being left, then an **intervention request**
   (Annexe 7) for the sector being entered.

The INAMI intervention of the old stay ends at the transfer moment, so no day is
billed twice.

:::{admonition} Exactly two documents, not four
:class: note

Ending a stay and opening one normally each trigger their own eAgreement
request. During a transfer, Resthome suppresses those automatic requests — you
get exactly the two transfer documents, in the right order, and nothing else.
:::

## What the assistant refuses

**A transfer that changes nothing.** If the destination sector and the room are
both identical to the current stay, the assistant refuses: it would close a live
stay and reopen an identical one, and cancelling that new stay afterwards would
leave the resident with no stay at all. It tells you what you probably meant:

- another sector → pick it in the assistant;
- another room, same sector → use **Change Room**;
- the **short-stay** flag → tick it directly on the stay, it is a modality, not
  a transfer.

**MRS below category B.** MRS requires a Katz category of **B or higher**. If the
resident's latest validated assessment is **O** or **A**, the assistant stops
before touching anything and asks you either to record a new assessment (tick
*With Katz category change*) or to set the destination to MR.

**A transfer already done.** If the stay is no longer active, the assistant
refuses rather than creating a duplicate destination stay. Start any new transfer
from the resident's current active stay.

## Cancelling a transfer

If you cancel the stay a transfer opened, the transfer never happened — and the
two annexes it created must not stay in the queue waiting to declare a move to
the insurer that will not take place.

Resthome cleans up on its own, but the rule depends on whether the annex has
already left:

- **Still in draft** — the pair is **removed**, and the resident's thread records
  it: *"Internal transfer cancelled — its draft eAgreement requests were
  removed."*
- **Already sent** — the annex is **left alone**, and the thread warns you:
  *"Internal transfer cancelled, but … was already sent to the OA."*

:::{admonition} A sent annexe is retracted with the insurer, not in the software
:class: warning

Resthome will never silently delete a declaration the insurer has already
received. If the transfer annexe went out and the transfer is cancelled, the
insurer holds a move that did not happen: **contact them** to correct it. The
same rule applies when you reopen a stay whose end-of-stay annexe was already
sent — Resthome then refuses the reopening outright rather than leaving a
contradiction.
:::

Only the pair created with that stay is touched. A request belonging to an
earlier transfer of the same resident is never affected, and the cleanup never
blocks the cancellation itself.

## Further reading

- [Agreements (eAgreement Light)](eagreement.md) — the requests the transfer creates.
- [Following a request](eagreement-suivi.md) — deadlines and the insurer's decision.
- [Room change and transfer](../residents/changement-chambre.md) — moving room within the same sector.
- [The Katz assessment](../residents/katz.md) — the category that conditions MRS.
