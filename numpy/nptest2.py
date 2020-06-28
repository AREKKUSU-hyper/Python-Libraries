import numpy as np
a=np.array([[2,23,4],
            [2,32,4]],dtype=np.int64) # np.float16
print(a.dtype)
print(a)

b=np.zeros((3,4)) # shape(行,列)
print(b)

b1=np.ones((3,4),dtype=np.float16) 
print(b1)

b2=np.empty((2,3)) 
print(b2)

c=np.arange(10,20,2)
print(c)

c1=np.arange(16).reshape(4,4)
print(c1)

d=np.linspace(0,10,5)
print(d)

d2=np.linspace(1,10,20).reshape(5,4)
print(d2)