# Eyes and Lips Segmentation in a Face
Python program which inputs an image of a face, and creates a mask around the eyes and lips of the face. 

## Overview
The network architecture used here is based on BiSeNet [1] and ResNet. The dataset used is CelebAMask-HQ Dataset [2]. 

## How to run

### Prerequisties
- Python 3
- PyTorch
- Scikit-Image
- OpenCV
- Pillow

### Steps
- Download the pre-trained model from [here](https://drive.google.com/file/d/154JgKpzCPW82qINcVieuPH3fZ2e0P812/view). Put the `.pth` file in `cp` folder.
- Run `eyes-and-lips.py` with the path of the image as argument. For example:
``` 
python eyes-and-lips.py --img-path images/img1.jpg
```

## Results

#### Demo 1
![Input](/images/img1.jpg)
![Mask](/images/results/img1-mask.PNG)
![Output](/images/results/img1-op.PNG)

#### Demo 2
![Input](/images/img3.jpg)
![Mask](/images/results/img3-mask.PNG)
![Output](/images/results/img3-op.PNG)

## Sources
- [1] [BiSeNet: Bilateral Segmentation Network for Real-time Semantic Segmentation](https://github.com/CoinCheung/BiSeNet)
- [2] [CelebAMask-HQ Dataset](https://github.com/switchablenorms/CelebAMask-HQ)
- [3] https://github.com/zllrunning/face-parsing.PyTorch
