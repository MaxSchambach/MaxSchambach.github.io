---
title: A simulation framework for the design and evaluation of computational cameras
layout: publication

ref-authors: Nürnberg, T., <b>Schambach, M.</b>, Uhlig, D., Heizmann, M., and Puente León, F.
ref-year: 2019
ref-conference: Automated Visual Inspection and Machine Vision III (Vol. 11061, p. 1106102)
ref-organizer: International Society for Optics and Photonics (SPIE)
ref-link: https://doi.org/10.1117/12.2527599
ref-code: https://gitlab.com/iiit-public/raytracer
---

In the emerging field of computational imaging, rapid prototyping of new camera concepts becomes increasingly difficult since the signal processing is intertwined with the physical design of a camera. As novel computational cameras capture information other than the traditional two-dimensional information, ground truth data, which can be used to thoroughly benchmark a new system design, is also hard to acquire. We propose to bridge this gap by using simulation. In this article, we present a raytracing framework tailored for the design and evaluation of computational imaging systems. We show that, depending on the application, the image formation on a sensor and phenomena like image noise have to be simulated accurately in order to achieve meaningful results while other aspects, such as photorealistic scene modeling, can be omitted. Therefore, we focus on accurately simulating the mandatory components of computational cameras, namely apertures, lenses, spectral filters and sensors. Besides the simulation of the imaging process, the framework is capable of generating various ground truth data, which can be used to evaluate and optimize the performance of a particular imaging system. Due to its modularity, it is easy to further extend the framework to the needs of other fields of application. We make the source code of our simulation framework publicly available and encourage other researchers to use it to design and evaluate their own camera designs.