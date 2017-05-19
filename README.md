# Synthetic for Computer Vision

This is a repo for tracking the progress of using synthetic images for computer vision research. If you found any important work is missing or information is not up-to-date, please edit this file directly and make a pull request. Each publication is tagged with a keyword to make it easier to search.

If you find anything missing from this page, please edit this `README.md` file to add it. When adding a new item, you can simply follow the format of existing items. How this document is structured is documented in [`contribute.md`](contribute.md).


**How to use**: Click publication to jump to the paper title, detailed information such as code and project page will be provided together with pdf file.**

<div id="dataset"></div>

## Synthetic image dataset

- [SURREAL](#varol2017learning)
- [Virtual KITTI](#gaidon2016virtual)      
- [Synthetia](#ros2016synthia)         
- [Sintel](#butler2012naturalistic), A synthetic dataset for optical flow
- [SceneFlow](#mayer2015large)
- [4D Light Fields](#honauer2016dataset)

<div id="models"></div>

## 3D Model Repository

Realistic 3D models are critical for creating realistic and diverse virtual worlds. Here are research efforts for creating 3D model repositories.

- [ShapeNet](#chang2015shapenet)  
- [3dscan](#choi2016large)      
- [seeing3Dchairs](#aubry2014seeing)

<div id="tool"></div>

## Tools

- Render SMPL human bodies on Blender, see [CVPR2017](#varol2017learning)
- Render for CNN, based on Blender, see [ICCV2015](#su2015render)
- UETorch, based on UE4, see [ICML2016](#lerer2016learning)
- UnrealCV, based on UE4, see [ArXiv](#qiu2016unrealcv)
- VizDoom, based on Doom, see [ArXiv](#kempka2016vizdoom)
- OpenAI Universe, see [project page](https://universe.openai.com/)
- Blender addon for 4D light field rendering, see [project page](https://github.com/lightfield-analysis/blender-addon)

<div id="resource"></div>

## Resources

[ECCV 2016 Virtual/Augmented Reality for Visual Artificial Intelligence (VARVAI) workshop](http://adas.cvc.uab.es/varvai2016/)

[Role of Simulation in Computer Vision](https://www.microsoft.com/en-us/research/event/iccv-2017-role-of-simulation-in-computer-vision/)

[Virtual Reality Meets Physical Reality:
Modelling and Simulating Virtual Humans and Environments
Siggraph Asia 2016 workshop](http://sigvr.org/)

See also: http://riemenschneider.hayko.at/vision/dataset/index.php?filter=+synthetic

## Misc.
- RealismCNN [github](https://github.com/junyanz/RealismCNN)
- Abnormality Detection in Images(http://paul.rutgers.edu/~babaks/abnormality_detection.html)

<div id="reference"></div>

## Reference

<!-- The div id is bib citekey from google scholar, use div id makes it easier to reference a work in this document. -->

### 2017

(Total=5)

<div id="varol2017learning"></div>

- Learning from Synthetic Humans
	<span class="octicon octicon-mark-github"></span>
	([:octocat:code](https://github.com/gulvarol/surreal))
	([pdf](https://arxiv.org/abs/1701.01370))
	([project](http://www.di.ens.fr/willow/research/surreal/))
	tag: synthetic human
	
- [Nvidia Issac](http://www.marketwired.com/press-release/nvidia-ushers-new-era-robotics-with-breakthroughs-making-it-easier-build-train-intelligent-2215481.htm)

- Configurable, Photorealistic Image Rendering and Ground Truth Synthesis by Sampling Stochastic Grammars Representing Indoor Scenes

<div id="airsim"></div>

- Aerial Informatics and Robotics Platform
	<span class="octicon octicon-mark-github"></span>
	([:octocat:code](https://github.com/Microsoft/AirSim))
	([pdf](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/02/aerial-informatics-robotics-TR.pdf))
	([project](https://www.microsoft.com/en-us/research/project/aerial-informatics-robotics-platform/))
	tag: tool


<div id="tobin2017domain"></div>

- Tobin, Josh, et al. "Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World." arXiv preprint arXiv:1703.06907 (2017). tag: domain
	([pdf](https://arxiv.org/pdf/1703.06907.pdf))

### 2016
(Total=17)

<div id="sadeghi2016rl"></div>

- Sadeghi, Fereshteh, and Sergey Levine. "rl: Real single-image flight without a single real image. arXiv preprint." arXiv preprint arXiv:1611.04201 12 (2016). tag: rl

- Johnson, Justin, et al. "CLEVR: A Diagnostic Dataset for Compositional Language and Elementary Visual Reasoning." arXiv preprint arXiv:1612.06890 (2016).
	([pdf](https://arxiv.org/abs/1612.06890))

- McCormac, John, et al. "SceneNet RGB-D: 5M Photorealistic Images of Synthetic Indoor Trajectories with Ground Truth." arXiv preprint arXiv:1612.05079 (2016).

- de Souza, César Roberto, et al. "Procedural Generation of Videos to Train Deep Action Recognition Networks." arXiv preprint arXiv:1612.00881 (2016).
	([pdf](https://arxiv.org/abs/1612.00881))
	([project](http://adas.cvc.uab.es/phav/))
	tag: synthetic human

- Synnaeve, Gabriel, et al. "TorchCraft: a Library for Machine Learning Research on Real-Time Strategy Games." arXiv preprint arXiv:1611.00625 (2016).
	([pdf](https://arxiv.org/abs/1611.00625))
	([code](https://github.com/TorchCraft/TorchCraft))

- Lin, Jenny, et al. "A virtual reality platform for dynamic human-scene interaction." SIGGRAPH ASIA 2016 Virtual Reality meets Physical Reality: Modelling and Simulating Virtual Humans and Environments. ACM, 2016.
	([pdf](https://xiaozhuchacha.github.io/projects/siggraphasia16_vrplatform/vrplatform2016siggraphasia.pdf))
	([project](https://xiaozhuchacha.github.io/projects/siggraphasia16_vrplatform/index.html))

- Mahendran, A., et al. "ResearchDoom and CocoDoom: Learning Computer Vision with Games." arXiv preprint arXiv:1610.02431 (2016).
	([pdf](https://arxiv.org/pdf/1610.02431.pdf))
	([project](www.robots.ox.ac.uk/~vgg/research/researchdoom/))

<div id="ros2016synthia"></div>

- The SYNTHIA dataset: A large collection of synthetic images for semantic segmentation of urban scenes.  2016
	 ([pdf](http://www.cv-foundation.org/openaccess/content_cvpr_2016/html/Ros_The_SYNTHIA_Dataset_CVPR_2016_paper.html))
	 ([project](http://synthia-dataset.net/))
	 ([citation:4](http://scholar.google.com/scholar?cites=9178628328030932213&as_sdt=2005&sciodt=0,5&hl=en))

<div id="gaidon2016virtual"></div>

-   Virtual Worlds as Proxy for Multi-Object Tracking Analysis.  2016   
	 ([pdf](http://arxiv.org/abs/1605.06457))
	 ([project](http://www.xrce.xerox.com/Research-Development/Computer-Vision/Proxy-Virtual-Worlds))
	 ([citation:5](http://scholar.google.com/scholar?cites=11727455440906017188&as_sdt=2005&sciodt=0,5&hl=en))

-   Playing for data: Ground truth from computer games.  2016   
	 ([pdf](http://link.springer.com/chapter/10.1007/978-3-319-46475-6_7))
	 ([citation:1](http://scholar.google.com/scholar?cites=12822958035144353200&as_sdt=2005&sciodt=0,5&hl=en))

-   Play and Learn: Using Video Games to Train Computer Vision Models.  2016   
	 ([pdf](http://arxiv.org/abs/1608.01745))
	 ([citation:1](http://scholar.google.com/scholar?cites=16081073673799361643&as_sdt=2005&sciodt=0,5&hl=en))

-   ViZDoom: A Doom-based AI Research Platform for Visual Reinforcement Learning.  2016    
	([:octocat:code](https://github.com/Marqt/ViZDoom))
	([pdf](http://arxiv.org/abs/1605.02097))
	([project](http://vizdoom.cs.put.edu.pl/))
	([citation:4](http://scholar.google.com/scholar?cites=4101579648300742816&as_sdt=2005&sciodt=0,5&hl=en))

<div id="choi2016large"></div>

-   A large dataset of object scans.  2016   
	 ([pdf](http://arxiv.org/abs/1602.02481))
	 ([project](http://redwood-data.org/3dscan/))
	 ([citation:6](http://scholar.google.com/scholar?cites=5989950372336055491&as_sdt=2005&sciodt=0,5&hl=en))

<div id="qiu2016unrealcv"></div>

-   UnrealCV: Connecting Computer Vision to Unreal Engine  2016    
	<span class="octicon octicon-mark-github"></span>
	([:octocat:code](https://github.com/unrealcv/unrealcv))
	([project](http://unrealcv.github.io))
	([pdf](http://arxiv.org/abs/1609.01326))   

<div id="lerer2016learning"></div>

-   Learning Physical Intuition of Block Towers by Example  2016   
	([:octocat:code](https://github.com/facebook/UETorch))
	([pdf](http://arxiv.org/abs/1603.01312))
	([citation:12](http://scholar.google.com/scholar?cites=12846348306706460250&as_sdt=2005&sciodt=0,5&hl=en))

-   Target-driven Visual Navigation in Indoor Scenes using Deep Reinforcement Learning  2016   
	 ([pdf](http://arxiv.org/abs/1609.05143))   

<div id="honauer2016dataset"></div>

-   A Dataset and Evaluation Methodology for Depth Estimation on 4D Light Fields. ACCV 2016   
	 ([:octocat:code](https://github.com/lightfield-analysis))
	 ([pdf](http://lightfield-analysis.net/benchmark/paper/lightfield_benchmark_accv_2016.pdf))
	 ([project](http://lightfield-analysis.net/))
	 ([citation](https://scholar.google.de/scholar?cluster=3369030498099069181&hl=en&as_sdt=0,5))   

### 2015
(Total=3)

-   A Large Dataset to Train Convolutional Networks for Disparity, Optical Flow, and Scene Flow Estimation.  2015    
	 ([pdf](http://arxiv.org/abs/1512.02134))
	 ([citation:9](http://scholar.google.com/scholar?cites=16431759299155441580&as_sdt=2005&sciodt=0,5&hl=en))

<div id="su2015render"></div>

-   Render for cnn: Viewpoint estimation in images using cnns trained with rendered 3d model views.  2015   
	([:octocat:code](https://github.com/ShapeNet/RenderForCNN))
	([pdf](http://www.cv-foundation.org/openaccess/content_iccv_2015/html/Su_Render_for_CNN_ICCV_2015_paper.html))
	([citation:33](http://scholar.google.com/scholar?cites=1209553997502402606&as_sdt=2005&sciodt=0,5&hl=en))

<div id="chang2015shapenet"></div>

-   Shapenet: An information-rich 3d model repository.  2015    
	 ([pdf](http://arxiv.org/abs/1512.03012))
	 ([project](http://shapenet.cs.stanford.edu/))
	 ([citation:27](http://scholar.google.com/scholar?cites=1341601736562194564&as_sdt=2005&sciodt=0,5&hl=en))

### 2014
(Total=2)

-   Virtual and real world adaptation for pedestrian detection.  2014    
	 ([pdf](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6587038))
	 ([citation:46](http://scholar.google.com/scholar?cites=2637402509859183337&as_sdt=2005&sciodt=0,5&hl=en))

<div id="aubry2014seeing"></div>

-   Seeing 3d chairs: exemplar part-based 2d-3d alignment using a large dataset of cad models.  2014   
	([:octocat:code](https://github.com/dimatura/seeing3d))
	([pdf](http://www.cv-foundation.org/openaccess/content_cvpr_2014/html/Aubry_Seeing_3D_Chairs_2014_CVPR_paper.html))
	([project](http://www.di.ens.fr/willow/research/seeing3Dchairs/))
	([citation:110](http://scholar.google.com/scholar?cites=18030645502969108287&as_sdt=2005&sciodt=0,5&hl=en))

### 2013
(Total=1)

-   Detailed 3d representations for object recognition and modeling.  2013   
	 ([pdf](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6516504))
	 ([citation:67](http://scholar.google.com/scholar?cites=6595507135181144034&as_sdt=2005&sciodt=0,5&hl=en))

### 2012
(Total=1)

<div id="butler2012naturalistic"></div>

-   A naturalistic open source movie for optical flow evaluation.  2012    
	 ([pdf](http://link.springer.com/chapter/10.1007/978-3-642-33783-3_44))
	 ([project](http://sintel.is.tue.mpg.de/))
	 ([citation:227](http://scholar.google.com/scholar?cites=15124407213489971559&as_sdt=20000005&sciodt=0,21&hl=en))

### 2010
(Total=1)

-   Learning appearance in virtual scenarios for pedestrian detection.  2010   
	 ([pdf](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5540218))
	 ([citation:79](http://scholar.google.com/scholar?cites=17243485674852907889&as_sdt=2005&sciodt=0,5&hl=en))

### 2007
(Total=1)

-   Ovvv: Using virtual worlds to design and evaluate surveillance systems.  2007   
	 ([pdf](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=4270516))
	 ([citation:58](http://scholar.google.com/scholar?cites=3459961090644684583&as_sdt=2005&sciodt=0,5&hl=en))
