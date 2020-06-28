import matplotlib.pyplot as plt
import numpy as np

n=1024 # data size
X=np.random.normal(0,1,n) # 常態分布數據組(平均数是0，方差为1) 
Y=np.random.normal(0,1,n) 
T=np.arctan2(Y,X) # for color value
plt.figure(num=1)
plt.scatter(X,Y,s=75,c=T,alpha=0.5)

plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))
plt.xticks(()) # ignore xticks
plt.yticks(()) # 隐藏y坐标轴

plt.figure(num=2)
plt.scatter(np.arange(5),np.arange(5))

plt.show()