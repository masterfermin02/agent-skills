#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 3 ]; then
  echo "usage: render_still_video.sh <image> <audio> <output> [size]" >&2
  exit 1
fi

IMAGE="$1"
AUDIO="$2"
OUTPUT="$3"
SIZE="${4:-1920x1080}"

ffmpeg -y -loop 1 -i "$IMAGE" -i "$AUDIO" \
  -vf "scale=${SIZE}:force_original_aspect_ratio=decrease,pad=${SIZE}:(ow-iw)/2:(oh-ih)/2" \
  -c:v libx264 -tune stillimage -c:a aac -b:a 192k \
  -pix_fmt yuv420p -shortest "$OUTPUT"
