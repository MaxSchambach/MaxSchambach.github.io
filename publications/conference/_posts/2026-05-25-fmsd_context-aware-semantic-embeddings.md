---
title: "Enhancing Tabular Learners with Context-Aware Semantic Embeddings"
layout: publication
ref-authors: Schindler, G., and <b>Schambach, M.</b>, and Höhne, J.
ref-year: 2026
ref-conference: "2nd ICML Workshop on Foundation Models for Structured Data"
ref-link: https://openreview.net/forum?id=QArxQg4U71
---

While modern tabular learners excel at capturing statistical patterns, they frequently operate in a semantic vacuum, treating categorical values as discrete symbols and ignoring the rich world knowledge inherent in feature names and cell entries. We propose Context-Aware Semantic Embeddings (CASE), a novel framework that bridges the gap between the semantic understanding of Large Language Models (LLMs) and the statistical capabilities of tabular learners. Unlike existing methods that embed rows in isolation, CASE utilizes a contextualization strategy: we pre-fill a tabular LLM’s KV cache with a representative sample of rows to establish a persistent anchor of the dataset’s semantic distribution. This ensures that generated row embeddings are dynamically contextualized, resolving semantic ambiguities and anchoring representations in domain-specific context. Our experiments across several benchmarks (CARTE, TextTab, and TabArena) demonstrate that CASE significantly improve performance -- particularly in low-data regimes and on semantically rich datasets -- setting a new state of the art when combined with tabular in-context learners.