---
name: file-share-cli
description: Send local files into chat using the OpenClaw CLI `openclaw message send` command, especially for Telegram document delivery when a generated PDF, image, or output file must be sent back to Fermin without manual server access. Use when a file already exists locally and the task is to share it into chat via CLI rather than just returning a filesystem path.
---

Use this skill when a file exists on disk and should be sent to chat through the OpenClaw CLI.

## Workflow
1. Confirm the file path exists.
2. Identify the target chat id or username.
3. Use `openclaw message send --channel telegram --target <id> --media <file>` for PDFs and other files.
4. Add `--message` only when a caption helps.
5. If the send fails, check path quoting, permissions, and channel config.

## Rules
- Prefer absolute paths for CLI sends.
- Quote file paths.
- Use the current Telegram user id when the user wants the file in the current DM.
- Do not claim a file was sent unless the command succeeds.

## Current default target
- Fermin Telegram user id: `201588450`

## Read references when needed
- `references/commands.md`
- `references/troubleshooting.md`
