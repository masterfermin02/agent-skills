---
name: meal-log
description: "Log food and drinks for Fermin into the fitness food log. Use whenever Fermin mentions eating, drinking, or having any food/beverage — including meals, snacks, protein shakes, coffee, water, or any item with nutritional value. Triggers on: 'I ate', 'I drank', 'I had', 'log this', 'I just ate', mentions of specific foods (eggs, rice, chicken, Huel, coffee, banana, etc.), or sending a photo of food. Also use when asked for today's nutrition summary or protein/calorie totals."
---

## Food Log File
`/home/node/.openclaw/.openclaw/workspace/fitness/db/food-log.json`

## Profile
- **Goal:** Fat loss, natural bodybuilding
- **Daily protein target:** 150g
- **Timezone:** Colombia (UTC-5)

## Log Entry Format
Append to `log[]` array:
```json
{
  "date": "YYYY-MM-DD",
  "meal": "<breakfast|lunch|dinner|snack|coffee|pre-workout|post-workout>",
  "time": "HH:MM",
  "foods": [
    { "item": "description", "protein": 0, "carbs": 0, "fat": 0, "calories": 0 }
  ],
  "totals": { "protein": 0, "carbs": 0, "fat": 0, "calories": 0 },
  "notes": "optional"
}
```

## Common Items (quick reference)
| Item | Protein | Carbs | Fat | kcal |
|---|---|---|---|---|
| Scrambled egg (1) | 6g | 1g | 5g | 70 |
| Arepa colombiana (1) | 3g | 20g | 2g | 110 |
| Banana (1 medium) | 1g | 27g | 0g | 105 |
| White rice (1 cup) | 4g | 45g | 0g | 200 |
| Grilled chicken (150g) | 35g | 0g | 5g | 185 |
| Red beans (1 cup) | 8g | 35g | 1g | 180 |
| Huel Black (1 serving) | 40g | 28g | 16g | 400 |
| Black coffee + sugar (1 tsp) | 0g | 4g | 0g | 16 |
| Avocado (1/4) | 1g | 3g | 7g | 80 |
| Sweet plantain (1) | 1g | 30g | 0g | 120 |
| Fried egg (1) | 6g | 0g | 5g | 70 |

For unlisted items, estimate macros based on standard nutritional values.

## Workflow
1. Parse what Fermin said/sent (text or image)
2. Identify foods and quantities
3. Look up macros (use table above or estimate)
4. Calculate totals for the entry
5. Append entry to `log[]` in the JSON file
6. Reply with: logged item + running daily totals (kcal / protein)
7. Note how far from 150g protein target

## Daily Summary
When asked for summary, sum all entries for today and show:
- Total kcal
- Total protein vs 150g target
- Remaining protein needed
