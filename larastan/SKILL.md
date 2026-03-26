---
name: larastan
description: "Use Larastan (the PHPStan extension for Laravel) when a Laravel project needs static analysis, PHPStan setup, Laravel-aware type checking, or fixes for Larastan/PHPStan errors. Trigger when asked to install Larastan, run static analysis on a Laravel app, fix Larastan errors, configure phpstan.neon, improve PHP types for Laravel models/collections/builders, or make code pass `vendor/bin/phpstan` or `vendor/bin/larastan`. Prefer Larastan over plain PHPStan guidance in Laravel projects." 
compatible_agents:
  - claude-code
  - cursor
  - windsurf
  - github-copilot
  - opencode
tags:
  - laravel
  - php
  - larastan
  - phpstan
  - static-analysis
---

Use **Larastan** for static analysis in Laravel projects.

## Core rules
- Prefer `vendor/bin/phpstan` with Larastan configured; do not assume a standalone `vendor/bin/larastan` binary exists.
- Treat Larastan as Laravel-aware PHPStan, not a separate analyzer.
- Fix root typing issues instead of suppressing errors blindly.
- Add precise PHPDoc / generics / return types when needed.

## Install
```bash
composer require --dev larastan/larastan phpstan/phpstan
```

## Minimal setup
Create or update `phpstan.neon`:
```neon
includes:
  - ./vendor/larastan/larastan/extension.neon

parameters:
  paths:
    - app
  level: 5
```

## Run
```bash
vendor/bin/phpstan analyse
```

Or with config explicitly:
```bash
vendor/bin/phpstan analyse -c phpstan.neon
```

## Use when
- setting up static analysis in a Laravel project
- fixing PHPStan/Larastan findings
- improving Eloquent relation types
- documenting collection generics
- fixing builder/model/query inference issues
- tightening service/repository/controller return types

## Workflow
1. Confirm project is Laravel.
2. Ensure `larastan/larastan` is installed as a dev dependency.
3. Ensure `phpstan.neon` includes Larastan's extension.
4. Run `vendor/bin/phpstan analyse`.
5. Fix type issues in code first.
6. Only add ignores for true false positives with explanation.

## Read references when needed
- Read `references/setup.md` for install/config/run guidance.
- Read `references/fixes.md` for common Laravel typing fixes.

## Important note
If someone says "run larastan", the practical command is usually:
```bash
vendor/bin/phpstan analyse
```
not `vendor/bin/larastan`.
