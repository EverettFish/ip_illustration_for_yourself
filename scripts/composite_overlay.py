#!/usr/bin/env python3
"""Place a transparent IP overlay over an unchanged source photograph."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageChops


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Alpha-composite a transparent IP overlay without changing source pixels outside its rectangle."
    )
    parser.add_argument("--background", required=True, type=Path)
    parser.add_argument("--overlay", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--x", required=True, type=int)
    parser.add_argument("--y", required=True, type=int)
    parser.add_argument("--width", required=True, type=int)
    parser.add_argument("--height", type=int, help="Optional exact height; otherwise preserve overlay aspect ratio.")
    parser.add_argument("--opacity", type=float, default=1.0, help="Overlay opacity from 0 to 1.")
    return parser.parse_args()


def region_changed(before: Image.Image, after: Image.Image, box: tuple[int, int, int, int]) -> bool:
    if box[0] >= box[2] or box[1] >= box[3]:
        return False
    return ImageChops.difference(before.crop(box), after.crop(box)).getbbox() is not None


def main() -> None:
    args = parse_args()
    if args.width <= 0 or (args.height is not None and args.height <= 0):
        raise SystemExit("width and height must be positive")
    if not 0 <= args.opacity <= 1:
        raise SystemExit("opacity must be between 0 and 1")

    background = Image.open(args.background).convert("RGBA")
    overlay = Image.open(args.overlay).convert("RGBA")

    height = args.height or round(overlay.height * args.width / overlay.width)
    overlay = overlay.resize((args.width, height), Image.Resampling.LANCZOS)

    if args.opacity < 1:
        alpha = overlay.getchannel("A").point(lambda value: round(value * args.opacity))
        overlay.putalpha(alpha)

    right = args.x + overlay.width
    bottom = args.y + overlay.height
    if args.x < 0 or args.y < 0 or right > background.width or bottom > background.height:
        raise SystemExit("overlay rectangle must remain fully inside the background")

    result = background.copy()
    result.alpha_composite(overlay, dest=(args.x, args.y))

    outside_boxes = (
        (0, 0, background.width, args.y),
        (0, bottom, background.width, background.height),
        (0, args.y, args.x, bottom),
        (right, args.y, background.width, bottom),
    )
    unchanged = not any(region_changed(background, result, box) for box in outside_boxes)
    if not unchanged:
        raise SystemExit("validation failed: pixels changed outside the overlay rectangle")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    result.save(args.out, format="PNG")
    print(
        f"saved={args.out} size={result.width}x{result.height} "
        f"overlay_box={args.x},{args.y},{overlay.width},{overlay.height} outside_unchanged=true"
    )


if __name__ == "__main__":
    main()
