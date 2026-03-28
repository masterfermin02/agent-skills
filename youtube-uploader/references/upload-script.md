# Upload Script Shape

## Inputs
- `--file`
- `--title`
- `--description`
- `--privacy`
- optional `--tags`
- optional `--category-id`
- optional `--thumbnail`

## Output
Return:
- uploaded video id
- video URL when available
- privacy status used

## Failure handling
Be explicit when blocked by:
- missing credentials
- missing token
- expired/revoked auth
- invalid file path
- unsupported metadata
