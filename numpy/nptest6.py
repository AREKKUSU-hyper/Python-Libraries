import numpy as np
A=np.array([1,1,1])
# B=np.array([2,2,2])

A=A[:,np.newaxis]
print(A.shape)
B=np.array([2,2,2])[:,np.newaxis]
C=np.hstack((A,B))
D=np.vstack((A,B))
print(C)
print(C.shape, D.shape)
E1=np.hstack((A,A,B,B))
E=np.concatenate((A,A,B,B),axis=1)
print(E)
print(E1)
