---
name: youtube-transcribe
description: Transcribe a YouTube video to clean plain text. Triggers on a YouTube URL with a request to transcribe/get the transcript/text of a video, or `/youtube-transcribe <url>`. Produces a cleaned transcript plus video metadata (title, channel, upload date, URL) ready to hand off to the article/KG processing workflow.
---

# YouTube → Text Transcription

Turn a YouTube video into clean plain text so it can be fed into the normal
[[article-processing-instruction]] / `awesome-search-knowledge-graph` workflow.

## When to use

- The user gives a YouTube URL and asks to transcribe it, "get the text", "get the transcript", or "process this video".
- `/youtube-transcribe <url>`

This skill only produces text + metadata. It does **not** create vault notes — hand the
result off to the `awesome-search-knowledge-graph` skill (which, per [[video_notes_convention]],
puts video content in `Awesome Search/Videos/` with `type: video`, not `Articles/`).

## Tooling (verified available on this machine)

- `yt-dlp` — downloads captions and audio. **Primary path** — no transcription model needed when captions exist.
- `ffmpeg` — audio extraction (fallback path only).
- `whisper` is **not** installed. The fallback path needs it; see step 3.

Work in the scratchpad directory, not the vault or `/tmp`.

## Workflow

### 1. Fetch metadata

```bash
yt-dlp --skip-download --print "%(title)s\n%(uploader)s\n%(upload_date)s\n%(webpage_url)s\n%(duration_string)s" "<URL>"
```

Capture: **title**, **channel/uploader** (→ author), **upload_date** YYYYMMDD (→ published),
**canonical URL** (→ source), duration. Keep these — the downstream note needs them.

### 2. Primary path — extract captions (fast, preferred)

Most videos have manual or auto-generated captions. Prefer manual (`--write-subs`) over
auto (`--write-auto-subs`); convert to a stable format and clean.

```bash
cd "<scratchpad>"
yt-dlp --skip-download \
  --write-subs --write-auto-subs \
  --sub-langs "en,en-orig" --sub-format vtt \
  --convert-subs vtt \
  -o "cap.%(ext)s" "<URL>"
```

**Do not** use a wildcard like `--sub-langs "en.*"` — it matches every machine-translated
`en-XX` track (en-ar, en-bn, …), which downloads dozens of files and trips YouTube's
`HTTP 429 Too Many Requests` rate limit. List exact codes: `en` (and `en-orig` for the
original track of a dubbed video). To see what a video actually offers, run
`yt-dlp --list-subs --skip-download "<URL>"` first.

Then clean the `.vtt` into deduplicated prose with the bundled script:

```bash
python3 ~/.claude/skills/youtube-transcribe/scripts/vtt2text.py cap.en.vtt > transcript.txt
```

Notes:
- If both a manual `cap.en.vtt` and an auto-generated file appear, prefer the manual one
  (human captions have punctuation and casing). Use `--list-subs` to tell them apart.
- For non-English videos, pass the exact language code (e.g. `--sub-langs "ru,ru-orig"`).
  If the user wants English from a foreign video, try `--sub-langs "en"` for a translated
  track; if none exists, fall back to the original language.
- Inspect `transcript.txt` — captions lack punctuation/casing but are fully usable for KG extraction.

### 3. Fallback path — no captions available

If step 2 yields no `.vtt` (or an empty transcript), the video has no captions. `whisper` is not
installed, so **stop and tell the user** rather than silently failing. Offer:

- **Install a transcriber** (one-time), e.g. `pipx install openai-whisper` or `brew install whisper-cpp` / `uv tool install mlx-whisper` (Apple Silicon, fastest). Then:
  ```bash
  yt-dlp -x --audio-format mp3 -o "audio.%(ext)s" "<URL>"
  whisper audio.mp3 --model small --output_format txt --output_dir .   # or: mlx_whisper audio.mp3
  ```
- Or the user pastes any transcript they already have.

Don't assume a transcriber exists — verify with `which` before invoking, and don't download
large models without asking.

### 4. Assemble the handoff

Produce a small text/markdown block the article workflow can consume directly:

```markdown
---
title: "<title>"
type: video
source: <canonical URL>
author: "<channel/uploader>"
published: <YYYY-MM-DD>
tags: [video]
---

# <title>

<cleaned transcript text>
```

Save it to the vault's `raw_articles/` staging folder (or the scratchpad if the user prefers),
then offer to run the `awesome-search-knowledge-graph` skill on it to create the linked
`Videos/` note and extract entities.

## Guardrails

- Only transcribe videos the user explicitly provides. Don't batch-crawl channels/playlists unless asked.
- Downloading full audio is bandwidth-heavy — only do it on the fallback path, and prefer captions.
- Report honestly when captions are missing or a language track isn't available; don't fabricate transcript text.
