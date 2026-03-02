---
title: "TabGemma: Text-Based Tabular ICL via LLM using Continued Pretraining and Retrieval"
layout: publication
ref-authors: Schindler, G., and <b>Schambach, M.</b>, and Medek, M., and Thelin, S.
ref-year: 2025
ref-conference: "EurIPS'25 Workshop on AI for Tabular Data"
ref-link: https://arxiv.org/abs/2511.03570
---

We study LLMs for tabular prediction with mixed text, numeric, and categorical fields. We introduce TabGemma, a schema-agnostic in-context learner that treats rows as sequences and tackles two practical hurdles when adapting pretrained LLMs for tabular predictions: unstable numeric tokenization and limited context size. We propose to canonicalize numbers via signed scientific notation and continue pretraining of a 12B Gemma 3 model with a target imputation objective using a large-scale real world dataset. For inference, we use a compact n-gram-based retrieval to select informative exemplars that fit within a 128k-token window. On semantically rich benchmarks, TabGemma establishes a new state of the art on classification across low- and high-data regimes and improves monotonically with more context rows. For regression, it is competitive at small sample sizes but trails conventional approaches as data grows. Our results show that LLMs can be effective tabular in-context learners on highly semantic tasks when paired with dedicated numeric handling and context retrieval, while motivating further advances in numeric modeling and long-context scaling.
