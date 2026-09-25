---
title: "FlexTab: A Flexible Encoder-Decoder Architecture for In-Context Learning Across Diverse Tabular Tasks"
layout: publication
ref-authors: Polewczyk, M.*, and <b>Schambach, M.*</b>, and Spinaci, M.*, and Thelin, S., and Höhne, J.
ref-year: 2026
ref-conference: "Conference on Neural Information Processing Systems (NeurIPS)"
ref-link: https://openreview.net/forum?id=LnVFK5y1uh
ref-code: https://github.com/SAP-samples/flextab
---

We introduce FlexTab, a flexible encoder-decoder architecture for in-context learning on tabular data that pairs a single, task-agnostic encoder with a suite of task-specific decoders. Unlike existing tabular in-context learners, which entangle feature representations with a specific prediction target, our design produces target-agnostic row embeddings that can be leveraged across a wide range of downstream tasks within a table-native in-context learning setup. We demonstrate this flexibility on six distinct problems: classification, regression, anomaly detection, clustering, entity matching, and entity classification in relational databases. Both the encoder and the task-specific decoders are trained on a large corpus of real-world, unlabeled tables. FlexTab achieves state-of-the-art performance on classification, regression, anomaly detection and entity matching, while remaining competitive with specialized models on entity classification in a relational setting. These results demonstrate that a single shared encoder, paired with task-specific decoders, can serve as an effective general-purpose backbone for diverse tabular prediction problems. The inference code and checkpoints will be made publicly available.