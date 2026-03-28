---
name: pdf-toolkit
description: Merge PDFs, reorder pages, highlight text, extract specific pages, combine statements, build visa-ready document packs, annotate supporting evidence, and optionally compress or optimize PDFs later. Use when Fermin asks to merge statements, replace one PDF with another, highlight proof inside PDFs, assemble document packs, or do repeatable PDF operations for banking, visa, legal, or admin workflows.
---

Use this skill for bank statements, visa evidence packs, and general PDF operations where multiple files or pages must become one clean output.

## Workflow
1. Confirm the source files, desired order, and final output goal.
2. Merge into a clean output PDF in `workspace/merged/` when the task is file-level combination.
3. Reorder or extract pages when the user wants only part of a document or a different sequence.
4. If a file must be replaced, rebuild the merged PDF with the replacement file.
5. If the user wants proof highlighted or annotated, search the PDF for the target phrase and add visible annotations.
6. If the task is visa/admin packaging, produce a clean final filename and summarize what is included.
7. Consider compression/optimization only when file size matters and quality loss is acceptable.

## Supported operations
- merge PDFs
- reorder pages
- highlight text
- extract specific pages
- combine statements
- build visa-ready document packs
- annotate supporting evidence
- compress / optimize later when needed

## Preferred tools
- Use Python scripts in `scripts/` for deterministic PDF work.
- Prefer local virtualenv-based dependencies over system Python changes.
- Keep outputs in `workspace/merged/` with clean names.
- Never overwrite source PDFs unless the user explicitly asks.

## Good output naming
- `Bank_Statements_Dec_2025_to_Feb_2026_Merged.pdf`
- `Bank_Statements_with_Credique_Highlighted.pdf`
- `Visa_Evidence_<topic>.pdf`
- `Supporting_Evidence_<topic>.pdf`

## Read references when needed
- `references/usage.md`
- `references/highlighting.md`
- `references/page-ops.md`
