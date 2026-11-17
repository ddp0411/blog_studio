---
name: stats-review
description: Diagnose how a published post performed and decide what to change next time. Use when Devanshu says /stats-review, pastes Medium/Dev.to/LinkedIn stats, or asks "why didn't this post do well".
argument-hint: "<slug>"
---

# stats-review: what the numbers say

1. Ask me to paste stats (or a screenshot) per platform if I haven't. Medium: presentations, views, reads, read ratio, claps, responses, follows. Dev.to: views, reactions, comments. LinkedIn: impressions, reactions, comments, reposts, link clicks.
2. If the post has been live under 3 days, say it's too early and stop.
3. Diagnose with the funnel from `context/medium-playbook.md`:

| What you see | What it means | Change next time |
| --- | --- | --- |
| Few presentations | Not shown much | Better topics; submit to a publication |
| Many presentations, few views | Title didn't land | Another title formula; show value up front |
| Many views, low read ratio | Opening didn't deliver the title's promise | Rewrite opening to match the title |
| Reads but few follows | No reason to follow | Bio, footer, ending |

4. Compare with earlier rows in `stats/log.md`: which title formula, format, and opening type did best so far?
5. Append one row per platform to `stats/log.md`.
6. Give me at most 3 concrete changes for the next post. If one is a rule worth keeping (it worked twice), offer to add it to CLAUDE.md.
