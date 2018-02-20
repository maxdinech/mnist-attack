"""
Basic PyTorch functions
"""


import torch
from torch.autograd import Variable
import torchvision.models as models
import architectures


# Returns a Variable containing `tensor`, on the GPU if CUDA is available.
def to_Var(tensor, requires_grad=False):
    if torch.cuda.is_available():
        tensor = tensor.cuda()
    return Variable(tensor, requires_grad=requires_grad)


def load_architecture(model_name):
    model = getattr(architectures, model_name)()
    if torch.cuda.is_available():
        model = model.cuda()
    return model


def load_model(dataset, model_name):
    if dataset is not 'ImageNet':
        try:
            model = torch.load('../models/' + dataset + '/' + model_name + '.pt',
                               map_location=lambda storage, loc: storage)
            if torch.cuda.is_available():
                model = model.cuda()
            return model
        except FileNotFoundError:
            raise ValueError('No trained model found.')
    else:
        return getattr(models, model_name)(pretrained=True)
