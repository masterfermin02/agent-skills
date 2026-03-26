# Larastan Setup

## Install
```bash
composer require --dev larastan/larastan phpstan/phpstan
```

## Config file
Typical `phpstan.neon`:
```neon
includes:
  - ./vendor/larastan/larastan/extension.neon

parameters:
  level: 5
  paths:
    - app
    - routes
    - database
```

## Run commands
```bash
vendor/bin/phpstan analyse
vendor/bin/phpstan analyse -c phpstan.neon
vendor/bin/phpstan analyse app/Http/Controllers
```

## CI example
```bash
vendor/bin/phpstan analyse --no-progress
```

## Notes
- Larastan extends PHPStan; it usually runs through the PHPStan binary.
- Tune level gradually instead of jumping too high immediately.
- Keep the baseline strategy conservative.
