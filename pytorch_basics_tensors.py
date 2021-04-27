import torch
import numpy as np

#build a tensor directly from an array
data = [[7, 2],[35, 4]]
x_data = torch.tensor(data)

#build a tensor from NumPy 
np_array = np.array(data)
x_np = torch.from_numpy(np_array)


#shape can be used to build the multi-dimensional array or tensor -> (5,4,) means 5 main numbers and 4 sub numbers
shape = (5,4,)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

print(f"Random Tensor: \n {rand_tensor} \n")
print(f"Ones Tensor: \n {ones_tensor} \n")
print(f"Zeros Tensor: \n {zeros_tensor}")