import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.figure(num=3,figsize=(8,5))

plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel("I am X")
plt.ylabel("I am Y")

new_ticks=np.linspace(-1,2,5) # np.linspace定义范围以及个数：范围是(-1,2);个数是5
plt.xticks(new_ticks) # 重新设置x轴刻度
plt.yticks([-2,-1.8,-1,1.22,3],
           ["really bad","bad","normal","good","really good"])

# set line styles
l2,=plt.plot(x,y2,label="parabola")
l1,=plt.plot(x,y1,color="purple",linewidth=1.0,linestyle="--",label="linear line")
# plt.legend(loc="upper right") # 图例 legend 显示的信息来自于上面代码中的 label
# 如想单独修改之前的 label 信息，可以在 plt.legend()输入更多参数，上面先用变量 l1 和 l2 存储
plt.legend(handles=[l1,l2],labels=["this is L1","this is L2"],loc="best") # 上面l1, l2,要以逗号结尾, 因为plt.plot() 返回的是一个列表.
# 其中’loc’参数有多种，’best’表示自动分配最佳位置
#  'best' : 0,          
#  'upper right'  : 1,
#  'upper left'   : 2,
#  'lower left'   : 3,
#  'lower right'  : 4,
#  'right'        : 5,
#  'center left'  : 6,
#  'center right' : 7,
#  'lower center' : 8,
#  'upper center' : 9,
#  'center'       : 10,

plt.show()