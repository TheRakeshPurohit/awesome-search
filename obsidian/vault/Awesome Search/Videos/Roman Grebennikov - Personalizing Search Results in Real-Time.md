---
type: video
title: "Personalizing search results in real-time (MICES 2019)"
speaker: "[[Roman Grebennikov]]"
company: "Findify"
medium: talk / video
url: https://www.youtube.com/watch?v=AYdOpfY8jQU
slides: https://mices.co/mices2019/slides/grebennikov_search-real-time.pdf
published: 2019-07-18
topics:
  - "[[E-commerce Search]]"
  - "[[Personalization in Search]]"
concepts:
  - "[[Learning to Rank]]"
  - "[[LambdaMART]]"
  - "[[Position Bias]]"
  - "[[Exploration vs Exploitation]]"
  - "[[NDCG]]"
  - "[[Click Models]]"
  - "[[Implicit Judgments]]"
  - "[[Reranking]]"
tools:
  - "[[Elasticsearch]]"
people:
  - "[[Roman Grebennikov]]"
created: 2026-07-12
---

# Personalizing Search Results in Real-Time (MICES 2019)

📺 **Watch:** https://www.youtube.com/watch?v=AYdOpfY8jQU · 📄 [Slides](https://mices.co/mices2019/slides/grebennikov_search-real-time.pdf)

Talk by [[Roman Grebennikov]] (Findify) at [[MICES]] 2019. War stories from rolling out [[Learning to Rank]] across ~1,500 white-label e-commerce stores: how naive click-through training makes models degrade via [[Position Bias]], how a shuffled exploration segment fixes it, and why the "perfect ranking" behind [[NDCG]] is a business decision, not a given.

## Key Moments

| Time | Moment |
|---|---|
| [00:00](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=0s) | Intro — Findify: white-label search, ~1,500 stores, ~20M products, Shopify origins |
| [01:51](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=111s) | Eyeballing the data: most clicks land in the top-5 results |
| [02:48](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=168s) | Typical SMB customer session — the ~10-second personalization window |
| [04:20](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=260s) | First fix: popularity script-scoring in Elasticsearch ("linear regression") |
| [05:50](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=350s) | Learning to Rank & why LambdaMART |
| [06:57](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=417s) | Two-phase ranking: ES top-500 → reranking microservice |
| [08:07](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=487s) | The ~60–70 features: search, product, variant, session, scoped counters |
| [09:09](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=549s) | The mystery: metrics improve, then slowly degrade (+8% → +6%) |
| [10:26](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=626s) | Cause: feedback loop from training on own clicks — position bias |
| [11:01](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=661s) | Proof: random-ranking segment shows identical click histogram |
| [11:51](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=711s) | Fix: exploration/exploitation traffic split |
| [12:28](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=748s) | The ~1% shuffled-first-page exploration segment |
| [13:21](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=801s) | Low-traffic problem: the €5,000-sofa merchant |
| [14:10](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=850s) | Suggestions hackathon; [15:07](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=907s) big-merchant model transfers to small merchant |
| [15:37](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=937s) | One generic cross-merchant model; [16:12](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=972s) feature scaling ($100 socks vs sofa) |
| [16:46](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=1006s) | NDCG and what "perfect ranking" means; [17:36](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=1056s) cascade click model |
| [17:59](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=1079s) | 🌟 The Stanley bong story — clicks ≠ purchases |
| [18:52](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=1132s) | Weighting purchases over clicks; [19:20](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=1160s) optimizing for margin |
| [19:53](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=1193s) | Offline NDCG ladder: random ≈ 0.54 → unbiased data best |
| [20:57](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=1257s) | Online A/B results vs ES baseline; unbiased LambdaMART on top |
| [22:02](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=1322s) | Dog-food merchant: when ranking doesn't matter at all |
| [22:44](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=1364s) | Conclusion: NDCG↔conversion is correlation, not causation |
| [24:28](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=1468s) | Q&A: eye-tracking — above-the-fold positions get equal attention |
| [26:16](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=1576s) | Q&A: GDPR/privacy of cross-merchant models |
| [27:31](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=1651s) | Q&A: the 1% random segment — free-plan merchants "pay with data" |
| [29:01](https://www.youtube.com/watch?v=AYdOpfY8jQU&t=1741s) | Q&A: downsampling high-traffic merchants (merchant bias) |

## Context: Findify

Findify is a white-label search provider for ~1,500 stores and ~20M products, originally a Shopify add-on focused on better search UI on top of [[Elasticsearch]] — so ranking was initially roughly the same as Shopify's own. Eyeballing the data showed most clicks land in the top five results, and SMB shoppers do one or two searches before leaving for good. Unlike music recommendations, there is no "retrain overnight and be better tomorrow": the behavioral signal (platform, clicked products → gender/size/color interests) arrives seconds before the search it should influence, so personalization must be real-time.

## Step 1: popularity scoring, then LTR

First iteration was script scoring in [[Elasticsearch]]: blend text relevance with product popularity built from purchases, pageviews, and popularity within the current query. Versus the plain BM25 baseline it gave a solid conversion/AOV lift — but it is essentially a linear regression. The research field to draw from is [[Learning to Rank]]; [[LambdaMART]] stands out for having many ready open-source implementations. Rather than fight LTR integration inside Elasticsearch (as of 2016-era tooling), Findify chose **two-phase ranking**: Elasticsearch returns a top-500 candidate set, and a separate [[Reranking]] microservice — which consumes the live customer event stream — reorders it. The model used ~60–70 features in groups: search-scoped (term count, filters enabled, query popularity), product (price, pageviews over multiple time windows), variant, customer session, and scoped counters (e.g. pageviews within the current category or query).

## The degradation mystery: position bias

A/B tests were positive, but business metrics improved and then **slowly degraded** across merchants (ending around +6% vs a peak of +8%) with no obvious cause. The culprit: training on raw click-through data the system itself generated — the model eats its own output in a feedback loop, driven by [[Position Bias]] (with [[Presentation Bias]] and model bias as siblings). To prove it, they ran a small random-ranking segment: the click histogram by position looked the same as with real ranking — users click the top results because Google trained them to trust position — even though business metrics drop, since people can't find what they want.

## Fix: exploration / exploitation split

The remedy is an [[Exploration vs Exploitation]] traffic split: ~1% or less of traffic (smaller for higher-paying merchants) becomes an exploration segment where the **first page is shuffled** — results are still relevant, just randomly ordered. Averaged over many impressions of the same query, position cancels out and the true drivers of clicks emerge. Only this segment feeds training, which stopped the model degradation. In the Q&A: most merchants on the free plan get the 1% randomization and effectively "pay with their data", which powers the enterprise tier.

## One generic model across merchants

Per-merchant training fails for small merchants — a luxury sofa store (€5,000 sofas, double-digit conversion, tens of visitors a day) would need years of click-throughs, and randomizing a sliver of tiny traffic makes it hopeless. A suggestions hackathon revealed the way out: a suggestion-ranking model trained on one large merchant *improved* results when applied to an unrelated small merchant, because its features (query popularity, term counts) are merchant-agnostic. That led to one generic cross-merchant search-ranking model: more training samples, no cold-start wait per merchant. The catch is feature scaling — raw price is meaningless across catalogs ($100 is expensive for socks, cheap for a sofa), so features must be normalized to comparable scales. They also downsample high-traffic merchants (a few contribute ~10% of all platform traffic) to avoid merchant bias — the same debiasing idea one level up.

## What "perfect ranking" optimizes: the Stanley bong story

[[NDCG]] compares observed interactions against a constructed *perfect* ranking; under a cascade [[Click Models|click model]], a click on result C says C beats A and B, and nothing about unexamined D. After enabling personalization, a merchant selling smoking accessories complained that a giant expensive bong jumped from the bottom to the top of a high-traffic collection — everyone clicked it out of curiosity ("how can it be so huge?") but nobody bought it. Optimizing pure clicks rewards curiosity. Weighting purchases far above clicks in the perfect ranking sent the bong back down — and the same lever lets you optimize for margin (profit) instead of clicks or purchases. The perfect ranking is a business-goal encoding.

## Results

Offline NDCG over 1,000+ merchants' randomized data: random ≈ 0.54, popularity sort improves it, text relevancy more, popularity+relevancy mix more, their LTR model more, and unbiased (exploration-trained) data the most. Online, against the Elasticsearch baseline: full randomization trashes everything ("plenty of opportunity to trash your search and get fired"); the regression approach raises conversion while CTR oddly drops; [[LambdaMART]] beats baseline; unbiased LambdaMART beats that (A/B still running at talk time). Caveats: results are averages over very diverse merchants ("average temperature over the whole hospital"); one dog-food merchant saw zero relevancy gains from any algorithm because customers use search as a shortcut to a known product — precise queries with one or two results leave nothing to rank, unlike discovery-driven apparel search. And the NDCG↔conversion relationship is correlation, not causation.

## Q&A highlights

- **Click-by-position curve** (audience, eye-tracking data): in gallery layouts, everything above the fold gets roughly equal attention; attention drops once scrolling is needed. Mobile is worse — often only one product is above the fold.
- **Privacy/GDPR of cross-merchant models**: merchants consent by contract; no IPs or emails stored, only anonymous IDs; no cross-merchant user tracking. Sharing statistical knowledge is framed as win-win — opt out and you wait a year to collect your own click-throughs.
- **Sample imbalance**: currently simple downsampling of top-traffic merchants; sampling by click position or via a bias model would be finer-grained.

## Related

- [[Position Bias]] · [[Presentation Bias]] — the biases that degraded the model
- [[Exploration vs Exploitation]] — the traffic-split fix
- [[Learning to Rank]] · [[LambdaMART]] · [[LTR Feature Engineering]] · [[Reranking]]
- [[NDCG]] · [[Click Models]] · [[Implicit Judgments]] · [[Click Signals]]
- [[A-B Testing for Search]] — how every step was validated
- [[Rene Kriegler - Query Relaxation]] — another MICES talk in this vault
- [[Metarank]] — Grebennikov's later open-source reranker, same two-phase idea
