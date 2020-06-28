import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

f, ax=plt.subplots()

x=np.arange(0,2*np.pi,0.01)
line,=ax.plot(x,np.sin(x)) # 0~2π的正弦曲线

def anime(i):
    line.set_ydata(np.sin(x+i/10))
    return line,

def init():
    line.set_ydata(np.sin(x))
    return line,

ani=animation.FuncAnimation(fig=f,func=anime,frames=100,init_func=init,interval=20,blit=True)

# 调用FuncAnimation函数生成动画。参数说明：
# fig 进行动画绘制的figure
# func 自定义动画函数
# frames 动画长度，一次循环包含的帧数
# init_func 自定义开始帧
# interval 更新频率，以ms计
# blit 选择更新所有点(False)，还是仅更新产生变化的点(True)

plt.show()

# 也可以将动画以mp4格式保存下来，但首先要保证你已经安装了ffmpeg 或者mencoder
# ani.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])