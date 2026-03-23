---
name: laravel-update-with-rector
description: >
  Upgrades a Laravel application or package to a newer Laravel version using Rector and driftingly/rector-laravel.
  Inspects composer.json, detects current and target versions, configures Rector with the correct LaravelSetList
  or LaravelLevelSetList rulesets, updates dependencies conservatively, runs a dry-run first, and produces
  an upgrade checklist covering both automated code changes and manual skeleton/breaking-change steps.
  The latest stable Laravel version is Laravel 13 (March 2026). Activate for phrases like
  "upgrade to Laravel 12", "upgrade to Laravel 13", "migrate my Laravel app",
  "fix Laravel deprecation warnings", "help me with the Laravel upgrade guide",
  "set up Rector for Laravel upgrade", or any request to automate a Laravel version migration —
  even when Rector is not mentioned by name.
source: masterfermin02/laravel-agent-skill
sourceType: github
skill: laravel-update-with-rector
license: MIT
compatible_agents:
  - claude-code
  - cursor
  - windsurf
tags:
  - laravel
  - php
  - rector
  - upgrade
  - migration
---

> **This is a reference skill.**
> The full skill lives at [masterfermin02/laravel-agent-skill](https://github.com/masterfermin02/laravel-agent-skill/tree/main/skills/laravel-update-with-rector).
> Install it directly from there — this entry is a pointer for discoverability in this collection.
