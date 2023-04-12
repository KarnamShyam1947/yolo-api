# converting into onxx format

import torch
import torch.onnx
import torchvision
import torchvision.models as models
import sys
 
onnx_model_path = "yolo_model/"
 
# https://pytorch.org/hub/pytorch_vision_densenet/
model = torch.load('yolo_model/efficientdet-d2_0_0.pth',  map_location=torch.device('cpu'))
 
# set the model to inference mode
# model.eval()
 
# Create some sample input in the shape this model expects 
# This is needed because the convertion forward pass the network once 
dummy_input = torch.randn(1, 3, 224, 224)

torch.onnx.export(model, dummy_input, onnx_model_path, verbose=True)