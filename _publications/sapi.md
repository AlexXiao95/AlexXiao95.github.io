---
title: "SAPI: Surroundings-Aware Vehicle Trajectory Prediction at Intersections"
collection: publications
permalink: /publications/sapi
date: 2023-8-01
venue: 'arxiv'
---

[[Paper]](https://arxiv.org/pdf/2306.01812)


## Abstract
In this work we propose a deep learning model, i.e., SAPI, to predict vehicle trajectories at intersections. SAPI uses an abstract way to represent and encode surrounding environment by utilizing information from real-time map, right-of-way, and surrounding traffic. The proposed model consists of two convolutional network (CNN) and recurrent neural network (RNN)-based encoders and one decoder. A refiner is proposed to conduct a look-back operation inside the model, in order to make full use of raw history trajectory information. We evaluate SAPI on a proprietary dataset collected in real-world intersections through autonomous vehicles. It is demonstrated that SAPI shows promising performance when predicting vehicle trajectories at intersection, and outperforms benchmark methods. The average displacement error(ADE) and final displacement error(FDE) for 6-second prediction are 1.84m and 4.32m respectively. We also show that the proposed model can accurately predict vehicle trajectories in different scenarios.

## Framework
<div style="text-align: center">
<img src="https://alexxiao95.github.io/publications/sapi/framework.png" width = "700">
</div>


## Reference
Please cite this paper in your publications if it helps your research:

```
@article{zhang2023sapi,
  title={SAPI: Surroundings-Aware Vehicle Trajectory Prediction at Intersections},
  author={Zhang, Ethan and Xiao, Hao and Gan, Yiqian and Wang, Lei},
  journal={arXiv preprint arXiv:2306.01812},
  year={2023}
}
```