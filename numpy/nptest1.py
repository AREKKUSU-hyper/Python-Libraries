import numpy as np
# array=np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9]])
array=np.array([[1,2,3],[4,5,6],[7,8,9]])

print(array)
print("number of dimension: ",array.ndim)
print("shape: ",array.shape)
print("size: ",array.size)

import matplotlib.pyplot as plt
labels = ['SGD', 'Momentum', 'RMSprop', 'Adam']
losses_his = [[1,2,3], [], [], [6,55,100,5]] 
for i, l_his in enumerate(losses_his):
    plt.plot(l_his, label=labels[i])
plt.legend(loc='best')
plt.xlabel('Steps')
plt.ylabel('Loss')
plt.show()