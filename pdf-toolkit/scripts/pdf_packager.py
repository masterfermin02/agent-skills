#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from pypdf import PdfReader, PdfWriter
import fitz


def merge_pdfs(inputs: list[Path], output: Path) -> None:
    writer = PdfWriter()
    for pdf in inputs:
        writer.append(str(pdf))
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('wb') as fh:
        writer.write(fh)


def extract_pages(input_pdf: Path, output_pdf: Path, pages: list[int]) -> None:
    reader = PdfReader(str(input_pdf))
    writer = PdfWriter()
    for page_num in pages:
        writer.add_page(reader.pages[page_num - 1])
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    with output_pdf.open('wb') as fh:
        writer.write(fh)


def reorder_pages(input_pdf: Path, output_pdf: Path, pages: list[int]) -> None:
    extract_pages(input_pdf, output_pdf, pages)


def highlight_pdf(input_pdf: Path, output_pdf: Path, needles: list[str]) -> int:
    doc = fitz.open(input_pdf)
    count = 0
    for page in doc:
        for needle in needles:
            rects = page.search_for(needle)
            for rect in rects:
                annot = page.add_highlight_annot(rect)
                annot.set_colors(stroke=(1, 1, 0))
                annot.update()
                count += 1
    if count == 0:
        for page in doc:
            for needle in needles:
                rects = page.search_for(needle)
                for rect in rects:
                    annot = page.add_highlight_annot(rect)
                    annot.set_colors(stroke=(1, 1, 0))
                    annot.update()
                    count += 1
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    doc.save(output_pdf)
    return count


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest='cmd', required=True)

    m = sub.add_parser('merge')
    m.add_argument('--output', required=True)
    m.add_argument('inputs', nargs='+')

    h = sub.add_parser('highlight')
    h.add_argument('--input', required=True)
    h.add_argument('--output', required=True)
    h.add_argument('--needle', action='append', required=True)

    e = sub.add_parser('extract')
    e.add_argument('--input', required=True)
    e.add_argument('--output', required=True)
    e.add_argument('--pages', required=True, help='1-based comma-separated page numbers, e.g. 1,3,5')

    r = sub.add_parser('reorder')
    r.add_argument('--input', required=True)
    r.add_argument('--output', required=True)
    r.add_argument('--pages', required=True, help='1-based comma-separated page numbers in desired order')

    args = parser.parse_args()
    if args.cmd == 'merge':
        merge_pdfs([Path(p) for p in args.inputs], Path(args.output))
    elif args.cmd == 'highlight':
        count = highlight_pdf(Path(args.input), Path(args.output), args.needle)
        print(count)
    elif args.cmd == 'extract':
        pages = [int(x) for x in args.pages.split(',') if x.strip()]
        extract_pages(Path(args.input), Path(args.output), pages)
    elif args.cmd == 'reorder':
        pages = [int(x) for x in args.pages.split(',') if x.strip()]
        reorder_pages(Path(args.input), Path(args.output), pages)


if __name__ == '__main__':
    main()
