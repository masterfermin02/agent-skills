# Laravel Money Review Checklist

Use this when auditing a Laravel codebase.

## Red flags
- `float`, `double`, or `decimal` values used directly in business logic
- `number_format()` used before calculations finish
- raw `+`, `-`, `*`, `/` over price fields without money objects
- no currency column / hardcoded currency assumptions
- taxes/discounts calculated from floats
- inconsistent storage between tables

## Safer target state
- `cknow/laravel-money` installed
- money represented as value objects in Laravel models/services
- clear DB storage strategy
- clear API serialization
- explicit currency handling
- backend-owned formatted fields such as `amount_formatted`
- avoid frontend money-formatting duplication

## Migration approach
1. Identify every monetary column
2. Decide canonical storage format
3. Add or confirm currency source
4. Add casts
5. Move arithmetic into services/value-object-aware code
6. Update tests around rounding, taxes, totals, refunds

## What to suggest in reviews
- replace floats with money casts/value objects
- centralize total calculation rules
- add tests for rounding and discounts
- make currency explicit in schema and domain logic
