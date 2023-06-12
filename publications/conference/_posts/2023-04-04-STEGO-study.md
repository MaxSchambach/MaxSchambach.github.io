---
title: Uncovering the Inner Workings of STEGO for Safe Unsupervised Semantic Segmentation
layout: publication

ref-authors: Koenig, A., <b>Schambach, M.</b>, and Otterbach, J.
ref-year: 2023
ref-conference: Conference on Computer Vision and Pattern Recognition Workshop (CVPR Workshop)
ref-link: https://openaccess.thecvf.com/content/CVPR2023W/SAIAD/html/Koenig_Uncovering_the_Inner_Workings_of_STEGO_for_Safe_Unsupervised_Semantic_CVPRW_2023_paper.html
---

Self-supervised pre-training strategies have recently shown impressive results for training general-purpose feature extraction backbones in computer vision. In combination with the Vision Transformer architecture, the DINO self-distillation technique has interesting emerging properties, such as unsupervised clustering in the latent space and semantic correspondences of the produced features without using explicit human-annotated labels. 
The STEGO method for unsupervised semantic segmentation contrastively distills feature correspondences of a DINO-pre-trained Vision Transformer and recently set a new state of the art. However, the detailed workings of STEGO have yet to be disentangled, preventing its usage in safety-critical applications.
    
This paper provides a deeper understanding of the STEGO architecture and training strategy by conducting studies that uncover the working mechanisms behind STEGO, reproduce and extend its experimental validation, and investigate the ability of STEGO to transfer to different datasets. Results demonstrate that the STEGO architecture can be interpreted as a semantics-preserving dimensionality reduction technique.
