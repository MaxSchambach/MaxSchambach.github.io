---
title: Scaling Experiments in Self-Supervised Cross-Table Representation Learning
layout: publication
ref-authors: <b>Schambach, M.</b>, Paul, D., and Otterbach, J.
ref-year: 2023
ref-conference: NeurIPS Table Representation Learning Workshop
ref-link: https://openreview.net/forum?id=IbiiNw4oRj
---

To analyze the scaling potential of deep tabular representation learning models, we introduce a novel Transformer-based architecture specifically tailored to tabular data and cross-table representation learning by utilizing table-specific tokenizers and a shared Transformer backbone. Our training approach encompasses both single-table and cross-table models, trained via missing value imputation through a self-supervised masked cell recovery objective. To understand the scaling behavior of our method, we train models of varying sizes, ranging from approximately 104 to 107 parameters. These models are trained on a carefully curated pretraining dataset, consisting of 135M training tokens sourced from 76 diverse datasets. We assess the scaling of our architecture in both single-table and cross-table pretraining setups by evaluating the pretrained models using linear probing on a curated set of benchmark datasets and comparing the results with conventional baselines.
