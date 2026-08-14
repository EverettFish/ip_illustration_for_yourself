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
- `references/style/style_ref_03_user_catgirl_anchor.png`

They define style, composition, and finish—not the user's character identity. Uploaded character images take precedence for identity.

Use the first two references for sparse scene composition, visibly broken pen contours, and loose line-to-fill registration. Use the third reference for mini character proportions, facial simplification, and the same imperfect line-and-fill finish. Never borrow the third reference's cat ears, green hair, outfit, or other identity traits.

Treat all three references as **mark-making and geometry references, not color-palette references**. Do not copy their muted palette, gray cast, aging, or low saturation. The color lock in section 2 overrides their color treatment.

Do not use generated examples, prior rejected outputs, or unrelated character samples as style references.

## 2. Apply the style lock

Aim for a **mini pen-doodle illustration on a large white canvas**:

- Keep the character and props small, usually occupying 20–35% of the canvas.
- Preserve abundant empty white space.
- Use thin-to-medium black pen-like outlines with natural wobble, small hesitations, uneven pressure, and clearly visible intermittent breaks.
- Make shapes slightly awkward and asymmetrical, as if drawn by hand with imperfect control.
- Keep major contours mostly readable but not fully sealed. Leave several short, irregular gaps around hair tips, sleeves, hands, shoes, props, and other turning points. Vary gap length and placement so the contour feels hesitant, not uniformly dashed or dotted.
- Use simple flat color shapes whose interiors remain clean and even, while their edges are deliberately a little misregistered from the black outline. "Clean flat color" describes the fill surface, not perfect clipping.
- Let selected fills stop slightly short of the outline, cross it by a tiny amount, or leave a narrow white sliver. Make the mismatch noticeable at normal viewing size but small enough to preserve the object and character silhouette.
- Use a restrained palette. "Restrained" means using fewer colors, not lowering their saturation.
- Keep colors at normal, clean saturation: preserve clear hue identity, natural skin tone, solid neutral blacks, and fresh accent colors. Match the user's reference colors closely when provided.
- Prevent an overall faded, dusty, gray-brown, beige, vintage, or low-contrast cast. Do not mix gray or brown into every local color merely to make the image feel handmade.
- Repeat broken-contour and loose-registration treatment across the character and essential props; do not confine it to one decorative edge.
- Keep facial features tiny and expressive.
- Add sweat drops, motion marks, emphasis lines, or small emotion marks only when they improve the scene.
- Prefer one character plus one to three essential props.
- Keep the result cute, childlike, loose, and quietly funny rather than polished or formal.

Avoid:

- crayon, oil-pastel, chalk, watercolor, or dry-brush texture
- mottled, grainy, streaky, or heavily variegated color blocks
- uniformly desaturated, faded, dusty, muddy, grayish, brownish, beige-tinted, vintage-filtered, or washed-out palettes
- glossy anime rendering, 3D rendering, vector-perfect curves, or polished commercial line art
- continuous perfectly closed outlines around every shape, uniformly dashed outlines, or fills clipped exactly to every contour
- large sloppy paint spills, severe registration errors, missing facial features, or distortions that weaken identity and legibility
- large characters filling the frame
- dense scenery, decorative clutter, dramatic lighting, shadows, gradients, or textured backgrounds
- random objects that do not communicate the source material
- text, letters, numbers, labels, logos, watermarks, or UI unless explicitly requested

Use this core phrase in each prompt:

> mini pen-doodle illustration, tiny subject on a large pure-white canvas, hesitant wobbly black pen contours with clearly visible irregular breaks, awkward hand-drawn shapes, internally clean flat color shapes deliberately slightly misregistered from the outlines with tiny white slivers or small edge overhangs, normal clear saturation, sparse composition, childlike messy-cute charm; limited color count, not desaturated color; broken but not uniformly dashed, misregistered but still legible

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

STYLE: mini pen-doodle illustration, tiny subject on a large pure-white canvas, hesitant wobbly black pen contours with clearly visible irregular breaks, awkward hand-drawn shapes, internally clean flat color shapes deliberately slightly misregistered from the outlines, normal clear saturation, sparse composition, childlike messy-cute charm.

MARK-MAKING LOCK: keep major forms readable but do not fully seal every contour. Place several short irregular breaks around hair tips, sleeves, hands, shoes, and clothing turns; vary their length so the line never looks mechanically dashed. On selected edges, let flat fills stop slightly short, leave a narrow white sliver, or cross the outline by a tiny amount. Make this loose registration visible at normal size without becoming sloppy or damaging identity. Do not render vector-perfect closed contours or perfectly clipped fills.

COLOR LOCK: keep the reference colors clean and normally saturated. Preserve natural skin color, neutral solid blacks, and clear signature accent colors. A restrained palette means fewer colors, not faded colors. No dusty, muddy, gray-brown, beige-tinted, vintage-filtered, washed-out, or uniformly desaturated cast.

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

STYLE: mini pen-doodle illustration, tiny subject on a large pure-white canvas, hesitant wobbly black pen contours with clearly visible irregular breaks, awkward hand-drawn shapes, internally clean flat color shapes deliberately slightly misregistered from the outlines, normal clear saturation, sparse composition, childlike messy-cute charm.

MARK-MAKING LOCK: keep forms readable but do not fully seal every contour. Place several short irregular breaks across the character and essential props, especially at tips, corners, overlaps, sleeves, hands, shoes, and prop turns. Vary the breaks so the line never becomes a uniform dotted or dashed effect. Let selected flat fills stop slightly short, leave a narrow white sliver, or cross the outline by a tiny amount. Make the loose registration clearly visible at normal size without becoming sloppy. Do not use vector-perfect closed contours or perfectly clipped fills.

COLOR LOCK: keep every local color clean and normally saturated while limiting the total number of colors. Preserve the character's reference palette and use fresh, clearly distinguishable prop colors. No faded, dusty, muddy, gray-brown, beige-tinted, vintage-filtered, washed-out, or uniformly desaturated cast.

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
2. The three approved style images in `references/style/` control drawing style and line-to-fill registration, never identity or color saturation.
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
- Let selected title underlines, arrows, border accents, and emphasis marks share the same fine-crayon trace. Keep large color surfaces internally even, but let selected illustration, icon, chart, callout, and border fills sit slightly loose against their outlines through tiny white slivers or small overhangs.
- Use a restrained accent palette, usually three to five colors plus black. Restrain the number of colors, not their saturation: keep accents fresh and clearly identifiable, blacks neutral, and the IP character's reference colors normally saturated.
- Do not apply a global gray, brown, beige, vintage, faded, or low-contrast color cast to information blocks, charts, accents, or the IP character.
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

HOUSE STYLE: cute mini pen-doodle infographic on a clean white canvas. Render the main title and section headings with narrow fine-wax-crayon or colored-pencil strokes: subtle dry gaps, uneven pressure, slight opacity variation, and imperfect baselines. Render body copy as clear loose black marker handwriting. Use hesitant wobbly pen contours with clearly visible irregular breaks; boxes and arrows must look individually hand-drawn with uneven corners, small overshoots, occasional openings, variable line weight, and faint second-pass traces. Keep illustration and diagram fills internally clean and flat but deliberately slightly misregistered from selected outlines through tiny white slivers, shortfalls, or small edge overhangs. Keep forms readable and never turn the contour into a uniform dashed pattern. Do not break text strokes or misregister text enough to hurt legibility. Use a restrained accent palette. "Restrained" means three to five well-chosen accent colors, not faded color: keep every hue at normal clean saturation, keep blacks neutral, and preserve the IP character's reference colors. Keep visible crayon texture limited to titles, selected border accents, arrows, and emphasis marks; never use broad crayon fill across characters or information blocks. No dusty, muddy, gray-brown, beige-tinted, vintage-filtered, washed-out, or uniformly desaturated cast; no perfectly clipped vector fills, oil-pastel slabs, grainy color blocks, glossy rendering, digital-font perfection, identical rounded cards, or vector-perfect geometry.

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
9. normal clean saturation across the IP character, charts, accents, and information blocks, without a faded or gray-brown cast
10. clearly visible irregular contour breaks and slightly loose line-to-fill registration across illustrations, icons, charts, callouts, and borders without harming text legibility

Regenerate a page when critical text or data is wrong. Keep the accepted pages and repair only the failing page.

## 6. Validate and repair

Check every output against this order of priority:

1. It communicates the selected article idea.
2. The character identity matches the anchor.
3. The subject is mini and the white space is generous.
4. The outline feels pen-drawn, wobbly, hesitant, and visibly broken at multiple irregular locations rather than fully closed or uniformly dashed.
5. Flat fills remain internally even but sit slightly loose against selected outline edges through tiny white slivers, shortfalls, or overhangs.
6. The registration mismatch is visible at normal size without becoming sloppy, distorting identity, or weakening legibility.
7. Colors retain normal, clear saturation without a dusty, muddy, gray-brown, beige, vintage, or washed-out cast.
8. No unwanted text or clutter appears.

Regenerate a failed image with a direct correction. Use these repair clauses as needed:

- **Too large:** `Shrink the entire character-and-prop group substantially; keep it near 25% of the canvas and restore large white margins.`
- **Too polished:** `Make the black pen outline more hesitant, uneven, and occasionally broken; simplify the shapes and remove formal illustration polish.`
- **Too continuous:** `Break several outline segments at irregular hair tips, sleeves, hands, shoes, prop corners, and turning points. Keep the silhouette readable, but do not leave every contour perfectly closed and do not create a uniform dashed pattern.`
- **Too perfectly registered:** `Loosen the line-to-fill registration on selected edges. Let flat fills stop slightly short, leave narrow white slivers, or cross the black outline by tiny amounts while keeping fill interiors even, colors saturated, and identity fully legible.`
- **Too painterly:** `Replace every textured or mottled area with clean flat color; keep roughness only in the black outline.`
- **Too faded:** `Restore normal clean saturation to every local color while keeping the palette limited. Remove the global gray, brown, beige, dusty, vintage, and washed-out cast; keep blacks neutral, skin natural, and accent colors fresh.`
- **Too generic:** `Tie the scene directly to [article idea] using [specific action/prop]; remove unrelated decorative objects.`
- **Identity drift:** `Restore the exact anchor hairstyle, outfit, accessories, palette, face, and proportions.`

## 7. Deliver

For ordinary generated illustrations, return the images in article order with a short label explaining the source idea. For infographics, return the automatically selected page count, the page plan, and the 3:4 images in reading order. For API handoff, return the character anchor, storyboard or infographic page plan, exact text manifests, and final prompts in copy-ready form together with the two official links from section 0.
