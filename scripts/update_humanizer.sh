#!/usr/bin/env bash
# Pull the latest humanizer SKILL.md from github.com/blader/humanizer into this folder
# (and into ~/.claude/skills if it's installed there). Review the diff before committing.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

git clone -q --depth 1 https://github.com/blader/humanizer.git "$TMP/humanizer"
DEST="$HERE/.claude/skills/humanizer"
cp "$TMP/humanizer/SKILL.md" "$TMP/humanizer/LICENSE" "$DEST/"
git -C "$TMP/humanizer" rev-parse --short HEAD > "$DEST/VERSION_COMMIT"
echo "Updated project copy to commit $(cat "$DEST/VERSION_COMMIT")"

if [[ -d "$HOME/.claude/skills/humanizer" ]]; then
  cp "$DEST/"* "$HOME/.claude/skills/humanizer/"
  echo "Updated ~/.claude/skills/humanizer"
fi
grep -m1 'version:' "$DEST/SKILL.md" || true
echo "Check 'git diff .claude/skills/humanizer' before committing."
