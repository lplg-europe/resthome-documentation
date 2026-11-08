---
modules: [resthome_helpdesk]
sectors: [mr]
---

# Billing an intervention

:::{rh-description}
Billing the cost of a technical intervention to the resident in Resthome: the Bill the intervention button, the line added to the supplement envelope, and the price kept up to date.
:::

:::{rh-faq}
At what price is an intervention billed?
: At its **Ticket Cost**: products, time spent and vendor bill. The price of the service product does not matter.

On which invoice does it appear?
: On the resident's supplement envelope of the current month, so on that month's invoice. When the current month is already invoiced, it goes to the next open month.

What if the cost changes after billing?
: The billed line follows the new cost as long as the month's envelope is open and the line not invoiced. The ticket notes each change.

Can an intervention be billed twice?
: No. Once billed, the button disappears and a **Billed** button opens the envelope it was billed on.
:::

Billing an intervention is a **decision of the administration**: by default, an
intervention is only valued. When the home decides the resident pays for it,
one click adds its cost to the resident's monthly supplements.

## Setting

In **Helpdesk → Configuration → Helpdesk Teams**, on the room maintenance team,
under **Rooms maintenance**: **Intervention Service Product**. It is the service
that carries the intervention on the resident's envelope. Resthome provides one,
**Technical Intervention**. It is set at installation on the room maintenance
teams that had none; for a team you turn on later, choose it yourself.

:::{admonition} VAT
:class: note

The service product keeps the company's usual sales taxes. On the resident's
envelope, the **Resident Fiscal Position** setting applies, as for every
supplement: see [Billing settings](../configuration/reglages-facturation.md).
:::

## Bill the intervention

On the ticket, click **Bill the intervention**. Resthome adds **one line** to the
resident's **supplement envelope**:

- the **Intervention Service Product** of the team;
- the ticket's reference and title as description;
- the **Ticket Cost** as price.

The envelope then opens, and the ticket's thread notes the billing. The
**Billed** button on the ticket leads back to it.

The billing is refused when:

- the ticket has no **Resident**;
- the team has no **Intervention Service Product**;
- the **Ticket Cost** is zero — add products, time or a vendor bill first;
- the resident has no active stay, so no envelope can be opened.

:::{admonition} Which month
:class: tip

The intervention goes on the envelope of the **current month**. When that month
has already been invoiced, it goes on the next month still open, rather than
being refused.
:::

## A cost that moves after billing

A timesheet added later, a vendor bill cancelled: the cost of the ticket moves.
The billed line follows it as long as the month's envelope is still **open**
and the line has not been invoiced. Each change is noted on the ticket, with the
old and the new amount.

Once the line is invoiced, or the month closed, the billed amount no longer
changes: what the resident was charged stays as it was.

## What's next

- [Following an intervention](suivre-une-intervention.md)
- [Supplements](../facturation/supplements.md)
- [Technical interventions](index.md)
