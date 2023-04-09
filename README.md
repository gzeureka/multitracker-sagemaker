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

## Two inference modes:
### Local Test
In this mode, track.py does people tracking on an local file and gives output (mp4, json) in ./runs/exp[last epoch] and visualize bounding boxes and tracks. First, install requirements.
```
pip install -r requirements.txt
```
then start local inference
```
python track.py --local-mode  --show-vid  --source abc.mp4
```
for multiple camera from video file inference
```
python track.py --local-mode  --show-vid --save-vid --use-local-json-file --save-to-numpy-sample  --source ./local_test_2.json
```
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
