---
type: video
title: The Search Engine Migration Circus
speaker: "[[Max Irwin]]"
company: "[[OpenSource Connections]]"
event: Haystack Live meetup
medium: talk / video
url: https://www.youtube.com/watch?v=TaFLWrc4JEE
topics:
  - "[[Migration between Search Engines]]"
concepts:
  - "[[Learning to Rank]]"
tools:
  - "[[Quepid]]"
  - "[[Rated Ranking Evaluator]]"
---

# The Search Engine Migration Circus

📺 **Watch:** https://www.youtube.com/watch?v=TaFLWrc4JEE ([Haystack Live playlist](https://www.youtube.com/watch?v=TaFLWrc4JEE&list=WL))

Haystack Live talk by [[Max Irwin]] ([[OpenSource Connections]]), drawn from his search migration experience at Wolters Kluwer (MediRegs division and the Search Center of Excellence). Companion note to the topic [[Migration between Search Engines]].

## Core Framing

**Customers do not care about your technology** — they just want to find what they need. A migration is like a restaurant that renovated its kitchen: the change is invisible to the customer, but the disruption to their favorite dish is very real. The goal is a new system that is *better*, not merely *different*.

## Why Migrate

- Vendor kills the product (his first migration, ~2014–15, was forced by Microsoft deprecating **FAST ESP**).
- Expensive enterprise licensing → move to open source.
- Need new capabilities the old engine can't deliver.
- Old version of the same engine (e.g. Elasticsearch 1.2 → 7).
- Internal politics / platform standardization.

Migrations are hard because a mature search system is not just an engine — it's an organic web of config, plugins, content pipelines, and wrapping services accreted over years (**Gall's Law**).

## The Playbook

1. **Define success first.** If you can't define what success looks like, don't start. Document goals, current-system knowledge, and every decision (with reasons) in a wiki.
2. **Measure before you migrate.** Without a baseline of current search quality you'll only know the new system is *different*, not *better*. Measurement is the theme of the whole talk.
3. **"Hello Search" before estimating.** Stand up a quick proof-of-concept with the new engine and as much real content as possible. Discover the quirks, *then* estimate — and be willing to bail early.
4. **Feature parity is impossible.** Map the gap between old and new capabilities; decide what's actually used and worth rebuilding vs. replacing/dropping. Risk of a feature ≈ time × complexity.
5. **Risk register + Iron Triangle.** Track big risks; respect time/scope/money trade-offs; avoid scope creep.
6. **Content is the timeline killer.** Features are relatively clear-cut to a developer; content hides edge cases, weird field mappings, huge volume, and ETL surprises. Always add a buffer.
7. **Work streams.** Split responsibility: content, analytics, infrastructure/ops, services, relevance.
8. **Report & tune.** Data-driven, hypothesis-driven tuning; watch KPI dashboards; communicate every change.
9. **Gradual customer migration.** Run both systems in parallel, let users self-migrate voluntarily, and give them a *carrot* (a compelling new feature) rather than forcing a hard cutover.
10. **Celebrate milestones** — these projects are long and grinding.

## Practical Cases & War Stories

- **FAST ESP deprecation (~2014–15):** Microsoft killed the product → forced engine selection. Textbook "vendor deprecates" trigger.
- **Search-as-a-service onboarding:** Ran a shared search service at WK and onboarded other product teams off different engines. Origin of the time × complexity risk formula (~2016).
- **Custom query parser + highlighter = highest risk.** Legacy custom query language and highlighting were tightly coupled. They **staggered releases** (basic highlighting + a subset of the query language first, then evolve) rather than blocking launch for a year+.
- **The AWS lift-and-shift mistake.** Huge content set in a third-party data center in **Plano, TX**; "some genius" decided to *also* move to **AWS** during the engine migration. Couldn't size the cluster → "very expensive mistake." → **Stay in your existing infrastructure; migrate only the engine** until you understand the new engine's memory/cost behavior.
- **Forced cutover vs. gradual (A/B from real products).** One product where they moved everybody at once: "wasn't fun… scrambled to fix things, lost customers, angry feedback." Another where users gently self-migrated: much smoother. Hence the voluntary-migration recommendation.
- **C → Java garbage-collection gotcha.** Moving from a C-based engine (no GC) to a Java framework introduced GC, sharding, replication, and instance-sizing concerns they'd never had before.

## "Damage" Metric

Compare the top-N result IDs for the same query across legacy vs. target systems. Documents that dropped off or newly appeared = "damage." Combine with analytics: a lost doc nobody clicked doesn't matter; a lost high-download doc must be tuned back in. Run real query logs in batch to get an average difference number.

## Q&A Notes

- **Deep-learning re-ranking latency (3–4s):** don't score all results with the model — use traditional search + boosts to get good candidates into the top ~100, then **re-rank only those**.
- **Improving ETL during migration:** path of least resistance is fine, but beware hidden edge cases in the old "hooky bash scripts."
- **Relevance measurement tools:** [[Quepid]] (OSC-stewarded) and [[Rated Ranking Evaluator]] (RRE, by Sease — command-line, JSON judgments across engines).
- **Parallel indexing:** during the overlap period, index new content into *both* systems so they stay equivalent, then flip the switch and keep the old one as emergency backup before turning it off.

## Caveat

Anecdotal — named companies (Wolters Kluwer, MediRegs) and a data-center location (Plano) but no hard metrics (% traffic drop, dollar costs). Stories illustrate principles rather than serving as detailed case studies.
