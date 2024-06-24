import torch
from torch import nn


class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        total = torch.sum(exp_x, dim=0, keepdim=False)
        return exp_x / total
    
data = torch.Tensor([1, 2, 3])
softmax = MySoftmax()
output = softmax(data)
print(output)


class MySoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        c,_ = torch.max(x, dim=0, keepdim=True)
        exp_x = torch.exp(x - c)
        total = torch.sum(exp_x, dim=0, keepdim=False)
        return exp_x / total

softmax_stable = MySoftmaxStable()
output_2 = softmax_stable(data)
print(output)