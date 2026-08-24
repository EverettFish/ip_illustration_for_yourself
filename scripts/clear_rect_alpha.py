#!/usr/bin/env python3
"""Clear a rectangular photo window to genuine transparent alpha."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Set one rectangular image region to transparent alpha.")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--x", required=True, type=int)
    parser.add_argument("--y", required=True, type=int)
    parser.add_argument("--width", required=True, type=int)
    parser.add_argument("--height", required=True, type=int)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    image = Image.open(args.input).convert("RGBA")
    if args.width <= 0 or args.height <= 0:
        raise SystemExit("width and height must be positive")

    right = args.x + args.width
    bottom = args.y + args.height
    if args.x < 0 or args.y < 0 or right > image.width or bottom > image.height:
        raise SystemExit("clear rectangle must remain fully inside the image")

    image.paste(Image.new("RGBA", (args.width, args.height), (0, 0, 0, 0)), (args.x, args.y))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    image.save(args.out, format="PNG")

    alpha = image.getchannel("A").crop((args.x, args.y, right, bottom))
    if alpha.getbbox() is not None:
        raise SystemExit("validation failed: cleared window still contains non-zero alpha")
    print(f"saved={args.out} cleared={args.x},{args.y},{args.width},{args.height} alpha=0")


if __name__ == "__main__":
    main()
