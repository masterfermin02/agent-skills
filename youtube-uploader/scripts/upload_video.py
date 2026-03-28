#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
CREDENTIALS_PATH = Path("~/.openclaw/credentials/youtube.json").expanduser()
TOKEN_PATH = Path("~/.openclaw/credentials/youtube-token.json").expanduser()
DEFAULT_CATEGORY_ID = "10"  # Music


def load_credentials() -> Credentials:
    if not CREDENTIALS_PATH.exists():
        print(f"Missing OAuth client credentials: {CREDENTIALS_PATH}", file=sys.stderr)
        raise SystemExit(1)

    creds: Credentials | None = None

    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    elif not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_PATH), SCOPES)
        creds = flow.run_local_server(port=0)
        TOKEN_PATH.parent.mkdir(parents=True, exist_ok=True)
        TOKEN_PATH.write_text(creds.to_json())

    return creds


def build_service():
    creds = load_credentials()
    return build("youtube", "v3", credentials=creds)


def upload_video(file_path: Path, title: str, description: str, privacy: str, tags: list[str] | None, category_id: str) -> dict:
    youtube = build_service()

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "categoryId": category_id,
        },
        "status": {
            "privacyStatus": privacy,
        },
    }

    if tags:
        body["snippet"]["tags"] = tags

    media = MediaFileUpload(str(file_path), chunksize=-1, resumable=True)

    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media,
    )

    response = None
    while response is None:
        _status, response = request.next_chunk()

    return response


def main() -> None:
    parser = argparse.ArgumentParser(description="Upload a video to YouTube")
    parser.add_argument("--file", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--description", required=True)
    parser.add_argument("--privacy", required=True, choices=["private", "unlisted", "public"])
    parser.add_argument("--tags", nargs="*")
    parser.add_argument("--category-id", default=DEFAULT_CATEGORY_ID)
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON output")
    args = parser.parse_args()

    file_path = Path(args.file).expanduser()
    if not file_path.exists():
        print(f"File not found: {file_path}", file=sys.stderr)
        raise SystemExit(1)

    try:
        response = upload_video(
            file_path=file_path,
            title=args.title,
            description=args.description,
            privacy=args.privacy,
            tags=args.tags,
            category_id=args.category_id,
        )
    except HttpError as exc:
        print(f"YouTube API error: {exc}", file=sys.stderr)
        raise SystemExit(1)

    video_id = response.get("id")
    url = f"https://www.youtube.com/watch?v={video_id}" if video_id else None

    result = {
        "videoId": video_id,
        "url": url,
        "privacy": args.privacy,
        "title": args.title,
        "file": str(file_path),
    }

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("Upload succeeded")
        print(f"Video ID: {video_id}")
        print(f"URL: {url}")
        print(f"Privacy: {args.privacy}")


if __name__ == "__main__":
    main()
