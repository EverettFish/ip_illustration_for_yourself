# Personal-IP Polaroid frames

Use this route for photo overlays, Polaroid-style borders, transparent photo frames, or themed cutout frames.

## Layout references

Use these only for border architecture, thematic distribution, and character placement:

- `polaroid-frame/polaroid_ref_01_chinese-new-year.jpg`
- `polaroid-frame/polaroid_ref_02_night-tech.jpg`
- `polaroid-frame/polaroid_ref_03_winter.jpg`
- `polaroid-frame/polaroid_ref_04_love.jpg`

Ignore the example characters, franchise designs, words, logos, and exact decorative motifs.

## Default set

Unless the user changes themes or count, generate four separate exact 3:4 portrait transparent PNG frames, one call per theme:

1. **Love**: red, coral, or pink hearts, ribbon, flowers, IP making heart-hands
2. **Birthday**: cake, candles, balloons, gift, confetti, IP celebrating
3. **Reading**: books, bookmark, reading lamp, glasses motif, IP reading
4. **Tech**: blue, violet, or mint circuits, stars, small robot/device motifs, IP using a laptop or inspecting technology

## Strict frame architecture

- Use exact 3:4 portrait.
- Create one large clean rectangular photo window occupying about 58–68% of the canvas.
- Keep the window centered with a slightly thicker lower margin when a classic Polaroid feel is useful.
- Reserve enough border width for theme decorations without shrinking the photo area.
- Place one to three small accepted-IP appearances on the border, never inside the usable window except for a deliberate edge overlap of at most about 5%.
- Distribute decorations around all four sides with one clear visual rhythm; avoid crowding one edge.
- Use no title or slogan by default.

## Transparency

- Output genuine PNG alpha.
- Make the entire central photo window fully transparent.
- Make the exterior beyond the outer frame silhouette transparent.
- Keep only the illustrated frame and its attached decorations opaque.
- Request transparency directly from the image tool. If the center is not clean, run `scripts/clear_rect_alpha.py` with the measured window rectangle.

## Prompt structure

```text
Create one exact 3:4 portrait transparent personal-IP Polaroid frame.

IDENTITY LOCK:
[accepted anchor fidelity lock]

THEME:
[Love / Birthday / Reading / Tech]

FRAME:
one large centered rectangular photo window occupying 58–68%; comfortable border on all sides; slightly deeper lower border when suitable; balanced themed decoration; one to three small accepted-IP border scenes; no decoration covers more than 5% of the window.

ALPHA:
central photo window fully transparent; exterior beyond the outer frame fully transparent; only the frame and attached art opaque.

STYLE:
Mengli mini pen-doodle, wobbly broken contours, awkward hand-drawn geometry, clean flat normally saturated theme colors, slight selected-edge misregistration.

TEXT:
NONE

No white background, filled center, photo placeholder, checkerboard, logo, watermark, copied character, digital typography, 3D frame mockup, cast-shadow surface, hand holding the frame, or identity drift.
```

## Validate

Check exact 3:4 ratio, theme, accepted identity, 58–68% central window, four-side balance, no important art blocking the photo area, and actual alpha in both center and exterior. Inspect the PNG alpha channel rather than trusting a checkerboard preview. Keep accepted frames and repair only the failing theme.
