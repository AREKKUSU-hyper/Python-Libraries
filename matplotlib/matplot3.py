import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)
y=2*x+1
plt.figure(num=1,figsize=(8,5))
plt.plot(x,y)
# plt.scatter(x,y) # plot出散點圖而非線

ax=plt.gca()
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
ax.spines["bottom"].set_position(("data",0))
ax.spines["left"].set_position(("data",0))

x0=1
y0=2*x0+1
plt.scatter(x0,y0,s=50,color="b") # set dot styles # plt.scatter([x0, ], [y0, ], s=50, color='b') 亦可
plt.plot([x0,x0],[y0,0],"k--",lw=2.5) # 画出一条垂直于x轴的虚线 # 'k--':黑色 虛線；lw：LineWidth

# 标注 method 1
plt.annotate(r'$2x+1=%s$' % y0, # 註釋文字的內容
            xy=(x0,y0), # 被註釋的座標點，二維元組形如(x,y)
            xycoords="data", # 被註釋點的座標系屬性，"data"(亦是預設值):以被註釋的座標點xy為參考
            xytext=(+30,-30), # 註釋文字的座標點，預設與xy相同
            textcoords="offset points", # 註釋文字的座標系屬性，預設與xycoords屬性值相同。'offset points'：相對於被註釋點xy的偏移量（單位是點）
            fontsize=16, # 字體大小
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2")) # 箭头类型的设置，dict（字典）型資料。arrowstyle：箭頭的樣式；connectionstyle：連線線的樣式。

# 标注 method 2
plt.text(-3.7,3,                                             # text的位置
        r"$Here\ is\ some\ text.\ \mu\ \sigma_i\ \delta_t$", # _表示下標i,t。
        fontdict={"size":16,"color":'r'})                    # fontdict设置文本字体。

plt.show()


