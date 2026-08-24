# Personal-IP scene avatars

Use this route for square personal-IP avatars, profile images, or small shoulder-up theme portraits.

## Default set

Unless changed by the user, generate four separate 1:1 images, one call per theme:

1. **Coffee**: shoulder-up IP holding or sipping a coffee; warm relaxed expression
2. **Work**: upper torso with hands holding or working behind a small plain unbranded laptop; focused expression
3. **Sleep**: head and shoulders resting on a pillow, sleepy expression, exact small mouse-drawn `Zzz`
4. **Heart**: shoulder-up heart-hands or holding one heart; warm supportive expression

## Composition

- Use exact 1:1 with pure white background.
- Frame shoulders and above by default; allow a small amount of upper torso or hands when needed for the prop.
- Keep the complete anchored hair, fur, ears, horns, glasses, or other identifying head geometry visible.
- Center the face and keep safe margins; do not crop crown, ears, hair tips, hands, or theme prop.
- Let props occupy the lower 15–30% without covering the eyes or changing face recognition.
- Keep the image simple enough to read at avatar size.
- Use no scene background, frame, circle crop, logo, or shadow.

## Prompt structure

```text
Create one exact 1:1 personal-IP scene avatar on pure white.

IDENTITY LOCK:
[accepted anchor fidelity lock; complete hairstyle/fur/ears visible]

THEME AND ACTION:
[Coffee / Work / Sleep / Heart scene]

CROP:
shoulders and above, with only enough upper torso and hands for the prop; centered face; complete crown and side hair; generous safe margin; nothing cropped.

STYLE:
Mengli mini pen-doodle, wobbly broken black contours, awkward hand-drawn shapes, clean flat normally saturated colors with slight selected-edge misregistration.

TEXT:
[NONE, except exact naive mouse-drawn Zzz for Sleep]

Pure white background. No environment, frame, gradient, logo, watermark, extra character, glossy anime, 3D, large prop hiding the face, or identity drift.
```

## Validate

Check 1:1 ratio, pure white background, shoulder-up crop, complete identifying head silhouette, readable theme at small size, unobscured face, correct `Zzz` only on Sleep, and no extra text. Keep accepted avatars and repair only the failing theme.
