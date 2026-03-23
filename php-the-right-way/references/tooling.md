# PHP Tooling — The Right Way

Source: https://phptherightway.com

## Composer

The standard PHP dependency manager. Required for every project.

```bash
# Install a dependency
composer require vendor/package

# Install dev dependency
composer require --dev phpunit/phpunit

# Install all dependencies from composer.lock
composer install

# Update dependencies
composer update

# Autoload setup in composer.json
{
    "autoload": {
        "psr-4": {
            "App\\": "src/"
        }
    }
}
```

```php
// Include in your entry point
require 'vendor/autoload.php';
```

Rules:
- Commit `composer.lock` to version control
- Use `composer install` in CI/CD (not `composer update`)
- Never edit files in `vendor/`

## Static Analysis — PHPStan

Catches bugs without running code.

```bash
composer require --dev phpstan/phpstan

# Run analysis (level 0-9, 9 = strictest)
./vendor/bin/phpstan analyse src --level=8
```

Recommended: run in CI at level 6+ for new projects.

## Code Style — PHP CS Fixer

```bash
composer require --dev friendsofphp/php-cs-fixer

# Fix a file
./vendor/bin/php-cs-fixer fix src/

# Check only (no changes)
./vendor/bin/php-cs-fixer fix --dry-run --diff src/
```

`.php-cs-fixer.php` config:
```php
<?php
$finder = PhpCsFixer\Finder::create()->in(__DIR__ . '/src');

return (new PhpCsFixer\Config())
    ->setRules([
        '@PSR12' => true,
        'strict_comparison' => true,
        'declare_strict_types' => true,
    ])
    ->setFinder($finder);
```

## Testing — PHPUnit / Pest

```bash
# PHPUnit
composer require --dev phpunit/phpunit
./vendor/bin/phpunit

# Pest (expressive, Laravel-style)
composer require --dev pestphp/pest
./vendor/bin/pest
```

Example Pest test:
```php
it('hashes passwords correctly', function () {
    $hash = password_hash('secret', PASSWORD_ARGON2ID);
    expect(password_verify('secret', $hash))->toBeTrue();
});

it('throws on invalid email', function () {
    expect(fn() => new User('not-an-email'))
        ->toThrow(InvalidArgumentException::class);
});
```

## Debugging — Xdebug

```bash
# Install via PECL
pecl install xdebug

# php.ini
zend_extension=xdebug
xdebug.mode=debug
xdebug.start_with_request=yes
xdebug.client_port=9003
```

- Never use `var_dump()` + `die()` in production — use Xdebug or a logger
- Use `\Symfony\Component\VarDumper\VarDumper::dump()` for dev dumps

## Logging — PSR-3

Use PSR-3 compatible loggers (Monolog is the standard).

```bash
composer require monolog/monolog
```

```php
use Monolog\Logger;
use Monolog\Handler\StreamHandler;

$log = new Logger('app');
$log->pushHandler(new StreamHandler('storage/logs/app.log', Logger::WARNING));

$log->warning('Something suspicious happened', ['user_id' => 42]);
$log->error('Critical failure', ['exception' => $e]);
```

Never use `error_log()` directly in application code — use PSR-3.

## Environment Config — dotenv

```bash
composer require vlucas/phpdotenv
```

```php
$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();

$dbHost = $_ENV['DB_HOST'];
```

Rules:
- Never commit `.env` files
- Always have `.env.example` with keys but no values
- Never call `getenv()` or `$_ENV` directly in business logic — wrap in config classes
