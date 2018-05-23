---
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Please refer to [*my latest resume(pdf)*](http://academicpages.github.io/files/resume_Hao.pdf) [May. 2018] or my [*LinkedIn profile*](https://www.linkedin.com/in/hao-xiao-1b1257124/).

Education
======
### [University of Washington](https://www.washington.edu) (UW)
* M.S. in Electrical Engineering, Sep.2017 - Mar. 2019(expected)
* Member of Information Processing Lab where the main research areas are computer vision and image processing

### [Shanghai Jiao Tong University](http://www.sjtu.edu.cn) (SJTU)
* B.S. in Electrical Engineering, Sep. 2013 - Jun. 2017
* Outstanding Graduate


Skills
======
* Interests: Computer Vision, Video/Image Processing, Machine Learning, Deep Learning
* language: C/C++, Python, Java, Matlab
* Tools: OpenCV, Linux, Git, Vim, Bash, TensorFlow, Azure, AWS

Work Experiences
======
### [TuSimple Future Tech Co., Ltd](http://www.tusimple.com/index-en.html)
* Incoming machine learning intern working on developing state-of-the-art algorithms for **autonomous driving**

### [Clobotics Tech Co., Ltd](https://www.clobotics.com)
Machine Learning & Computer Vision Intern

* Refactored the model training setup by utilizing multiprocessing pool to reduce time at assembling data and cropping images
* Improved classification accuracy by using super-resolution technique to do **fine-grained classification** (more than 2000 types)
* Trained an end-to-end fine-grained classification model by combining image super-resolution and classification into a single model
  
Experiences
======

### [Information Processing Lab](http://allison.ee.washington.edu/index_files/Page701.htm) (IPL), UW

Graduate Research Assistant, supervised by [*Prof. Jenq-Neng Hwang*](http://www.ee.washington.edu/people/jenq-neng-hwang/)

* Realized a fully unsupervised online learning framework to achieve **multi-camera tracking** of people
* Designed multi-camera tracking of vehicle with a fusion of adaptive appearance, semantic features and comparison of license plates
* Participated in [*NVIDIA AI City challenge 2018*](), which held as a workshop at [*CVPR 2018*](http://cvpr2018.thecvf.com), and achieved a superiority performance in both Track 1: Traffic Flow Analysis and Track 3: Multi-camera Vehicle Detection & Reidentification, among over 20 teams

### **[Image, Video, and Multimedia Communication Lab](http://ivm.sjtu.edu.cn) (IVM), SJTU**

Undergraduate Research Assistant, supervised by [*Prof. Weiyao Lin*](http://wylin2.vosi.biz).

* Collected two challenging [group re-identification datasets]() by tracking people in a crowd scene and implementing socially constraint structure learning to detect groups.* Developed a multi-grain **group re-identification** process which derives features for multi-grain objects and iteratively evaluates their importance to handle interferences from group dynamics.* Proposed a multi-order matching process by a personalized random walk scheme through a multi-order association graph, which integrated multi-grain information to obtain more reliable group matching results.

Project Leader of an Intelligent System

* Achieved a real-time object detection system by training convolutional neural network and iteratively advancing model performance, which can classify normal people and fallen people.* Utilized graph matching algorithm based on confident tracklets to develop multiple object tracking algorithm.* Implemented a **real-time tracking system** on surveillance video stream by combining detection and tracking algorithm, which realized pedestrian counting as well as fall warning.

### **[Research Center of Intelligent Internet of Things]((http://iiot.sjtu.edu.cn/)) (IIOT), SJTU**

Project Team Leader, supervised by [*Prof. Xinbing Wang*](http://www.cs.sjtu.edu.cn/~wang-xb/).

* Conducted the construction and maintenance of an academic search system: [*Acemap*](http://www.papersbook.org).* Analyzed a large scale academic dataset, [*Microsoft Academic Graph*](https://www.microsoft.com/en-us/research/project/microsoft-academic-graph/) (MAG), which included data crawling, cleaning and processing.
* Applied for a patent: Construction and Visualization of Heterogeneous Topic Web Based on Text Network, which can recognize the relationship between word topics and document topics.* Designed a novel “interactive map” approach to visualize large-scale and high-dimensional academic literatures and display the underlying relationship among them, which is available on the Acemap website.

Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Patent
======
* Construction and Visualization of Heterogeneous Topic Web Based on Text Network, Patent #: ZL201610757401.0 (Chinese) [[Link](http://www.soopat.com/Patent/201610757401)]
  
Honors
======
* Winner Team, Track 1 & Track 3 at the NVIDIA AI City Challenge Workshop at CVPR 2018, Apr. 2018
* First Prize, China Undergraduate Mathematical Contest in Modeling, Jan. 2016
* First Prize, Chinese Mathematical Olympiad, Dec. 2012

Service
======
* Conference and Journal Reviewer: CVPR 2018, ETRI 2018
