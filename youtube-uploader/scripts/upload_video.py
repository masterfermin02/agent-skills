#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import sys


def main() -> None:
    parser = argparse.ArgumentParser(description='YouTube upload helper skeleton')
    parser.add_argument('--file', required=True)
    parser.add_argument('--title', required=True)
    parser.add_argument('--description', required=True)
    parser.add_argument('--privacy', required=True, choices=['private', 'unlisted', 'public'])
    parser.add_argument('--tags', nargs='*')
    parser.add_argument('--category-id')
    parser.add_argument('--thumbnail')
    args = parser.parse_args()

    video = Path(args.file)
    if not video.exists():
        print(f'File not found: {video}', file=sys.stderr)
        raise SystemExit(1)

    print('Upload script skeleton ready.')
    print('Next step: wire Google OAuth + YouTube Data API v3 client.')
    print(f'File: {video}')
    print(f'Title: {args.title}')
    print(f'Privacy: {args.privacy}')


if __name__ == '__main__':
    main()
