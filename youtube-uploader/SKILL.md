---
name: youtube-uploader
description: Prepare and upload videos to YouTube with the right title, description, privacy setting, and metadata. Use when Fermin wants to publish or schedule a video on YouTube, check whether a video is upload-ready, prepare YouTube metadata, or wire a repeatable upload workflow after rendering a final MP4.
---

Use this skill when the final output is a YouTube upload or YouTube-ready package.

## Workflow
1. Confirm the final video file exists and is upload-ready.
2. Confirm metadata:
   - title
   - description
   - privacy status
   - optional tags
   - optional thumbnail
3. Check format readiness:
   - MP4 preferred
   - H.264 video
   - AAC audio
4. Confirm YouTube auth/setup exists or guide the user through OAuth setup.
5. Use the chosen upload path or API workflow.
6. Return the result clearly: uploaded, scheduled, draft, or blocked by auth/setup.

## Planned tooling
- OAuth client credentials file at `~/.openclaw/credentials/youtube.json`
- stored OAuth token at `~/.openclaw/credentials/youtube-token.json`
- Python upload script
- optional metadata JSON input

## Good uses
- upload a final MP4 to YouTube
- prepare title/description/package for upload
- validate whether a rendered video is YouTube-safe
- create a repeatable publishing workflow

## Rules
- Prefer MP4 uploads.
- Confirm whether the user wants `private`, `unlisted`, or `public`.
- Do not claim an upload succeeded without a real success result.
- If auth is missing, stop and explain exactly what is needed.

## Read references when needed
- `references/checklist.md`
- `references/metadata.md`
- `references/workflow.md`
