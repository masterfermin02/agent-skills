# Common Larastan Fixes

## Eloquent collections
Add generic annotations:
```php
/** @return \Illuminate\Database\Eloquent\Collection<int, User> */
public function activeUsers()
{
    return User::query()->where('active', true)->get();
}
```

## Relations
Add explicit relation return types:
```php
use Illuminate\Database\Eloquent\Relations\BelongsTo;

public function company(): BelongsTo
{
    return $this->belongsTo(Company::class);
}
```

## Builders
Type query scopes and builders clearly:
```php
use Illuminate\Database\Eloquent\Builder;

public function scopeActive(Builder $query): Builder
{
    return $query->where('active', true);
}
```

## Request validation output
Do not assume validated data types magically narrow; normalize where needed.

## Nullability
Fix nullable model lookups explicitly:
```php
$user = User::find($id);
if (! $user) {
    throw new RuntimeException('User not found');
}
```

## Avoid lazy suppressions
Prefer fixing:
- missing return types
- missing PHPDoc generics
- wrong nullable assumptions
- mixed arrays from request/input

Use ignores only for proven false positives.
