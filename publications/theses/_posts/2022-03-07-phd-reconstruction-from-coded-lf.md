---
title: Reconstruction from Spatio-Spectrally Coded Multispectral Light Fields
layout: publication

ref-authors: <b>Schambach, M.</b>
ref-year: 2022
ref-thesis: PhD Thesis, Institute of Industrial Information Technology, Karlsruhe Institute of Technology
ref-link: https://doi.org/10.5445/IR/1000143731
ref-code: https://maxschambach.github.io/thesis/
---

In this thesis, spatio-spectrally coded multispectral light fields, as taken by a light field camera with a spectrally coded microlens array, are investigated. For the reconstruction of the coded light fields, two methods are developed and evaluated in detail.

First, a full reconstruction of the spectral light field, based on the principles of compressed sensing, is developed. To sparsely represent spectral light fields, fixed 5D-DCT bases are investigated as well as a dictionary learning approach. The conventional vectorized dictionary learning approach is generalized to a tensorial notation to tensorially factorize the light field dictionary.

Due to the reduced number of trainable parameters, this approach allows for larger effective atom sizes.

Second, a deep learning-based reconstruction of the spectral central view and its aligned disparity map from the coded light field is developed. Here, the desired information is estimated from the coded measurements directly. Several strategies of the corresponding multi-task training are compared. To further improve the quality of the reconstruction, a novel method to incorporate auxiliary losses, based on their respective normalized gradient similarity, is developed and shown to outperform previous adaptive methods.

To train and evaluate the different reconstruction approaches, two datasets are created. First, a large synthetic spectral light field dataset with available disparity ground truth is created using a custom ray tracer. This dataset, containing roughly 100k spectral light field and disparity patches, is split into a training, validation, and test dataset. To further evaluate the performance, seven hand-crafted scenes, so-called dataset challenges, are created. Finally, a real-world spectral light field dataset is captured using a custom-built spectral light field camera. The radiometric and geometric calibration of the camera are discussed in detail.

Using the novel datasets, the proposed reconstruction approaches are evaluated in detail. Different coding masks are investigated---random, regular, as well as end-to-end optimized coding masks generated using a novel differentiable fractal generation. Several ablation studies are considered, for example investigating the dependence on noise, angular resolution, or depth. Overall, the results are convincing and show a high reconstruction quality. The deep learning-based reconstruction, in particular when trained with adaptive multi-task and auxiliary loss strategies, outperforms the compressed sensing-based reconstruction and subsequent state-of-the-art disparity estimation.