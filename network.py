from PIL import Image
import torch
from torchvision import models
from torchvision import transforms
import torch.nn as nn


def get_prediction(path):
    model = models.resnet18(pretrained=True)
    num_features = model.fc.in_features
    last_layer = nn.Linear(num_features, 2)
    model.fc = last_layer

    model.load_state_dict(torch.load('models/Adam_step_5_20_dop_0_937', map_location='cpu'))
    model = model.to("cpu")
    model.eval()

    image = Image.open(path)

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])

    image = transform(image)
    image = image.unsqueeze(0)
    _, prediction = torch.max(model(image), 1)
    if prediction[0].item() == 1:
        return True
    else:
        return False
