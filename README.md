# Synthetic for Computer Vision

A list of synthetic dataset for computer vision. This is a repo for tracking the progress of using synthetic images for computer vision research.

If you found any important work is missing, please edit this file directly and make a pull request.

See also: http://riemenschneider.hayko.at/vision/dataset/index.php?filter=+synthetic

# 1. Image dataset
Synthetic image dataset. Information includes, number of images, task, project link (click project title) .

| Name          | Task         | Ground Truth | Publication                         |
|:--------------|:-------------|:-------------|:------------------------------------|
| Virtual KITTI |              |              | [CVPR2016](#gaidon2016virtual)      |
| Synthetia     |              |              | [CVPR2016](#ros2016synthia)         |
| Sintel        | Optical Flow |              | [ECCV2012](#butler2012naturalistic) |
| SceneFlow     |              |              | [CVPR2016](#mayer2015large)         |

## Project page

- [Virtual KITTI](http://www.xrce.xerox.com/Research-Development/Computer-Vision/Proxy-Virtual-Worlds)
- [Synthetia dataset](http://synthia-dataset.net/)
- [Sintel dataset](http://sintel.is.tue.mpg.de/)

# 2. 3D Model Repository

| Name           | No. Objects | No. Types | Format | Publication                  |
|:---------------|:------------|:----------|:-------|:-----------------------------|
| ShapeNet       |             |           |        |                              |
| 3dscan         |             |           | PLY    | [ArXiv](#choi2016large)      |
| seeing3Dchairs |             |           |        | [CVPR2014](#aubry2014seeing) |

## Project page
- [ShapeNet](http://shapenet.cs.stanford.edu/)
- [3dscan](http://redwood-data.org/3dscan/)
- [seeing3Dchairs](http://www.di.ens.fr/willow/research/seeing3Dchairs/) [github](https://github.com/dimatura/seeing3d)

# 3. Tools

| Name           | Platform             |
|:---------------|:---------------------|
| Render for CNN | Blender              |
| UETorch        | Unreal Engine 4(UE4) |
| UnrealCV       | UE4                  |
| VizDoom        | Doom                 |

## Project page
- Render for CNN
[github](https://github.com/shapenet/RenderForCNN)
<iframe src="http://ghbtns.com/github-btn.html?user=shapenet&repo=RenderForCNN&type=star&count=true" frameborder="0" scrolling="0" width="170px" height="20px"></iframe>
- ViZDoom
[github](https://github.com/Marqt/ViZDoom)
<iframe src="http://ghbtns.com/github-btn.html?user=Marqt&repo=ViZDoom&type=star&count=true" frameborder="0" scrolling="0" width="170px" height="20px"></iframe>
- UETorch
[github](https://github.com/facebook/UETorch)
<iframe src="http://ghbtns.com/github-btn.html?user=facebook&repo=UETorch&type=star&count=true" frameborder="0" scrolling="0" width="170px" height="20px"></iframe>
- UnrealCV [github](http://unrealcv.github.io)

## Misc.
- RealismCNN [github](https://github.com/junyanz/RealismCNN)
- Abnormality Detection in Images(http://paul.rutgers.edu/~babaks/abnormality_detection.html)

# Related topics
## Domain Transfer

## Reinforcement Learning

# Reference

This reference list is generated automatically using script `gen-reference.py` in this repo. The script uses the awesome [scholar.py](https://github.com/ckreibich/scholar.py) library.

Information is retrieved from google scholar. Send [me](qiuwch@gmail.com) an email if you spot any mistake. Citation information is from google scholar by the date: 09/27/16 as an indicator of impact. It is also helpful to discover related works.

Only the first author is shown in the text. Hover on the author name to see the complete author list.

## 2016
(Total=10)
- ResearchDoom and CocoDoom: Learning Computer Vision with Games. 2016
	([pdf](https://arxiv.org/pdf/1610.02431.pdf))
	([project](www.robots.ox.ac.uk/~vgg/research/researchdoom/))


-   The SYNTHIA dataset: A large collection of synthetic images for semantic segmentation of urban scenes.  2016

	 ([pdf](http://www.cv-foundation.org/openaccess/content_cvpr_2016/html/Ros_The_SYNTHIA_Dataset_CVPR_2016_paper.html)) ([project](http://synthia-dataset.net/)) ([citation:4](http://scholar.google.com/scholar?cites=9178628328030932213&as_sdt=2005&sciodt=0,5&hl=en))

-   Virtual Worlds as Proxy for Multi-Object Tracking Analysis.  2016

	 ([pdf](http://arxiv.org/abs/1605.06457)) ([project](http://www.xrce.xerox.com/Research-Development/Computer-Vision/Proxy-Virtual-Worlds)) ([citation:5](http://scholar.google.com/scholar?cites=11727455440906017188&as_sdt=2005&sciodt=0,5&hl=en))

-   Playing for data: Ground truth from computer games.  2016

	 ([pdf](http://link.springer.com/chapter/10.1007/978-3-319-46475-6_7))  ([citation:1](http://scholar.google.com/scholar?cites=12822958035144353200&as_sdt=2005&sciodt=0,5&hl=en))

-   Play and Learn: Using Video Games to Train Computer Vision Models.  2016

	 ([pdf](http://arxiv.org/abs/1608.01745))  ([citation:1](http://scholar.google.com/scholar?cites=16081073673799361643&as_sdt=2005&sciodt=0,5&hl=en))

-   ViZDoom: A Doom-based AI Research Platform for Visual Reinforcement Learning.  2016

	([code](https://github.com/Marqt/ViZDoom)) ([pdf](http://arxiv.org/abs/1605.02097)) ([project](http://vizdoom.cs.put.edu.pl/)) ([citation:4](http://scholar.google.com/scholar?cites=4101579648300742816&as_sdt=2005&sciodt=0,5&hl=en))

-   A large dataset of object scans.  2016

	 ([pdf](http://arxiv.org/abs/1602.02481)) ([project](http://redwood-data.org/3dscan/)) ([citation:6](http://scholar.google.com/scholar?cites=5989950372336055491&as_sdt=2005&sciodt=0,5&hl=en))

-   UnrealCV: Connecting Computer Vision to Unreal Engine  2016

	([code](http://unrealcv.github.io)) ([pdf](http://arxiv.org/abs/1609.01326))   

-   Learning Physical Intuition of Block Towers by Example  2016

	([code](https://github.com/facebook/UETorch)) ([pdf](http://arxiv.org/abs/1603.01312))  ([citation:12](http://scholar.google.com/scholar?cites=12846348306706460250&as_sdt=2005&sciodt=0,5&hl=en))

-   Target-driven Visual Navigation in Indoor Scenes using Deep Reinforcement Learning  2016

	 ([pdf](http://arxiv.org/abs/1609.05143))   
## 2015
(Total=3)

-   A Large Dataset to Train Convolutional Networks for Disparity, Optical Flow, and Scene Flow Estimation.  2015

	 ([pdf](http://arxiv.org/abs/1512.02134))  ([citation:9](http://scholar.google.com/scholar?cites=16431759299155441580&as_sdt=2005&sciodt=0,5&hl=en))

-   Render for cnn: Viewpoint estimation in images using cnns trained with rendered 3d model views.  2015

	([code](https://github.com/ShapeNet/RenderForCNN)) ([pdf](http://www.cv-foundation.org/openaccess/content_iccv_2015/html/Su_Render_for_CNN_ICCV_2015_paper.html))  ([citation:33](http://scholar.google.com/scholar?cites=1209553997502402606&as_sdt=2005&sciodt=0,5&hl=en))

-   Shapenet: An information-rich 3d model repository.  2015

	 ([pdf](http://arxiv.org/abs/1512.03012)) ([project](http://shapenet.cs.stanford.edu/)) ([citation:27](http://scholar.google.com/scholar?cites=1341601736562194564&as_sdt=2005&sciodt=0,5&hl=en))
## 2014
(Total=2)

-   Virtual and real world adaptation for pedestrian detection.  2014

	 ([pdf](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6587038))  ([citation:46](http://scholar.google.com/scholar?cites=2637402509859183337&as_sdt=2005&sciodt=0,5&hl=en))

-   Seeing 3d chairs: exemplar part-based 2d-3d alignment using a large dataset of cad models.  2014

	([code](https://github.com/dimatura/seeing3d)) ([pdf](http://www.cv-foundation.org/openaccess/content_cvpr_2014/html/Aubry_Seeing_3D_Chairs_2014_CVPR_paper.html)) ([project](http://www.di.ens.fr/willow/research/seeing3Dchairs/)) ([citation:110](http://scholar.google.com/scholar?cites=18030645502969108287&as_sdt=2005&sciodt=0,5&hl=en))
## 2013
(Total=1)

-   Detailed 3d representations for object recognition and modeling.  2013

	 ([pdf](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6516504))  ([citation:67](http://scholar.google.com/scholar?cites=6595507135181144034&as_sdt=2005&sciodt=0,5&hl=en))
## 2012
(Total=1)

-   A naturalistic open source movie for optical flow evaluation.  2012

	 ([pdf](http://link.springer.com/chapter/10.1007/978-3-642-33783-3_44)) ([project](http://sintel.is.tue.mpg.de/)) ([citation:227](http://scholar.google.com/scholar?cites=15124407213489971559&as_sdt=20000005&sciodt=0,21&hl=en))
## 2010
(Total=1)

-   Learning appearance in virtual scenarios for pedestrian detection.  2010

	 ([pdf](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5540218))  ([citation:79](http://scholar.google.com/scholar?cites=17243485674852907889&as_sdt=2005&sciodt=0,5&hl=en))
## 2007
(Total=1)

-   Ovvv: Using virtual worlds to design and evaluate surveillance systems.  2007

	 ([pdf](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=4270516))  ([citation:58](http://scholar.google.com/scholar?cites=3459961090644684583&as_sdt=2005&sciodt=0,5&hl=en))
