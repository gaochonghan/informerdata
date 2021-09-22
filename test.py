from modulefinder import Module

import torch
import torch.nn as nn
import torch.nn.functional as F
import os
import matplotlib.pyplot as plt
from data.data_loader import Dataset_ETT_hour
import time

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.L = nn.Linear(2, 4)
    def forward(self, x):
        return self.L(x)

m = MyModel()
for p in m.parameters():
    print(p)
    p.data.sub_(2, 3)
    print(p)
a = torch.ones(3, 4, 5) * 3
b = torch.ones(3, 4, 5) * 2
a.requires_grad = True
print(a.sub(b, b))
# data_set = Dataset_ETT_hour(
#             root_path="/Users/marc-antoine/Documents/Github/ETDataset/ETT-small",
#             data_path='ETTh1.csv',
#             flag='train',
#             size=[96, 48, 24],
#             features="M",
#             target='OT',
#             inverse=False,
#             timeenc=1,
#             freq='h',
#             cols=None
#         )
