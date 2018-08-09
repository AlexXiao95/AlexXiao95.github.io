---
title: "Group Re-Identification: Leveraging and Integrating Multi-Grain Information"
collection: publications
permalink: /publication/acmmm2018
excerpt: '[[paper]](http://alexxiao95.github.io/files/paper_acmmm.pdf), Camera-ready version to appear.'
date: 2018-7-01
venue: 'ACM Multimedia'
paperurl: ''
citation: 'Hao Xiao, Weiyao Lin, Bin Sheng, Ke Lu, Junchi Yan, Jingdong Wang, Errui Ding, Yihao Zhang, and Hongkai Xiong. 2018. Group Re-Identification: Leveraging and Integrating Multi-Grain Information. In 2018 ACM Multimedia Conference'
---

[[paper]](http://alexxiao95.github.io/files/paper_acmmm.pdf), Camera-ready version to appear.

# Abstract
This paper addresses an important yet less-studied problem: re-identifying groups of people in different camera views. Group re-identification (Re-ID) is very challenging since it is not only interfered by view-point and human pose variations in the traditional single-object Re-ID tasks, but also suffers from group layout and group member variations. To handle these issues, we propose to leverage the information of multi-grain objects: individual person and subgroups of two and three people inside a group image. We compute multi-grain representations to characterize the appearance and spatial features of multi-grain objects and evaluate the importance weight of each object for group Re-ID, so as to handle the interferences from group dynamics. We compute the optimal group-wise matching by using a multi-order matching process based on the multi-grain representation and importance weights. Furthermore, we dynamically update the importance weights according to the current matching results and then compute a new optimal group-wise matching. The two steps are iteratively conducted, yielding the final matching results. Experimental results on various datasets demonstrate the effectiveness of our approach.

# Framework
<div style="text-align: center">
<img src="https://alexxiao95.github.io/publications/acmmm/framework.png" width = "700">
</div>

This figure illustrates the overview of our proposed approach. Given the probe group image captured from one camera, our goal is to find the matched group images from a set of gallery group images captured from another camera. We represent each group image by a set of multi-grain objects, and extract the features for the multi-grain objects. The matching process is an iterative process. We compute the static and dynamic importance weights of multi-grain objects for the probe and gallery images according to the intermediate matching results. Then, we use a multi-order matching algorithm to compute intermediate matching results, which are used to update the dynamic importance weights. We perform the two stages iteratively, and obtain the final matching results.

# Multi-grain Representation and Importance Weighting
<div style="text-align: center">
<img src="https://alexxiao95.github.io/publications/acmmm/figure1.png" width = "600">
</div>

Figure 1: (a) Illustration of matched-people sets and their distributions in the feature space (The color solid arrows indicate the one-to-one mapping results between individuals. People circled by the same color rectangles in camera B are matched to the same person in A, and belong to the same matched people set). (b) The derived importance weights for multi-grain objects (individuals, 2-people subgroup s, 3-people subgroups) in two group images. Note: the importance weights for some 2-people/3-people subgroups are not displayed in order for a cleaner illustration. (Best viewed in color)

# Multi-order Matching
<div style="text-align: center">
<img src="https://alexxiao95.github.io/publications/acmmm/matching.png" width = "600">
</div>

Figure 2: Illustration of multi-order association graph. Left: A cross-view group pair being matched; Right: The multi-order association graph constructed for the group pair.

# Results

We perform experiments on three datasets: (1) the public i-LID MCTS dataset which contains 274 group images for 64 groups; (2) our own constructed DukeMTMC Group dataset which includes 177 group image pairs extracted from a 8-camera-view DukeMTMC dataset; (3) our own constructed Road Group dataset which includes 162 group pairs taken from a two-camera crowd road scene. When constructing our own datasets, we automatically detect groups, and randomly select groups with different sizes & variations as the target groups in our dataset. Moreover, we define two cross-view groups as the same group when they have more than 60% members in common.

<div style="text-align: center">
<img src="https://alexxiao95.github.io/publications/acmmm/res.png" width = "800">
</div>

Figure 3: CMC results of Group Re-ID on different datasets. We compares our approach with the state-of-the-art group re-identification methods on different datasets: CRRRO-BRO, Covariance, PREF, BSC+CM. To further demonstrate the effectiveness of our approach, we also include the results of two state-of-the-art methods designed for single person Re-ID, which utilize patch saliency or a KMFA(Rχ2) distance metric to calculate image-wise similarity (Saliency and Mirror+KMFA). From this table, we can observe that our approach has better results than the existing group Re-ID methods. This demonstrates the effectiveness of our approach.


<div style="text-align: center"> 
<img src="https://alexxiao95.github.io/publications/acmmm/table.png" width = "800"> 
</div>