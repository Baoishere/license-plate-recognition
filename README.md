# Vietnamese License Plate Recognition

This repository provides you with a detailed guide on how to training and build a Vietnamese License Plate detection and recognition system. This system can work on 2 types of license plate in Vietnam, 1 line plates and 2 lines plates.

## Installation

```bash
  git clone https://github.com/Baoishere/license-plate-recognition.git
  cd license-plate-recognition

  # install dependencies using pip 
  pip install -r ./requirement.txt
```

- **Pretrained model from this link:** [Models](https://drive.google.com/drive/folders/1qB8QYr-b-PWsXMO0K3mef66P_kXfhfmM?usp=sharing) 

- **Download yolov5 (old version) from this link:** [yolov5](https://drive.google.com/drive/folders/16Urwqj_x9Y_3KWLcc1cKMDOdYdhaQhxx?usp=sharing)

- Copy yolov5 and Models folder to project folder

## Run License Plate Recognition

```bash
  #(new) run integrated system of functions
  python main.py

  # run inference on webcam (15-20fps if there is 1 license plate in scene)
  python webcam.py 

  # run inference on image
  python lp_image.py -i test_image/3.jpg

  # run LP_recognition.ipynb if you want to know how model work in each step
```

## Result
![Demo 1](result/image.jpg)

![Vid](result/video_1.gif)

## Vietnamese Plate Dataset

This repo uses 2 sets of data for 2 stage of license plate recognition problem:

- [License Plate Detection Dataset](https://drive.google.com/drive/folders/1vlxqJHJzv44X6ECtxH2-FFNbcBc9DIth?usp=sharing)
- [Character Detection Dataset](https://drive.google.com/drive/folders/1wtL4to1LKBO1fBVJEWkYHSun5yh9HRho?usp=sharing)

Thanks [Mì Ai](https://www.miai.vn/thu-vien-mi-ai/) and [winter2897](https://github.com/winter2897/Real-time-Auto-License-Plate-Recognition-with-Jetson-Nano/blob/main/doc/dataset.md) for sharing a part in this dataset.

(new) Thanks [trungdinh22](https://github.com/trungdinh22) for sharing this project.

## Training

**Training code for Yolov5:**

Use code in ./training folder
```bash
  training/Plate_detection.ipynb     #for LP_Detection
  training/Letter_detection.ipynb    #for Letter_detection
```
