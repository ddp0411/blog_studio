#!/usr/bin/env bash
# macOS: double-click this file in Finder to run setup in Terminal.
# If macOS says it can't be opened, right-click it > Open > Open (needed once).
cd "$(dirname "$0")" || exit 1
bash ./setup.sh "$@"
echo
read -r -p "Press Return to close this window..." _
