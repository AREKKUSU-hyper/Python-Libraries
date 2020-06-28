import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-5,5,10)
y1=2*x+1
y2=x**2
# plt.figure()
# plt.plot(x,y1,linewidth=1.0,linestyle=":") # plot展示

# 使用plt.figure定义一个图像窗口：编号为3；大小为(8, 5).
plt.figure(num=3,figsize=(8,5)) #原默認fig.照順序1,2,3...排列
plt.plot(x,y2)
plt.plot(x,y1,color="purple",linewidth=10.0,linestyle="--") # 曲线的类型为虚线

# set x limits
plt.xlim((-1,2)) # 设置x坐标轴范围
plt.ylim((-2,3))
plt.xlabel("I am X") # 设置x坐标轴名称
plt.ylabel("I am Y")

# set new sticks
new_ticks=np.linspace(-1,2,5) # np.linspace定义范围以及个数：范围是(-1,2);个数是5
plt.xticks(new_ticks) # 重新设置x轴刻度
plt.yticks([-2,-1.8,-1,1.22,3],
           [r"$really\ bad$",r"$bad\ \alpha$",r"$normal$",r"$good$",r"$really\ good$"]) # y轴刻度及对应刻度的名称

# 移动 matplotlib 中 axis 坐标轴
# gca = get current axis
ax=plt.gca() # 获取当前坐标轴信息
# 拿掉右邊及上方的軸
ax.spines["right"].set_color("none") # 使用.spines设置边框 spines=圖的脊梁(四邊)
ax.spines["top"].set_color("none")
ax.xaxis.set_ticks_position("bottom") # 設置下方軸顯示 x坐標軸刻度数字或名称的位置 # 所有位置：top，bottom，both，default，none
ax.yaxis.set_ticks_position("left")
ax.spines["bottom"].set_position(('data', 0)) # 使用.set_position设置边框位置(下方軸在y=0位置)
ax.spines["left"].set_position(('data', 0)) # 位置所有属性：outward，axes，data
# ax.spines["left"].set_position(('axes', 0.66)) # axes是指定位至軸百分之多少，EX:0.1=10%的位置
plt.show()