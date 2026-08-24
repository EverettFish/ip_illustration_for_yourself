# Personal-IP folder icons

Use this route for Mac folder icons, desktop folder artwork, or transparent personal-IP folder graphics.

## Default set

- Unless the user specifies another count, generate **four separate folder icons**, one generation call per icon.
- Treat the user's folder purpose as one umbrella theme, then create four genuinely different concepts rather than four color swaps:
  1. IP peeking from the top opening with one tiny theme prop
  2. IP leaning or sitting on one folder edge in a different silhouette
  3. IP emerging from behind the front lip with a small action
  4. IP integrated into a simple front-panel mini scene
- Vary folder color, IP pose, integration position, silhouette direction, and one small thematic prop while preserving the same accepted anchor and 4:3 folder geometry.
- If the user provides several folder categories, distribute the four icons across those categories instead of inventing unrelated ones.
- Prepare a four-item manifest before generation. Record folder purpose, palette, character pose, integration method, tiny prop, and `TEXT: NONE` for every icon; reject near-duplicates.

## Layout references

Use these only for folder geometry and IP integration:

- `folder-icon/folder_icon_ref_01_character-folders.jpg`
- `folder-icon/folder_icon_ref_02_desktop-icons.jpg`
- `folder-icon/folder_icon_ref_03_clean-shape.jpg`

Ignore every example character, word, desktop label, screenshot UI, and background color.

## Output geometry

- Generate a genuine transparent PNG on an exact **4:3 landscape canvas**.
- Keep a recognizable macOS-like folder silhouette: shallow back layer with an upper-left tab, rounded front pocket, and clear top opening or lip.
- Let the complete folder occupy about 78–90% of the canvas with even transparent margins.
- Keep the folder dominant. Integrate the accepted IP as one coherent part of the icon, normally 20–45% of the folder height.
- Good integrations: peeking from behind the front lip, emerging from the top opening, leaning over one edge, printed as a simple front-panel illustration, or interacting with one tiny folder-theme prop.
- Do not place a separate white-bordered sticker on top of the folder.
- Use no text or label by default. Infer the folder theme from context; ask one concise question only when no purpose or motif is available.
- Use clean normal saturation and a limited palette derived from the anchor plus the requested folder category.

## Prompt structure

```text
Create one transparent 4:3 landscape personal-IP folder icon.

SET ITEM:
[n/4; distinct concept name]

IDENTITY LOCK:
[accepted anchor fidelity lock]

FOLDER PURPOSE OR THEME:
[study/work/travel/photos/finance/etc.]

GEOMETRY:
strict 4:3 transparent canvas; recognizable rounded folder with a shallow rear layer, upper-left tab, front pocket, and clear top lip; folder fills 78–90% with even transparent margins.

IP INTEGRATION:
[peeking/emerging/leaning/front-panel scene], visibly connected to the folder rather than floating above it. Keep the folder dominant.

STYLE:
Mengli mini pen-doodle identity on a simplified clean folder shape; wobbly broken pen details inside the character; clean flat normally saturated folder colors; no separate sticker halo.

TEXT:
NONE

Genuine transparent background. No desktop screenshot, square tile, white rectangle, label, logo, watermark, cast-shadow floor, glossy 3D mockup, extra character, or crop.
```

## Validate

Check exact 4:3 ratio, real alpha outside the folder, clear tab/front-pocket geometry, even margins, integrated anchor identity, category readability without text, and absence of white fringe, screenshot background, or floating sticker treatment. At set level, verify four separate icons by default, with four distinct poses and integration methods; changing only the folder color does not count as variation.

## Always tell the user how to apply it on Mac

1. Open the final transparent PNG in Preview.
2. Press `Command+A`, then `Command+C`.
3. In Finder, select the target folder and press `Command+I`.
4. Click the small folder icon in the upper-left of the Info window so it gains a highlight.
5. Press `Command+V`.
6. To restore the default icon later, select that small icon again and press `Delete`.

## Windows version only when requested

Windows needs a square icon asset. Run:

```text
python scripts/make_windows_icon.py --input folder-4x3.png --png folder-square.png --ico folder.ico
```

This centers the transparent 4:3 artwork on a transparent 1:1 canvas without stretching and writes common ICO sizes. Then tell the user: right-click the folder → Properties → Customize → Change Icon → choose the `.ico` file.
