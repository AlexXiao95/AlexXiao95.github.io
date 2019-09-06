---
title: "Group Re-Identification with Multi-grained Matching and Integration"
collection: publications
permalink: /publications/tcyber2019
excerpt: '[[Paper]](https://arxiv.org/pdf/1905.07108.pdf), [[Dataset]](http://min.sjtu.edu.cn/lwydemo/GroupReID.html)'
date: 2019-5-01
venue: 'IEEE Transactions on Cybernetics'
---

[[Paper]](https://arxiv.org/pdf/1905.07108.pdf), [[Dataset]](http://min.sjtu.edu.cn/lwydemo/GroupReID.html)

## Abstract
The task of re-identifying groups of people underdifferent camera views, is an important yet less-studied problem. Group re-identification (Re-ID) is a very challenging task since it is not only adversely affected by common issues in traditionalsingle object Re-ID problems such as viewpoint and human posevariations, but it also suffers from changes in group layout and group membership. In this paper, we propose a novel concept of group granularity by characterizing a group image by multi-grained objects: individual persons and sub-groups of two andthree people within a group. To achieve robust group Re-ID, we first introduce multi-grained representations which can be extracted through the development of two separate schemes, i.e. one with hand-crafted descriptors and another with deep neural networks. The proposed representation seeks to characterize both appearance and spatial relations of multi-grained objects, and is further equipped with importance weights which capture variations in intra-group dynamics. Optimal group-wise matching isfacilitated by a multi-order matching process which in turn,dynamically updates the importance weights in iterative fashion.We evaluated on three multi-camera group datasets containingcomplex scenarios and large dynamics, with experimental results demonstrating the effectiveness of our approache.

## Dataset
### Road Group
Our newly constructed Road Group dataset [1] consists of 162 group pairs taken from a 2-camera-view of a crowded road scene. The bounding box coordinates of totally 1099 pedestrians are also provided. This dataset is challenging due to its large variation of group layout and human pose.

<div style="text-align: center">
<img src="https://alexxiao95.github.io/publications/acmmm/dataset.png" width = "600">
</div>


### Annotations
For each of our constructed dataset, we provide 3 different kinds of annotations, the group id annotations, the single pedestrian correspondance annotations and single pedestrian bounding box annotations.

The group id annotations is a json file with the following format. The field "id" is the group id number, "image name" denotes the names of images containing this group. 
 

```
group_id{
		"id"           : int, 
		"image names"  : [str, str]
}
```


The single pedestrian bounding box annotations is a json file with the following format. The field "image name" denotes the name of group image. The "pedestrian" field is a list of person annotation type, which includes two sub-fields. The "person id" field is the index of the person within this group and the "bbox" field is the bounding box corrdinate of the person.

```
person_bounding_box{
		"image name"   : str, 
		"pedestrian"   : [person, person, ....],
}

person{
		"person id"    : int, 
		"bbox"         : [xmin, ymin, xmax, ymax]
}
```

The single pedestrian correspondance annotations indicate the individual correspondance between two matched groups. It is a json file with the following format. The field "group pair" is the list containing names of two images, and the "person pairs" field denotes the correspondance relationship between people in the two images, which is a list of person_pair annotation type. The person_pair annotation type includes two fields, "person1 id" and "person2 id", which denote the person ids in the first and second group in the group pair.

```
person_correspondance{
		"group pair"   : [str, str], 
		"person pairs" : [person_pair, person_pair, ...]
}

person_pair{
		"person1 id"   : int, 
		"person2 id"   : int,
}
```


## Reference
Please cite this paper in your publications if it helps your research:

```
@inproceedings{xiao2018group,
  title={Group Re-Identification: Leveraging and Integrating Multi-Grain Information},
  author={Xiao, Hao and Lin, Weiyao and Sheng, Bin and Lu, Ke and Yan, Junchi and Wang, Jingdong and Ding, Errui and Zhang, Yihao and Xiong, Hongkai},
  booktitle={2018 ACM Multimedia Conference on Multimedia Conference},
  pages={192--200},
  year={2018},
  organization={ACM}
}

@article{lin2019group,
    title={Group Re-Identification with Multi-grained Matching and Integration},
    author={Lin, Weiyao and Li, Yuxi and Xiao, Hao and John, See and Zou, Junni and Xiong, Hongkai and Wang, Jingdong and Mei Tao},
    journal={IEEE Transaction on Cybernetics},
    year={2019},
    doi={10.1109/TCYB.2019.2917713},
    organization={IEEE}
    }
```