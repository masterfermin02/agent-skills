# Agent Skills

Custom agent skills built by [@masterfermin02](https://github.com/masterfermin02).

This repository contains a mix of:
- **full skills** — installable directly from this repo
- **reference pointers** — entries that point to a dedicated source repository for the full skill

## Available Skills

| Skill | Type | Description |
|-------|------|-------------|
| [unit-testing](./unit-testing/) | Full | Framework-agnostic unit testing best practices (AAA, Object Mother, Builder, test doubles, anti-patterns) |
| [csharp-unit-testing](./csharp-unit-testing/) | Full | C#-specific unit testing with xUnit, Moq, and FluentAssertions |
| [csharp-best-practices](./csharp-best-practices/) | Pointer | C# / .NET best practices for code reviews and generation — points to [csharp-best-practices](https://github.com/masterfermin02/csharp-best-practices) |
| [laravel-best-practices](./laravel-best-practices/) | Pointer | Laravel best practices for controllers, FormRequests, Eloquent, services/actions, policies, jobs, and Inertia — points to [laravel-agent-skill](https://github.com/masterfermin02/laravel-agent-skill) |
| [laravel-update-with-rector](./laravel-update-with-rector/) | Pointer | Upgrade Laravel applications using Rector — points to [laravel-agent-skill](https://github.com/masterfermin02/laravel-agent-skill) |
| [php-update-with-rector](./php-update-with-rector/) | Pointer | Upgrade plain PHP code to newer PHP versions using Rector — points to [laravel-agent-skill](https://github.com/masterfermin02/laravel-agent-skill) |
| [php-the-right-way](./php-the-right-way/) | Full | PHP best practices based on phptherightway.com — PSR standards, security, design patterns, Composer, testing, and modern PHP idioms |
| [meal-log](./meal-log/) | Full | Log food and drinks into a fitness log with macro tracking |
| [pr-review](./pr-review/) | Full | Review GitHub Pull Requests and apply language-specific review rules |
| [laravel-money](./laravel-money/) | Full | Use `cknow/laravel-money` for safe monetary values, casts, formatting, and calculations in Laravel |
| [larastan](./larastan/) | Full | Use Larastan for Laravel-aware PHPStan static analysis, setup, and fixing static analysis errors |

## Installation

### Install the repo package
```bash
npx skills add masterfermin02/agent-skills
```

### Install a single skill from this repo
```bash
npx skills add masterfermin02/agent-skills --skill unit-testing
npx skills add masterfermin02/agent-skills --skill laravel-money
```

### Install a dedicated source repo for pointer skills
For pointer entries, install from the source repository linked in that skill.

## Structure

Each skill follows the Agent Skills pattern:

```text
skill-name/
├── SKILL.md
└── references/
```

## Notes
- Skills are distributed from this GitHub repo.
- Visibility on skills.sh comes from installs through the skills CLI telemetry.
- Review skills before installing, especially if scripts are ever added.

## Contributing
PRs and cleanup improvements are welcome.
