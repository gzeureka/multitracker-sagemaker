# Multi-Camera Tracking for Yolov5 + ByteTrack, with S3 exporting support

## modification for HMS

### config.yaml
config.yaml file notes the configurations for reid on cloud, including [TBD]

```
# start tracking using bytetrack and osnet weights, on rtmp cameras listed on local_test.txt
python track.py --classes 0 --source ./local_test.txt --tracking-method bytetrack --reid-weights osnet_x0_25_market1501.pt --vid-stride 20

# start tracking using bytetrack and osnet weights, on rtmp cameras listed on cam_list.txt
python track.py --classes 0 --source ./cam_list.txt --tracking-method bytetrack --reid-weights osnet_x0_25_market1501.pt --vid-stride 20

# start tracking using bytetrack and osnet weights using connected front camera
python track.py --classes 0 --source 0 --tracking-method bytetrack --reid-weights osnet_x0_25_market1501.pt --vid-stride 20
```