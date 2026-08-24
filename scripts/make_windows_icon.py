#!/usr/bin/env python3
"""Fit a transparent 4:3 folder graphic onto a square PNG and optional ICO."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a square transparent Windows folder icon asset.")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--png", required=True, type=Path)
    parser.add_argument("--ico", type=Path)
    parser.add_argument("--size", type=int, default=1024)
    parser.add_argument("--margin", type=int, default=64)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.size <= 0 or args.margin < 0 or args.margin * 2 >= args.size:
        raise SystemExit("size must be positive and margin must leave a visible interior")

    source = Image.open(args.input).convert("RGBA")
    alpha_box = source.getchannel("A").getbbox()
    if alpha_box is None:
        raise SystemExit("input contains no visible pixels")
    source = source.crop(alpha_box)

    available = args.size - 2 * args.margin
    scale = min(available / source.width, available / source.height)
    target = (
        max(1, round(source.width * scale)),
        max(1, round(source.height * scale)),
    )
    source = source.resize(target, Image.Resampling.LANCZOS)

    canvas = Image.new("RGBA", (args.size, args.size), (0, 0, 0, 0))
    position = ((args.size - source.width) // 2, (args.size - source.height) // 2)
    canvas.alpha_composite(source, dest=position)

    args.png.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(args.png, format="PNG")

    if args.ico:
        args.ico.parent.mkdir(parents=True, exist_ok=True)
        sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        canvas.save(args.ico, format="ICO", sizes=sizes)

    print(
        f"saved_png={args.png} size={args.size}x{args.size} "
        f"content={source.width}x{source.height} position={position[0]},{position[1]} "
        f"saved_ico={args.ico or 'none'}"
    )


if __name__ == "__main__":
    main()
