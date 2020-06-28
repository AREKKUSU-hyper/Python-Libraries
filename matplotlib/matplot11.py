import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
###############################################################################
# method 1: subplot2grid
plt.figure(num=1)
# subplot2grid(shape(图像窗口分成幾行幾列), loc(起始點), rowspan=默認值1, colspan=默認值1) 
ax1=plt.subplot2grid((3,3),(0,0),rowspan=1,colspan=3) # colspan表示列的跨度, rowspan表示行的跨度
ax1.plot([1,2],[1,2]) # 在ax1上plot
ax1.set_title("ax1_title")

ax2=plt.subplot2grid((3,3),(1,0),colspan=2)
ax3=plt.subplot2grid((3,3),(1,2),rowspan=2)
ax4=plt.subplot2grid((3,3),(2,0))
ax5=plt.subplot2grid((3,3),(2,1))

ax4.scatter([1,2],[2,2])
ax4.set_xlabel("ax4_x")
ax4.set_ylabel("ax4_y")
plt.tight_layout() # 自动调整子图参数，使之填充整个图像区域。仅仅检查坐标轴标签、刻度标签以及标题的部分。
###############################################################################
# method 2: gridspec
plt.figure(num=2)         # 使用plt.figure()创建一个图像窗口
gs=gridspec.GridSpec(3,3) # 使用gridspec.GridSpec将整个图像窗口分成3行3列
ax6=plt.subplot(gs[0,:])  # 表示这个图占第0行和所有列
ax7=plt.subplot(gs[1,:2])
ax8=plt.subplot(gs[1:,2])
ax9=plt.subplot(gs[-1,0])
ax10=plt.subplot(gs[-1,-2]) # 表示这个图占倒数第1行和倒数第2列
plt.tight_layout()

###############################################################################
# # method 3: subplots (easy to define structure)
f, ((ax11,ax12),(ax21,ax22))=plt.subplots(2,2,sharex=True,sharey=True) # 表示第1行从左至右依次放ax11和ax12, 第2行从左至右依次放ax21和ax22
ax11.scatter([1,2],[1,2])
ax12.set_title("ax12_title")
plt.tight_layout()

plt.show()
