#!/usr/bin/env python3
"""Lint a blog post for AI-writing tells and house-style rules.

Usage:
    python3 scripts/ai_tells.py posts/2026-11-20-slug/draft.md [more files...]

Skips YAML frontmatter (except title/subtitle checks), fenced code blocks,
inline code, HTML comments, and URLs. Exit code 1 if any FAIL is found.
No dependencies beyond the Python 3.8+ standard library.
"""
import re
import statistics
import sys
from pathlib import Path

# ---------------------------------------------------------------- word lists

BANNED_WORDS = [
    "genuinely", "delve", "delves", "delving", "crucial", "crucially", "pivotal",
    "seamless", "seamlessly", "leverage", "leverages", "leveraging", "leveraged",
    "landscape", "tapestry", "testament", "showcase", "showcases", "showcasing",
    "underscore", "underscores", "underscoring", "vibrant", "meticulous",
    "meticulously", "intricate", "intricacies", "game-changer", "game changer",
    "unlock", "unlocks", "unlocking", "unleash", "unleashes", "elevate",
    "elevates", "empower", "empowers", "empowering", "harness", "harnessing",
    "realm", "embark", "embarking", "supercharge", "supercharged",
    "revolutionize", "revolutionizes", "revolutionizing", "cutting-edge",
    "ever-evolving", "synergy", "bustling", "nestled", "furthermore",
    "moreover", "additionally",
]

BANNED_PHRASES = [
    "in today's fast-paced", "in the ever-changing", "ai is changing everything",
    "let's dive in", "let's dive deep", "deep dive", "without further ado",
    "let's break it down", "let's break this down", "here's the thing",
    "here's what you need to know", "here's the kicker", "honestly?", "real talk",
    "the real question is", "at its core", "at the end of the day",
    "what really matters", "it's worth noting", "it is worth noting",
    "it's important to note", "it is important to note", "needless to say",
    "in conclusion", "to sum up", "in summary", "i hope this helps",
    "happy coding", "the future looks bright", "exciting times ahead",
    "a step in the right direction", "let that sink in", "read that again",
    "that's the real win", "plays a key role", "plays a crucial role",
    "stands as a testament", "serves as a", "as an ai", "as of my last update",
    "i don't have access to", "worth knowing", "the lesson:", "concretely:",
    "here's what i got wrong",
]

BRITISH = [
    "behaviour", "behaviours", "colour", "colours", "favourite", "favourites",
    "optimise", "optimised", "optimising", "optimisation", "organise",
    "organised", "organising", "organisation", "organisations", "analyse",
    "analysed", "analysing", "realise", "realised", "realising", "recognise",
    "recognised", "prioritise", "prioritised", "summarise", "summarised",
    "centre", "centres", "modelling", "modelled", "travelled", "travelling",
    "cancelled", "cancelling", "labelled", "labelling", "licence", "programme",
    "programmes", "catalogue", "utilise", "utilised", "minimise", "maximise",
    "standardise", "visualise", "visualisation", "customise", "customised",
    "initialise", "serialise", "normalise", "normalised", "categorise",
    "emphasise", "apologise", "humour", "flavour", "neighbour", "honour",
    "labour", "defence", "offence", "grey", "judgement", "learnt", "spelt",
]

WARN_WORDS = {"robust": 1, "just": 4, "actually": 2, "simply": 2, "quietly": 1,
              "really": 3, "very": 3, "basically": 1, "literally": 1}

CONTRAST_PATTERNS = [
    r"\bnot (?:just|only|merely|simply) [^.!?]{1,80}?\bbut\b",
    r"\b(?:isn't|is not|wasn't|was not|aren't|are not)\b [^.!?]{1,60}?[,;:] (?:it's|it is|it was|they're|they are)\b",
    r"\b(?:it's|it is|this is|that's) not\b[^.!?]{1,60}?[,;:] (?:it's|it is|this is|but)\b",
    r"\bnot because\b[^.!?]{1,80}?\bbut because\b",
    r"[a-z]\w*, not (?!only\b|just\b|sure\b|yet\b|always\b|all\b|every\b|even\b|to\b|that\b|a lot\b)[a-z]",
    r"\brather than\b",
]

EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F2FF⭐⬆↔-⇿✅❌]"
)

# ---------------------------------------------------------------- helpers


def strip_inline(line):
    line = re.sub(r"`[^`]*`", " ", line)                   # inline code
    line = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", line)       # images
    line = re.sub(r"\]\([^)]*\)", "]", line)                # link targets
    line = re.sub(r"https?://\S+", " ", line)               # bare URLs
    line = re.sub(r"<!--.*?-->", " ", line)                 # one-line comments
    return line


def split_sentences(text):
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"'(\[])", text.strip())
    return [p for p in parts if len(p.split()) > 0]


def is_title_case(heading):
    words = [w for w in re.findall(r"[A-Za-z][\w']*", heading)]
    small = {"a", "an", "the", "and", "or", "but", "of", "to", "in", "on", "at",
             "for", "with", "vs", "by", "is", "it", "as", "from"}
    candidates = [w for w in words[1:] if w.lower() not in small and not w.isupper()]
    if len(candidates) < 3:
        return False
    caps = sum(1 for w in candidates if w[0].isupper())
    return caps / len(candidates) > 0.75


# ---------------------------------------------------------------- main lint


def lint(path):
    raw = Path(path).read_text(encoding="utf-8")
    lines = raw.splitlines()
    fails, warns, info = [], [], []

    # frontmatter
    start = 0
    meta = {}
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                start = i + 1
                break
            m = re.match(r"^(\w+):\s*\"?(.*?)\"?\s*$", lines[i])
            if m:
                meta[m.group(1)] = m.group(2)

    title = meta.get("title", "")
    if not title or title.startswith("["):
        for ln in lines[start:]:
            if ln.startswith("# "):
                title = ln[2:].strip()
                break
    for label, val in (("title", title), ("subtitle", meta.get("subtitle", ""))):
        lv = val.lower()
        for w in BANNED_WORDS + [b for b in BANNED_PHRASES]:
            if re.search(rf"(?<![\w-]){re.escape(w)}", lv):
                fails.append(f"{label}: banned word/phrase '{w}'")
        if "\u2014" in val or "\u2013" in val:
            fails.append(f"{label}: dash")
    if title and not title.startswith("["):
        n = len(title.split())
        if not 8 <= n <= 12:
            warns.append(f"title: {n} words (aim for 8 to 12): {title!r}")
    sub = meta.get("subtitle", "")
    if sub and not sub.startswith("[") and len(sub.split()) > 15:
        warns.append(f"subtitle: {len(sub.split())} words (keep under 15)")

    in_code = False
    in_comment = False
    prose_lines = []          # (lineno, text)
    headings = []
    bold_count = 0
    triads = []

    for idx in range(start, len(lines)):
        lineno = idx + 1
        line = lines[idx]
        s = line.strip()
        if s.startswith("```") or s.startswith("~~~"):
            in_code = not in_code
            prose_lines.append((lineno, ""))
            continue
        if in_code:
            continue
        if "<!--" in s and "-->" not in s:
            in_comment = True
            continue
        if in_comment:
            if "-->" in s:
                in_comment = False
            continue

        text = strip_inline(line)
        low = text.lower()

        # TODO markers (check raw line so inline code doesn't hide them)
        if "[TODO" in line:
            fails.append(f"L{lineno}: leftover [TODO] marker")

        # punctuation
        for ch, name in (("—", "em dash"), ("–", "en dash")):
            if ch in text:
                fails.append(f"L{lineno}: {name}: {s[:90]}")
        if re.search(r"\s--\s", text):
            fails.append(f"L{lineno}: double hyphen used as dash")
        if re.search(r"[“”‘’]", text):
            fails.append(f"L{lineno}: curly quotes (use straight quotes)")
        if EMOJI_RE.search(text):
            fails.append(f"L{lineno}: emoji")
        no_quotes = re.sub(r"\"[^\"]*\"", " ", text)
        if "!" in no_quotes.replace("![", ""):
            fails.append(f"L{lineno}: exclamation mark outside a quote")

        # words and phrases
        for w in BANNED_WORDS:
            if re.search(rf"(?<![\w-]){re.escape(w)}(?![\w-])", low):
                fails.append(f"L{lineno}: banned word '{w}'")
        for p in BANNED_PHRASES:
            if p in low.replace("’", "'"):
                fails.append(f"L{lineno}: banned phrase '{p}'")
        for w in BRITISH:
            if re.search(rf"\b{w}\b", low):
                fails.append(f"L{lineno}: British spelling '{w}'")

        # structure
        if s.startswith("#"):
            h = s.lstrip("#").strip()
            headings.append((lineno, h))
            if is_title_case(h):
                warns.append(f"L{lineno}: heading looks Title Case (use sentence case): {h!r}")
            prose_lines.append((lineno, ""))
            continue
        bold_count += len(re.findall(r"\*\*[^*]+\*\*", text))
        for m in re.finditer(r"\b\w+(?: \w+)?, \w+(?: \w+)?,? and \w+", text):
            triads.append(lineno)
        prose_lines.append((lineno, text))

    # paragraph / sentence analysis
    paragraphs, cur, cur_start = [], [], None
    for lineno, t in prose_lines + [(None, "")]:
        st = t.strip()
        is_list = bool(re.match(r"^([-*+]|\d+\.)\s", st)) or st.startswith("|") or st.startswith(">")
        if not st or is_list:
            if cur:
                paragraphs.append((cur_start, " ".join(cur)))
            cur, cur_start = [], None
            continue
        if cur_start is None:
            cur_start = lineno
        cur.append(st)

    all_sentences = []
    for lineno, para in paragraphs:
        sents = split_sentences(para)
        all_sentences.extend(sents)
        if len(sents) > 4:
            warns.append(f"L{lineno}: paragraph has {len(sents)} sentences (aim for 1 to 3)")

    body_text = " ".join(p for _, p in paragraphs)
    low_body = body_text.lower()

    spans = []
    for pat in CONTRAST_PATTERNS:
        for m in re.finditer(pat, low_body):
            if not any(a <= m.end() and m.start() <= b for a, b, _ in spans):
                spans.append((m.start(), m.end(), m.group(0)))
    contrasts = [t for _, _, t in spans]
    if title:
        for pat in CONTRAST_PATTERNS:
            contrasts += [m.group(0) for m in re.finditer(pat, title.lower())]
    if len(contrasts) > 1:
        sample = "; ".join(c[:50] for c in contrasts[:4])
        warns.append(f"{len(contrasts)} 'not X but Y' style contrasts (max 1): {sample}")

    for w, limit in WARN_WORDS.items():
        n = len(re.findall(rf"\b{w}\b", low_body))
        if n > limit:
            warns.append(f"'{w}' used {n} times (limit {limit})")

    if bold_count > 3:
        warns.append(f"{bold_count} bold phrases (keep to 3 or fewer)")
    if len(triads) > 2:
        warns.append(f"{len(triads)} lists of three in prose (lines {sorted(set(triads))[:8]}): vary them")

    h2 = [h for h in headings if not h[1].startswith("[")]
    if h2 and not 3 <= len(h2) <= 7:
        warns.append(f"{len(h2)} headings (aim for 3 to 6 plus title)")

    lengths = [len(s.split()) for s in all_sentences if len(s.split()) > 0]
    words = len(body_text.split())
    if len(lengths) >= 8:
        sd = statistics.pstdev(lengths)
        mean = statistics.mean(lengths)
        info.append(f"sentences: {len(lengths)}, mean {mean:.1f} words, spread (stdev) {sd:.1f}")
        if sd < 4:
            warns.append(f"sentence lengths are too even (stdev {sd:.1f}); mix short and long")
        short = sum(1 for n in lengths if n <= 6)
        if short == 0:
            warns.append("no short sentences (6 words or fewer); add a couple for rhythm")

    info.append(f"words: {words}, reading time ~{max(1, round(words / 265))} min")
    if 1100 < words < 1900:
        warns.append(f"{words} words is the muddy middle (pick 600-1,000 opinion or 2,000+ guide)")

    first150 = " ".join(body_text.split()[:150]).lower()
    if re.match(r"^(in today|in the world of|ai is|\w+ is a (?:type|kind|form) of|according to wikipedia)", first150):
        warns.append("opening starts with background or a definition")

    return fails, warns, info


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    any_fail = False
    for path in argv[1:]:
        fails, warns, info = lint(path)
        print(f"\n== {path}")
        for i in info:
            print(f"  INFO  {i}")
        for w in warns:
            print(f"  WARN  {w}")
        for f in fails:
            print(f"  FAIL  {f}")
        if fails:
            any_fail = True
            print(f"  -> {len(fails)} FAIL, {len(warns)} WARN")
        else:
            print(f"  -> clean ({len(warns)} WARN to review)")
    return 1 if any_fail else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
