# PHP Basics — The Right Way

Source: https://phptherightway.com

## Comparison Operators

Always use strict comparisons to avoid unexpected type coercion:

```php
$a = 5;
var_dump($a == '5');   // true  — BAD: loose comparison
var_dump($a === '5');  // false — GOOD: strict comparison
```

Gotcha with `strpos()`:
```php
// WRONG — strpos returns 0 (falsy) when found at position 0
if (strpos('testing', 'test')) { ... }

// CORRECT
if (strpos('testing', 'test') !== false) { ... }
```

## Control Flow

### Early return — avoid unnecessary `else`
```php
// BAD
function test($a) {
    if ($a) {
        return true;
    } else {
        return false;
    }
}

// GOOD
function test($a) {
    if ($a) {
        return true;
    }
    return false;
}

// BEST
function test($a): bool {
    return (bool) $a;
}
```

### Return boolean directly
```php
// BAD
return ($a == 3) ? true : false;

// GOOD
return $a === 3;
```

## Strings

### Use single quotes for literals (no variable parsing)
```php
echo 'This is a plain string, $var is not parsed.';
```

### Use double quotes for interpolation
```php
$name = 'World';
echo "Hello, {$name}!"; // wrap complex vars in {}
```

### Multi-line strings
```php
// Nowdoc (like single quotes, no parsing)
$str = <<<'EOD'
No $variable parsing here.
EOD;

// Heredoc (like double quotes, variables parsed)
$str = <<<EOD
Hello $name, welcome!
EOD;
```

### Concatenation style
```php
// BAD
$a = 'Multi-line';
$a .= "\n";
$a .= 'example';

// GOOD
$a = 'Multi-line'
    . "\n"
    . 'example';
```

## Ternary Operators

Use sparingly — one ternary per line max. Never nest ternaries.

```php
// GOOD
$result = ($a === 5) ? 'yes' : 'no';

// BAD — nested, unreadable
echo ($a) ? ($a == 5) ? 'yay' : 'nay' : ($b == 10) ? 'excessive' : ':(';
```

Null coalescing (PHP 7+):
```php
$value = $input ?? 'default'; // returns $input if set and not null
```

## Namespaces

Every class must be namespaced. Reference global functions with `\`:

```php
namespace App\Services;

function myFunction() {
    $file = \fopen('path', 'r'); // \ = global namespace
    $arr = new \ArrayIterator(); // \ = global class
}
```

## Standard PHP Library (SPL)

Use SPL data structures when appropriate:
- `SplStack`, `SplQueue`, `SplHeap` — typed data structures
- `SplFileInfo`, `SplFileObject` — file handling
- Iterators — for traversing collections

## CLI PHP

```php
#!/usr/bin/env php
<?php
declare(strict_types=1);

if ($argc !== 2) {
    echo "Usage: php script.php <name>" . PHP_EOL;
    exit(1); // non-zero = failure
}

$name = $argv[1];
echo "Hello, {$name}" . PHP_EOL;
```
