# OAuth Setup

## Goal
Enable repeatable YouTube uploads using the YouTube Data API v3.

## What to create
1. Google Cloud project
2. YouTube Data API v3 enabled
3. OAuth client credentials
4. local credentials file
5. local token file after first consent

## Recommended local paths
- credentials: `~/.openclaw/credentials/youtube.json`
- token: `~/.openclaw/credentials/youtube-token.json`

## Scope
Use the minimum upload scope needed for video publishing.
Typical scope:
- `https://www.googleapis.com/auth/youtube.upload`

## First-run flow
- create credentials in Google Cloud
- download the OAuth client secret JSON
- run the auth/upload script
- open the consent URL
- grant access to the intended YouTube channel
- token is stored for later reuse

## Security
- never commit credentials or tokens
- keep them outside the repo
- treat refresh tokens as secrets
