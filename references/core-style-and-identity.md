# Core style and identity

Read this file for every route.

## Approved style references

Use these images only for mark-making, geometry, and mini proportions:

- `style/style_ref_01_user_docs_reader.png`
- `style/style_ref_02_user_searcher.png`
- `style/style_ref_03_user_catgirl_anchor.png`

Use the first two for sparse composition, broken pen contours, and loose line-to-fill registration. Use the third only for mini proportions and facial simplification. Never copy its cat ears, green hair, outfit, palette, or other identity traits. Omit it whenever it could be confused with the target.

Treat style references as geometry references, not palette references. The user's identity and colors always win.

## Mengli style lock

Aim for a mini pen-doodle illustration:

- Use thin-to-medium black pen-like outlines with natural wobble, uneven pressure, small hesitations, and several irregular breaks.
- Keep major forms readable without sealing every contour. Break lines around hair tips, sleeves, hands, shoes, props, and turning points; never create a uniform dashed outline.
- Use awkward, gently asymmetrical hand-drawn shapes rather than vector-perfect curves.
- Keep flat color interiors clean and even, while selected edges sit slightly loose against the outline through a narrow white sliver, tiny shortfall, or small overhang.
- Keep the mismatch visible at normal size but small enough to preserve identity and legibility.
- Limit the number of colors without desaturating them. Preserve natural skin, neutral blacks, and clear signature colors.
- Keep facial features tiny and expressive. Use motion marks, sweat drops, stars, or emotion marks only when they clarify the action.
- Keep the character mini and the result childlike, relaxed, and quietly funny rather than glossy or commercial.

Avoid:

- glossy anime, 3D, vector-perfect rendering, polished commercial line art
- continuous perfectly closed contours or uniformly dashed outlines
- watercolor, broad crayon, oil-pastel, chalk, dry-brush, grainy, streaky, or mottled fills
- faded, dusty, muddy, gray-brown, beige, vintage, or washed-out casts
- dramatic lighting, gradients, dense scenery, random icons, invented text, logos, or watermarks

Use this phrase in generation prompts:

> mini pen-doodle illustration, hesitant wobbly black pen contours with clearly visible irregular breaks, awkward hand-drawn shapes, internally clean flat color shapes deliberately slightly misregistered from selected outlines with tiny white slivers or small edge overhangs, normal clear saturation, limited color count, childlike messy-cute charm; broken but not uniformly dashed, misregistered but still legible

## Extract the identity

Record only visible or user-confirmed traits:

- hair or fur outer silhouette, crown tufts, part, bangs, side locks, and back length
- face shape, eye shape and color, skin or body color, and signature expression
- ears, horns, tail, glasses, hat, jewelry, or other identifying geometry
- clothing, shoes, accessories, and signature colors
- body proportions and the silhouette that must remain stable
- fixed traits versus scene-dependent traits

Ignore captions, QR codes, backgrounds, products, and watermarks unless the user asks to preserve them. Resolve conflicts with the latest explicit user instruction, then the clearest repeated visible trait.

## Build and accept the anchor

When no accepted anchor exists, create:

1. one 1:1 front-facing full-body anchor on pure white
2. one horizontal front/side/back turnaround sheet

Keep clothing, colors, accessories, face, hair, and proportions identical across views. Do not add view labels unless requested.

Use this prompt structure:

```text
Create a 1:1 front-facing full-body personal-IP anchor.

REFERENCE ROLES:
- [identity image] is the only identity source and overrides every other reference.
- [style images] control pen-doodle mark-making only; do not borrow their characters or palette.

IDENTITY LOCK:
[exact visible hair/fur, face, eyes, body, outfit, accessories, proportions, palette, and traits that must never change]

STYLE:
mini pen-doodle illustration, hesitant wobbly black pen contours with clearly visible irregular breaks, awkward hand-drawn shapes, internally clean flat color shapes deliberately slightly misregistered from selected outlines with tiny white slivers or small edge overhangs, normal clear saturation, limited color count, childlike messy-cute charm.

POSE:
front-facing full-body, simple relaxed stance, small expressive face.

COMPOSITION:
pure white square canvas; complete character occupies about 25–35%; generous margins; nothing cropped.

No text, logo, watermark, scenery, shadow, extra character, invented accessory, glossy rendering, 3D, or vector-perfect linework.
```

## Anchor-fidelity lock

After acceptance, write a compact lock and reuse it verbatim. Include exact hairstyle geometry rather than only color and length. For head-only outputs, keep the complete hair or fur mass and identifying ears or accessories. For themed clothing, preserve the fixed face, hair, body proportions, signature colors, and identifying accessory unless the user explicitly approves a change.

## Core validation

Check:

1. identity matches the source and accepted anchor
2. no borrowed trait from a style or layout reference
3. complete silhouette and required crop
4. wobbly broken pen contours in multiple locations
5. slightly loose but legible fill registration
6. clean normal saturation without a muddy cast
7. no unwanted text, logo, watermark, or extra character

Repair only the failing dimension. Never accept a technically attractive output with identity drift.
