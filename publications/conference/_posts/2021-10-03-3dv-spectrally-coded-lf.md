---
title: Spectral Reconstruction and Disparity from Spatio-Spectrally Coded Light Fields via Multi-Task Deep Learning
layout: publication

ref-authors: <b>Schambach, M.</b>, Shi, J., and Heizmann, M.
ref-year: 2021
ref-conference: International Conference on 3D Vision (3DV)
ref-link: https://ieeexplore.ieee.org/document/9665944
ref-data: https://dx.doi.org/10.35097/500
---

We present a novel method to reconstruct a spectral central view and its aligned disparity map from spatio-spectrally coded light fields. Since we do not reconstruct an intermediate full light field from the coded measurement, we refer to this as principal reconstruction. We show that the direct estimation is superior to a full light field reconstruction and subsequent disparity estimation. The coded light fields correspond to those captured by a light field camera in the unfocused design with a spectrally coded microlens array. In this application, the spectrally coded light field camera can be interpreted as a single-shot spectral depth camera.
We investigate several multi-task deep learning methods and propose a new auxiliary loss-based training strategy to enhance the reconstruction performance. The results are evaluated using a synthetic as well as a new real-world spectral light field dataset that we captured using a custom-built camera. The results are compared to state-of-the art compressed sensing reconstruction and disparity estimation.
We achieve a high reconstruction quality for both synthetic and real-world coded light fields. The disparity estimation quality is on par with or even outperforms state-of-the-art disparity estimation from uncoded RGB light fields.
