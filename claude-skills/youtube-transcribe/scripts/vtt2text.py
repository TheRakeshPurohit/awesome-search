#!/usr/bin/env python3
"""Convert a WebVTT subtitle file into clean, deduplicated plain text.

YouTube auto-generated captions are noisy: rolling windows repeat the previous
line, and lines carry inline timing tags like <00:00:01.200><c> word</c>.
This strips all of that and collapses the rolling duplicates into readable prose.

Usage: python3 vtt2text.py input.vtt > output.txt
"""
import re
import sys


def clean(vtt_text: str) -> str:
    out_lines: list[str] = []
    last = None
    for raw in vtt_text.splitlines():
        line = raw.strip()
        if not line:
            continue
        # Header / metadata lines
        if line.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")):
            continue
        # Cue timing lines, e.g. "00:00:00.000 --> 00:00:02.000 align:start position:0%"
        if "-->" in line:
            continue
        # Numeric cue index lines (SRT-style)
        if line.isdigit():
            continue
        # Strip inline timestamp/style tags: <00:00:01.200>, <c>, </c>, <c.colorXXXX>
        line = re.sub(r"<[^>]+>", "", line)
        line = line.strip()
        if not line:
            continue
        # Collapse rolling-caption duplicates (consecutive identical lines)
        if line == last:
            continue
        out_lines.append(line)
        last = line
    return "\n".join(out_lines)


if __name__ == "__main__":
    src = sys.stdin.read() if len(sys.argv) < 2 else open(sys.argv[1], encoding="utf-8").read()
    sys.stdout.write(clean(src) + "\n")
