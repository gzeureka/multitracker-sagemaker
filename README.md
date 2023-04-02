# Multi-Camera Tracking for Yolov5 + ByteTrack, with S3 exporting support

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
for local multiple camera inference
```
python track.py --local-mode  --show-vid --save-vid --use-local-json-file --save-to-numpy-sample  --source ./local_test_2.json
```
### Sagemaker Notebook Server
Sagemaker Notebook Server mode is for deployment on sagemaker, and read & write files to S3. For further instruction, plz send us a ticket for more details. The follow should be run in order to start the server mode
```
python track.py
```
Send requests to process files on S3

### TO-DOs
1. terminate tracks that are still alive when video stops