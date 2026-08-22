---
name: ip-illustration-character-system
description: Build a reusable personal IP character and create consistent mini pen-doodle visuals, including article illustrations, information-rich 3:4 article infographics, and themed 3:4 kiss-cut sticker sheets. Use when the user asks to establish a mascot, make a turnaround sheet, illustrate a long article, create cute knowledge cards or infographics, visualize timelines, processes, comparisons, or data, keep one IP character consistent across multiple images, or make stickers, sticker pages, sticker sheets, die-cut stickers, or kiss-cut stickers. Require Codex with GPT Image 2 for direct generation; otherwise hand off a complete prompt package and the official GPT Image 2 API links.
---

# IP Mini Illustration System

## Attribution

Author: **everettfish**

Create a consistent personal character and use it in sparse, cute article illustrations, information-rich infographics, or themed sticker sheets. Use `gpt-image-2` only.

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

## 6. Create themed 3:4 sticker-sheet sets

Use this workflow whenever the user mentions stickers, a sticker page or sheet, die-cut stickers, kiss-cut stickers, or the Chinese terms “贴纸”“贴纸页”“贴纸图”“异形贴纸”“模切贴纸”.

### Establish the identity before the sheets

Reuse an accepted character anchor when one exists. When the user supplies a character reference but no accepted anchor, first generate the front-facing 1:1 full-body anchor from section 3 in the Skill's house style. Use that generated anchor as the identity reference for every sticker page; do not jump directly from a non-house-style source image to the sticker sheets.

When the user supplies multiple IP characters, repeat the complete anchor-plus-three-page workflow for each IP separately. Do not combine characters on one sheet unless the user explicitly asks for a crossover.

Before planning stickers, write an anchor-fidelity lock that records the exact hair outer silhouette, crown tufts, bang divisions, side-lock length, back-hair length, ear or horn geometry and placement, eye shape and color, face proportions, outfit, accessories, and signature palette. Repeat these invariants in the prompt. Every character appearance—including tiny scenes and head-only stickers—must preserve them; never shorten, simplify, restyle, mirror, or improvise the hairstyle. A head-only sticker must still show the complete anchored hair mass and identifying ears or accessories.

### Default to three theme pages

Unless the user explicitly changes the themes or count, create exactly three 3:4 portrait sticker sheets per IP, one page per generation call and in this order:

1. **Life / eating, drinking, and leisure:** everyday food, drinks, rest, entertainment, outings, hobbies, and playful reactions.
2. **Work:** a preserved anchor identity adapted through office actions and removable outfit variations such as a simple suit, coffee, a silver MacBook with no visible logo, notebook, presentation board, headphones, or desk accessories.
3. **Self-media / creator support:** heart-hands, thumbs-up, visual like and repost gestures, thanking supporters, filming, editing, posting, microphone, phone, camera, ring light, hearts, and share arrows. Communicate these ideas visually by default. Use short copy such as `比心`, `求赞`, `求转发`, or `感谢支持` only when the user explicitly requests words or when the intended meaning cannot be communicated clearly without them.

Use an English thematic series name in the header by default: `Life Stickers`, `Work Stickers`, and `Media Stickers`. Never put the IP name, a person's name, account handle, or other personal identifier in the header unless the user explicitly requests it.

Vary the character action, expression, crop, prop combination, and decorative motif across and within the three pages. Preserve the fixed face, hair, skin tone, silhouette, signature colors, and identifying accessories even when clothing changes for a theme.

### Build one coherent peel-off sticker page

- Use a 3:4 portrait canvas with two integrated zones: a shallow illustrated series header and a larger sticker field. Give both zones harmonious light pastel backgrounds from one palette family, separated by a gentle hue shift rather than harsh contrast. Keep them flat and free of paper grain, gradients, realistic shadows, or mockup texture.
- Reserve only the top 12–16% for one full-width rectangular card header in the first light pastel tone. Keep the color block complete from left edge to right edge with no packaging hole.
- Render one short locked English thematic series name of one to three words inside the header. Draw it with the naive mouse-lettering rules below. Do not use a character name, person's name, handle, or personal identifier.
- Make the entire header a small complete mini illustration rather than a sticker. Run one continuous decorative ground strip across the full header width from edge to edge—normally a low lawn or meadow with grass, flowers, leaves, stones, or theme-relevant tiny details—and place one tiny accepted-IP scene within it. Never leave the decoration as one isolated corner cluster. Let everything merge naturally into the color block; do not add a white die-cut border, halo, separate sticker contour, or cut line around header art.
- Use the lower 84–88% as one uninterrupted second light pastel sticker field that harmonizes with the header while remaining visibly distinct.
- Arrange 10–20 separate die-cut pieces in the sticker field; default to 18 when no count is supplied.
- Keep the main stickers modest in size, then fill interstitial gaps with several much smaller theme-related stickerlets. Aim for the combined cut-border footprint to cover about 75–82% of the sticker field without touching or crowding. After placing the primary stickers, perform a density pass and add or reposition micro stickerlets until no empty pocket is much larger than one planned micro stickerlet.
- Give every sticker its own free, irregular die-cut silhouette and a clearly visible continuous white or very pale border. The outer cut border may be clean and closed for production readability; the illustration inside it must retain the Skill's hesitant broken pen contours and slightly misregistered flat fills.
- Keep every body sticker fully visible, separated, and non-overlapping. Preserve clear but compact paper gaps between cut borders and comfortable margins along the sticker field.
- Arrange the body as a balanced staggered field with a gentle diagonal or S-curve rhythm. Occupy the upper, middle, and lower parts of the sticker field; distribute gaps evenly so no local void feels much larger than a small-to-medium sticker. Keep the overall bounding shape tidy: align the leftmost and rightmost sticker extents into two clean visual rails with roughly equal side margins while offsetting individual sticker centers. Never create straight rows, uniform columns, a mechanical grid, or a separate bottom row of standalone props.
- Make nearby stickers meaningfully related as loose visual micro-clusters while keeping their cut borders separate. For example, place an IP breakfast scene near a tiny drink-and-snack accent, or an IP editing scene near a tiny camera-and-headphone accent. Do not scatter unrelated orphan objects merely to fill gaps.
- Vary both scale and silhouette decisively, but keep the composition orderly. Mix two or three wider IP scenes, several medium tall or diagonal IP actions, compact roundish or cropped IP heads, and tiny angular or elongated accent motifs. Use only gentle rotations and stable upright reading direction. Avoid giving every sticker the same rounded blob, oval, full-body pose, or repeated cut shape.
- Use this default 18-piece content mix unless the theme suggests a better equivalent: 3 scene-led stickers with the IP visible inside the setting; 5 full-body or half-body IP actions; 4 head-only, face-only, or expressive IP busts; and 6 very small theme-specific filler stickerlets.
- Keep the IP as the identity anchor without making every sticker character-dominant. A page may include tiny characters inside scenes, cropped heads, hands, or partial silhouettes. Do not default to a page of uniformly sized full-body figures.
- Every large and medium body sticker must contain the accepted IP or be an IP-led scene; cameras, computers, food, drinks, office gear, and other objects may support that character but must not become large standalone stickers. Restrict prop-only pieces to the smallest filler tier, interleave them beside related IP stickers, and never collect them along one edge or below the character content.
- Use six to eight of the smallest pieces as theme-related filler stickerlets, usually about 2–5% of the sticker-field width, while keeping the total at or below 20. Distribute them through upper, middle, side, and lower interstitial gaps instead of placing them all at the bottom. Examples include one tiny heart-and-dot cluster, a miniature drink, paw mark, paperclip, share arrow, flower, camera sparkle, or theme-colored symbol. Keep each filler directly relevant; avoid generic random confetti.
- Keep the palette limited but normally saturated. Let the pale sheet and white cut borders create separation instead of fading the character colors.
- Use no sticker overlap, cropped cut contours, cast shadows, glossy vinyl effects, 3D blister effects, rectangular panels, UI cards, mockup hands, branding, logos, or watermarks.

### Reuse a small amount of relevant conversation context

- Inspect the current conversation for additional objects, products, places, colors, motifs, screenshots, or supporting images that directly relate to the chosen sticker theme.
- When a relevant contextual element would make the sheet feel more personal, weave in only one or two such elements on a default 18-piece page, or keep all contextual elements below about 20% of the manifest.
- Integrate a contextual element as a small scene detail, micro prop accent, outfit accent, or decorative motif. Keep the IP identity and the page theme dominant.
- Treat supporting images as object or content references only, never as style or character-identity references. Preserve the Skill's approved house style and accepted character anchor.
- Skip irrelevant context. Do not add a second character, visible brand logo, slogan, UI copy, or unrelated easter egg unless the user explicitly requests it.

### Keep text optional and mouse-drawn

- Include one short English thematic series name in the illustrated header by default. Lock it exactly before generation. This title is part of the header illustration, not a die-cut sticker. Never include a personal or character name unless explicitly requested.
- Set the body-sticker text manifest to `none` by default, including on self-media pages. Prefer poses, expressions, hearts, thumbs-up, share arrows, phones, cameras, and gratitude gestures over written slogans.
- Add body words only when the user explicitly requests them or when a required meaning cannot be communicated clearly through imagery.
- Keep any necessary copy very short and render only the locked words.
- Draw required text as deliberately naive mouse lettering: visibly hand-positioned strokes, gentle wobble, uneven stroke width, slight baseline drift, awkward but readable spacing, and small local corrections. It must look like a child carefully drawing letters with a basic mouse or trackpad.
- Never render sticker copy as a typeset font, polished hand-lettering, calligraphy, vector typography, uniform marker lettering, or a clean digital caption.

### Plan the sticker manifest before generation

Prepare a compact manifest for each page containing:

- exact theme
- exact short header series name and full-width header mini-scene
- total body sticker count
- scene-led stickers with tiny-IP action, setting, and essential props
- character-action stickers with pose, expression, outfit, and prop
- head-only or expressive-bust stickers
- six to eight theme-specific micro filler stickerlets, including any prop-only accents
- scale tier and intended outer-silhouette type for every sticker
- zero to two optional conversation-context elements and the exact sticker or scene where each belongs
- exact body-text manifest, or `none`
- dominant sheet color and two to four accent colors derived from the anchor

Ensure the planned count is between 10 and 20, no planned sticker depends on overlapping another sticker, and the manifest does not produce a straight row of standalone elements.

### Sticker-sheet prompt

```text
Create one 3:4 portrait kiss-cut sticker sheet using GPT Image 2.

IDENTITY REFERENCE — HIGHEST PRIORITY: use the accepted mini pen-doodle character anchor exactly. Preserve [exact hair outer silhouette, crown tufts, bang divisions, side-lock and back-hair lengths, ear or horn geometry and placement, face proportions, eye shape and color, skin tone, signature colors, outfit and accessories]. Repeat these invariants in every character appearance, including tiny scenes and head-only stickers. Never shorten, simplify, restyle, mirror, or improvise the hair. Theme-appropriate clothing may vary only as specified below.

HOUSE STYLE INSIDE EACH STICKER: mini pen-doodle illustration; hesitant wobbly black pen contours with clearly visible irregular breaks; awkward hand-drawn shapes; internally clean flat color shapes deliberately slightly misregistered from selected outlines through tiny white slivers, shortfalls, or small edge overhangs; normal clear saturation; limited color count; childlike messy-cute charm. Broken but not uniformly dashed, misregistered but still legible. No glossy anime rendering, 3D rendering, vector-perfect curves, painterly texture, crayon fills, mottled color, or faded gray-brown cast.

PAGE STRUCTURE: exact 3:4 portrait with two integrated zones using two harmonious light pastel tones from one palette family. HEADER: reserve only the top 12–16% as one full-width rectangular [light pastel color] block with no packaging hole. Render this exact short series name: [locked title]. Build [continuous lawn/meadow or comparable decorative ground] all the way from the left edge to the right edge, with grass, flowers, leaves, stones, and sparse theme details distributed across the whole width; integrate one tiny accepted-IP scene into it. Never reduce the decoration to one isolated corner cluster. The header is one continuous illustration, not a sticker: no white border, die-cut halo, sticker contour, cut line, floating sticker, or separate panel around its art or text. STICKER FIELD: use the lower 84–88% as one uninterrupted [harmonizing second light pastel color] backing field, flat and texture-free.

BODY LAYOUT: arrange exactly [10–20] independent irregular die-cut pieces only inside the sticker field as a balanced staggered field with a gentle diagonal or S-curve rhythm. Default to 18. Combined cut-border footprint covers about 75–82% of the sticker field. After placing the primary pieces, perform a density pass: add or reposition six to eight very small theme-related filler stickerlets until no empty pocket is much larger than one micro stickerlet, while preserving clear separation. Occupy upper, middle, side, and lower areas; do not push prop-only accents into one bottom band. Form two tidy visual rails with roughly equal side margins. Every body piece is fully visible, has its own continuous white or very pale kiss-cut border, and does not touch, overlap, merge, or crop. Keep compact consistent breathing gaps and gentle rotations. Never arrange items in straight rows, uniform columns, a rigid grid, or a separate prop strip.

THEME: [life / work / self-media creator support].
STICKER MANIFEST: [enumerate every IP-led scene, IP action, cropped IP head or bust, micro prop accent, text element if required, and decoration accent; include scale tier and silhouette direction; the enumeration count must equal the requested total].
CONTENT MIX: for a default 18-piece sticker field, use about 3 scene-led stickers with the IP visible, 5 IP action stickers, 4 head-only or expressive-IP bust stickers, and 6 very small theme-specific filler stickerlets. Every large and medium sticker contains the accepted IP or is an IP-led scene. Cameras, computers, food, drinks, and other standalone props are micro accents only, never large stickers. Vary outer silhouettes: wide IP scene, tall action, diagonal action, compact head with the complete anchored hairstyle, and tiny irregular motifs. Do not make every sticker a full-body character or the same rounded shape.

CONVERSATION CONTEXT: [NONE, or list one to two directly relevant contextual elements and the exact scene or cluster where each appears]. Keep contextual material below about 20% of the manifest. Use it only as content detail, never as a style or identity source.

HEADER TITLE — RENDER EXACTLY:
[locked short series name]

BODY TEXT MANIFEST:
[exact requested body text or NONE]

TEXT STYLE WHEN THE MANIFEST IS NOT NONE: render every required word as naive mouse-drawn lettering with visibly wobbly hand-positioned strokes, uneven stroke width, slight baseline drift, awkward but readable spacing, and tiny local corrections. No typeset font, vector typography, polished hand-lettering, calligraphy, or clean digital caption.

Keep nearby body items thematically related as loose visual micro-clusters without touching. Balance them across the sticker field and scatter micro fillers into upper, middle, side, and lower gaps. No large empty pocket, bottom-loaded props or accents, overlap, cropped cut contours, straight rows, bottom prop strip, repeated blob silhouettes, chaotic rotations, cast shadows, glossy vinyl effects, 3D mockup, unrelated clip art, logo, watermark, invented body text, or paper texture.
```

Pass the accepted character anchor as the primary identity reference plus `style_ref_01` and `style_ref_02` as style-only references. Include `style_ref_03` only when its character cannot be confused with the target identity; omit it for cat-eared, green-haired, or otherwise visually similar targets. The accepted anchor always overrides every style reference for hair, ears, face, outfit, palette, and proportions.

### Validate and repair sticker pages

Check each page before continuing:

1. correct 3:4 portrait ratio and a shallow 12–16% full-width header; both zones use harmonious but distinguishable light pastel backgrounds, with no packaging hole
2. exact naive mouse-drawn series name plus one complete tiny-IP header scene and a continuous decorative ground strip across the entire header width, with no isolated corner decoration, white border, die-cut halo, sticker contour, or cut line
3. 10–20 individually countable body pieces matching the manifest, defaulting to 18
4. about 75–82% sticker-field cut-border footprint, with compact even gaps and no empty pocket much larger than one micro stickerlet
5. balanced body field with occupied upper, middle, side, and lower zones; tidy left and right visual rails; no straight rows, uniform columns, rigid grid, separate prop strip, or bottom-loaded accents
6. decisive variation in scale and silhouette across wide scenes, tall or diagonal actions, compact heads, angular or elongated clusters, and tiny filler stickerlets
7. no overlapping, touching, cropping, or merged body cut borders
8. one continuous white or pale irregular cut border around every body piece, but none around the header illustration
9. coherent theme relationships and a balanced mix of IP-led scenes, IP actions, IP heads, and micro fillers; every large or medium sticker contains the IP and prop-only stickers stay tiny
10. six to eight micro fillers distributed through gaps rather than collected at the bottom, while total pieces remain at or below 20
11. unmistakable anchor identity in every appearance; exact anchored hair silhouette, bangs, side and back lengths, ear geometry, eyes, face proportions, outfit cues, and palette even when the IP is tiny, cropped, or secondary to a scene
12. original broken pen contours and slightly loose flat-fill registration inside each body sticker
13. normal clean saturation without a dusty, gray-brown, beige, vintage, or washed-out cast
14. exact readable mouse-drawn header title; no body text unless explicitly requested or essential
15. any reused conversation-context element is directly relevant, limited to one or two items or below about 20% of the manifest, and does not alter the house style or IP identity

Keep accepted pages and regenerate only the failing page. Use direct corrections such as:

- **Header missing or incomplete:** `Restore one complete light-pastel header across only the top 12–16%. Add the exact mouse-drawn series name, one tiny integrated IP scene, and a continuous lawn, meadow, or comparable decorative ground from left edge to right edge.`
- **Header too tall:** `Reduce the full-width header to 12–16% of page height and return the saved space to the sticker field.`
- **Header looks like a sticker:** `Remove every white halo, cut border, floating sticker contour, and die-cut line from the header. Merge the tiny IP, props, text, and scene directly into one continuous full-bleed color-block illustration.`
- **Overlapping or crowded:** `Shrink every sticker by about 15–25% while preserving its content. Separate every cut border and restore evenly distributed backing paper; no touching, overlap, or merged silhouettes.`
- **Uneven density or large empty zone:** `Redistribute the same body stickers across upper, middle, side, and lower zones. Add or relocate six to eight tiny theme-relevant filler stickerlets until no empty pocket is much larger than one micro stickerlet, keep the total at or below 20, and preserve separate cut borders.`
- **Too chaotic:** `Keep the varied sizes and silhouettes but reduce rotations, stabilize the upright reading direction, regularize the breathing gaps, and preserve one calm staggered visual rhythm.`
- **Arranged in rows:** `Break every straight row and separate prop strip. Reposition the same stickers along an asymmetric diagonal or S-curve flow, interleaving IP scenes, IP actions, IP heads, and micro accents with compact clear gaps.`
- **Large standalone props or bottom-loaded accents:** `Replace every large or medium standalone camera, computer, food, drink, or office object with an IP-led action or scene. Keep prop-only stickers in the smallest filler tier and distribute them beside related IP stickers throughout the field.`
- **Shapes too similar:** `Diversify the outer cut silhouettes: make IP scenes wide and irregular, IP actions tall or diagonal, IP heads compact and cropped, and tiny accent motifs angular, elongated, or asymmetrical. Do not use repeated oval or rounded-blob borders.`
- **Too character-dominant:** `Replace several large full-body poses with two or three scene-led stickers containing a smaller IP, plus expressive IP heads and tiny related accents, while preserving the total count and keeping every large or medium sticker IP-led.`
- **Unrelated elements:** `Remove orphan filler objects. Rebuild the page as three or four loose theme micro-clusters whose scenes, heads, actions, and props clearly relate to one another without touching.`
- **Missing cut lines:** `Add one continuous white or very pale irregular die-cut border around every individual sticker, including the small decorative stickers.`
- **Too generic:** `Replace unrelated icons with anchor-specific scenes, expressions, actions, and tiny tightly related prop accents.`
- **Wrong count:** `Render exactly [count] individually countable stickers matching the enumerated manifest; do not split or merge items.`
- **Identity drift:** `Restore the accepted anchor in every appearance. Copy the exact hair outer silhouette, crown tufts, bang divisions, side-lock and back-hair lengths, ear geometry and placement, eye shape and color, face proportions, outfit cues, and palette. Do not simplify the hairstyle on head-only stickers; show the complete anchored hair mass.`
- **Unnecessary or wrong text:** `Keep only the exact header series name and any explicitly locked body text. Redraw the header title with naive wobbly mouse lettering, uneven stroke width, slight baseline drift, awkward but readable spacing, and no typeset-font appearance.`
- **Context overload:** `Keep at most one or two directly relevant contextual elements, below about 20% of the manifest. Remove unrelated easter eggs and restore the accepted IP and page theme as the dominant content.`

## 7. Validate and repair

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

## 8. Deliver

For ordinary generated illustrations, return the images in article order with a short label explaining the source idea. For infographics, return the automatically selected page count, the page plan, and the 3:4 images in reading order. For stickers, return each IP's accepted character anchor followed by the life, work, and self-media 3:4 sticker sheets, plus the three compact sticker manifests. For API handoff, return the character anchor, storyboard, infographic page plan, or sticker manifests as applicable; include exact text manifests and final prompts in copy-ready form together with the two official links from section 0.
