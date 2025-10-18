---
title: "ConTextTab: A Semantics-Aware Tabular In-Context Learner"
layout: publication
ref-authors: Spinaci, M.*, Polewczyk, M.*, and <b>Schambach, M.*</b>, and Thelin, S.
ref-year: 2025
ref-conference: "Conference on Neural Information Processing Systems (NeurIPS, Spotlight)"
ref-link: https://arxiv.org/abs/2506.10707
ref-code: https://github.com/SAP-samples/contexttab
---

Tabular in-context learning (ICL) has recently achieved state-of-the-art (SOTA) performance on several tabular prediction tasks. Previously restricted to classification problems on small tables, recent advances such as TabPFN and TabICL have extended its use to larger datasets. Although current table-native ICL architectures are architecturally efficient and well-adapted to tabular data structures, their exclusive training on synthetic data limits their ability to fully leverage the rich semantics and world knowledge contained in real-world tabular data. At the other end of the spectrum, tabular ICL models based on pretrained large language models such as TabuLa-8B integrate deep semantic understanding and world knowledge but are only able to make use of a small amount of context due to inherent architectural limitations. With the aim to combine the best of both these worlds, we introduce ConTextTab, integrating semantic understanding and alignment into a table-native ICL framework. By employing specialized embeddings for different data modalities and by training on large-scale real-world tabular data, our model is competitive with SOTA across a broad set of benchmarks while setting a new standard on the semantically rich CARTE benchmark. Code and model checkpoints are available at: [Link](https://github.com/SAP-samples/contexttab)
