---
title: Improving light efficiency in multispectral imaging via complementary notch filters
layout: publication

ref-authors: Panther,T.*, <b>Schambach, M.</b>*, and Heizmann, M.
ref-year: 2021
ref-conference: Automated Visual Inspection and Machine Vision III (accepted)
ref-organizer: International Society for Optics and Photonics (SPIE)
---

Multispectral imaging is widely used in research and industry, e.\,g.\ for classification, defect detection or material abundance estimation. Such applications often require a larger spectral resolution compared to conventional RGB cameras. Typically, multispectral cameras are either based on diffractive elements such as prisms and gratings or narrow bandpass filters. Using these narrow bandpass filters, high spectral resolutions can be achieved, however narrow bandpass filters lead to a low number of detected photons per wavelength range and thus decrease the signal-to-noise-ratio (SNR) of the measured data. 

To overcome these limitations, a multispectral imaging approach using complementary notch filters is proposed. Instead of using a collection of $N$ bandpass filters with spectral transmissivity $\varphi(\lambda_i)$, $i=1,2,\dots N$, of varying central wavelength $\lambda_i$, the complementary filters with a spectral transmissivity of $\hat{\varphi}(\lambda)=1-\varphi(\lambda)$ are used. Each wavelength range that is sampled once in the case of the conventional bandpass filters is instead sampled $N-1$ times by the complementary filters due to the large filter overlap. Therefore, only little power of the incoming photon signal is lost even at high spectral resolution and the SNR of the multispectral data can be significantly improved. In addition, the SNR for complementary filters increases with increasing spectral resolution.

Hence, the resulting (complementary) image data is not a multispectral image in the conventional sense while containing the same spectral information. By relating the transmissivities, multispectral data collected with  complementary filters can be transformed into the standard basis of the bandpass filters. The transformed data can then be evaluated as a conventional multispectral image. However, an evaluation of the images is also possible in the complementary basis directly, thus eliminating the need for further postprocessing.

To validate the proposed approach, simulations of conventional bandpass filters as well as complementary notch filters are presented. To compare the resulting SNRs, the EMVA 1288 standard, initially developed for monochromatic cameras, is adopted in such a way that it is applicable to notch filter-based multispectral cameras. For this purpose, all $N$ channels of the camera are illuminated with $N$ monochromatic light sources with central wavelengths $\lambda_i$ and the SNR is calculated for each channel and each light source separately. Further, this adoption allows to obtain additional information about the filter widths and the overlap of the individual filters.
The SNRs are studied for complementary data, conventional data as well as complementary data transformed to the conventional bandpass basis as a function of the number of photons and the number of spectral channels. Moreover, the influence of different filter types such as ideal filters (rectangularly shaped) and more realistic filters (Gaussian shaped) is investigated. It is found that the SNR can be significantly improved by using complementary filters instead of the conventional bandpass filters, especially at high spectral resolution. This originates mainly from a strongly increased photon statistics but also from a reduction of dark noise caused by a significantly shorter exposure time.

According to the presented simulations, the approach allows to combine a high SNR with a high spectral resolution and thus it has a great potential to increase the sensitivity of multispectral imaging. 