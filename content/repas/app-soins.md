---
modules: [resthome_meal_mobile]
sectors: [mr, csj]
---

# Meals and drinks in the care app

:::{rh-description}
Record the meal round and the residents' drinks on a phone with the WideCare care app: served, refused, later, absent, the amount eaten and each glass.
:::

:::{rh-faq}
Who sees the Meals and Hydration screens in the care app?
: Everyone allowed to record the meal round or to log a drink: carers, nurses and, when their role allows it, kitchen and housekeeping staff. Without that right, the cards and the buttons do not appear.

Why is the Meals screen empty?
: The places are laid when the kitchen confirms its menu. As long as the menu is a draft, the screen says the kitchen has not confirmed it yet.

How do I mark a resident served?
: Swipe the resident's line to the right. Swipe to the left for **Refused**, or press and hold the line for every other choice.

Does it work without Wi-Fi?
: Yes. What you record is kept on the phone, marked **On this phone**, and sent when the connection comes back, with the hour of your gesture.

Is a drink given with the meal counted in hydration?
: Yes. When you note the amount eaten, you can add the glass drunk with it: it is written in the resident's fluid chart.
:::

Whoever serves the meal or brings the drinks has a phone in hand, not the desk.
The [care app](../soins-mobile/index.md) has two screens for them: **Meals**,
for the meal round, and **Hydration**, for the drinks. Everything recorded
there lands in the same records as the desk: see [The meal
round](distribution.md).

## The cards of the shift screen

On the shift screen, two cards sit beside the cares and the doses:

- **The meal card** — before and during the meal, the number of places still
  **to serve** for the meal of the hour; once the meal's hour has passed, the
  **Amounts to note** for the residents followed for nutrition. It says **not
  confirmed by the kitchen** while the menu is a draft.
- **Hydration** — the number of residents **without a drink today**.

Each card appears only for someone allowed to record there. Neither is ever
red: a meal to serve at noon is the work of the shift, not an emergency.

## The Meals screen

Open it from the meal card. At the top:

- the sector button, to show one sector or the whole house;
- the **meals of the day**, the one of the hour already chosen;
- the dishes of the menu, with its alternatives;
- the counts: to serve, served, absent, and the amounts still to note;
- **Dining room**, **Room** or **All**, to show where the meal is eaten;
- **Serve all**, to mark everyone at the table served in one go. The absent,
  the residents away, the plates put off to later and the plates with a
  critical dietary alert are left out.

Then three lists, in the order of the round: **To serve**, **Served**, **Absent**.

### What each line shows

- the resident, with their photo and room;
- the **texture** (highlighted when it is a modified one), the **diet** codes,
  the help needed at the table, the medical devices (stoma, gastric tube) and
  the **food allergies**;
- the **Nutrition** cares of the period, done or to do, with the carer assigned
  (for example **Meal assistance** or **Intake monitoring**);
- what the resident does not like;
- in **red** only, a critical dietary alert: the plate must be changed before
  it is put down; a warning appears in plain text;
- the plate, only when it is not the menu's;
- the state: served at what hour and how much, refused and why, later.

### Recording a plate

- **Swipe right** — **Served**.
- **Swipe left** — **Refused**: choose why (**Not hungry**, **Does not like
  it**, **Nausea / unwell**, **Asleep**, **Other**); **Other** needs a word.
- **Press and hold** — every other choice the plate allows: **In room** or
  **Dining room**, **Refused**, **Later** (stays to serve, with an optional
  reason), **Absent**, **Change dish**, **Note the amount**, **Undo**.

**Change dish** only offers the dishes of the menu, alternatives included, that
raise **no warning** for this resident. If none suits, ask the kitchen.

After each act, a message offers **Undo** for a few seconds.

### Noting the amount eaten

After the meal, a served line without an amount shows **Note the amount**. The
button is large when the amount is owed (resident followed for nutrition,
marked **To note**), smaller when it is optional.

1. Tap **Note the amount**.
2. Choose the amount: **0**, **¼**, **½**, **¾** or **1** (the whole plate).
3. Optionally add **A drink with it**: the kind of drink and the glass
   (100, 150, 200 or 250 ml).
4. Add a word if needed, then tap **Save**.

The sheet says beforehand which care it closes (for example the **Intake
monitoring** care of the period). If the resident refused, tap **Refused? give
the reason** instead.

<!-- screenshot to add: Meals screen of the care app with the three lists and a line with its texture and diet chips -->

## The resident's meal sheet

On a resident's sheet in the care app, the diets and the texture appear next to
the allergies, and two buttons open:

- **Meals** — the resident's meal sheet:
  - a banner when something needs attention: intake or fluids below target these
    last days (**Tell the nurse**), a resident followed for nutrition (note every
    amount), or nothing recorded yet;
  - **Today** — each meal of the day with its state, hour and dishes, and
    **Open the meal round**;
  - **Intake of the day** — energy, protein and fluids against the resident's
    targets, and the coverage of the last 3 days;
  - **At the table** — texture, diets, food allergies, help needed, dislikes
    and likes.
- **Drink** — the resident's drinks of the day (see below).

## The Hydration screen

Open it from the **Hydration** card. The chips **All**, **No drink yet** and
**Below target** narrow the list.

Each line shows what the resident drank today against their target, the hour of
the last drink and, in amber, **Below target these last days**.

- **One tap is one glass**: tap 100, 150, 200 or 250 ml. The glass is recorded
  with the hour of the tap.
- The drink button next to the glasses sets the **kind of drink** when it is not
  water (coffee or tea, juice, milk, soup, oral supplement…).
- **Press and hold** a glass for another amount or another drink, with an
  optional word, then **Record**.

### One resident's drinks

From the resident's sheet, **Drink** opens their drinks of the day, newest
first:

- **swipe left** on a line to **Delete** it;
- **press and hold** to **Edit** it: amount, kind of drink, the hour (**Drunk
  at**, with − and + by 5 minutes) and a word, then **Save**.

You can delete or edit your own lines of the day; someone allowed to delete any
line of the fluid chart can change all of them. Right after a tap, **Undo**
takes the last glass back. **Every resident** brings back the whole
list.

:::{admonition} Drinks and hydration rounds
:class: note

A glass marks done the **Hydration round** care of its period. Deleting or
moving that glass opens the round again, unless another glass of the period
answers it.
:::

## From a care to the right screen

In the care app's task list, a **Hydration round** care opens the resident's
drinks, and an **Intake monitoring** care opens the meal round, where the amount
eaten is noted.

## Going further

- [Care app](../soins-mobile/index.md)
- [The meal round](distribution.md)
- [Food textures (IDDSI)](textures.md)
- [Nutritional monitoring and undernutrition](suivi-nutritionnel.md)
