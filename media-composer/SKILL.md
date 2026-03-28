---
name: media-composer
description: Turn photos, images, audio, and simple text overlays into shareable videos, especially YouTube-ready MP4 files. Use when Fermin wants to combine one or more images with audio, make a slideshow, export a video for YouTube, create a simple talking/static-image video, or prepare media in horizontal or vertical video formats.
---

Use this skill to build lightweight videos from still images and audio.

## Default output
Prefer:
- MP4 container
- H.264 video codec
- AAC audio codec
- 1080p output
- 30 fps

## Workflow
1. Confirm inputs: image(s), audio, optional title/captions, and target format.
2. Choose aspect ratio:
   - YouTube standard: 1920x1080
   - Shorts / Reels: 1080x1920
3. Build a simple video from the image timeline and audio.
4. Export as MP4 unless the user explicitly wants something else.
5. Return the output path and summarize the render settings.

## Good use cases
- single photo + audio = MP4
- multiple photos + audio slideshow
- podcast-style static cover video
- simple background image with voice/audio
- YouTube upload preparation

## Rules
- Prefer MP4 for final delivery.
- Keep the first version simple and reliable before adding advanced effects.
- Match the video duration to the audio duration.
- Avoid unnecessary transitions unless the user asks.

## Read references when needed
- `references/presets.md`
- `references/workflow.md`
- `references/ffmpeg-notes.md`
