---
modules: [resthome_meal]
sectors: [mr, csj, rs]
---

# Food textures (IDDSI)

:::{rh-description}
Give each resident with swallowing difficulties the right IDDSI texture, say in which textures each dish can be prepared, and let WideCare flag a plate that is too coarse.
:::

:::{rh-faq}
What is a texture, compared with a diet?
: A diet says what the food contains (no sugar, no salt…). A texture says how it is prepared: regular, minced and moist, pureed, or a thickened drink. Each resident has one texture and may have several diets.

Which textures does WideCare provide?
: The eleven levels of the IDDSI framework, from **Thin** (level 0) to **Regular** (level 7). You can add your own in **Meals → Configuration → Textures**.

What happens if a dish is not available in a resident's texture?
: If the dish is only offered in a coarser texture, WideCare raises a critical alert (choking risk) and refuses to mark the plate as served. If it is only offered in a finer texture, it shows a warning.

Where do the carers see the texture?
: On the printed distribution sheet, on each line of the meal round in the care app, and on the resident's sheet in the app.
:::

The **texture** says how a resident's food is prepared or their drinks
thickened. WideCare follows the **IDDSI** framework (International Dysphagia
Diet Standardisation Initiative): levels 0 to 4 for drinks, 3 to 7 for food.
Each resident has **one** texture; each dish says in which textures it can be
served.

## The textures provided

| Level | Drinks | Food | Colour |
| --- | --- | --- | --- |
| 0 | **Thin** | | White |
| 1 | **Slightly Thick** | | Grey |
| 2 | **Mildly Thick** | | Pink |
| 3 | **Moderately Thick (drink)** | **Liquidised (food)** | Yellow |
| 4 | **Extremely Thick (drink)** | **Pureed (food)** | Green |
| 5 | | **Minced & Moist** | Orange |
| 6 | | **Soft & Bite-Sized** | Blue |
| 7 | | **Easy to Chew**, **Regular** | Black |

**Regular** is the ordinary texture, given by default to every new resident. The
others are **modified** textures: only those are flagged to the kitchen and on
the printed sheets.

## Setting up the textures

**Meals → Configuration → Textures** lists the textures in IDDSI order. On a
texture:

- **Code** — the IDDSI code (TN0, ST1, MT2, MO3, LQ3, EX4, PU4, MM5, SB6,
  EC7, RG7). It must be unique.
- **IDDSI Level** and **IDDSI Kind** (**Drink** or **Food**).
- **IDDSI Colour** — set from the level; it is the colour of the tray label.
- **Modified Texture** — untick it only for the ordinary texture.
- **Description** — how the kitchen prepares it.
- The **Residents** button lists the residents on that texture.

You can add a texture of your own. Archive a texture rather than deleting it: a
texture still given to a resident cannot be deleted.

## Giving a resident their texture

1. Open the resident, tab **Nutrition**, block **Diets and Textures**.
2. Choose the **Texture**.

The nurse can also change it from the **Nutrition** tab of the care plan: it is
the same field, and the change is written in the plan's history.

## Dishes and textures

On a dish, **Available Textures** lists the textures the kitchen can prepare it
in. Left empty, the dish is offered in **every** texture. See [Dishes and
nutritional values](plats.md).

For each place laid, WideCare compares the dish with the resident's texture:

| Situation | Result |
| --- | --- |
| The dish is offered in the resident's texture, or in every texture, or the resident has the ordinary texture | Nothing |
| The dish is only offered in a **finer** texture (lower level) | Warning: served smoother than needed |
| The dish is only offered in a **coarser** texture | **Critical alert**: choking risk |

:::{admonition} Choking risk
:class: warning

A plate with a critical texture alert **cannot be marked as served**, at the
desk or in the care app. Choose another dish: **Compatible Dishes** on the meal
service, or **Change dish** in the care app, only offers dishes without a
warning.
:::

## Where the texture appears

- On the **printed distribution sheet**, next to the diets, when the texture is a
  modified one.
- In the care app, on each line of the **Meals** screen (highlighted when it is a
  modified texture), on the resident's sheet next to the diets, and in the **At
  the table** block of the resident's meal sheet. See [Meals and drinks in the
  care app](app-soins.md).

:::{admonition} Homes that used the former texture list
:class: note

The textures of the former list were converted to IDDSI on update: normal
became **Regular**, soft became **Easy to Chew**, chopped became **Minced &
Moist**, pureed became **Pureed (food)** and liquid became **Thin**. The former
mashed texture was merged into **Pureed (food)** and archived, and each resident
concerned has a note on their record. Check that each resident's texture is
still the right one. Textures your home created itself are left unchanged.
:::

## Going further

- [Menus, diets and allergies](menus-regimes.md)
- [The meal round](distribution.md)
- [Meals and drinks in the care app](app-soins.md)
