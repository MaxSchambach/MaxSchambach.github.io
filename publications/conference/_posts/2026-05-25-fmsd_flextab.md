---
title: "FlexTab: Towards a Flexible Encoder-Decoder Architecture for Tabular In-Context Learning"
layout: publication
ref-authors: Polewczyk, M., and <b>Schambach, M.</b>, and Spinaci, M., and Thelin, S., and Höhne, J.
ref-year: 2026
ref-conference: "2nd ICML Workshop on Foundation Models for Structured Data"
ref-link: https://openreview.net/forum?id=fOph6xxdyP
---

We introduce FlexTab, a flexible encoder-decoder architecture for in-context learning on tabular data that combines a single, task-agnostic encoder with a suite of task-specific decoders. Unlike existing tabular in-context learners, which entangle feature representations with a specific prediction target, our design produces target-agnostic row embeddings that can be leveraged across a range of downstream tasks. We demonstrate this flexibility on three distinct tasks: classification, regression, and entity matching. We note that our architecture can be extended to problems such as outlier detection, clustering, and entity classification in relational databases, among others. Both the encoder and the task-specific decoders are trained on a large corpus of real-world, unlabeled tables. FlexTab achieves state-of-the-art or competitive performance across the examined tasks. Our results demonstrate that a single shared encoder, paired with task-specific decoders, can serve as an effective general-purpose backbone for diverse tabular prediction problems.