# FFmpeg Notes

Use FFmpeg when available for deterministic media rendering.

## Typical single-image + audio approach
- loop the image
- add the audio
- stop the video at the shortest stream if needed
- encode video as H.264 and audio as AAC inside MP4

## Typical flags
- `-loop 1`
- `-c:v libx264`
- `-c:a aac`
- `-pix_fmt yuv420p`
- `-shortest`

## Example shape
```bash
ffmpeg -loop 1 -i image.jpg -i audio.mp3 \
  -c:v libx264 -tune stillimage -c:a aac \
  -b:a 192k -pix_fmt yuv420p -shortest output.mp4
```

Adjust scale/pad filters for horizontal vs vertical output.
