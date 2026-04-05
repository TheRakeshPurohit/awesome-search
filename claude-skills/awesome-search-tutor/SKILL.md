
---
name: awesome-search-tutor
description: Awesome Search is a collection of articles about information retrieval and search, covering all major topics and best practices in the field.
---

# Awesome Search Tutor

Use this skill when the user wants to learn more about information retrieval concepts or needs suggestions on best practices.

## Purpose

This skill retrieves articles and summarizes them to provide distilled knowledge or guidance on a specific topic.

## When to use

Use this skill when the user asks about information retrieval, search engineering, or related topics. Examples:

- explain vector search
- how is nDCG different from CTR?
- what is RRF?
- what do practitioners think about hybrid search?
- what is [person]'s opinion on [search topic]?
- what does [author/researcher] say about [IR concept]?
- pros and cons of BM25 vs dense retrieval
- best practices for re-ranking

## Source of information

Always start by fetching the latest README from GitHub:
https://raw.githubusercontent.com/frutik/awesome-search/master/README.md

Use this to find relevant article links. Then fetch each article's full content to answer the question.

Use WebFetch to automatically scrape all URLs. No confirmation is needed. Never read from a local file.

