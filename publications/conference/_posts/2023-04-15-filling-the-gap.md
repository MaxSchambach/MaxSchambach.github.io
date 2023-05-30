---
title: "Filling the Gap: Fault-Tolerant Updates of On-Satellite Neural Networks Using Vector Quantization"
layout: publication

ref-authors: Kondrateva, O., Dietzel, S., <b>Schambach, M.</b>, Otterbach, J., and Scheuermann, B. 
ref-year: 2023
ref-conference: IFIP Networking
---

The use of small, low-Earth-orbit satellites enables many novel Earth observation use cases due to their cost efficiency.
To cope with the challenging communication environment, machine learning algorithms, such as artificial neural networks, canbe applied onboard the satellites. 
They help to prioritize or preprocess sensor measurements and to reduce the amount of data transmitted to Earth. 
However, transferring and updating machine learning models to suit changing prioritization requirements poses a number of challenges in itself due to short contact times of satellites with ground stations and lossy communication links. 
We propose a new transmission mechanism for model updates that retains high performance even when these updates have been only partially transmitted. 
We achieve this by approximating missing model weights using a vector quantization approach. 
Using a support structure of quantized vector indices, we can approximate the model with a small amount of data, which is transmitted first, while retaining a high performance. 
The model performance can then be incrementally improved, as more exact model weights are transmitted to the satellites. 
Our evaluation shows that this approach significantly outperforms existing baselines.
