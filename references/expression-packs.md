# Personal-IP expression packs

Use this route for 表情包、反应图、reaction images, or a themed emotion series.

## Ask for the series first

If the user has not supplied a series concept, theme, or communication context, ask one concise question before planning. Examples: creator support, workplace survival, study, parenting, fitness, fandom, travel, customer service, or daily chat.

If the user explicitly asks for a default/general pack, use:

1. happy
2. laughing
3. heart or affection
4. thanks
5. okay or approval
6. cheer or celebration
7. shocked
8. confused
9. angry
10. upset
11. crying
12. tired or sleepy

## Output

- Default to 12 separate 1:1 images, one generation call per expression.
- Keep the outer canvas pure white and preserve a clear white margin on every side.
- Use a head, bust, half-body, or small full-body crop according to the expression, while preserving the complete identifying hair/fur/ears.
- Make action, face, hands, and one or two emotion marks carry the meaning.
- Make the character-and-essential-prop group occupy roughly **45–70%** of the canvas so the reaction remains readable at chat-thumbnail size.
- Across a default 12-image pack, use a **compact irregular micro-scene patch in 4–6 images** and a clean white cutout composition in the others. A micro-scene may be a broken-edged patch of floor, desk, grass, cloud, bed, window light, or another theme-specific setting.
- Keep every micro-scene local and subordinate: it must have an organic, asymmetrical outer edge, occupy no more than about 45% of the canvas, and leave at least about 12% clear white margin around the overall composition. Never use a full-bleed background, rectangular card, circular badge, or framed panel.
- Use the same Mengli broken-pen contours and clean flat palette inside the micro-scene. Do not switch to painterly scenery, gradients, or unrelated clip art.
- Use no text by default. Add only short exact copy required by the chosen series.
- Vary crop, gesture, and silhouette across the pack without changing identity or outfit cues.
- Do not merge the 12 expressions into one sheet unless the user requests a contact sheet.

## Keep distinct from article mini illustrations

- Expression packs are **reaction-first**: the face, hands, and emotional action must read immediately, and the character is comparatively large.
- Article mini illustrations are **idea-first**: the complete character-and-prop scene stays around 20–35% of the canvas and visualizes one source idea with much more white space.
- A micro-scene in an expression image only supplies emotional context. It must not become a detailed narrative scene, infographic, or article illustration.

## Manifest

Before generating, lock all 12 items with expression, action, crop, essential prop, emotion marks, background mode (`WHITE CUTOUT` or `IRREGULAR MICRO-SCENE`), scene patch content when used, and exact text or `NONE`. Avoid near-duplicates and keep the default micro-scene count between 4 and 6.

## Prompt structure

```text
Create one exact 1:1 personal-IP expression image on pure white.

SERIES:
[user-specified theme]

EXPRESSION NUMBER AND MEANING:
[n/12; exact reaction]

IDENTITY LOCK:
[accepted anchor fidelity lock]

ACTION, CROP, AND MARKS:
[gesture, head/bust/half/full-body crop, zero to two relevant marks or props]

BACKGROUND MODE:
[WHITE CUTOUT, or IRREGULAR MICRO-SCENE: exact small setting patch with organic broken edge]

STYLE:
Mengli mini pen-doodle, hesitant broken black contours, awkward hand-drawn shapes, clean flat normally saturated colors with slight selected-edge misregistration.

TEXT:
[NONE or exact locked short copy]

Pure white outer canvas; character-and-prop group occupies about 45–70%; complete silhouette; nothing cropped. If background mode is IRREGULAR MICRO-SCENE, keep it local, asymmetrical, below about 45% of the canvas, and surrounded by clear white margin. No full-bleed environment, rectangular card, circular badge, frame, logo, watermark, extra character, random icon, glossy rendering, 3D, or identity drift.
```

## Validate

Check exact 12-count set, distinct meanings, theme coherence, identity stability, complete silhouette, 45–70% character scale, readable emotion at small size, and no invented text. For a default pack, verify that 4–6 images contain compact irregular micro-scenes, all others stay clean white cutouts, and every composition retains clear white outer margins. Reject full-bleed scenery, rectangular color cards, or scenes that overpower the reaction. Keep accepted images and regenerate only the failing expression.
