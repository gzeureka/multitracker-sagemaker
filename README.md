# Multi-Camera Tracking for Yolov5 + ByteTrack, with S3 exporting support
## Features:
This repo is a reorganized version for people tracking, based on Yolov5 + ByteTrack, features currently supported are the following:
1. multiple real-time streams / multple video files / local cameras inference support
2. detail export for each track (track_id, best_image in base64, large_image in base64, start_time, end_time, trajectory, camera_id in coordinates, etc.)
3. Closure of unfinished tracks support
4. Upload images, trajectory info to S3 support
5. Visualization enhanced - support trajectory visualization

### config.yaml
config.yaml file notes the configurations for reid on cloud, including [TBD]


## Start an EC2 instance running Ubuntu in your aws account using the following CloudFormation Template
https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/template?stackName=arm-ec2-instance&templateURL=https://eric-panorama-test-utility.s3.amazonaws.com/test-utility-env-setup/ec2-instance-panorama.yml

### clone this repo to your EC2 instance

## Install requirements
```
# Install pyenv
curl https://pyenv.run | bash

# Notice: use Python 3.10.11. Python 3.11 doesn't work
# Use pyenv to install Python 3.10.11 and create a virtualenv for this project
pyenv install 3.10.11
pyenv virtualenv 3.10.11 multitracker-sagemaker

# Clone this repository, change current directory to multitracker-sagemaker, then run:
pyenv local multitracker-sagemaker

# Install packages
pip install Cython
# Install numpy. Notice: numpy 1.18.5 doesn't work, numpy 1.24.0 doesn't work
pip install numpy==1.23.5
pip install scikit-build
pip install flask

# Change current directory to multitracker-sagemaker
pip install -r requirements.txt
```

### Enable X11Forwaring for Ubuntu
refer to https://wiki.archlinux.org/title/OpenSSH#X11_forwarding
```
sudo apt-get install xorg
```

### (Optional)If you are using macOS ssh to your Ubuntu, you need to install xQuartz on macOS
```brew install --cask xquartz```
Then run XQuartz app on macOS.

Open a terminal, run
```
export DISPLAY=:0
ssh -X -i "PATH-TO-YOUR-PEM-FILE" ubuntu@YOUR-EC2-IP-ADDRESS

```

## Inference Modes:
### Single Source Test
Track.py does people tracking on an local file and gives output (mp4, json) in ./runs/exp[last epoch] and visualize bounding boxes and tracks. Start local inference on one file:
```
python track.py --local-mode  --show-vid  --source abc.mp4
```
### Multiple Source Test
for multiple camera from video file inference, edit source json file, specify whether it is video_file or stream 
```
python track.py --local-mode  --show-vid --save-vid --use-local-json-file --save-to-numpy-sample  --source ./local_test_2.json
```
### Local Camera Test
for single local camera (mac cameras tested) inference
```
python track.py --local-mode --use-local-camera --show-vid --save-vid --save-to-numpy-sample
```
### Sagemaker Notebook Server
Sagemaker Notebook Server mode is for deployment on sagemaker, and read & write files to S3. For further instruction, plz send us a ticket for more details. The follow should be run in order to start the server mode
```
python track.py
```
Send requests to process files on S3

### TO-DOs
None
