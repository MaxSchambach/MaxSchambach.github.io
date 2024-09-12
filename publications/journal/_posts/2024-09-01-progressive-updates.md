---
title: Progressive Updates of Convolutional Neural Networks for Enhanced Reliability in Small Satellite Applications
layout: publication
ref-authors: Kondrateva, O., Dietzel, S., <b>Schambach, M.</b>, Otterbach, S., and Scheuermann, B.
ref-year: 2024
ref-journal: Computer Communications
ref-link: https://www.sciencedirect.com/science/article/pii/S0140366424002500
---

Small satellites enable many important applications for both economic and scientific purposes. Many of these applications are inherently data-centric and rely on large amounts of high-resolution satellite imagery to be delivered in a timely manner. However, communicating this data to Earth is challenging due to intermittent connectivity, high packet losses, low data rates, and similar issues. Therefore, efficient onboard prioritization and data processing are essential for future satellite missions. Machine learning methods, such as deep neural networks, are very suitable for such prioritization, as they are already used extensively for satellite imagery processing and they can be deployed onboard of satellites. However, updating them to support new classification requirements when the satellite is already in orbit is difficult, as often multiple passes are required to complete model transmission due to the communication challenges. To cope with this issue, we propose a progressive transmission mechanism for model updates, which leverages vector quantization and arithmetic coding. Our mechanism allows to achieve high accuracies even with partially updated models. Evaluation results show that our mechanism significantly outperforms other less optimized transmission schemes.