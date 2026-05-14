#!/usr/bin/env python3
from pathlib import Path
import argparse
import re

DATE_LINE = re.compile(r"^\d{4}/\d{1,2}/\d{1,2}|^\d{1,2}/\d{1,2}/\d{4}|^\d{1,2}/\d{1,2}\s")

def read_text(path: Path) -> str:
    for enc in ("utf-8", "utf-8-sig", "cp950", "big5", "big5hkscs"):
        try:
            return path.read_text(encoding=enc)
        except UnicodeDecodeError:
            pass
    return path.read_text(encoding="utf-8", errors="replace")

def split_file(input_path: Path, output_dir: Path, max_chars: int) -> None:
    text = read_text(input_path)
    lines = text.splitlines(keepends=True)

    output_dir.mkdir(parents=True, exist_ok=True)

    base = input_path.stem
    chunks = []
    current = []
    current_len = 0

    for line in lines:
        line_len = len(line)

        # 超過 max_chars 時切 chunk；如果這行像日期行，更適合當新 chunk 開頭
        should_split = current and (current_len + line_len > max_chars)

        if should_split:
            chunks.append("".join(current))
            current = []
            current_len = 0

        current.append(line)
        current_len += line_len

    if current:
        chunks.append("".join(current))

    for i, chunk in enumerate(chunks, 1):
        out = output_dir / f"{base}.part-{i:03d}.txt"
        header = (
            f"# Source: {input_path}\n"
            f"# Part: {i}/{len(chunks)}\n"
            f"# Note: split for org-map-distiller incremental processing\n\n"
        )
        out.write_text(header + chunk, encoding="utf-8")

    print(f"Input: {input_path}")
    print(f"Output dir: {output_dir}")
    print(f"Chunks: {len(chunks)}")
    for i, chunk in enumerate(chunks, 1):
        print(f"  part-{i:03d}: {len(chunk):,} chars")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("input")
    p.add_argument("-o", "--output-dir", default=None)
    p.add_argument("--max-chars", type=int, default=120_000)
    args = p.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output_dir) if args.output_dir else input_path.parent / f"{input_path.stem}.chunks"

    split_file(input_path, output_dir, args.max_chars)

if __name__ == "__main__":
    main()
