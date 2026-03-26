---
name: rental-finder
description: "Find and compare apartments, studios, lofts, monthly stays, Airbnb listings, and short-term rentals based on budget, dates, neighborhood, living preferences, and work/lifestyle priorities. Use when searching for housing, furnished apartments, temporary rentals, Airbnb options, Medellín neighborhoods, work-friendly stays, gym-friendly stays, or when ranking rental options and spotting red flags or scams."
compatible_agents:
  - claude-code
  - cursor
  - windsurf
  - github-copilot
  - opencode
tags:
  - housing
  - apartment-search
  - rentals
  - airbnb
  - medellin
  - short-term-stay
---

Use this skill to search, compare, and rank rental options.

## Goal
Turn vague housing requests into a clear shortlist.

## First questions to resolve
Ask or infer:
- city
- dates
- budget
- solo or shared
- entire place or room
- furnished or not
- kitchen required?
- washer required?
- neighborhood preferences
- priorities: gym, workspace, safety, internet, quiet, nightlife, transit

## Workflow
1. Clarify the constraints.
2. Pick the right platform(s): Airbnb, Booking, Facebook Marketplace, Finca Raíz, local groups, etc.
3. Search with filters.
4. Shortlist the best candidates.
5. Rank by actual fit, not just price.
6. Flag risks and tradeoffs.

## Ranking criteria
Prioritize according to the user’s goals:
- budget fit
- entire place vs shared
- neighborhood quality
- internet/work suitability
- gym access / walkability
- reviews / trust signals
- monthly discount or fee structure
- noise / safety / practicality

## Red flags
- too cheap for the zone
- very few or weak reviews
- vague location
- poor/no bathroom or kitchen photos
- hidden fees
- pressure to pay outside platform
- unclear internet quality
- street-noise warnings for work-focused stays

## Platform notes
### Airbnb
- Good for short furnished monthly stays
- Often more expensive
- Reviews and monthly discounts are useful
- JS-heavy; browser automation may be needed for real search extraction

### Local sites / Facebook / classifieds
- Better for tighter budgets
- More scam risk
- Validate location, photos, owner/host, and payment flow carefully

## Medellín-specific guidance
For work-friendly temporary stays under moderate budgets, consider:
- Laureles
- Estadio
- Floresta
- La América
- Belén

Use extra caution with unfamiliar sectors if the user values comfort and easy daily life.

## Output format
Return:
1. best-fit option
2. backup options
3. why they rank there
4. risks/tradeoffs
5. next action

## Read references when needed
- Read `references/medellin.md` for Medellín neighborhood logic.
- Read `references/checklist.md` for rental screening and comparison rules.
