# ip_illustration_for_yourself

## Purpose
`ip_illustration_for_yourself` is a reusable IP illustration skill for:

1. building a user's own chibi/IP character from reference images;
2. generating article illustrations that stay strongly tied to the article meaning;
3. keeping a very specific visual language: **naive, mini, lots of white space, rough broken pen outlines, dot-eye cuteness, clean simple fills**;
4. working in Codex, RedSkill, or other Agents with a clear fallback path when direct image generation is unavailable.

The default image model is **gpt-image-2** whenever the current runtime provides it.

## Single-package compatibility
This distribution is intentionally a **single package**. It contains both:
- local `references/` assets for Codex / Agents that can read packaged files; and
- a remote-reference URL map for RedSkill / text-only Agents that cannot upload bundled images.

Use local files when available. Use remote URLs when the host cannot access bundled files.

---

# 1. Runtime detection and mandatory fallback

Before image generation, determine the environment.

## Mode A — direct generation available
Use direct generation when BOTH are true:
- the current Agent/runtime can call an image-generation model;
- `gpt-image-2` is available.

Then generate images directly using:
- the user's character reference(s);
- the remote style-lock reference URLs below;
- any extra product / logo / UI / brand references supplied by the user.

## Mode B — RedSkill / other Agent cannot attach bundled reference images
Use the **remote reference URL mode** in this skill.

This single package still contains local copies under `references/` for compatible Agents, but RedSkill-like runtimes may not expose them to image generation. In that case, use the public URLs configured in the **REMOTE REFERENCE URLS** section.

If those URLs are still placeholders or inaccessible:
- tell the user that the style references need public URLs;
- ask them to provide public URLs, or guide them to host the companion reference assets on GitHub / a CDN;
- continue by preparing the prompt and reference list rather than silently dropping the references.

## Mode C — no gpt-image-2 / no image-generation capability
Do not pretend to have generated images.

Tell the user:
> 当前 Agent 没有可直接调用的 gpt-image-2 图片生成能力。我会把最终 prompt、参考图 URL 列表和 API 调用模板整理好，你可以直接通过 GPT Image 2 API 出图。

Official OpenAI image generation guide:
https://developers.openai.com/api/docs/guides/image-generation

Then provide:
1. final prompt;
2. the chosen reference URLs;
3. API/curl fallback guidance;
4. a note that the current OpenAI docs should be treated as the source of truth for the exact endpoint and request schema.

This fallback is mandatory across all Agents. Never dead-end just because the current Agent lacks direct image generation.

---

# 2. REMOTE REFERENCE URLS — RedSkill compatible

RedSkill may not support bundled image uploads, so this skill uses remote URLs.

## IMPORTANT
Replace every `YOUR_PUBLIC_BASE_URL` below before publishing the Skill to RedSkill.

Recommended hosting patterns:

### GitHub Raw
`https://raw.githubusercontent.com/<USER>/<REPO>/main/ip_illustration_for_yourself/references/...`

### jsDelivr for a public GitHub repo
`https://cdn.jsdelivr.net/gh/<USER>/<REPO>@main/ip_illustration_for_yourself/references/...`

## Style-lock URLs
These references jointly lock the desired style. Use multiple references, not only one.

- STYLE_01_DOCS_READER:
  `YOUR_PUBLIC_BASE_URL/references/style_lock/01_docs_reader_style.png`
- STYLE_02_SEARCHER:
  `YOUR_PUBLIC_BASE_URL/references/style_lock/02_searcher_style.png`
- STYLE_03_CATGIRL_ANCHOR:
  `YOUR_PUBLIC_BASE_URL/references/style_lock/03_catgirl_anchor.png`
- STYLE_04_CATGIRL_READING:
  `YOUR_PUBLIC_BASE_URL/references/style_lock/04_catgirl_reading.png`
- STYLE_05_CATGIRL_GLASSES:
  `YOUR_PUBLIC_BASE_URL/references/style_lock/05_catgirl_glasses.png`
- STYLE_06_CATGIRL_ROBOTS:
  `YOUR_PUBLIC_BASE_URL/references/style_lock/06_catgirl_robots.png`
- STYLE_07_CATGIRL_CHIP:
  `YOUR_PUBLIC_BASE_URL/references/style_lock/07_catgirl_chip.png`
- STYLE_08_CATGIRL_COMPANION:
  `YOUR_PUBLIC_BASE_URL/references/style_lock/08_catgirl_companion.png`

## Content-coupling reference URLs
These are secondary references for translating article meaning into a small visual scene.

- CONTENT_01_ARCHITECTURE:
  `YOUR_PUBLIC_BASE_URL/references/content_examples/01_architecture_advantage.png`
- CONTENT_02_ORDER_FROM_CHAOS:
  `YOUR_PUBLIC_BASE_URL/references/content_examples/02_order_from_chaos.png`
- CONTENT_03_JUDGMENT:
  `YOUR_PUBLIC_BASE_URL/references/content_examples/03_judgment_and_selection.png`

## Character example URLs
These are examples only, not universal characters.

- CHARACTER_EXAMPLE_01_GREEN_CATGIRL:
  `YOUR_PUBLIC_BASE_URL/references/character_examples/green_catgirl_source.jpg`
- CHARACTER_EXAMPLE_02_BLUE_HAIR_CREATOR:
  `YOUR_PUBLIC_BASE_URL/references/character_examples/blue_hair_creator_source.png`

---

# 3. Reference selection rules

## Packaged local paths
When the Agent can access files from the installed skill, use paths such as:
- `references/style_lock/01_docs_reader_style.png`
- `references/style_lock/02_searcher_style.png`
- `references/style_lock/03_catgirl_anchor.png`

All package-internal paths use forward slashes `/` for macOS / Linux / Windows archive compatibility.


Do not send every reference blindly.
Choose references based on the task.

## For a new character anchor
Use:
- user's own character reference(s);
- STYLE_01 + STYLE_02;
- 1–3 catgirl style-lock images that best match the desired pose / complexity.

## For article illustration
Use:
- established character anchor or user character reference;
- STYLE_01 + STYLE_02;
- 2–4 style-lock references;
- optionally 1 content-coupling reference if it helps scene structure.

## For brand / product / logo / UI work
The user may provide extra public image URLs at **first use or any later prompt**.
These may include:
- brand logo;
- product photo;
- device photo;
- app / website screenshot;
- packaging;
- courseware page;
- map / diagram;
- specific location reference;
- character turnaround;
- clothing reference;
- any article-specific object.

Preserve the core style lock. Use the added reference only to import the requested identity/detail.

---

# 4. Non-negotiable visual style

## North star
**稚拙、mini、留白多、钢笔手绘、外描边断断续续、整体粗糙、豆豆眼可爱、色块简单干净、和文章强相关。**

## Core prompt sentence
Always include this or an equivalent instruction:

**EXTREMELY cute mini pen-doodle illustration, tiny chibi subject on a large pure-white page, naive dot-eye face, rough black ink contour, visibly hand-drawn line jitter, uneven stroke character, micro-hesitations, frequent tiny contour breaks and incomplete closures, imperfect pen control, simple clean flat color fills, very light fill misregistration, messy-cute and childlike, sparse article-relevant micro-scene.**

---

# 5. Rough outline is a HARD PASS/FAIL criterion

This is one of the most important rules in the entire skill.

The outer line MUST NOT look slick, smooth, vector-clean, or professionally inked.

Required contour behavior:
- visible natural wobble;
- uneven stroke pressure / thickness;
- micro-hesitations;
- slight angular awkwardness on curves;
- short broken segments;
- tiny gaps in some contours;
- a few incomplete closures;
- occasional double-touch / imperfect retrace is acceptable;
- the roughness should be obvious when looking at the silhouette.

## Failure condition
If the outline is:
- too smooth;
- too continuous;
- too elegant;
- too vector-like;
- too clean;
- too “丝滑”;

then the image is **off-style and should be regenerated**.

Use this repair clause:

**The contour is too smooth. Redraw it with visibly rougher hand-controlled pen lines: more natural wobble, uneven pressure, micro-hesitations, short broken segments, tiny contour gaps, and slightly awkward curves. Do not clean up the linework. Preserve the clean flat fills and large white space. The silhouette itself must visibly read as imperfect pen doodling.**

---


## 5.1 Mandatory rough-line gate
Before accepting any generated image, inspect the outer contour. If it reads as smooth, slick, vector-clean, or continuously polished, the result MUST be rejected and regenerated.

A passing image should visibly contain several of these characteristics across the silhouette:
- small pen jitter;
- uneven curvature;
- slight pressure/thickness variation;
- short line breaks;
- tiny contour gaps;
- micro-hesitations;
- imperfect joins;
- occasional awkward retrace.

**Do not compensate by making the color fill dirty.** The roughness belongs primarily to the black pen outline; the fill stays simple and comparatively clean.

# 6. Fill behavior

The roughness comes mainly from the **line**, not the fill.

Use:
- simple flat fills;
- clean color blocks;
- minimal shading;
- slight edge mismatch is okay;
- occasional tiny white gap between line and fill is okay.

Avoid:
- crayon;
- oil pastel;
- wax pencil;
- colored-pencil grain;
- painterly brush texture;
- speckled / mottled fills;
- heavy marker streaks.

---

# 7. Mini composition and whitespace

Default:
- character + props occupy roughly **20–40% of canvas area**;
- often smaller is better;
- pure white background;
- large quiet margins;
- 1–4 supporting objects in most article illustrations.

Think:
**“一个很小的可爱钢笔 doodle 掉在一张大白纸上。”**

Avoid:
- big hero character filling the canvas;
- dense infographic;
- poster composition;
- cluttered full-frame scenery.

---

# 8. Face language

Prefer:
- dot eyes / bean eyes / small round eyes;
- tiny mouth;
- simple blush if needed;
- restrained expressions;
- cute awkward body language.

Do not over-render anime eyes unless the user's character identity absolutely requires them.

---

# 9. Workflow A — build the user's IP character

## Input
User provides one or more character references.
In RedSkill, these should preferably be public image URLs.

## Extract
Lock:
- hairstyle / fur / ears / silhouette;
- face cues;
- hat / glasses / accessories;
- outfit;
- palette;
- signature object;
- personality / expression range;
- elements that must never change.

## Output
1. concise character anchor description;
2. one full-body anchor image;
3. optional front / side / back turnaround.

## Anchor composition
- small figure;
- lots of white space;
- rough broken pen contour;
- clean fills;
- simple face.

---

# 10. Workflow B — generate article illustrations

Default: **5 images** unless user requests another count.

## Read the article for meaning
Do not split mechanically by paragraph.
Extract the article's strongest visual concepts.

Recommended five-role pattern:
1. overview / framing;
2. thinking / preparation / tension;
3. key action / turning point;
4. structure / metaphor / relationship;
5. judgment / conclusion / emotional landing.

## HARD semantic relevance rule
Every image must correspond to a **specific article idea**.

Good:
- architecture training → building / structure / user journey;
- information → structure → beauty → 3-stage visual sequence;
- moodboard → pinned references / feeling board;
- “what is worth creating” → selecting one meaningful idea from many;
- robot feels offended → tiny character confronting a sulky robot.

Bad:
- random robot + laptop + sparkle;
- generic “AI” symbol unrelated to the article;
- decorative scene that could fit any article.

When article relevance and decoration conflict, **article relevance wins**.

---

# 11. Text policy

Default:
- no title inside image;
- no labels;
- no paragraph text;
- no watermark;
- no random UI copy.

Only include text when the user explicitly requests it or the exact branded text is essential to the object identity.

---

# 12. Brand / product / logo reference mode

At first installation OR later prompts, explicitly tell users:

> 你还可以继续补充品牌 Logo、具体产品照片、App / 网站截图、包装、UI、课程页、地点照片等参考图。RedSkill 里建议直接提供公开图片链接；我会保持人物和稚拙 mini 钢笔画风，只吸收你希望保留的产品/品牌细节。

When such references are supplied:
- keep style-lock references active;
- keep character identity active;
- use extra references only for the relevant product / logo / UI / object details;
- never let a glossy product photo make the entire image glossy.

---

# 13. Prompt template

**1:1 square illustration, EXTREMELY cute mini pen-doodle illustration, tiny chibi subject on a large pure-white page, naive dot-eye face, rough black ink contour, visibly hand-drawn line jitter, uneven stroke character, micro-hesitations, frequent tiny contour breaks and incomplete closures, imperfect pen control, simple clean flat color fills, very light fill misregistration, messy-cute and childlike, sparse article-relevant micro-scene.**

Character:
[locked character identity]

Article scene:
[one precise article concept / event / metaphor]

Objects:
[1–4 essential supporting objects]

Hard constraints:
- subject stays mini;
- lots of empty white space;
- contour must look visibly rough, slightly broken, and hand-drawn;
- if contour looks smooth/vector-like, regenerate;
- clean flat fills, no crayon/oil-pastel texture;
- dot-eye/simple-face language where compatible with character identity;
- strong semantic connection to article;
- no text unless explicitly requested.

---

# 14. RedSkill publication checklist

Before uploading this Skill to RedSkill:

1. Host the companion reference assets publicly.
2. Replace `YOUR_PUBLIC_BASE_URL` in this file with the actual public base URL.
3. Test at least 2–3 reference URLs in a browser/incognito window.
4. Make sure URLs return the image file directly without login.
5. Keep URL paths with `/`, never Windows `\`.
6. Upload/publish this text-based Skill to RedSkill.
7. Test one character-anchor task and one article-illustration task.
8. If linework is too smooth, use the hard repair clause in section 5.

---

# 15. Final principle

`ip_illustration_for_yourself` should turn a user's identity and article meaning into:

**tiny, naive, rough-pen, slightly broken-line, dot-eye, white-space-heavy illustrations that are cute because they are imperfect — and useful because they actually say what the article means.**
