# Real-photo IP fusion

Use this route when the user uploads real photographs from a store, exhibition, trip, event, street, restaurant, or other location and asks to integrate the accepted personal IP.

The required outcome is a newly generated **final fused photograph**, not a transparent character asset for the user to assemble later. Treat the supplied photograph as the primary edit target and the accepted anchor as the only identity source.

## Layout references

Use these as interaction, placement, and scale references only:

- `photo-fusion/photo_fusion_ref_01_store-display.jpg`
- `photo-fusion/photo_fusion_ref_02_blackboard.jpg`
- `photo-fusion/photo_fusion_ref_03_corridor.jpg`

They demonstrate a mini illustrated character responding to a photographed place and feeling grounded inside it. Do not copy their characters, brands, signs, text, merchandise, or venue content.

## Non-negotiable fusion rule

The character must **interact with the real photographed environment**. Do not fulfill this route by generating a complete transparent character and pasting it over the photograph.

Every accepted result needs:

1. **one specific scene interaction** tied to visible photo content, such as leaning on a railing, sitting on a step, peeking from behind a display, holding a door handle, pointing at a real sign, examining an exhibit, reaching toward food, or standing partly behind foreground furniture; and
2. **at least two physical integration cues**, chosen from foreground occlusion, feet or body contacting a real surface, contact shadow, reflection, perspective match, local light direction, or local color-temperature match.

Generic standing, waving, or posing counts only when the character is visibly responding to a specific object or spatial feature. A fully visible clean-edged figure floating above the scene, even with a small shadow, is an overlay and must be rejected.

## Photograph-preservation boundary

- Preserve the original crop, dimensions, orientation, camera viewpoint, and overall composition.
- Preserve faces, bodies, products, artwork, architecture, signs, logos, and readable text outside the planned interaction zone.
- Do not globally repaint, relight, blur, extend, retouch, clean up, translate, or redesign the photograph.
- Permit localized edits only where the IP enters the scene and where occlusion, contact shadow, reflection, or object interaction requires them.
- Compare the result with the source and reject material drift in unrelated regions. The goal is a localized scene edit, not a regenerated approximation of the whole photo.

## Direct fusion workflow

1. Inspect the real photograph and choose one visible **interaction anchor**: a surface, prop, architectural edge, exhibit, sign, doorway, food item, piece of furniture, or other scene element.
2. Write an interaction contract before generation: `[character action] + [specific real object] + [front/behind relation] + [contact point] + [light/shadow/reflection cue]`.
3. Avoid covering a face, important sign, artwork, product, or the photograph's primary subject unless the user's requested interaction requires it.
4. Measure the photo height and plan the visible IP height. Default to 22–26% of final photo height, then adjust within the allowed range for perspective and the interaction anchor.
5. Use the supplied photograph as the actual image-edit target. Generate the character **inside the photo in one integrated edit**, using the accepted anchor for identity and the photo for perspective, scale, occlusion, contact, light direction, and color temperature.
6. Inspect the generated composite at final delivery size. If identity, interaction, or preservation fails, make one targeted edit to the failed region while retaining the source photograph and accepted areas.
7. Save one final composite per input photo unless the user requests a collage.
8. Render or attach every accepted final composite in the response. Do not stop after producing a prompt, edit plan, transparent IP layer, or local path.

Do not use ordinary alpha compositing or a complete cutout pasted over the source as the final route output. An intermediate mask or character study may be used internally only when the final tool call still performs a localized generative edit that creates real scene interaction.

## Scale and visual integration

- Keep the IP clearly illustrated rather than photorealistic.
- Match the photo's perspective, eye line, camera angle, and ground plane.
- Measure scale by the visible character from head or hat to feet, excluding shadow and reflection.
- Keep that visible character height at **18–30% of the final photo height** by default, aiming for **22–26%** in ordinary scenes.
- For an intentionally distant panoramic or very wide venue, use **16–22%** only when the character remains immediately readable. Do not go below 16% or above 32% unless the user explicitly requests a tiny or dominant figure.
- Judge the result at the final delivered size: the face, anchor hairstyle, pose, and interaction must be readable without zooming, while the IP must not dominate the venue or cover its primary subject.
- Make the front/behind relationship unambiguous. When a railing, counter, plant, seat, doorframe, shelf, or other object should cross in front of the IP, preserve that occlusion instead of drawing the whole character on top.
- Place feet, hands, or the seated body on the chosen photographed surface and align the contact angle with that surface.
- Match local light direction and warmth. Add only the shadow or reflection that the photographed material and lighting justify.
- Use one IP appearance per photo unless the user asks for a group or narrative sequence.
- Keep props minimal and derive them from the actual visit.

## Direct-edit prompt structure

```text
Edit the supplied real photograph into one final integrated real-photo/IP composite.

REFERENCE ROLES:
- [real photo] is the primary edit target. Preserve its crop, dimensions, viewpoint, overall composition, and all content outside the localized interaction zone.
- [anchor] is the only identity source for the illustrated character.
- [style refs] control the Mengli pen-doodle finish only.

IDENTITY LOCK:
[accepted anchor fidelity lock]

INTERACTION CONTRACT:
[character action] + [specific visible scene object] + [what passes in front or behind] + [exact contact point] + [local shadow/reflection/light cue]

CAMERA AND SCALE:
[front/three-quarter/back view, eye line, ground-plane angle, local light direction]
visible IP height = [planned percent]% of final photo height, approximately [planned pixels] px; keep within the route's 18–30% default range

LOCAL EDIT BOUNDARY:
Change only the character's occupied region and the minimal pixels required for convincing occlusion, contact shadow, reflection, or object interaction. Keep faces, signs, text, products, artwork, architecture, and all unrelated photo regions unchanged.

OUTPUT:
one complete final composite photograph at the source dimensions, with the Mengli character generated into and interacting with the real scene.

STYLE:
Mengli mini pen-doodle character, wobbly broken black contours, awkward hand-drawn shapes, clean flat normally saturated colors with slight selected-edge misregistration; preserve the photographic appearance of the real scene.

Reject a transparent cutout look, white fringe, sticker halo, floating pose, complete character pasted above foreground objects, generic interaction, scene recreation, extra person, invented logo or text, watermark, glossy rendering, or 3D character.
```

## Validate

Check:

1. the delivered asset is the visible final composite, not an overlay, prompt, or assembly instruction
2. source dimensions, crop, viewpoint, and overall composition are preserved
3. the character performs one specific action with a visible photographed object or surface
4. at least two physical integration cues are convincing, including a clear contact or front/behind relationship
5. IP identity matches the accepted anchor
6. measured visible IP height is normally 18–30% of photo height and close to the planned target
7. no face, sign, artwork, product, or primary subject is unnecessarily covered or distorted
8. unrelated photo regions have no material repainting, relighting, translation, or cleanup
9. there is no white fringe, sticker halo, floating figure, or uniformly sharp pasted-cutout boundary
10. every accepted composite is rendered or attached in the final response

If scale alone fails, make a localized edit that preserves the interaction geometry. If interaction or occlusion fails, regenerate that local scene relationship; do not fall back to ordinary cutout compositing.
