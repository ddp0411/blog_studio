# Platforms: where and how each post goes out

Order: my site first, then the copies, each with a canonical link back to the site. The canonical tells search engines the site is the original, so copies on high-authority sites (Medium, Dev.to, Hashnode) don't outrank it.

Checked November 2026. Platforms change their editors; if a menu has moved, check the platform's help page.

## Release order

| When | Where | How |
| --- | --- | --- |
| Day 0 | devanshupatil.blog | Publish `platforms/site.md`. Grab the final URL. |
| Day 0 | LinkedIn | Native post from `platforms/linkedin.md`. Link goes in the first comment. |
| Day 1 to 3 | Medium | Import tool or paste with canonical (below). Submit to a publication. |
| Day 3 to 7 | Dev.to and Hashnode | Paste with canonical. Waiting a few days gives Google time to index the original first. |

## devanshupatil.blog (canonical)

- Full post, markdown with frontmatter (see `templates/post-template.md`). `[TODO: confirm the site's frontmatter fields (MDX? Next.js? Astro?) and update the template]`
- Slug: lowercase, hyphens, 3 to 6 words, keyword first. Never change it after publishing; every canonical points at it.
- Category: one of AI Engineering, Machine Learning, Computer Vision, Data Engineering.
- Footer: newsletter signup, LinkedIn, GitHub.

## Medium

- Best: Import a story (profile → Stories → Import a story, or medium.com/p/import) and paste the site URL. It sets the canonical link and backdates the post automatically. Check formatting and re-upload images if they didn't come over.
- If import fails: paste manually, then Story settings → Advanced settings → "This story was originally published elsewhere" → paste site URL → Save canonical link.
- Title 8 to 12 words; subtitle under 15 words.
- 5 topics: 2 broad + 3 specific (e.g. AI · Programming · Claude Code · Data Engineering · Software Testing).
- Submit to one niche publication (e.g. Data Science Collective, Towards Data Engineering, Level Up Coding). `[TODO: keep a list of publications that accepted me]`
- Free, not member-only, while building reach.
- Custom footer once in Settings → Publishing → Manage Story Footer: newsletter, LinkedIn, GitHub buttons.
- The first ~150 words must hook (non-members and previews see only that much).

## Dev.to

Paste into the basic markdown editor with this frontmatter:

```yaml
---
title: "Post title"
published: false
description: "One sentence for previews, under 155 characters"
tags: ai, claudecode, productivity, dataengineering
canonical_url: https://www.devanshupatil.blog/blog/slug
cover_image: https://www.devanshupatil.blog/images/slug-cover.png
series: "Optional series name"
---
```

- Max 4 tags, lowercase, no spaces, existing tags only. The first tag is the primary one.
- Cover image best at 1000 x 420.
- Dev.to shows "Originally published at devanshupatil.blog" automatically when canonical_url is set.
- Dev.to readers like code and step-by-step. Keep the code blocks; tone stays the same.

## Hashnode

- Paste markdown. Draft settings (down-arrow in the editor header) → set the canonical / "originally published" URL.
- Subtitle field: same as Medium subtitle.
- Tags: up to 5. At least 1 required.
- Cover image around 1600 x 840.
- SEO description under 155 characters.
- Turn on table of contents for long posts.

## LinkedIn

Don't paste the article. Write a native post that stands on its own.

- Hard limit 3,000 characters. Aim for 900 to 1,500.
- Only about the first 140 characters (mobile) to 210 (desktop) show before "see more". The first line is the whole game: a number, a scene, or a confession.
- Short lines with blank lines between them. No walls of text.
- Put the article link in the first comment, not the post body. Posts with external links in the body get noticeably less reach.
- 3 to 5 specific hashtags at the very end (#ClaudeCode #DataEngineering), never mid-sentence.
- No emoji bullets, no "🚀", no "Agree?" bait. End with one real question.
- Optional, for guides: a PDF carousel of the key steps (document posts tend to get good distribution).
- LinkedIn articles have no canonical field, so republishing the full post there competes with the site. Use posts, not articles.

## Same text everywhere?

Body text stays the same on site, Medium, Dev.to, and Hashnode (that's what canonical is for). What changes per platform:

| | Site | Medium | Dev.to | Hashnode | LinkedIn |
| --- | --- | --- | --- | --- | --- |
| Title | SEO-friendly | Click-friendly, can differ | Same as site | Same as site | n/a (hook line) |
| Subtitle | Description | Yes | description field | Yes | n/a |
| Tags | 1 category | 5 topics | 4 tags | up to 5 | 3 to 5 hashtags |
| Canonical | self | import / settings | frontmatter | draft settings | n/a |
| CTA | newsletter form | footer buttons | last paragraph | last paragraph | first comment link |
