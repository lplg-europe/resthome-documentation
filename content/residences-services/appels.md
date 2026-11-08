---
howto_auto: true
modules: [serviced_living_call]
---

# Calls and duty rota

:::{rh-description}
Keep the call register of a serviced residence: when a resident called, why, who answered, how fast and what came of it, with the duty rota that says who answers.
:::

:::{rh-faq}
Where is the call register?
: In **Serviced Living → Calls**. Each call keeps when it came, who answered, the delay in minutes and what came of it.

Is the call system connected?
: No. Calls are entered by hand, at the desk or from the phone of whoever is on duty.

Why can I not close a call?
: When the regime keeps a call register, a call is only closed once it is answered and its follow-up is written.

Who is proposed as the person on duty?
: The person whose shift in the **Duty rota** covers the moment of the call. Without a rota, the person who presses **Answered now** is recorded.

How do I take a call from my phone?
: In the care app, open the **Residence** tab, then **New call**. See the page on the Residence tab of the care app.
:::

Some regimes ask the residence to keep a **register of calls for help**: the day,
the hour, the delay before an answer and what came of it. The **Calls** menu is
that register, and the **Duty rota** says who answers.

:::{admonition} A separate module
:class: note

The **Calls**, **Requests** and **Duty rota** menus appear once the calls and
requests module of the Serviced Living application is installed.
:::

## 1. Plan the duty rota

In **Serviced Living → Registers → Duty rota**, add one line per shift:
**Residence**, **On duty**, **From**, **Until** and a **Note**.

The residence form then shows **On duty now**. When the residence keeps a rota
and nobody's shift covers the present moment, it warns: *Nobody is on duty right
now.*

## 2. Record a call

In **Serviced Living → Calls**, click **New**:

- **Resident**, **Residence** and **Unit**;
- **Nature** — **Help**, **Health**, **Technical**, **Company**, **False alarm**
  or **Other**;
- **Called at** — now by default;
- **On duty** — proposed from the duty rota.

## 3. Answer and close

1. Click **Answered now** when someone answers. **Answered at** is filled in and
   the **Delay (minutes)** is worked out.
2. Write the **Follow-up**: what was done, who was told.
3. Click **Close**. The call becomes **Closed**; **Reopen** puts it back to
   **Open**.

<!-- screenshot to add: a call form with its nature, the person on duty, the answer time, the delay and the follow-up -->

:::{admonition} When the regime keeps a register
:class: warning

When the regime ticks **Call register required**, a call cannot be closed
without its answer time and its follow-up. The message names the calls still
incomplete.
:::

## Reading the register

The list shows the calls with their nature, the person on duty, the answer time,
the delay and the follow-up. The filters **Open** and **Unanswered**, the
**Date** filter, and the groupings by **Nature** and **On duty** answer the usual
questions of an inspection. The residence's **Open calls** smart button opens
the calls still open there.

## Going further

- [Service requests](demandes.md)
- [The Residence tab of the care app](app-terrain.md)
- [Regimes](regimes.md)
