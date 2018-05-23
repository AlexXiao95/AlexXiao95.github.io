---
title: "Single-Camera and Inter-Camera Vehicle Tracking and 3D Speed Estimation Based on Fusion of Visual and Semantic Features "
collection: research
type: "Workshop"
permalink: /research/research-mct
venue: "University of Washington"
date: 2018-04-01
location: "City, Country"
---

Tracking of vehicles across multiple cameras with non-overlapping views has been a challenging task for the intelligent transportation system (ITS). It is mainly because of high similarity among vehicle models, frequent occlusion, large variation in different viewing perspectives and low video resolution. In this work, we propose a fusion of visual and semantic features for both single-camera tracking (SCT) and inter-camera tracking (ICT). Specifically, a histogram-based adaptive appearance model is introduced to learn long-term history of visual features for each vehicle target. Besides, semantic features including trajectory smoothness, velocity change and temporal information are incorporated into a bottom-up clustering strategy for data association in each single camera view. Across different camera views, we also exploit other information, such as deep learning features, detected license plate features and detected car types, for vehicle re-identification. Additionally, evolutionary optimization is applied to camera calibration for reliable 3D speed estimation. Our algorithm achieves the top performance in both 3D speed estimation and vehicle re-identification at the NVIDIA AI City Challenge Workshop at CVPR 2018. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/_i4numqiv7Y" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/Jlvh_KxHl40" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

[Accepted by [CVPR 2018](http://cvpr2018.thecvf.com)]

[Source code available at [GitHub](https://github.com/zhengthomastang/2018AICity_TeamUW)]