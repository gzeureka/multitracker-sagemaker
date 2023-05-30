import torchvision
import torch
from yolov5.models.common import DetectMultiBackend
from yolov5.utils.torch_utils import select_device

yolo_weights = ['./weights/yolov5m.pt']

dnn = False,  # use OpenCV DNN for ONNX inference
device = select_device('')
half = False  # use FP16 half-precision inference

print(f'loading yolo model from {yolo_weights}')
model = DetectMultiBackend(yolo_weights, device=device, dnn=dnn, data=None, fp16=half)
stride, names, pt = model.stride, model.names, model.pt

# model = torchvision.models.resnet18(pretrained=True)
model.eval()
inp = torch.rand(1, 3, 640, 640)
model_trace = torch.jit.trace(model, inp)

# Save your model. The following code saves it with the .pth file extension
model_trace.save('model.pth')

# Save as a compressed tar file
import tarfile
with tarfile.open('model.tar.gz', 'w:gz') as f:
    f.add('model.pth')
f.close()