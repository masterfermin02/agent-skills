---
name: csharp-pragmatic-architecture
description: Apply pragmatic AI-era architecture rules to C# projects, including .NET Framework, ASP.NET, ASP.NET Core, and services/jobs. Use when deciding how to organize controllers, services, domain logic, repositories, integrations, and application workflows without over-engineering.
---

Use this skill to structure C# codebases so business rules stay clear and controllers/services do not become dumping grounds.

## Preferred shape
- thin controllers/endpoints
- orchestration in application services or use-case services
- domain logic separated from controllers and infrastructure
- repositories only for persistence
- integrations isolated by provider

## Read references when needed
- `references/folder-structure.md`
- `references/rules.md`
