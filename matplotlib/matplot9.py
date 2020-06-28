import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
ax=Axes3D(fig) # 在图像窗口上添加3D坐标轴

# 给进 X 和 Y 值，并将 X 和 Y 编织成栅格。
x=np.arange(-4,4,0.25)
y=np.arange(-4,4,0.25)
X,Y=np.meshgrid(x,y)
R=np.sqrt(X**2+Y**2) # square root calculations 平方根計算
Z=np.sin(R) # height value

ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap("rainbow")) # plot 3D 图像 # 畫在ax上面 # cmap=plt.cm.rainbow
# rstride 和 cstride 分别代表 row 和 column 的跨度。

ax.contourf(X,Y,Z,zdir="z",offset=-2,cmap="rainbow") # 如果 zdir 选择了x，那么效果将会是对于 XZ 平面的投影。offset選擇要投影到哪。
ax.set_zlim(-2,2)

plt.show()