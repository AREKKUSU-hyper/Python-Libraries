import matplotlib.pyplot as plt
import numpy as np

n=12
X=np.arange(n)
Y1=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
Y2=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white') # 用facecolor设置主体颜色，edgecolor设置边框颜色
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')

for x,y in zip(X,Y1):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x,y+0.05, "%.2f" % y,ha="center",va="bottom") # 輸出浮點數時指定精度，保留到小數第2位。
for x,y in zip(X,Y2):
    plt.text(x,-y-0.05, "-%.2f" % y,ha="center",va="top")   # 横向居中对齐、纵向顶部对齐。

plt.xlim((-.5,n))
plt.ylim((-1.25,1.25))
plt.xticks(())
plt.yticks(())

plt.show()