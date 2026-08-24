# Real-photo IP fusion

Use this route when the user uploads real photographs from a store, exhibition, trip, event, street, restaurant, or other location and asks to integrate the accepted personal IP.

## Layout references

Use these as placement and scale references only:

- `photo-fusion/photo_fusion_ref_01_store-display.jpg`
- `photo-fusion/photo_fusion_ref_02_blackboard.jpg`
- `photo-fusion/photo_fusion_ref_03_corridor.jpg`

They demonstrate a mini illustrated character standing in an open foreground area, looking at the exhibit, and feeling grounded in the photograph. Do not copy their characters, brands, signs, text, merchandise, or venue content.

## Non-negotiable background rule

Treat the user's photograph as immutable:

- preserve every original pixel outside the added IP overlay
- preserve the original crop, dimensions, orientation, perspective, lighting, color, contrast, text, faces, products, architecture, reflections, and signage
- do not repaint, relight, blur, extend, retouch, remove, translate, or regenerate the photograph
- do not replace visible brands or copyrighted exhibit art

The only allowed change is the added Mengli IP overlay and transparent pixels belonging to its tiny contact shadow or reflection.

## Preferred two-step workflow

1. Inspect the real photo and identify one open floor or foreground area that does not cover a face, important sign, artwork, product, or path.
2. Measure the photo height and write a numeric target for the visible IP height before generation. Default to 22–26% of final photo height, then adjust within the allowed range for perspective and available floor space.
3. Plan a pose that reacts to the actual scene: looking up, pointing, taking a photo, holding a ticket, reading a panel, carrying a shopping bag, or waving beside the location.
4. Generate the IP as a **transparent PNG cutout**, using the accepted anchor as identity reference and the photo only as perspective, pose, scale, light-direction, and color-temperature context.
5. Include a tiny soft contact shadow or faint floor reflection inside the transparent overlay only when the surface needs grounding.
6. Place the transparent overlay over the untouched original with `scripts/composite_overlay.py`.
7. Measure the composited character bounding box. Resize or reposition the accepted overlay when the measured visible height misses the planned range; do not regenerate the photograph.
8. Save one composite per input photo unless the user requests a collage.

Use direct photo-edit mode only when the user explicitly needs complex occlusion behind a fixed object. In that case, repeat the immutable-background rule in the prompt and compare the result against the source before acceptance.

## Scale and integration

- Keep the IP clearly illustrated rather than photorealistic.
- Match the photo's perspective, eye line, camera angle, and ground plane.
- Measure scale by the visible character from head or hat to feet, excluding transparent padding, contact shadow, and reflection.
- Keep that visible character height at **18–30% of the final photo height** by default, aiming for **22–26%** in ordinary scenes.
- For an intentionally distant panoramic or very wide venue, use **16–22%** only when the character remains immediately readable. Do not go below 16% or above 32% unless the user explicitly requests a tiny or dominant figure.
- Judge the result at the final delivered size: the face, anchor hairstyle, pose, and interaction must be readable without zooming, while the IP must not dominate the venue or cover its primary subject.
- Place both feet or the seated body on a plausible surface.
- Match only local light direction and warmth. Do not add dramatic global lighting.
- Use one IP appearance per photo unless the user asks for a group or narrative sequence.
- Keep props minimal and derived from the actual visit.
- Do not cover the primary subject of the photograph.

## Overlay prompt structure

```text
Create a transparent-background Mengli personal-IP overlay for compositing onto the supplied real photograph.

REFERENCE ROLES:
- [anchor] is the only identity source.
- [real photo] is immutable scene context for camera angle, ground plane, scale, pose, and light direction only. Do not reproduce the photograph in the output.
- [style refs] control pen-doodle finish only.

IDENTITY LOCK:
[accepted anchor fidelity lock]

POSE AND INTERACTION:
[exact reaction to the real scene]

CAMERA MATCH:
[front/three-quarter/back view, eye line, floor angle, local light direction, approximate scale]

SCALE TARGET:
visible IP height = [planned percent]% of final photo height, approximately [planned pixels] px after compositing; keep within the route's 18–30% default range

OUTPUT:
one isolated complete IP cutout on genuine transparent alpha; include only a subtle contact shadow or faint reflection if specified; nothing cropped.

STYLE:
Mengli mini pen-doodle, wobbly broken black contours, awkward hand-drawn shapes, clean flat normally saturated colors with slight selected-edge misregistration.

No photo background, rectangle, white field, scene recreation, extra person, logo, text, watermark, glossy rendering, or 3D.
```

## Composite command

```text
python scripts/composite_overlay.py --background PHOTO --overlay IP.png --out RESULT.png --x X --y Y --width W
```

Choose `X`, `Y`, and `W` from the planned open area. The script preserves the source dimensions and reports whether pixels outside the overlay rectangle remained unchanged.

## Validate

Check:

1. source photo dimensions and crop are unchanged
2. background outside the overlay rectangle is pixel-identical
3. IP identity matches the anchor
4. measured visible IP height is normally 18–30% of photo height and close to the planned target; the figure is readable without zooming but does not dominate the photo
5. no face, sign, artwork, or product is unnecessarily covered
6. no white rectangle or cutout fringe surrounds the IP
7. the photo itself was not repainted, relit, translated, or cleaned up

If scale alone fails, keep the accepted overlay and change only its composite width and position. Repair the transparent overlay or its placement rather than regenerating the photograph.
