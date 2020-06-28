import matplotlib.pyplot as plt
import numpy as np

# 等高线 数据集即三维点 (x,y) 和对应的高度值
def f(x,y):
    # the height function
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)
n=256
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)
# numpy.meshgrid()——生成网格点坐标矩阵
X,Y=np.meshgrid(x,y) # 在二维平面中将每一个x和每一个y分别对应起来，编织成栅格
# 坐标矩阵：横坐标矩阵XX中的每个元素，与纵坐标矩阵YY中对应位置元素，共同构成一个点的完整坐标。

# use plt.contourf to filling contours
plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot) # 8代表等高线的密集程度，这里被分为10个部分。如果是0，则图像被一分为二。

# use plt.contour to add contour lines
C=plt.contour(X,Y,f(X,Y),8,colors="black",linewidths=.5)

# adding label
plt.clabel(C,inline=True,fontsize=9) # inline控制是否将Label画在线里面

# 将坐标轴隐藏
plt.xticks(())
plt.yticks(())

plt.show()