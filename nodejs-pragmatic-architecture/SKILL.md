---
name: nodejs-pragmatic-architecture
description: Apply pragmatic AI-era architecture rules to Node.js backends and Node + React projects. Use when defining folder structure, separating routes/controllers/services/domain/repositories/integrations, or deciding how much architecture a Node.js codebase really needs.
---

Use this skill for Node.js project structure that keeps important logic easy to find and avoids over-engineering.

## Preferred shape
- thin routes/controllers
- service or use-case orchestration
- domain logic separated from transport/framework code
- repositories for database access
- integrations isolated by provider

## Good default folders
- `app/`
- `modules/`
- `domain/`
- `integrations/`
- `db/`
- `jobs/`
- `shared/`

## Read references when needed
- `references/folder-structure.md`
- `references/rules.md`
