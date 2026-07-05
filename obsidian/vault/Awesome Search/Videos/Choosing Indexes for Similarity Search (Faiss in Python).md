---
title: "Choosing Indexes for Similarity Search (Faiss in Python)"
type: video
source: "https://www.youtube.com/watch?v=B7wmo_NImgM"
author: ["James Briggs"]
published: 2021-08-09
duration: "31:33"
tags:
  - video
  - vector-search
  - ann
  - faiss
  - infrastructure
concepts:
  - Approximate Nearest Neighbor Search
  - Dense Vector Retrieval
  - HNSW
  - IVF
  - LSH
  - Vector Similarity Metrics
topics:
  - Search Platforms
people:
  - James Briggs
created: 2026-07-05
---

# Choosing Indexes for Similarity Search (Faiss in Python)

A hands-on video walkthrough by [[James Briggs]] of the four main index families in
[[FAISS]] — **Flat, [[LSH]], [[HNSW]], and [[IVF]]** — and how to pick one based on
your data. It is the video companion to his Pinecone write-up
[[Nearest Neighbor Indexes for Similarity Search]]. All benchmarks run on the
**Sift1M** dataset (1M vectors, 128 dimensions), using the exact Flat result as the
100%-recall baseline against which each approximate index is scored.

---

## Core Framing

Every [[Approximate Nearest Neighbor Search|ANN]] index is a trade of **search quality
vs. speed** (and, separately, **index size / memory**). Flat search is pure quality
(exhaustive), and every other index gives up a little recall to go much faster. The
practical skill is tuning each index's knobs to sit where you want on that curve.

## The Four Indexes

### Flat (exact / brute force)
- `faiss.IndexFlatL2(d)` or `faiss.IndexFlatIP(d)` — L2 distance or inner product.
- Compares the query against **every** vector → 100% recall, O(n) cost.
- No training, no parameters. Used here as the **ground-truth baseline**.
- **Baseline latency: ~157 ms** (single query, Sift1M).
- Use only for small datasets or when exactness is mandatory.

### LSH — Locality Sensitive Hashing
- `faiss.IndexLSH(d, nbits)`.
- Deliberately **maximizes hash collisions** so similar vectors land in the same
  bucket; at query time the vector is hashed and search is restricted to nearby
  buckets (Hamming distance) — the opposite goal of a normal hash table.
- `nbits` is the key knob and must **scale with dimensionality** (video uses `d*4`).
  Higher `nbits` → better recall but larger index and slower search.
- **Curse of dimensionality**: great at low `d`, degrades fast at high `d` (e.g. 512).
- **Result: ~17.6 ms (~10× faster than Flat)** with good recall at `nbits = d*4`.

### HNSW — Hierarchical Navigable Small World
- `faiss.IndexHNSWFlat(d, M)`.
- Builds a multi-layer proximity **graph**; search hops between layers to reach the
  nearest neighbor in very few steps (the "small world" property — cf. Facebook's
  ~3.6-hop average between any two users).
- Knobs:
  - `M` — connections per node/vertex (video uses 16). Higher `M` → better recall, bigger index.
  - `efSearch` — how much of the graph to explore **at query time**. Higher → more accurate, slower.
  - `efConstruction` — exploration **at build time**. Raises build time but **not** query time, so it's cheap to set high.
- **Results**: build ~43.6 s (high `efConstruction`); search ~3.7 ms but *poor recall*
  at default `efSearch`; raising `efSearch` to 32 gave **strong recall** at higher latency.
- Among the **best-performing indexes** and the basis of much current SOTA — but
  **index size is very large** (memory is the main cost).

### IVF — Inverted File Index
- `quantizer = faiss.IndexFlatIP(d)` → `faiss.IndexIVFFlat(quantizer, d, nlist)`.
- **Clusters** vectors into `nlist` Voronoi cells around centroids. At query time the
  vector is compared only to the **centroids**, then searched within the closest
  cell(s) — not the whole dataset.
- Requires **`index.train(vectors)`** before adding (clustering step); `is_trained`
  is `False` until then, unlike the other indexes.
- Knobs:
  - `nlist` — number of cells/centroids. Barely affects index size (grows ~100 KB per doubling).
  - `nprobe` — how many nearest cells to search. `nprobe=1` risks the **edge problem** (a true neighbor just across a cell boundary is missed); raising `nprobe` fixes it at the cost of speed.
- **Results**: `nprobe=1` → ~3.3 ms but only ~50% recall; raising `nprobe` → near-perfect
  recall but slower; `nprobe=2` was the **fast + accurate** sweet spot.
- Very popular and strong; commonly paired with Product Quantization (IVF-PQ) at scale.

## Benchmark Summary (Sift1M, single query)

| Index | Latency | Recall vs. Flat | Main cost / caveat |
|-------|---------|-----------------|--------------------|
| Flat  | ~157 ms | 100% (baseline) | Exhaustive; doesn't scale |
| LSH   | ~17.6 ms | Good at `nbits=d*4` | Curse of dimensionality at high `d` |
| HNSW  | ~3.7 ms | Poor default → strong at `efSearch=32` | Huge index size; slow build |
| IVF   | ~3.3 ms | ~50% at `nprobe=1` → near-perfect at `nprobe≥2` | Needs training; edge problem |

## Takeaways

- **There is no single best index** — choose by dataset size, latency budget, memory,
  and required recall, then tune the knobs.
- **Free lunch knob**: HNSW's `efConstruction` buys recall without query-time cost.
- **HNSW and IVF** are the go-to production choices here; **LSH** shines only at low
  dimensionality; **Flat** is a baseline, not a deployment target.
- The video is intentionally high-level; deeper per-index treatment is promised in
  follow-ups (mirrored by the Pinecone FAISS series).

## Related Articles

- [[Nearest Neighbor Indexes for Similarity Search]] — the Pinecone article this video accompanies (same author, same indexes)

## Related Concepts

- [[Approximate Nearest Neighbor Search]] — the problem all four indexes solve
- [[Dense Vector Retrieval]] — where these indexes are used
- [[HNSW]] · [[IVF]] · [[LSH]] — the approximate indexes covered
- [[Vector Similarity Metrics]] — L2 vs. inner product distance choice
- [[Vector Quantization]] — IVF-PQ extension for scale

## Tools

- [[FAISS]] — the library used throughout

## People

- [[James Briggs]] — author / presenter (Pinecone)
