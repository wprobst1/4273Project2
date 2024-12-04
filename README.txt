4273 Project 2 Group 1 - Object Recognition Using YOLOv5

------------------------Dependencies----------------------------------------------
The YOLO model is dependent on the following packages:
gitpython>=3.1.30
matplotlib>=3.3
numpy>=1.23.5
opencv-python>=4.1.1
pillow>=10.3.0
psutil
PyYAML>=5.3.1
requests>=2.32.2
scipy>=1.4.1
thop>=0.1.1
torch>=1.8.0
torchvision>=0.9.0
tqdm>=4.66.3
ultralytics>=8.2.34

------------------------Installation----------------------------------------------
The following commands comprise the installation procedure of the model
git clone https://github.com/wprobst1/4273Project2
cd 4273Project2
pip install -r requirements.txt

---------------------------Usage--------------------------------------------------
To use the model for object detection, use the command:
python detect.py --source 0 #for use with web camera
python detect.py --source "path to .mp4 source" #for use with video input
Add --conf_thres float to adjust the sensitivity of the model when drawing boxes
Add --iou_thres float to adjust intersection sensitivity of objects in the frame
Add --view_img to see the output in real time from a .mp4

--------------------------Credits-------------------------------------------------
The base model was sourced from Ultralytics at https://github.com/ultralytics/yolov5
The training and validation data was sourced from Roboflow at
@misc{
                            pikachu-nmdik_dataset,
                            title = { Pikachu Dataset },
                            type = { Open Source Dataset },
                            author = { Pikachu },
                            howpublished = { \url{ https://universe.roboflow.com/pikachu-9uv9m/pikachu-nmdik } },
                            url = { https://universe.roboflow.com/pikachu-9uv9m/pikachu-nmdik },
                            journal = { Roboflow Universe },
                            publisher = { Roboflow },
                            year = { 2024 },
                            month = { jul },
                            note = { visited on 2024-12-03 },
                            }
@misc{
                            drones4_dataset,
                            title = { Drones4 Dataset },
                            type = { Open Source Dataset },
                            author = { Ivonne },
                            howpublished = { \url{ https://universe.roboflow.com/ivonne/drones4 } },
                            url = { https://universe.roboflow.com/ivonne/drones4 },
                            journal = { Roboflow Universe },
                            publisher = { Roboflow },
                            year = { 2023 },
                            month = { feb },
                            note = { visited on 2024-12-03 },
                            }
@misc{
                            dog-uxste_dataset,
                            title = { DOG Dataset },
                            type = { Open Source Dataset },
                            author = { Max },
                            howpublished = { \url{ https://universe.roboflow.com/max-evo5q/dog-uxste } },
                            url = { https://universe.roboflow.com/max-evo5q/dog-uxste },
                            journal = { Roboflow Universe },
                            publisher = { Roboflow },
                            year = { 2024 },
                            month = { may },
                            note = { visited on 2024-12-03 },
                            }
@misc{
                            catdetection-gy4yk_dataset,
                            title = { catdetection Dataset },
                            type = { Open Source Dataset },
                            author = { qb d },
                            howpublished = { \url{ https://universe.roboflow.com/qb-d/catdetection-gy4yk } },
                            url = { https://universe.roboflow.com/qb-d/catdetection-gy4yk },
                            journal = { Roboflow Universe },
                            publisher = { Roboflow },
                            year = { 2024 },
                            month = { may },
                            note = { visited on 2024-12-03 },
                            }
@misc{
                            people-counting-oh6y8_dataset,
                            title = { People Counting Dataset },
                            type = { Open Source Dataset },
                            author = { CONTADOR },
                            howpublished = { \url{ https://universe.roboflow.com/contador/people-counting-oh6y8 } },
                            url = { https://universe.roboflow.com/contador/people-counting-oh6y8 },
                            journal = { Roboflow Universe },
                            publisher = { Roboflow },
                            year = { 2024 },
                            month = { apr },
                            note = { visited on 2024-12-03 },
                            }