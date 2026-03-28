# Troubleshooting

## Command succeeds but file does not appear
- verify the target id
- confirm the bot is allowed to message that chat
- check whether the command was run on the correct host/account

## Path issues
- use absolute paths
- wrap paths in quotes
- confirm the file exists before sending

## Telegram/media issues
- verify `channels.telegram.mediaMaxMb`
- PDFs should send as documents automatically
- use `--force-document` for images or GIFs when document behavior is preferred

## Confidence rule
Only tell the user the file was sent after the CLI command returns success.
