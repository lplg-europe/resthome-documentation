---
modules: [healthcare_work_entry_attendance]
sectors: [mr, csj]
---

# Work entries from attendances

:::{rh-description}
Draw each employee's work entries from their attendances instead of their working schedule, with approved extra hours as a work entry of their own.
:::

:::{rh-faq}
What does "work entries from attendances" change?
: For the employees concerned, the work entry of a day is the time between their check-ins and check-outs of that day, instead of the hours of their working schedule.

Is the lunch break deducted?
: No. An employee counted from attendances clocks out and back in for the break; nothing else is deducted.

How are extra hours counted?
: The extra hours of the Attendances app are taken out of the attendance work entry. Once approved, they come back as a work entry of the type chosen on the employee; refused or still to approve, they are not counted.

What happens to time off and public holidays?
: They keep the hours of the working schedule, as before.

Can I change the attendances of a day already validated?
: The work entries of a day that holds a validated work entry are not regenerated.
:::

By default, an employee's **work entries** follow their **working schedule**:
the hours they are supposed to work. For staff whose hours vary from day to day,
WideCare can draw the work entries from the **attendances** they clock instead.

:::{note}
This option is for databases on the Community edition of Odoo. The Enterprise
edition has its own attendance-based work entries.
:::

## Count an employee from their attendances

1. Open the employee's record, tab **Payroll** (HR managers).
2. In **Work Entries From**, choose **Attendances**.
3. In **Overtime Work Entry Type**, choose the type the approved extra hours
   become. Leave it empty to count every hour attended as attendance
   (*Counted as attendance*).

From then on:

- the attendance work entry of a day is the time between the check-ins and
  check-outs of that day; **nothing is deducted for lunch**, the employee clocks
  the break; the Attendances app reads these employees the same way;
- the **extra hours** computed by the Attendances app are taken out of the
  attendance work entry; **approved**, they become a work entry of the
  overtime type; refused or still to approve, they are not counted;
- **time off** and **public holidays** keep the hours of the working schedule;
- a check-in, a check-out, a corrected attendance or an approved or refused
  extra hour **regenerates the work entries of its day**, unless that day holds
  a validated work entry.

<!-- screenshot to add: Payroll tab of an employee with Work Entries From set to Attendances and the Overtime Work Entry Type -->

## Read the work entries

The **Employees** app gets a **Work Entries** menu (HR officers), with:

- **Work Entries** — the work entries of every employee;
- **Work Entry Types** — the types they use, the overtime type included.

## Learn more

- [Hours, balance and coverage](heures-et-couverture.md)
- [Staff planning](index.md)
