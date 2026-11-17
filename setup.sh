#!/usr/bin/env bash
# Blog Studio setup for macOS / Linux / WSL / Git Bash.
# Safe to run more than once.
#   ./setup.sh                      full setup
#   ./setup.sh --no-global          skip ~/.claude changes (folder-only)
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_HOME="${HOME}/.claude"
GLOBAL=1
[[ "${1:-}" == "--no-global" ]] && GLOBAL=0

echo "Blog Studio: $HERE"

OS="$(uname -s)"

# macOS: files from a downloaded zip carry a quarantine flag that can block scripts
if [[ "$OS" == "Darwin" ]]; then
  xattr -dr com.apple.quarantine "$HERE" 2>/dev/null || true
fi

# 1. Tools
# On a fresh Mac, /usr/bin/python3 is a stub that only offers to install the
# Command Line Tools, so test that it really runs.
if ! python3 -c "import sys; assert sys.version_info >= (3, 8)" >/dev/null 2>&1; then
  echo "ERROR: Python 3.8+ is needed (setup and the lint script use it)."
  if [[ "$OS" == "Darwin" ]]; then
    echo "  On macOS run:  xcode-select --install   (or: brew install python)"
    echo "  Then run this setup again."
  fi
  exit 1
fi
command -v claude  >/dev/null || echo "WARN: 'claude' (Claude Code) not found. Install: https://docs.claude.com/en/docs/claude-code"
command -v git     >/dev/null || echo "WARN: git not found. Needed to sync this folder between laptops (macOS: xcode-select --install)."
if [[ "$OS" == "Darwin" ]] && ! command -v gh >/dev/null; then
  echo "TIP: install the GitHub CLI for one-command repo setup: brew install gh"
fi
chmod +x "$HERE/scripts/"*.py "$HERE/scripts/"*.sh 2>/dev/null || true

if [[ $GLOBAL -eq 1 ]]; then
  mkdir -p "$CLAUDE_HOME/skills"

  # 2. Global CLAUDE.md block (replaced between markers, never duplicated)
  GFILE="$CLAUDE_HOME/CLAUDE.md"
  touch "$GFILE"
  python3 - "$GFILE" "$HERE/global/CLAUDE.global.md" "$HERE" <<'PY'
import re, sys, pathlib
gfile, block_file, here = sys.argv[1:4]
g = pathlib.Path(gfile).read_text(encoding="utf-8")
block = pathlib.Path(block_file).read_text(encoding="utf-8").strip()
block = block.replace("work inside my blog-studio folder", f"work inside my blog-studio folder ({here})")
pat = re.compile(r"<!-- BLOG-STUDIO:START.*?BLOG-STUDIO:END -->", re.S)
if pat.search(g):
    g = pat.sub(lambda m: block, g)
    action = "updated"
else:
    g = (g.rstrip() + "\n\n" if g.strip() else "") + block + "\n"
    action = "added"
pathlib.Path(gfile).write_text(g, encoding="utf-8")
print(f"Global ~/.claude/CLAUDE.md: block {action}")
PY

  # 3. Humanizer as a personal skill, so /humanizer works in every folder
  rm -rf "$CLAUDE_HOME/skills/humanizer"
  cp -R "$HERE/.claude/skills/humanizer" "$CLAUDE_HOME/skills/humanizer"
  echo "Humanizer skill: installed to ~/.claude/skills/humanizer"
fi

# 4. Git
if command -v git >/dev/null && [[ ! -d "$HERE/.git" ]]; then
  git -C "$HERE" init -q -b main 2>/dev/null || git -C "$HERE" init -q
  echo "Git: initialized. Push it to a PRIVATE repo:"
  echo "  cd \"$HERE\" && git add -A && git commit -m 'Blog studio setup'"
  echo "  gh repo create blog-studio --private --source=. --push"
fi

cat <<EOF

Done. Next:
  1. Add 2-4 of your own paragraphs to voice/samples/ (see the README there).
  2. cd "$HERE" && claude
  3. Try:  /blog-draft new my-first-post

Optional: install humanizer as an auto-updating plugin instead (inside Claude Code):
  /plugin marketplace add blader/humanizer
  /plugin install humanizer@humanizer
EOF
