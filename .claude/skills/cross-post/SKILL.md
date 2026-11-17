---
name: cross-post
description: Make platform versions of an approved post (site, Medium, Dev.to, Hashnode, LinkedIn) with canonical links back to devanshupatil.blog. Use when Devanshu says /cross-post, "cross-post", "make the Medium/LinkedIn version", or "ready to publish".
argument-hint: "<slug>"
---

# cross-post: one post, every platform

Read `context/platforms.md` first. It has the current rules per platform.

## Preconditions

- `posts/<folder>/final.md` exists. If only `draft.md` exists, stop and ask whether it's approved.
- `python3 scripts/ai_tells.py posts/<folder>/final.md` exits clean. If not, list the failures and stop.
- Canonical URL: `https://www.devanshupatil.blog/blog/<slug>` unless I give the real published URL. Ask me to confirm it once if the site isn't live yet.

## Outputs in `posts/<folder>/platforms/`

Body text stays identical across site, Medium, Dev.to, and Hashnode. Only the wrapper changes.

1. **site.md**: `final.md` with the site's frontmatter. CTA: newsletter, LinkedIn, GitHub.
2. **medium.md**: top block of settings (title, subtitle, 5 topics as 2 broad + 3 specific, suggested publication, canonical URL, "free") then the body. Note at the top: "Import via medium.com/p/import with the site URL if possible."
3. **devto.md**: Dev.to frontmatter (`published: false`, description under 155 chars, 4 lowercase existing tags, `canonical_url`, `cover_image`), then the body. Make sure every code block has a language label.
4. **hashnode.md**: settings block (subtitle, up to 5 tags, SEO description under 155 chars, canonical URL, ToC on for long posts), then the body.
5. **linkedin.md**: a native post, not a summary of every section.
   - Line 1 under 140 characters: the strongest number, scene, or confession from the post.
   - 900 to 1,500 characters total, short lines, blank lines between.
   - One idea from the post, told well, plus why it matters to the reader.
   - Ends with a real question. 3 to 5 specific hashtags on the last line.
   - Separate section `FIRST COMMENT:` with the article link.
   - Character count shown at the bottom.
6. **schedule.md**: the release order from platforms.md with actual dates (site day 0, LinkedIn day 0, Medium day 1 to 3, Dev.to and Hashnode day 3 to 7, stats review day 7).

## Then

- Run `python3 scripts/ai_tells.py` on linkedin.md (it's new prose) and fix FAILs.
- Run humanizer on linkedin.md only.
- Tell me which files are ready and what I need to do by hand (cover image upload, publication submission).

Never log in or post anywhere unless I ask in that message.
