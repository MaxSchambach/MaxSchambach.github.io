---
title: "Enhancing Tabular Learners with Context-Aware Semantic Embeddings"
layout: publication
ref-authors: Schindler, G., and <b>Schambach, M.</b>, and Höhne, J.
ref-year: 2026
ref-conference: "Conference on Neural Information Processing Systems (NeurIPS)"
ref-link: https://openreview.net/forum?id=pV2wVDrTqK
---

While modern tabular learners excel at capturing statistical patterns, they frequently operate in a semantic vacuum, treating textual features as discrete symbols, ignoringing the rich semantics inherent in feature names or cell entries. We propose CASE (Context-Aware Semantic Embeddings), a novel framework that bridges the gap between the semantic understanding of Large Language Models (LLMs) and the statistical capabilities of tabular learners. Unlike existing methods that embed rows in isolation, CASE utilizes a contextualization strategy: we pre-fill the KV cache of a custom-trained Gemma~3-based Tabular Language Model with a representative sample of rows to establish a persistent anchor of the dataset’s semantics. This ensures that generated row embeddings are dynamically contextualized, resolving semantic ambiguities and anchoring representations in domain-specific context. Our experiments across several benchmarks (CARTE, TextTab, and TabArena) demonstrate that CASE significantly improve performance of tabular learners - particularly in low-data regimes and on semantically rich datasets - setting a new state of the art when combined with recent tabular in-context learners. Inference code and model checkpoints will be made publicly available.