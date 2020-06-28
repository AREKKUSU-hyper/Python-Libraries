import matplotlib.pyplot as plt

# 初始化figure
fig = plt.figure()

# 创建数据
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]
print(y[::-1])

# 大图
# 大图左下角的位置以及宽高
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8 # figure的百分比,10%的位置开始绘制,宽高是figure的80%
ax1=fig.add_axes([left, bottom, width, height])
ax1.plot(x,y,"r")
ax1.set_title("TITLE")
ax1.set_xlabel("x")
ax1.set_ylabel("y")

# 小圖 1
left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
ax2=fig.add_axes([left, bottom, width, height])
ax2.plot(y,x,"b")
ax2.set_title("inside_1")
ax2.set_xlabel("x")
ax2.set_ylabel("y")

# 小圖 2 (直接往plt里添加新的坐标系的方法)
plt.axes([.6, .2, 0.25, 0.25])
plt.plot(y[::-1],x,"g") # 对y进行了逆序处理
plt.title("inside_2")
plt.xlabel("x")
plt.ylabel("y")

plt.show()