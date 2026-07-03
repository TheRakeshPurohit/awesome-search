---
title: "NDCG Variants — The Flavors of NDCG"
type: topic
aliases: ["NDCG Flavors", "Flavours of NDCG", "NDCG formulations", "DCG variants", "flavors of NDCG (topic)"]
tags:
  - topic
  - search-evaluation
  - metrics
  - ndcg
related_concepts:
  - NDCG
  - Search Evaluation
  - Judgment Lists
  - UDCG
  - MRR
  - MAP
related_topics:
  - Search Quality Assurance
  - Relevance Program Setup
  - Relevance Evaluation Tools Compared
articles:
  - Flavors of NDCG
  - Flavors of NDCG - normalized to what
  - Demystifying nDCG and ERR
created: 2026-07-03
---

# NDCG Variants — The Flavors of NDCG

[[NDCG]] is reported as a single number in the [0, 1] range, which hides a trap: **there is no one NDCG**. The same ranking against the same [[Judgment Lists|judgment list]] can yield materially different scores depending on which "flavor" you compute. [[Doug Turnbull]]'s writing popularized the framing, and the ambiguity lives along **two independent axes** — how relevance grades become *gain*, and what the *ideal* is normalized against — plus a handful of smaller reporting choices. Getting these wrong turns cross-system comparison into apples-to-oranges.

> The one rule that survives all of this: **always state the flavor when you report an NDCG number**, especially when comparing against a published benchmark.

---

## Axis 1 — Gain Function (how a grade becomes gain)

How is a relevance grade `rel_i` turned into the value a document contributes?

### Järvelin & Kekäläinen (2002) — "grade gain" (linear)
```
DCG@k = rel₁ + Σᵢ₌₂ᵏ rel_i / log₂(i)
```
Gain is the grade itself. Position 1 takes full credit with **no discount**; positions 2+ are discounted by `log₂(i)`.

### Burges et al. (2005) — "exponential gain" (default in most ML frameworks)
```
DCG@k = Σᵢ₌₁ᵏ (2^rel_i − 1) / log₂(i + 1)
```
The `2^rel − 1` transform **amplifies highly relevant documents**: grade 3 → `2³−1 = 7`, grade 1 → `2¹−1 = 1`, so a highly relevant doc counts ~7× a marginal one. Every position, including the first, is discounted by `log₂(i+1)`.

Note this axis bundles **two** differences at once: the gain transform (linear vs. exponential) *and* the discount convention (`log₂(i)` with a free top slot vs. `log₂(i+1)` discounting all positions). For **binary relevance (0/1) the two gain transforms are equivalent** (`2¹−1 = 1`); they diverge only with graded judgments.

## Axis 2 — Normalization Target ("normalized to what?")

NDCG = DCG / **IDCG**, and the IDCG (the "ideal") is itself a choice. The `- normalized to what!?` piece enumerates four:

| Flavor | Ideal is computed from… | Answers | Risk |
|---|---|---|---|
| **NDCG-local** | only the **top-N retrieved**, sorted optimally | "Given what we returned, did we order it well?" — pure **ranking quality** | Blind to relevant docs that were never retrieved |
| **NDCG-recall** | a larger **recall set** (top K) before ideal ordering | Hybrid ranking + coverage | Middle ground, less crisp interpretation |
| **NDCG-global** | **all labels for the query**, retrieved or not | Overall performance — blends **recall and ranking** | Conflates "ranked better" with "retrieved more" |
| **NDCG-max** | maximum possible labels in every position | Catalog / coverage ceiling | Very sensitive to label quality |

A subtle consequence of the global/max end: **unjudged documents are scored as grade 0**. A system that retrieves genuinely good documents outside your judged pool gets penalized — so NDCG is biased against systems that retrieve *differently* from whatever seeded the judgment pool. This is why sampling strategy for judgments ([[Search Evaluation]]) matters as much as the metric.

## Smaller Reporting Choices

- **Cutoff `@k`** — `@3` (instant answers/autocomplete), `@5` (above the fold), `@10` (the de-facto benchmark standard: MS MARCO, BEIR), `@100` (first-stage recall quality). Different `k` answers different questions.
- **Missing-value handling** — how absent/unjudged results are treated (grade 0 vs. excluded).
- **Log base** — conventionally `log₂`, but the base is a free parameter; it cancels in normalization but must be consistent.

## Same Input, Different Numbers

The point of the whole framing: hold the ranking and judgments fixed, and the flavor alone moves the score.

| | Example NDCG@10 |
|---|---|
| Järvelin (grade gain) | 0.72 |
| Burges (exponential gain) | 0.68 |

A "4-point improvement" that is really just two systems measured on two flavors is **noise dressed as signal**.

## Which Flavor Do Common Tools Use?

| Library / benchmark | Flavor |
|---|---|
| scikit-learn `ndcg_score` | Burges (exponential) |
| RankLib | Järvelin (grade gain) |
| [[LightGBM]] LambdaRank | Burges |
| MS MARCO / BEIR leaderboards | Burges |
| [[Quepid]] | Configurable (variant is a setting) |

Because [[Quepid]] lets you pick the variant, it is one of the few tools where you can *make* your offline number match a published benchmark's flavor — which matters precisely because of everything above (see [[Relevance Evaluation Tools Compared]]).

## Practical Guidance

1. **Pick one flavor and hold it fixed** across an entire project — both axes plus `@k`.
2. **Be explicit when comparing to published numbers**; match their gain function and normalization or the comparison is meaningless.
3. **E-commerce with 0–4 grades → Burges (exponential)**: you *want* highly relevant items amplified.
4. **Binary relevance → the gain axis doesn't matter** (variants coincide); only normalization and `@k` remain.
5. Choose the **normalization axis to match the question you're actually asking** — ranking quality (local) vs. overall performance (global) — or you'll optimize the wrong thing.

## Related Concepts

- [[NDCG]] — the metric these are all variants of; see its "Variants" section for the formulas in context
- [[Search Evaluation]] — the practice; judgment sampling drives the unjudged-doc bias above
- [[Judgment Lists]] — the graded input; its coverage bounds every IDCG choice
- [[UDCG]] — a further NDCG extension adding *negative* utility for distractor docs in agentic RAG
- [[MRR]] · [[MAP]] · [[Precision and Recall]] — less flavor-ambiguous companion metrics

## Related Topics

- [[Relevance Evaluation Tools Compared]] — which tools expose the flavor as a setting
- [[Search Quality Assurance]] — the broader QA practice this ambiguity threatens
- [[Relevance Program Setup]] — where flavor consistency becomes an org-wide convention

## Related Articles

- [[Flavors of NDCG]] — the gain-function axis (Järvelin vs. Burges)
- [[Flavors of NDCG - normalized to what]] — the normalization axis (local / recall / global / max)
- [[Demystifying nDCG and ERR]] — NDCG formulations alongside ERR
- [[Choosing Your Search Relevance Evaluation Metric]] — where NDCG fits among metrics

## People

- [[Doug Turnbull]] — popularized the "flavors of NDCG" framing; practical NDCG guidance
- [[Daniel Tunkelang]] — frequent NDCG commentary; Evaluating Search series
