---
title: "CDMD: A Cross-Dataset Mixed-Type Diffusion Model for Tabular Data"
layout: publication
ref-authors: Ketata, M. A., <b>Schambach, M.</b>, and Günnemann, Stephan
ref-year: 2026
ref-conference: "BeNTo: Beyond Next‑Token Prediction, NeurIPS Workshop"
ref-link: https://openreview.net/forum?id=cYr7WLAF7U
---

Generative models for tabular data are typically trained separately for each dataset, preventing knowledge transfer across datasets and requiring the training and storage of many specialized models. In this paper, we introduce CDMD, a diffusion model that can be trained jointly across heterogeneous tabular datasets with different schemas and variable numbers of mixed numerical and categorical features. Unlike existing cross-dataset approaches based on generative modeling in a shared latent space, CDMD defines diffusion directly over the mixed-type feature space and is trained end-to-end. We construct a schema-dependent row-level diffusion process by composing feature-level processes and propose a schema-restricted reverse process parameterization for masked discrete diffusion, in which the categorical output space dynamically adapts to each feature's vocabulary. A schema-aware transformer denoiser then learns to reverse the row-level variable-sized process. Across seven real-world datasets, a single jointly trained CDMD achieves the best average synthetic-data quality among strong single-dataset and cross-dataset baselines while requiring substantially fewer total parameters than separately trained models. Furthermore, after pretraining on a corpus of 337 datasets, CDMD substantially improves generation in low-data settings on previously unseen datasets.