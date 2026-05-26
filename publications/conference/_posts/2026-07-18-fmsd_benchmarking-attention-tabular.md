---
title: "Benchmarking Attention for Tabular Foundation Models"
layout: publication
ref-authors: <b>Schambach, M.</b>, and Biehl, C., and Thelin, S.
ref-year: 2026
ref-conference: "2nd ICML Workshop on Foundation Models for Structured Data"
ref-link: https://openreview.net/forum?id=rwtcugrpDq
---

Tabular in-context learners such as TabPFN rely on alternating row and column attention over 2D sequences of latent embeddings. These attention patterns differ markedly from the one-dimensional case in language models: row attention involves longer sequences while column attention operates on much shorter ones. Furthermore, the strided memory layout of the data makes producing contiguous tensors costly. Yet efficient attention has been studied mostly for one-dimensional sequences, leaving the two-dimensional tabular setting unexplored.

To this end, we study the unique characteristics of tabular attention and benchmark different backends -- Torch SDPA (efficient and cuDNN) and FlashAttention-2, 3, and 4 -- measuring throughput across realistic tabular shapes on an H100 GPU.

We find that the optimal choice differs between column and row attention: cuDNN-based SDPA dominates column attention at short-to-medium sequence lengths, while FlashAttention-3 dominates row attention by supporting a more compact stride layout directly, avoiding costly tensor copies.

