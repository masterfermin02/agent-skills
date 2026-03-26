# Laravel Money Patterns

## Installation
```bash
composer require cknow/laravel-money
php artisan vendor:publish --provider="Cknow\Money\MoneyServiceProvider"
```

## Storage strategy
Prefer one of these and stay consistent:

1. **Integer minor units** (recommended)
   - `1999` = $19.99
   - best for precision and arithmetic

2. **Decimal string / decimal column**
   - only if legacy schema requires it
   - still convert to `Money` in code

## Eloquent casts
Typical pattern:
```php
use Cknow\Money\Casts\MoneyIntegerCast;

protected $casts = [
    'amount' => MoneyIntegerCast::class,
    'fee' => MoneyIntegerCast::class,
    'tax_total' => MoneyIntegerCast::class,
];
```

If currency varies per row, keep a currency column and make that relationship explicit in model logic.

## Request handling
Never trust raw decimal strings blindly.
Validate and normalize input before converting.

Example:
```php
$amount = Money::parse($request->input('amount'), 'USD');
```

## Domain rules
- Add/subtract only same-currency values
- Keep taxes, discounts, and totals as money objects until final serialization
- Avoid `number_format()` for domain logic
- Avoid `round()` on raw floats for billing decisions

## API / resource output
Use clear output contracts. Example:
```php
return [
    'amount' => $invoice->amount->getAmount(),
    'amount_formatted' => $invoice->amount->format(),
    'currency' => $invoice->amount->getCurrency()->getCode(),
];
```

## Views
Format at the last moment:
```php
{{ $order->total->format() }}
```

## Good fit examples
- invoices
- subscriptions
- checkout totals
- refunds
- wallet balances
- commissions
- tax calculations
- discount rules
