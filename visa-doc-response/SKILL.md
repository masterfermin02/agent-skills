---
name: visa-doc-response
description: "Parse visa or immigration request emails, extract required documents, identify apostille/translation/recency needs, and turn them into a clean action checklist. Use when a visa authority asks for more documents, when comparing immigration document burdens, or when building a response plan for nomad or residence visa applications."
compatible_agents:
  - claude-code
  - cursor
  - windsurf
  - github-copilot
  - opencode
tags:
  - visa
  - immigration
  - documents
  - apostille
  - checklist
---

Use this skill when handling visa or immigration document requests.

## Workflow
1. Parse the message and extract every requested item.
2. Mark which documents need apostille, translation, or freshness limits.
3. Separate what the user can get directly vs what must come from employer/company/government.
4. Produce a practical checklist ordered by difficulty.
5. Highlight blockers and unknowns.

## Output format
Return:
- what the message means in plain language
- exact required documents
- document-by-document action plan
- risk points / common mistakes
- the next 3 actions

## Rules
- Do not assume one named document is the only acceptable equivalent.
- Distinguish between employee, contractor, and company-owner cases.
- Call out document age limits explicitly.
- Prefer practical action plans over legal fluff.

## Read references when needed
- `references/checklist.md`
- `references/response-template.md`
