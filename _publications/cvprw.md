---
title: "Single-camera and inter-camera vehicle tracking and 3D speed estimation based on fusion of visual and semantic features"
collection: publications
permalink: /publication/cvpr2018
excerpt: '[[Paper]](http://openaccess.thecvf.com/content_cvpr_2018_workshops/papers/w3/Tang_Single-Camera_and_Inter-Camera_CVPR_2018_paper.pdf), 
[[Poster]](https://alexxiao95.github.io/publications/cvprw/cvpr_poster.pdf),
[[Code]](https://github.com/AlexXiao95/Multi-Camera-Vehicle-Tracking-and-Reidentification), 
[[2018 NVIDIA AI City Challenge]](http://openaccess.thecvf.com/content_cvpr_2018_workshops/papers/w3/Naphade_The_2018_NVIDIA_CVPR_2018_paper.pdf)'
date: 2018-5-01
venue: 'CVPR Workshop on the NVIDIA AI City Challenge'
paperurl: ''
citation: 'Zheng Tang, Gaoang Wang, **Hao Xiao**, Aotian Zheng and Jenq-Neng Hwang, "Single-camera and inter-camera vehicle tracking and 3D speed estimation based on fusion of visual and semantic features," In CVPR Workshop (CVPRW) on the AI City Challenge, 2018'
---

[[Paper]](http://openaccess.thecvf.com/content_cvpr_2018_workshops/papers/w3/Tang_Single-Camera_and_Inter-Camera_CVPR_2018_paper.pdf), 
[[Poster]](https://alexxiao95.github.io/publications/cvprw/cvpr_poster.pdf),
[[Code]](https://github.com/AlexXiao95/Multi-Camera-Vehicle-Tracking-and-Reidentification), 
[[2018 NVIDIA AI City Challenge]](http://openaccess.thecvf.com/content_cvpr_2018_workshops/papers/w3/Naphade_The_2018_NVIDIA_CVPR_2018_paper.pdf)


# Abstract
Tracking of vehicles across multiple cameras with non-overlapping views has been a challenging task for the intelligent transportation system (ITS). It is mainly because of high similarity among vehicle models, frequent occlusion, large variation in different viewing perspectives and low video resolution. In this work, we propose a fusion of visual and semantic features for both single-camera tracking (SCT) and inter-camera tracking (ICT). Specifically, a histogram-based adaptive appearance model is introduced to learn long-term history of visual features for each vehicle target. Besides, semantic features including trajectory smoothness, velocity change and temporal information are incorporated into a bottom-up clustering strategy for data association in each single camera view. Across different camera views, we also exploit other information, such as deep learning features, detected license plate features and detected car types, for vehicle re-identification. Additionally, evolutionary optimization is applied to camera calibration for reliable 3D speed estimation. Our algorithm achieves the top performance in both 3D speed estimation and vehicle re-identification at the NVIDIA AI City Challenge 2018.


# Demo Video
<iframe width="560" height="315" src="https://www.youtube.com/embed/_i4numqiv7Y?start=1200" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
<br />
 
<iframe width="560" height="315" src="https://www.youtube.com/embed/Jlvh_KxHl40" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

