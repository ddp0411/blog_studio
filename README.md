# Blog Studio

My Claude Code workspace for writing blog posts that sound like me, not like a model. Rough notes go in, a post comes out, and a humanizer pass plus a lint script catch the AI tells before anything ships.

## Set up on a new laptop

Needs: Claude Code, Python 3.8+, git.

**macOS**

One-time prerequisites (skip any you already have):

```bash
xcode-select --install        # gives you git and python3
brew install gh               # optional: GitHub CLI for syncing (needs Homebrew)
```

Then either double-click `setup.command` in Finder (first time: right-click > Open > Open, because macOS blocks unsigned scripts), or in Terminal:

```bash
unzip ~/Downloads/blog-studio.zip -d ~ && cd ~/blog-studio
bash setup.sh
```

Mac notes:
- `.claude/` is hidden in Finder. Press Cmd + Shift + . to show hidden files.
- Setup removes the macOS quarantine flag from the folder so the scripts can run.
- Works with the bash 3.2 that ships with macOS and with zsh as your login shell.
- The lint command is the same: `python3 scripts/ai_tells.py <file>`.

**Linux / WSL**

```bash
unzip blog-studio.zip -d ~ && cd ~/blog-studio
bash setup.sh
```

**Windows (PowerShell)**

```powershell
Expand-Archive blog-studio.zip -DestinationPath $HOME; cd $HOME\blog-studio
powershell -ExecutionPolicy Bypass -File .\setup.ps1
```

Setup does three things, and is safe to rerun:

1. Adds a short "who I am + writing rules" block to `~/.claude/CLAUDE.md` (between `BLOG-STUDIO` markers, so reruns replace it instead of duplicating).
2. Copies the humanizer skill to `~/.claude/skills/humanizer`, so `/humanizer` works in any folder.
3. Runs `git init` if needed. Push to a private GitHub repo to sync laptops; after that, `git pull` on the other machine instead of copying zips.

Use `--no-global` / `-NoGlobal` to leave `~/.claude` alone.

**Syncing Mac and Windows.** `.gitattributes` keeps line endings as LF for `.sh`, `.py`, and `.md` files, so a commit from Windows won't break the scripts on the Mac.

## Daily use

```bash
cd ~/blog-studio && claude
```

| You type | What happens |
| --- | --- |
| `/blog-draft new claude-code-tokens` | Makes `posts/<date>-claude-code-tokens/` with notes.md and a checklist |
| (paste notes into notes.md) `/blog-draft` | Picks format, 5 titles, writes draft.md with `[TODO]` gaps, humanizes, lints |
| Answer the TODOs in chat | Claude folds them in and re-lints |
| `/humanizer posts/<folder>/draft.md` | Extra humanizer pass any time |
| `python3 scripts/ai_tells.py posts/<folder>/draft.md` | Lint by hand |
| "approved, make final" | Copies to final.md |
| `/cross-post claude-code-tokens` | site, Medium, Dev.to, Hashnode, LinkedIn versions with canonical links |
| `/stats-review claude-code-tokens` (after 7 days) | Diagnoses the numbers, logs them, suggests changes |

## What's in here

```
CLAUDE.md                     rules Claude follows in this folder (loads profile, voice, banned list)
context/profile.md            who I am, projects, audience, CTA, off-limits
context/voice.md              my tone and the habits to drop
context/banned-patterns.md    FAIL/WARN list
context/platforms.md          per-platform format, canonical, tags, limits
context/medium-playbook.md    full Medium research
voice/samples/                my own paragraphs (add these!)
templates/                    post template, pre-publish checklist
posts/                        one folder per post; _ideas.md backlog
stats/log.md                  results per post per platform
scripts/ai_tells.py           lint (no dependencies)
scripts/update_humanizer.sh   pull latest humanizer from GitHub
.claude/skills/               humanizer (MIT, blader/humanizer), blog-draft, cross-post, stats-review
global/CLAUDE.global.md       the block setup adds to ~/.claude/CLAUDE.md
```

## Before the first post

- [ ] Add 2 to 4 voice samples to `voice/samples/` (dash-free; see the README there)
- [ ] Fill the TODOs in `context/profile.md` (paper titles, the 92% accuracy context)
- [ ] Confirm your site's frontmatter format and update `templates/post-template.md` and `context/platforms.md`
- [ ] Set the Medium custom footer once (Settings → Publishing → Manage Story Footer)

## Updating humanizer

```bash
./scripts/update_humanizer.sh && git diff .claude/skills/humanizer
```

Vendored version: humanizer 4.0.0 (commit in `.claude/skills/humanizer/VERSION_COMMIT`). Humanizer is MIT licensed by blader; its LICENSE file sits next to the skill.
