# Blog Studio: Devanshu's writing workspace

This folder is where I turn rough notes into blog posts that read like I wrote them by hand, then publish them to my site and cross-post everywhere else. Everything here is about writing. Do not treat it as a code project.

@context/profile.md
@context/voice.md
@context/banned-patterns.md

Read these on demand, not every session:

- `context/medium-playbook.md`: my full Medium research (titles, hooks, reach funnel, stats diagnosis)
- `context/platforms.md`: per-platform formatting, canonical links, tags, limits
- `voice/samples/`: paragraphs I wrote myself. Read them before drafting or humanizing.

## Hard rules (never break these)

1. **Never invent my experience.** No made-up stories, numbers, quotes, error messages, timings, dates, colleagues, or results. If the notes don't contain it, write `[TODO: what's needed]` and keep going. A fake anecdote is the fastest way to make a post read as AI-written.
2. **No em dashes or en dashes in prose.** Not one. Use a period, comma, colon, or parentheses. Dashes inside code, commands, URLs, and file names are fine. This rule beats humanizer's "match the sample's dash rate" rule, because my older posts overuse dashes.
3. **American English.** behavior, optimize, color, analyze, center, modeling.
4. **Work privacy.** I can say "at work" or "at Synthesys." Never name clients, show internal schemas, table names, dashboards, or internal numbers. Swap in generic names (`orders_raw`, "a retail client") and say they're changed.
5. **Sound like me.** First person, builder's log energy, calm field-notes delivery (see voice.md). If a sentence could appear in anyone's post, rewrite it with a detail only I would know, or cut it.
6. **My site is the original.** Every post is published on devanshupatil.blog first. Every other copy carries a canonical link back to it.
7. **Run the checks before calling anything done:** humanizer pass, `python3 scripts/ai_tells.py <file>`, then the checklist in `templates/checklist.md`.

## How a post gets made

I work by dumping rough notes. Don't interview me first; draft from what I gave you and mark the gaps.

| Step | What happens | Command |
| --- | --- | --- |
| 1. Notes | I create `posts/YYYY-MM-DD-slug/notes.md` and paste messy notes, logs, numbers, screenshots list | `/blog-draft new <slug>` makes the folder |
| 2. Draft | Claude picks the format, writes 5 titles, drafts `draft.md` with `[TODO]` markers | `/blog-draft` |
| 3. Fill gaps | I answer the TODOs (in the file or in chat). Claude folds them in. | |
| 4. Humanize | Humanizer in file mode on `draft.md`, using my voice samples, dash ban enforced | `/humanizer posts/<slug>/draft.md` |
| 5. Lint | Script flags dashes, banned words, British spelling, long paragraphs, leftover TODOs | `python3 scripts/ai_tells.py posts/<slug>/draft.md` |
| 6. Final | Copy to `final.md`, tick `templates/checklist.md` | |
| 7. Cross-post | Site version plus Medium, Dev.to, Hashnode, LinkedIn variants | `/cross-post <slug>` |
| 8. Stats | After 7 days, diagnose with the funnel table and log it | `/stats-review <slug>` |

Post folder layout:

```
posts/2026-11-20-claude-code-tokens/
  notes.md          # my raw dump (never edited by Claude)
  draft.md          # Claude's working draft
  final.md          # approved text, canonical version
  assets/           # cover image, screenshots, diagrams
  platforms/        # site.md, medium.md, devto.md, hashnode.md, linkedin.md
```

Ideas waiting to be written live in `posts/_ideas.md`. Results live in `stats/log.md`.

## Writing rules (condensed from my Medium research)

**Pick the format first.** Two formats work; the middle one doesn't.

- Short opinion or story: 3 to 5 min, 600 to 1,000 words. Gets claps, replies, follows.
- Complete guide: 10+ min, 2,000+ words, numbered steps, code, screenshots. Gets saves and search traffic.
- Avoid the 6 to 9 minute explainer that is neither sharp nor complete.

**Title.** A question people already argue about, or a bold claim. 8 to 12 plain words. A real number if the notes have one ("cut my tokens by 60%"). No jargon only experts get. No clickbait: the post must deliver exactly what the title says. Always offer 5 options using different formulas (question, small change/big result, firm opinion, complete guide, honest how/when) and mark the one you'd pick.

**Subtitle.** One line, under 15 words. Tease the answer or add the detail the title leaves out.

**Opening (first 150 words).** Non-members and LinkedIn scrollers see only this. Lines 1 and 2 are a scene, a hard number, a comparison, a surprising result, or a direct question. By word 150 the reader knows the problem, why I'm the one writing about it (one line), and what they'll get. Never open with background, a definition, or "AI is changing everything."

**Body.**
- 3 to 6 H2/H3 headings in sentence case. Headings say what the section holds, ideally as a mini-story ("The four hours before the fix"), not labels ("Problem statement").
- Paragraphs of 1 to 3 sentences. Reads well on a phone.
- Vary sentence length on purpose. Some 4-word sentences, some 25-word ones.
- Show what I tried, what broke, what I'd do differently. Honest limits get trust and comments.
- Real numbers with their source (my test, a doc page, a survey). Link it.
- Code blocks for anything a reader would copy, with a line after each saying what to notice.
- Technical posts: a screenshot, diagram, or code block every couple of sections. Mark needed visuals as `[IMAGE: description]`.
- Optional short FAQ at the end of guides.

**Ending.** One clear takeaway or a quotable line that adds something new (not a recap). Then one specific question for comments ("What's your token-saving trick?"). Then links to related earlier posts. The footer CTA comes from profile.md.

**Topics/tags.** 5 on Medium (2 broad, 3 specific), 4 on Dev.to, up to 5 on Hashnode. See platforms.md.

## How to use humanizer here

Humanizer (vendored in `.claude/skills/humanizer/`, from github.com/blader/humanizer) is the final prose pass. When running it:

- Use file mode on `draft.md`. It must leave code blocks, frontmatter, links, and `[TODO]` / `[IMAGE]` markers untouched.
- Give it the samples in `voice/samples/` for rhythm and word choice, but the dash ban (rule 2) still applies even if a sample has dashes.
- It must keep my voice details: specific odd details, mixed feelings, asides in parentheses, self-corrections, dry jokes.
- It must not drop or change any number, tool name, version, or claim.
- If humanizer and this file disagree, this file wins.

## Definition of done

A post is ready to publish when all of these are true:

- [ ] Zero `[TODO]` markers left
- [ ] `ai_tells.py` exits clean (no FAIL lines)
- [ ] Checklist in `templates/checklist.md` ticked
- [ ] I've read it aloud once and nothing sounds like a press release
- [ ] Every number traces back to my notes or a linked source

## Things Claude should not do here

- Don't edit `notes.md`. It's my raw record.
- Don't publish, post, or log in anywhere for me unless I ask in that message.
- Don't add emojis, hashtags inside the article body, or bold on every bullet.
- Don't write "In conclusion", a recap of the whole post, or a "the future looks bright" ending.
- Don't pad a short post to look like a guide, or cut a guide down to look like an opinion piece.
