---
name: ip-illustration-character-system
description: Build a reusable personal IP character and create consistent mini pen-doodle visuals, including article illustrations and information-rich 3:4 article infographics with an automatically selected page count. Use when the user asks to establish a mascot, make a turnaround sheet, illustrate a long article, create cute knowledge cards or infographics, visualize timelines, processes, comparisons, or data, or keep one IP character consistent across multiple images. Require Codex with GPT Image 2 for direct generation; otherwise hand off a complete prompt package and the official GPT Image 2 API links.
---

# IP Mini Illustration System

## Attribution

Author: **everettfish**

Create a consistent personal character and use it in sparse, cute article illustrations. Use `gpt-image-2` only.

## 0. Check the runtime before doing image work

Treat direct generation as available only when both conditions are true:

1. The skill is running inside Codex.
2. A callable image-generation tool explicitly supports or uses `gpt-image-2`.

Do not infer GPT Image 2 support from a generic image tool name. Do not silently substitute another model.

If either condition fails:

- Do not attempt image generation.
- Finish the useful preparation work: character anchor, storyboard, and complete prompts.
- Tell the user:

  > 当前环境不是 Codex，或没有可用的 GPT Image 2，因此无法按本 Skill 直接生图。请改用 OpenAI GPT Image 2 生图 API，并把下面整理好的提示词与参考图作为输入。

- Include both official links:
  - GPT Image 2 model: https://developers.openai.com/api/docs/models/gpt-image-2
  - Image generation API guide: https://developers.openai.com/api/docs/guides/image-generation

Stop after delivering the prompt package unless the user supplies a confirmed GPT Image 2 route.

## 1. Load the approved style references

Use only these packaged images as style anchors:

- `references/style/style_ref_01_user_docs_reader.png`
- `references/style/style_ref_02_user_searcher.png`

They define style, composition, and finish—not the user's character identity. Uploaded character images take precedence for identity.

Do not use generated examples, prior rejected outputs, or unrelated character samples as style references.

## 2. Apply the style lock

Aim for a **mini pen-doodle illustration on a large white canvas**:

- Keep the character and props small, usually occupying 20–35% of the canvas.
- Preserve abundant empty white space.
- Use thin-to-medium black pen-like outlines with natural wobble, small hesitations, and occasional tiny breaks.
- Make shapes slightly awkward and asymmetrical, as if drawn by hand with imperfect control.
- Use simple, clean, flat color fills in a restrained palette.
- Allow only tiny edge gaps or slight fill-to-line misalignment; keep the color surfaces clean.
- Keep facial features tiny and expressive.
- Add sweat drops, motion marks, emphasis lines, or small emotion marks only when they improve the scene.
- Prefer one character plus one to three essential props.
- Keep the result cute, childlike, loose, and quietly funny rather than polished or formal.

Avoid:

- crayon, oil-pastel, chalk, watercolor, or dry-brush texture
- mottled, grainy, streaky, or heavily variegated color blocks
- glossy anime rendering, 3D rendering, vector-perfect curves, or polished commercial line art
- large characters filling the frame
- dense scenery, decorative clutter, dramatic lighting, shadows, gradients, or textured backgrounds
- random objects that do not communicate the source material
- text, letters, numbers, labels, logos, watermarks, or UI unless explicitly requested

Use this core phrase in each prompt:

> mini pen-doodle illustration, tiny subject on a large pure-white canvas, naturally wobbly and slightly broken black pen outlines, awkward hand-drawn shapes, clean flat color fills with only subtle edge gaps, sparse composition, childlike messy-cute charm

## 3. Build the character identity

Use this workflow when the user uploads one or more character references.

### Extract the anchor

Record only visible or user-confirmed traits:

- hair shape and color
- face, eyes, skin tone, and signature expression
- clothing, shoes, accessories, and signature colors
- silhouette and chibi proportions
- traits that must never change
- optional traits that may vary by scene

Ignore QR codes, captions, backgrounds, and unrelated objects unless the user asks to preserve them. If references conflict, use the user's latest explicit instruction; otherwise preserve the clearest repeated traits.

### Generate the identity set

Create:

1. One front-facing full-body character anchor on pure white.
2. One horizontal front/side/back turnaround sheet.

Keep the character small and preserve identical clothing, colors, accessories, and proportions across all views. Do not add view labels unless requested.

### Character anchor prompt

```text
Create a 1:1 character anchor using GPT Image 2.

STYLE: mini pen-doodle illustration, tiny subject on a large pure-white canvas, naturally wobbly and slightly broken black pen outlines, awkward hand-drawn shapes, clean flat color fills with only subtle edge gaps, sparse composition, childlike messy-cute charm.

CHARACTER IDENTITY: [fixed visible traits]
POSE AND EXPRESSION: front-facing full-body, simple relaxed pose, [expression].
COMPOSITION: character occupies about 25–35% of the canvas; generous white space on all sides.

Preserve the uploaded character's identity exactly. No text, labels, logo, watermark, scenery, brush texture, crayon texture, or mottled fills.
```

## 4. Create long-article illustrations

Default to five images unless the user specifies another count.

### Read for meaning before drawing

1. Identify the article's thesis, emotional arc, and concrete examples.
2. Select distinct visual beats that collectively explain the article.
3. Map each beat to the exact passage or idea it represents.
4. Turn each beat into one immediately readable scene or visual metaphor.
5. Vary actions, props, scale, and emotional tone while preserving character identity.

Do not split the article mechanically by paragraph. Do not default to generic scenes such as repeatedly reading papers, pointing at icons, or standing beside devices. Every illustration must make sense as a visual answer to a specific idea in the article.

Before generation, prepare a compact storyboard with:

- image number
- source idea
- visual scene
- character action/expression
- essential props

If the user asked to generate images, proceed after this internal check without asking for confirmation unless a character reference or decisive article content is missing.

### Article illustration prompt

```text
Create a 1:1 article illustration using GPT Image 2.

STYLE: mini pen-doodle illustration, tiny subject on a large pure-white canvas, naturally wobbly and slightly broken black pen outlines, awkward hand-drawn shapes, clean flat color fills with only subtle edge gaps, sparse composition, childlike messy-cute charm.

CHARACTER IDENTITY: [repeat the fixed anchor traits precisely].
ARTICLE IDEA: [the exact idea this image communicates].
SCENE: [one concrete action or visual metaphor].
EXPRESSION: [small readable expression].
PROPS: [one to three essential objects only].
COMPOSITION: the complete scene occupies about 20–35% of the canvas with abundant white space; nothing cropped.

No text, letters, numbers, labels, logo, watermark, UI, dense background, painterly texture, crayon texture, oil-pastel texture, mottled fills, gradients, or glossy shading.
```

Pass the packaged style references and the user's character anchor as image references whenever the tool supports referenced images.

## 5. Create 3:4 article infographics

Use this attached workflow when the user asks for an information graphic, knowledge card, data card, article summary poster, or 3:4 long-form visual. Keep ordinary article illustrations in section 4 sparse and text-free; switch to this workflow only when information graphics are requested.

### Use the layout references correctly

Load these images as **layout and information-architecture references only**:

- `references/infographic-layout/layout_ref_01_annotated_evidence.png`
- `references/infographic-layout/layout_ref_02_timeline_dashboard.png`
- `references/infographic-layout/layout_ref_03_data_story.png`

Borrow their useful structures: strong title hierarchy, annotated evidence, numbered steps, timelines, comparison cards, compact charts, handwritten arrows, color-coded callouts, and a small IP guide character. Do not copy their rendering texture, exact content, logos, screenshots, brand marks, or character designs.

Apply this precedence:

1. The user's character anchor controls identity.
2. The two approved style images in `references/style/` control drawing style.
3. The three infographic images control layout ideas only.

### Choose the number of images automatically

Extract distinct information modules before designing pages. Count a thesis, process, timeline, comparison, case cluster, data story, checklist, framework, and conclusion as separate modules when each needs its own visual explanation.

Target four to six readable modules per 3:4 page:

- 1–5 modules: 1 image
- 6–10 modules: 2 images
- 11–15 modules: 3 images
- 16–20 modules: 4 images
- 21–30 modules: 5–6 images
- More than 30 modules: keep at most 8 images and merge or omit lower-priority repetition

Increase the page count instead of shrinking text or overloading a page. Use fewer pages when modules can be understood as one timeline, one process, or one coherent data story. Do not force a fixed count.

### Plan the infographic series

Give each page one clear communication job. Select the best layout for its content:

- overview or framework: title + thesis + 3–6 concept cards
- process: numbered steps with arrows and a start-to-finish path
- timeline: chronological rail with dated events and short outcomes
- comparison: two or three columns with matched criteria
- data story: one primary chart, exact callouts, and brief interpretation cards
- evidence or case page: central artifact or fact cluster with annotated arrows
- checklist or guide: grouped actions, warnings, and completion cues
- conclusion: distilled takeaway, action prompt, and expressive IP scene

Prepare a page plan containing:

- page number and communication goal
- exact title and subtitle
- information blocks in reading order
- layout type and visual hierarchy
- chart, timeline, or diagram requirements
- IP action, expression, outfit, and props
- exact text manifest

### Keep information rich but readable

- Use a 3:4 portrait canvas.
- Use a clean white or very lightly warm-white background with no paper grain.
- Establish a clear top-to-bottom reading path.
- Use one main title, one short subtitle, and several compact information blocks.
- Draw the main title and major section headings like hand-lettered **fine wax crayon or colored pencil**: slightly dry edges, faint paper-catching gaps inside the strokes, uneven pressure and opacity, and tiny baseline drift. Keep the strokes narrow rather than chunky.
- Keep body copy readable with a loose black marker or pen feel. Do not render any heading or body copy like a typeset digital font.
- Prefer short labels, numbers, dates, and concise sentences over paragraphs.
- Use visibly imperfect hand-drawn boxes, arrows, underlines, circles, stars, and color-coded accents. Make borders wobble, vary line weight, overshoot corners, leave occasional tiny openings, and sometimes show a faint second-pass line. Avoid identical rounded rectangles or mechanically aligned cards.
- Let selected title underlines, arrows, border accents, and emphasis marks share the same fine-crayon trace; keep large color surfaces clean and flat.
- Use a restrained accent palette, usually three to five colors plus black.
- Keep charts honest: preserve values, units, order, scale direction, and source notes supplied by the article.
- Leave breathing room between sections even when the page is information rich.
- Do not invent facts, dates, quotes, brands, sources, or metrics.

### Integrate the IP character meaningfully

Use one primary mini IP appearance or up to three small appearances per page. Make each pose contribute to understanding: point at a trend, compare two options, inspect evidence, walk along a timeline, demonstrate a step, carry a relevant tool, think, warn, or celebrate.

Adapt clothing and handheld props to the information context while preserving the anchor's face, hair, silhouette, signature colors, and identifying accessories. Examples include a lab coat for research, a hard hat for architecture, travel clothing for a route guide, or presentation attire for a business framework. Do not repeat the same pose and outfit mechanically across a series.

Keep the IP secondary to the information, usually occupying 8–18% of the page. Avoid a large mascot that crowds out content.

### Lock the text

Create a short exact-text manifest before generation. Copy all titles, dates, quantities, units, names, and labels from the article. Include only text that must appear; never ask the model to summarize or invent text inside the image.

When a paragraph is too long, summarize it outside the image first, verify that the meaning is preserved, then lock the shorter sentence. If exact dense text remains unreadable, split the content across more images.

### Infographic prompt

```text
Create one 3:4 portrait article infographic using GPT Image 2.

VISUAL IDENTITY: use the established IP character exactly. Preserve the fixed face, hair, silhouette, signature colors, and identifying accessories. Adapt the pose, expression, outfit, and props to this page's topic: [contextual character direction].

HOUSE STYLE: cute mini pen-doodle infographic on a clean white canvas. Render the main title and section headings with narrow fine-wax-crayon or colored-pencil strokes: subtle dry gaps, uneven pressure, slight opacity variation, and imperfect baselines. Render body copy as clear loose black marker handwriting. Use naturally wobbly and slightly broken pen outlines; boxes and arrows must look individually hand-drawn with uneven corners, small overshoots, occasional tiny openings, variable line weight, and faint second-pass traces. Use clean flat color fills and a restrained accent palette. Keep visible crayon texture limited to titles, selected border accents, arrows, and emphasis marks; never use broad crayon fill across characters or information blocks. No oil-pastel slabs, grainy color blocks, glossy rendering, digital-font perfection, identical rounded cards, or vector-perfect geometry.

PAGE GOAL: [one communication job].
LAYOUT: [overview / process / timeline / comparison / data story / evidence / checklist / conclusion].
READING ORDER: [top-to-bottom block order].
INFORMATION BLOCKS: [describe each block and its visual form].
DATA OR DIAGRAM RULES: [exact values, units, sequence, axes, relationships, or none].

RENDER THIS TEXT EXACTLY, WITH NO EXTRA WORDS:
[exact text manifest]

IP PLACEMENT: [location, action, expression, contextual outfit, relevant props], occupying about 8–18% of the page and supporting the information rather than covering it.

Make the page information rich but readable. Preserve exact facts. Do not add invented text, facts, logos, screenshots, watermarks, dense paragraphs, paper texture, or unrelated decorations.
```

Generate pages one at a time so each page can be checked before continuing.

### Validate infographic pages

Check each page for:

1. factual coverage and logical reading order
2. exact titles, names, dates, quantities, units, and labels
3. legible text without missing or invented characters
4. truthful charts, timelines, and comparisons
5. correct IP identity, context-aware action, and context-aware clothing
6. 3:4 aspect ratio and balanced information density
7. original mini pen-doodle linework with clean flat fills
8. fine-crayon title texture, loose handwritten body text, and visibly imperfect non-mechanical borders

Regenerate a page when critical text or data is wrong. Keep the accepted pages and repair only the failing page.

## 6. Validate and repair

Check every output against this order of priority:

1. It communicates the selected article idea.
2. The character identity matches the anchor.
3. The subject is mini and the white space is generous.
4. The outline feels pen-drawn, wobbly, and slightly broken.
5. Color fills are flat and clean, without crayon or brush mottling.
6. No unwanted text or clutter appears.

Regenerate a failed image with a direct correction. Use these repair clauses as needed:

- **Too large:** `Shrink the entire character-and-prop group substantially; keep it near 25% of the canvas and restore large white margins.`
- **Too polished:** `Make the black pen outline more hesitant, uneven, and occasionally broken; simplify the shapes and remove formal illustration polish.`
- **Too painterly:** `Replace every textured or mottled area with clean flat color; keep roughness only in the black outline.`
- **Too generic:** `Tie the scene directly to [article idea] using [specific action/prop]; remove unrelated decorative objects.`
- **Identity drift:** `Restore the exact anchor hairstyle, outfit, accessories, palette, face, and proportions.`

## 7. Deliver

For ordinary generated illustrations, return the images in article order with a short label explaining the source idea. For infographics, return the automatically selected page count, the page plan, and the 3:4 images in reading order. For API handoff, return the character anchor, storyboard or infographic page plan, exact text manifests, and final prompts in copy-ready form together with the two official links from section 0.
