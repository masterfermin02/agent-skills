---
name: php-the-right-way
description: "PHP best practices skill based on phptherightway.com. Use whenever writing, reviewing, or refactoring PHP code to ensure it follows modern PHP standards and idioms. Triggers on: writing PHP code, reviewing PHP files, asking about PHP best practices, PHP code style (PSR-1/PSR-12/PSR-4), PHP OOP patterns, namespaces, Composer, dependency management, security (XSS, CSRF, SQL injection, password hashing), error handling, testing (PHPUnit/Pest), templating, databases, design patterns (Factory, Singleton, MVC, Strategy), functional PHP, or any question about 'the right way' to do something in PHP."
compatible_agents:
  - Claude Code
  - Cursor
  - Windsurf
  - GitHub Copilot
tags:
  - php
  - best-practices
  - psr
  - composer
  - security
---

## Purpose
Guide PHP code to follow modern, idiomatic best practices as defined by the PHP community. Apply these rules when writing, reviewing, or refactoring any PHP code.

## Core Rules (always apply)

### Version
- Use PHP 8.2+ features; never write PHP 7.x style code for new projects
- Enable strict types: `declare(strict_types=1);` at the top of every file

### Code Style
- Follow **PSR-12** for formatting + **PSR-4** for autoloading
- Use **Composer** for all dependency management — never manual `require`
- Run `php-cs-fixer` or `phpcs` to enforce style automatically

### Comparisons
- Always use **strict comparison** (`===`, `!==`) — never loose `==`
- Check `strpos()`, `array_search()` etc. with `!== false`, not truthiness

### OOP
- Declare return types, parameter types, and property types on all methods
- Use `readonly` properties (PHP 8.1+) for immutable data / DTOs
- Prefer `enum` (PHP 8.1+) over class constants for fixed value sets
- Use constructor property promotion to reduce boilerplate
- Use interfaces to define contracts; depend on abstractions, not concretions
- Use named arguments for clarity on functions with many params

### Namespaces
- Every class must live in a namespace following PSR-4
- Never pollute the global namespace
- Prefix internal function calls with `\` when inside a namespace (e.g., `\array_map()`)

### Error Handling
- Use typed exceptions — never `throw new \Exception('generic message')`
- Catch specific exceptions, not bare `\Exception`
- Never suppress errors with `@`
- Set `error_reporting(E_ALL)` in development; log errors in production

### Security (non-negotiable)
- **SQL**: Always use PDO/MySQLi with prepared statements — never string interpolation in queries
- **Output**: Always `htmlspecialchars($var, ENT_QUOTES, 'UTF-8')` before echoing user input
- **Passwords**: Use `password_hash()` / `password_verify()` — never MD5/SHA1
- **CSRF**: Include CSRF tokens on all state-changing forms
- **Input**: Filter input with `filter_var()` / `filter_input()`
- **Sessions**: Regenerate session ID on login: `session_regenerate_id(true)`

## References

Load these when needed:

- **[basics.md](references/basics.md)** — Strings, comparisons, ternary, control flow gotchas
- **[design-patterns.md](references/design-patterns.md)** — Factory, Singleton, Strategy, MVC, Front Controller
- **[security.md](references/security.md)** — XSS, SQL injection, CSRF, password hashing, sessions
- **[tooling.md](references/tooling.md)** — Composer, PHPUnit/Pest, Xdebug, php-cs-fixer, PHPStan

## Workflow: Code Review
1. Check strict types declaration at top
2. Verify all comparisons are strict (`===`)
3. Check for raw SQL strings (injection risk)
4. Check output escaping (XSS risk)
5. Verify password handling (never MD5/SHA1)
6. Check PSR-4 namespacing and PSR-12 style
7. Look for missing type declarations
8. Flag any `@` error suppression

## Workflow: Code Generation
1. Start with `declare(strict_types=1);`
2. Apply PSR-4 namespace matching directory structure
3. Type all parameters, return values, and properties
4. Use constructor property promotion for simple classes
5. Throw typed exceptions with descriptive messages
6. Add PHPDoc only when types alone aren't self-documenting
