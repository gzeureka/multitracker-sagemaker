# Multi-Camera Tracking for Yolov5 + ByteTrack, with S3 exporting support

### config.yaml
config.yaml file notes the configurations for reid on cloud, including [TBD]

## Two inference modes:
### Local Test
In this mode, track.py does people tracking on an local file and gives output (mp4, json) in ./runs/exp[last epoch] and visualize bounding boxes and tracks
```
python track.py --local-mode  --show-vid  --source abc.mp4
```
### Sagemaker Notebook Server
Sagemaker Notebook Server mode is for deployment on sagemaker, and read & write files to S3. For further instruction, plz send us a ticket for more details. The follow should be run in order to start the server mode
```
python track.py
```
Send requests to process files on S3

### TO-DOs
1. terminate tracks that are still alive when video stops