# Banned patterns

`scripts/ai_tells.py` checks most of these automatically. Humanizer (§1 to §26) covers the rest. FAIL items block publishing; WARN items need a second look.

## FAIL: never in a published post

**Punctuation**
- Em dash (—) or en dash (–) in prose
- Double hyphen used as a dash ( -- )
- Curly quotes (“ ” ‘ ’) in markdown source. Use straight quotes.
- Exclamation marks outside quoted dialogue
- Emojis in headings or body

**Words**
genuinely, delve, crucial, pivotal, robust (figurative), seamless, seamlessly, leverage (verb), landscape (abstract), tapestry, testament, showcase, underscore (verb), vibrant, meticulous, intricate, game-changer, game changer, unlock, unleash, elevate, empower, harness, realm, embark, supercharge, revolutionize, cutting-edge, ever-evolving, synergy, bustling, nestled, furthermore, moreover, additionally

**Phrases**
- "In today's fast-paced world", "In the ever-changing world of", "AI is changing everything"
- "Let's dive in", "Let's dive deep", "deep dive", "Without further ado", "Let's break it down"
- "Here's the thing", "Here's what you need to know", "Here's the kicker", "Honestly?", "Real talk"
- "The real question is", "At its core", "At the end of the day", "What really matters"
- "It's worth noting", "It's important to note", "Needless to say"
- "In conclusion", "To sum up", "In summary"
- "I hope this helps", "Happy coding!", "Let me know in the comments if" (a specific question is fine)
- "The future looks bright", "Exciting times ahead", "a step in the right direction"
- "Let that sink in", "Read that again", "That's the real win"
- "plays a key role", "stands as a testament", "serves as a"

**British spellings** (we write American English): behaviour, colour, favourite, optimise, organise, analyse, realise, recognise, prioritise, summarise, centre, modelling, travelled, cancelled, labelled, licence (noun), programme (non-code), catalogue

**Leftovers**
- Any `[TODO` marker
- "As an AI", "as of my last update", "I don't have access to"

## WARN: allowed once, flagged when repeated

- "not X but Y", "isn't X, it's Y", "X, not Y", "rather than" contrasts: max 1 per post
- Rhetorical one-line paragraph that repeats the paragraph before it
- Lists of exactly three items appearing more than twice
- Paragraphs longer than 4 sentences
- More than 3 bolded phrases in a post
- Headings in Title Case
- Sentence lengths that are all similar (low variety)
- "quietly", "actually", "simply", "just" more than twice each
- Opening the post with a definition or background
