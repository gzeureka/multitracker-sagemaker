import os
import sys
from pathlib import Path
import torchvision
import torch

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # yolov5 strongsort root directory
WEIGHTS = ROOT / 'weights'

if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
if str(ROOT / 'yolov5') not in sys.path:
    sys.path.append(str(ROOT / 'yolov5'))  # add yolov5 ROOT to PATH
if str(ROOT / 'trackers' / 'strong_sort') not in sys.path:
    sys.path.append(str(ROOT / 'trackers' / 'strong_sort'))  # add strong_sort ROOT to PATH

ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

from yolov5.models.common import DetectMultiBackend
from yolov5.utils.torch_utils import select_device

yolo_weights = ['./weights/yolov5m.pt']

dnn = False,  # use OpenCV DNN for ONNX inference
device = select_device('')
half = False  # use FP16 half-precision inference

print(f'Loading yolo model from {yolo_weights}')
model = DetectMultiBackend(yolo_weights, device=device, dnn=dnn, data=None, fp16=half)
stride, names, pt = model.stride, model.names, model.pt

# Set the model to evaluation mode
model.eval()
# Create a random input tensor of shape (1, 3, 640, 640)
inp = torch.rand(1, 3, 640, 640)
# Trace the model using the TorchScript compiler
model_trace = torch.jit.trace(model, inp)

# Save the traced model to a file with the .pth extension
model_file = 'model.pth'
print(f'Saving model to {model_file}')
model_trace.save(model_file)

# Save as a compressed tar file
import tarfile
tar_gz_file = 'model.tar.gz'
print(f'Saving tar.gz file {tar_gz_file}')
with tarfile.open(tar_gz_file, 'w:gz') as f:
    f.add(model_file)
f.close()