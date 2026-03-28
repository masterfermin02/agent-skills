# Commands

## Send a PDF to Fermin on Telegram
```bash
openclaw message send --channel telegram --target 201588450 \
  --media "/absolute/path/to/file.pdf"
```

## Send with caption
```bash
openclaw message send --channel telegram --target 201588450 \
  --message "Here is your file" \
  --media "/absolute/path/to/file.pdf"
```

## Send an image as a document
```bash
openclaw message send --channel telegram --target 201588450 \
  --media "/absolute/path/to/image.png" \
  --force-document
```
