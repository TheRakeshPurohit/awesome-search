---
title: "Approximate Nearest Neighbor Search"
type: concept
aliases:
  - ANN
  - Approximate Nearest Neighbor
  - ANN Search
  - Nearest Neighbor Search
tags:
  - concept
  - vector-search
  - ann
---

# Approximate Nearest Neighbor Search (ANN)

**Approximate Nearest Neighbor (ANN) search** finds vectors close to a query vector
*without* comparing against every vector in the dataset. Exact nearest-neighbor search
is O(n × d) — an exhaustive scan that becomes infeasible at millions or billions of
vectors and real-time query rates. ANN methods trade a small, tunable loss of **recall**
for orders-of-magnitude gains in **speed** and (often) **memory**.

## The Core Trade-off

Every ANN index sits on a curve of **search quality vs. speed**, with **index size /
memory** as a third axis. Exact (Flat) search is 100% recall but slowest; each
approximate index gives up a little recall to prune the search space. The practical
skill is tuning each index's knobs to land where the application needs on that curve.

## Index Families

| Family | Approach | Note |
|--------|----------|------|
| Flat | Exhaustive brute force | Exact baseline, not an approximation |
| [[LSH]] | Hash similar vectors into shared buckets | Best at low dimensionality |
| [[HNSW]] | Multi-layer proximity graph traversal | Dominant for high-recall, low-latency |
| [[IVF]] | Cluster into Voronoi cells, probe nearest | Scales to very large corpora |
| [[Vector Quantization]] | Compress vectors (PQ/SQ/BQ) | Combined with IVF or HNSW |

## Evaluation

ANN quality is measured by **Recall@k** — the fraction of the true top-k neighbors an
approximate search returns — reported alongside query latency and index size. See
[[Vector Search Evaluation]].

## Related Concepts

- [[HNSW]] · [[IVF]] · [[LSH]] — the main ANN index structures
- [[Dense Vector Retrieval]] — the retrieval setting where ANN is applied
- [[Vector Quantization]] · [[Scalar Quantization]] · [[Binary Quantization]] — compression combined with ANN indexes
- [[Vector Similarity Metrics]] — the distance functions ANN indexes optimize over
- [[Vector Filtering]] — applying metadata predicates during ANN search

## Tools

- [[FAISS]] — reference library implementing all major ANN index families

## Articles

- [[Choosing Indexes for Similarity Search (Faiss in Python)]] — video comparing the four index families
- [[Nearest Neighbor Indexes for Similarity Search]] — Pinecone companion write-up
