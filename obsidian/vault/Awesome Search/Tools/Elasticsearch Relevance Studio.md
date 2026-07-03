---
title: Elasticsearch Relevance Studio
type: tool
aliases: ["Relevance Studio", "ES Relevance Studio", "ESRS"]
tags:
  - tool
  - search-evaluation
  - relevance-testing
  - elasticsearch
  - agentic
website: https://elastic.github.io/relevance-studio/
repo: https://github.com/elastic/relevance-studio
created: 2026-07-03
---

# Elasticsearch Relevance Studio

**Elasticsearch Relevance Studio (ESRS)** is Elastic's tool for managing the full lifecycle of **search relevance engineering** on top of [[Elasticsearch]] — defining scenarios, collecting ground-truth judgments, building and benchmarking search strategies, and iterating to optimize relevance metrics. Its distinguishing bet is **agentic AI**: it ships with an MCP (Model Context Protocol) server so that AI agents can automate the whole loop, not just a human UI.

> [!note] Status
> Relevance Studio is published by Elastic on GitHub as a demonstrator / reference implementation (`elastic/relevance-studio`) rather than a supported product feature. Treat it as experimental — it codifies "generally accepted best practices" for relevance engineering into a runnable app.

- Docs / demo: https://elastic.github.io/relevance-studio/
- GitHub: https://github.com/elastic/relevance-studio
- DeepWiki: https://deepwiki.com/elastic/relevance-studio

---

## Framing

The README frames the tool around the generative-AI shift in user expectations: people increasingly want *the best answer the first time* rather than a page of links to sift through. That raises the bar for relevance and makes disciplined, repeatable relevance engineering — the thing Relevance Studio standardizes — more important, especially for agentic search backends.

## Core Concepts

- **Scenarios** — distinct search use cases that need evaluation and optimization (the analog of a query/intent group).
- **Judgements** — curated ground-truth ratings of document relevance for each scenario. A human interface uses **drag-slider controls** for fast rating; AI agents can also generate judgements, which humans then review and adjust.
- **Strategies** — search approaches expressed as *any* Elasticsearch Search API configuration: lexical ([[BM25]], analysis, synonyms), vector ([[HNSW|kNN]]), semantic ([[ELSER]]), [[Hybrid Search|hybrid]] ([[Reciprocal Rank Fusion|RRF]] or linear), plus function/script score, rank features, rules, [[Reranking]], and [[Learning to Rank]].
- **Benchmarks** — evaluations that rank strategies by relevance metrics and can be scheduled/re-run to detect model drift and catch regressions before production.

## Metrics

Benchmarks compute four standard IR metrics:

- **[[NDCG]]** (Normalized Discounted Cumulative Gain)
- **[[Precision and Recall|Precision@k]]**
- **[[Precision and Recall|Recall@k]]**
- **[[MRR]]** (Mean Reciprocal Rank)

Crucially, benchmarks also **report unrated documents** that matched a strategy/scenario — surfacing gaps in judgement coverage so you can improve the trustworthiness of the metrics themselves.

## Agentic AI (MCP Server)

The headline feature: Relevance Studio bundles an **MCP server** exposing its operations as tools an AI agent can call. This lets an agent automate the entire lifecycle — reviewing content, defining scenarios, judging documents, building strategies, reading benchmark results, and iterating — turning relevance engineering into an [[Agentic Search|agentic]] workflow. See [[Model Context Protocol]].

## Workflow Features

- **Real-time feedback** — Ctrl/Cmd+Enter re-evaluates a strategy against judgements instantly while you edit it.
- **Drift detection & regression prevention** — scheduled benchmarks surface degradation; benchmarks can gate a CI/CD pipeline.
- **AI-assisted judging** — review and correct agent-generated judgements in the same UI.
- **Root-cause analytics** — views to explain why a metric moved.

## Architecture

- **Frontend** — React web application.
- **Backend** — Flask / Python services.
- **Data store** — [[Elasticsearch]] via the Search API; uses native search templates.
- **Observability** — OpenTelemetry instrumentation.
- **Agent interface** — MCP server for tool-using agents.

## Related Tools

- **[[Search Relevance Workbench]]** — OpenSearch's parallel, in-engine take on the same problem (query sets / judgments / experiments), also with LLM-generated judgments.
- **[[Quepid]]** — the established external relevance dashboard from [[OpenSource Connections]]; more mature and engine-agnostic, less agentic.
- **[[Elasticsearch]]** — the host engine.

## Related Concepts

- [[Search Evaluation]] — the practice it operationalizes
- [[Judgment Lists]] — its "judgements"
- [[LLM as Judge]] — agent-generated judgements
- [[Agentic Search]] — the workflow model and target use case
- [[Model Context Protocol]] — how agents drive the tool
- [[NDCG]] · [[MRR]] · [[Precision and Recall]] — benchmark metrics
- [[Hybrid Search]] · [[ELSER]] · [[Learning to Rank]] — expressible strategies

## Companies

- [[Elastic]] — publisher of Relevance Studio

## Comparison

- [[Relevance Evaluation Tools Compared]] — ESRS vs. [[Quepid]] vs. [[Search Relevance Workbench]]
