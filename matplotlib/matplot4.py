import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)
y=0.1*x
plt.figure()
plt.plot(x,y,linewidth=10,zorder=1,color="darkblue") # 设置 zorder 给 plot 在 z 轴方向排序。zorder越大，相当于画上去的越晚，也就在上面了。
plt.ylim(-2,2)
ax=plt.gca()
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
ax.spines["bottom"].set_position(("data",0))
ax.spines["left"].set_position(("data",0))

for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(12)                             # 重新调节字体大小
    label.set_bbox(dict(facecolor="white",             # facecolor调节box前景色 
                    edgecolor="none",                  # edgecolor设置边框
                    zorder=2,
                    alpha=0.5))                        # alpha设置透明度，亦可用於plot中


plt.show()