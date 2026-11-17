# Medium Blog Playbook

Nov 17, 2026 · @Devanshu Patil

## How to use this guide

The short version: on Medium, a story that gets read is one that wins the click with its title, keeps the reader with its opening, and gets passed along because readers trust it. Everything below tells you how to do each of those.

The guide combines two reviews:

- **The Medium Blog (official):** all 27 posts reviewed for structure (titles, length, headings, images). The 8 about reach, stats, AI and reading behaviour were read in full. These give Medium's own data on what drives distribution.
- **A sample of the Medium feed:** 5 stories from the feed (programming, AI agents, relationships, Netflix engineering, RAG), compared by claps and responses. These show what readers actually reward.

Where the two disagree, Medium's own data comes first. The feed sample is only 5 stories, so its patterns are strong hints, not rules.

How to use it: write your draft with the **template** near the end, then run it through the **pre-publish checklist** before you hit publish. A week after publishing, use the **stats diagnosis** table to plan your next post.

## How Medium decides who sees your story

A story reaches people in four stages, and Medium's stats page now shows each one. Every stage has one thing you control.

&#91;embedded content: Medium reach funnel · 4 stages, one lever each\]

A "presentation" is any time Medium shows your story: home feed, search, related stories, topic pages, email and push notifications. A "read" means someone stayed at least 30 seconds.

**Who pushes stories into feeds**

- **Medium's curators** review thousands of stories a day and label them for distribution. Good stories get Boosted; clickbait and AI slop get limited, down to **Network Only** (shown only to your own followers).
- **Publication editors** accept, feature and recommend stories to their readers.
- **Readers** follow and mute writers, publications and topics, and repost stories they like.
- Result: over 75% of stories in an average reader's feed are there because a **person** recommended them. You win by earning trust, not by gaming an algorithm.

## What the evidence shows

The shortest, most personal post in the feed sample got about 5× the claps of the next one, without any publication behind it. On the Medium Blog, the most-discussed posts were the ones that helped writers directly (stats, AI, trust).

**Feed sample (5 stories)**

| Post | Claps / responses | Length | Why it worked (or didn't) |
| --- | --- | --- | --- |
| What Should Programmers Do While the AI Writes Code? (Scott Batson, self-published) | 10.5K / 245 | 4 min | Personal, funny, timely question; short punchy paragraphs |
| Can Men and Women Really Be Just Friends? (Dori Kasa, in *Bitchy*) | 2.6K / 63 | 8 min | Question people already argue about; opens with a real scene and dialogue |
| A Step-by-Step Guide for Developing Your Personal Agentic System (Erdogan T, in *Data Science Collective*) | 2.1K / 52 | 36 min | Complete hands-on guide; gets saved and searched |
| Ontology-Driven Observability (Netflix TechBlog) | 929 / 24 | 13 min | Deep engineering; story-style headings, 10 images, 3 code blocks |
| RAG is a knowledge interpreter. Time for a compiler (J. Wasowski, self-published) | 282 / 5 | 13 min | Jargon title only experts understand |

**Medium Blog: most-responded posts**

| Post | Responses | Length | What it gave the reader |
| --- | --- | --- | --- |
| Which stories reach and grow your audience? | 340 | 5 min | How distribution works, with actions to take |
| Write for humans, not algorithms | 243 | 7 min | A clear opinion plus a personal test (AI detector on the author's own text) |
| How Medium moderates its open platform in the AI era | 243 | 9 min | Behind-the-scenes look at a hot topic |
| State of Writing Report 2026 | 152 | 7 min | Fresh survey numbers (1,175 writers) |
| Long reads just got easier to read | 138 | 4 min | Practical change readers and writers both feel |
| Try out custom footers | 124 | 6 min | A new tool, with a long FAQ |
| This tiny design tweak increased reads | 117 | 3 min | A surprising result, explained briefly |

Two lessons run through both sets: **useful or opinionated beats neutral**, and **personal beats generic**.

## Step 1: Pick the format and the topic

Decide the format before you write a word. Short opinion pieces get the most claps and comments. Complete guides get saved and keep coming up in search. Medium-length posts that are neither did worst in the sample.

| Format | Length | Best for | What it needs |
| --- | --- | --- | --- |
| **Short opinion / story** | 3–5 min (600–1,000 words) | Claps, responses, follows | One clear opinion, a personal story, humour, a question people argue about |
| **Complete guide / tutorial** | 10+ min (2,000+ words) | Saves, search, long-term reads | Numbered steps, headers, screenshots or code, a "what you'll build" up front |
| ~~Medium-length explainer~~ | 6–9 min | Avoid unless the topic is very hot | Neither the punch of an opinion nor the depth of a guide |

About 1 in 10 Medium stories is over 2,000 words. Tutorials and how-tos are among Medium's most popular stories, and long posts with headers now get an automatic table of contents.

**Choosing the topic**

- Write about a pain point that is hot **right now**. Three of the five feed stories were about AI and agents.
- Take a fresh angle on the hot topic. The top post wasn't another AI how-to; it was about the human side (overload, burnout).
- Write from your own experience. Medium readers want writing from someone who lived it, and trust it more than generic advice.
- Pick a question people already argue about, and give your answer.
- Good fits for us: Claude Code token savings (before/after numbers), lessons from the data engineering program (PostgreSQL, Snowflake, Airflow, AWS), and testing in the age of AI coding.

## Step 2: Write the title and subtitle

The title decides whether anyone clicks. Medium says: if your story is shown a lot but few people click, the title is the problem.

**Title rules**

1. Make it a **question people already argue about**, or a **bold claim**. The top two feed posts were both questions.
2. Promise a clear benefit or result the reader cares about.
3. Keep it to 8–12 words, in plain words. No jargon only experts understand (the RAG "interpreter vs compiler" title got the fewest claps).
4. Use specific numbers where you have them ("cut my tokens by 60%" beats "save tokens").
5. Never clickbait. Medium can mark clickbait as **Network Only**, which badly cuts reach.

**Title formulas that worked**

| Formula | Example from the research | Our version (example) |
| --- | --- | --- |
| A question people argue about | What Should Programmers Do While the AI Writes Code? | Should Testers Still Write Test Cases When AI Writes the Code? |
| A small change, a big result | This tiny design tweak increased reads across all of Medium | One config change cut my Claude Code token bill by half |
| A firm opinion | Write for humans, not algorithms | Stop prompting harder. Start giving Claude less to read. |
| The complete guide | A Step-by-Step Guide for Developing Your Personal Agentic System | The complete guide to Airflow for people coming from manual testing |
| The honest how/when | How (and when) does your writing show up inside AI chatbots? | How (and when) should a data team move from PostgreSQL to Snowflake? |

**Subtitle rules**

- Tease the answer without giving it away. Scott Batson's "Hint: not start another AI coding loop" makes you curious and shows a firm opinion.
- Or add the detail the title leaves out: "Two long-awaited updates to writer stats pages".
- One line, under about 15 words.

## Step 3: Write the opening (first 150 words)

The opening must deliver what the title promised, fast. Medium says that if people click but don't keep reading, the intro doesn't match the title. On member-only posts, non-members see only about the first 150 words, so the hook has to work there.

**Open with one of these, in the first two lines:**

- **A scene:** a real moment, ideally with a line of dialogue ("We were planning lunch when she said…").
- **A hard number:** "Jake Paul vs. Mike Tyson… 65 million concurrent streams."
- **A comparison:** programmers as The Flash, "zooming around faster than our intent."
- **A surprising result:** "You probably missed this subtle change…"
- **A direct question to the reader:** "What if you could instantly identify AI-written text? How would you use it?"

**Never open with** background or throat-clearing: "In today's fast-paced world…", "AI is changing everything…", or a definition from Wikipedia.

**By the end of the opening, the reader should know:**

1. What problem this is about.
2. Why you are the person to talk about it (your experience in one line).
3. What they will get if they keep reading.

## Step 4: Write the body

The body should be easy to scan on a phone and sound like a real person who did the work.

**Structure**

- Use 3–6 section headings (H2/H3). Medium now builds an automatic table of contents from them on desktop.
- Write headings as mini-stories, not labels: Netflix used "The four hours before a fix", not "Problem statement".
- For guides, number the steps and put a short "what you'll build / what you'll learn" at the top.

**Paragraphs and sentences**

- Keep paragraphs short: 1–3 sentences. Scott Batson's top post averaged about 13 words per paragraph.
- Use one-line paragraphs for punch ("A new page for managing user settings? It's in scope now!").
- Use plain words. Explain any jargon the first time you use it.

**Voice**

- Write in the first person. Say what you tried, what broke, what you learned.
- Be honest about limits and mistakes ("I was not fully in control", "Is this a perfect system? No."). Readers trust it and comment on it.
- Add light humour, especially at your own expense. It is the reason people reply.
- Show your own test or proof. The "Write for humans" post ran an AI detector on the author's own text and showed screenshots.

**Proof and numbers**

- Use real, specific numbers: before/after, percentages, counts, time saved.
- Say where a number comes from (your own test, a survey, a docs page) and link it.

**Visuals**

- Every post needs a cover image, ideally your own, with a short witty caption.
- Technical posts: add screenshots, diagrams or code blocks every few sections. The top technical posts had 7–11 images.
- Use code blocks for anything a reader would copy.

**Optional: an FAQ at the end**

Several Medium Blog posts end with a short FAQ. It answers questions before readers ask and works well for guides and tool posts.

## Step 5: End strong and turn readers into followers

The ending is what readers highlight, share and reply to. Medium says that if people read but don't follow, they haven't been given a reason to want more from you.

**The last lines**

- End with one clear takeaway, or a line worth quoting (the RAG post closed on a Peter Drucker quote).
- Ask readers a specific question to answer in the comments ("What's your token-saving trick?"). Medium Blog posts do this every time; responses help reach.
- Avoid a long recap of what you just said.

**Your profile and footer**

- Fill in your bio: who you are, what you write about, why follow ("Tester learning data engineering in public. Weekly notes on Claude Code, Airflow and Snowflake.").
- Use Medium's **custom footer** (Settings → Publishing → Manage Story Footer, web only). Set it once and it appears on every story: up to 4 buttons and your social links (LinkedIn, Substack, YouTube and others). Point it at your LinkedIn, GitHub or newsletter. It's free now; Medium plans to charge for it later and will email users first.
- Link your earlier posts at the end when they're related, so readers who liked this one keep reading.

## Step 6: Publish and read the stats

Where and how you publish decides who sees the story first, especially while you have few followers.

**Topics (tags)**

- Use all **5 topics**. Medium uses them to find interested readers, and since topic badges moved to the top of stories, they also work as a mini summary.
- Mix broad and specific. Scott Batson used: AI, Programming, AI Agent, Productivity, Software Development.
- Examples for us: Claude Code · AI · Productivity · Data Engineering · Software Testing.

**Publications**

- Submit to a publication in your niche (e.g. *Data Science Collective* for data and AI). Medium says publications and topics matter most for new writers without many followers.
- Three of the five feed stories went out through publications.

**Paywall (member-only)**

- Member-only stories can earn money and are promoted to members. If you choose it, make sure the hook works in the first \~150 words that non-members see.
- Free stories reach non-members and search more easily. For our first posts, reach matters more than earnings, so free is fine.

**AI search**

Medium lets AI chatbots cite stories by default. Clear headings and specific, factual answers make a post easier to cite. AI referrals are still small (under 0.5% of Google search traffic in August 2026), so don't write for them.

**Diagnose with the stats page (wait a few days first)**

| What you see | What it means | What to change next time |
| --- | --- | --- |
| Few presentations | Medium isn't showing the story much | Better topics; submit to a publication |
| Many presentations, few views | The title isn't appealing to those readers | Try another title style; show more value up front |
| Many views, low read ratio | The intro doesn't deliver what the title promised | Rewrite the opening to match the title |
| Reads, but few follows | Readers don't see a reason to follow you | Improve your bio, footer and ending |

## What to avoid

- **Clickbait titles or images.** Readers skip them, and Medium can mark them Network Only.
- **Jargon-only titles** that make sense only to experts.
- **Background openings** ("In today's world…"). Start with the scene, number or question.
- **Generic, AI-sounding text.** Medium's curators hold back writing that feels boring, repetitive or "too perfect". Use AI to edit and check, not to write the post for you; keep your own voice and experiences.
- **Writing for algorithms or SEO** instead of for a reader. Medium says over 75% of stories in a feed are there because a person recommended them.
- **Wall-of-text paragraphs** and posts with no headings.
- **The muddy middle:** a 7-minute post that is neither a sharp opinion nor a complete guide.
- **Judging a post on day one.** Wait a few days before drawing conclusions from the stats.

## Blog template

Copy this into a new Medium draft and fill in each part.

```markdown
# [TITLE: a question or bold claim, 8–12 words, plain words, a number if you have one]
## [SUBTITLE: teases the answer or adds the missing detail, under 15 words]

[COVER IMAGE: your own photo or visual]
[Caption: short, a little witty]

[OPENING, 2–4 short paragraphs, under 150 words]
- Line 1–2: a scene, a hard number, a comparison or a question
- Why you: one line on your experience with this
- The promise: what the reader gets by reading on

## [Heading 1: the problem, told as a story]
[Short paragraphs. First person. What happened, what it cost.]

## [Heading 2: what I tried / step 1]
[Screenshot, diagram or code block]

## [Heading 3: what worked / step 2]
[Before/after numbers, with where they came from]

## [Heading 4: what I'd do differently / step 3]
[Honest limits and mistakes]

## [Optional: FAQ]
[2–4 questions readers will ask]

[ENDING]
- One clear takeaway or a line worth quoting
- A question for readers to answer in the comments
- Links to related earlier posts

[Custom footer: LinkedIn / GitHub / newsletter]

Topics (5): [broad] · [broad] · [specific] · [specific] · [specific]
Publication: [niche publication to submit to]
```

## Pre-publish checklist

Tick every box before you hit publish.

**Before writing**

- [ ] Format chosen: short opinion (3–5 min) or complete guide (10+ min)
- [ ] Topic is timely and comes from my own experience

**Title and subtitle**

- [ ] Title is a question or bold claim, 8–12 plain words
- [ ] Title has a specific number or result, if I have one
- [ ] No clickbait: the post delivers exactly what the title promises
- [ ] Subtitle teases the answer or adds the missing detail

**Opening**

- [ ] First two lines: a scene, number, comparison or question
- [ ] Says why I'm the one writing this
- [ ] The hook works within the first 150 words

**Body**

- [ ] 3–6 headings, written as mini-stories or numbered steps
- [ ] Paragraphs are 1–3 sentences; it reads well on a phone
- [ ] First person, honest about mistakes, a bit of humour
- [ ] Real numbers, with their source
- [ ] Cover image with caption; screenshots or code blocks for technical parts
- [ ] Read aloud once: nothing sounds generic or AI-written

**Ending and profile**

- [ ] Ends with a clear takeaway or quotable line
- [ ] Asks readers a specific question
- [ ] Bio filled in; custom footer set up

**Publishing**

- [ ] All 5 topics added (broad + specific)
- [ ] Submitted to a niche publication
- [ ] Free or member-only decided
- [ ] Stats checked after a few days, using the diagnosis table
