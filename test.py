from matplotlib import pyplot as plt
import numpy as np
import torch
data1 = torch.from_numpy(np.load('/Users/marc-antoine/Desktop/374575/0/arch0.npy'))[:, None, None]
data2 = torch.from_numpy(np.load('/Users/marc-antoine/Desktop/374575/0/arch1.npy'))
data3 = torch.from_numpy(np.load('/Users/marc-antoine/Desktop/374575/0/arch2.npy'))
a = torch.rand(3, 5)
b = torch.rand(3, 5)
print(torch.max(a))
# plt.hist(data, bins=20)
# plt.show()
# plt.scatter(np.arange(len(data)), data, s=0.5)
# plt.show()
# plt.hist(2/(1+np.exp(-data)), bins=20)
# plt.show()
