#!/usr/bin/env bash
set -e

TARGET_DIR="${1:-$HOME/.claude/skills}"

echo "Installing skills into $TARGET_DIR"

mkdir -p "$TARGET_DIR"

cp -R claude-skills/* "$TARGET_DIR/"

echo "Done."
