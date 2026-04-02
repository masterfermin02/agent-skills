---
name: laravel-pragmatic-architecture
description: Apply pragmatic AI-era architecture rules to Laravel projects. Use when deciding how to organize controllers, actions/services, domain rules, Eloquent models, jobs, policies, and external integrations while keeping Laravel code easy to navigate and avoiding unnecessary ceremony.
---

Use this skill for Laravel architecture that stays idiomatic but still protects important business rules.

## Preferred shape
- thin controllers
- validation in Form Requests where useful
- business workflows in actions/services/use-case classes when they become non-trivial
- Eloquent for persistence, but avoid burying all business rules in models/controllers
- integrations isolated in dedicated service classes

## Read references when needed
- `references/folder-structure.md`
- `references/rules.md`
