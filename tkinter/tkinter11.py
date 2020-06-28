# pack grid place 放置位置
import tkinter as tk
window=tk.Tk()
window.title("QQ")
window.geometry("400x400")

# pack
# tk.Label(window,text="北").pack(side="top")    # 上
# tk.Label(window,text="南").pack(side="bottom") # 下
# tk.Label(window,text="西").pack(side="left")   # 左
# tk.Label(window,text="東").pack(side="right")  # 右

# grid 方格 # grid就是用表格的形式定位的
for i in range(4):
    for j in range(3):
        tk.Label(window,text=2).grid(row=i,column=j,padx=20,pady=20) 
        # row为行，colum为列，padx就是单元格左右间距，pady就是单元格上下间距 
        # pad為外部擴展；ipad為內部擴展，
        # ipad 和 pad 的單位是畫素，而不是一個字元的寬度
        # ipadx：设置控件里面x方向空白区域大小
        # ipady：设置控件里面y方向空白区域大小
        # padx：设置控件周围x方向空白区域保留大小
        # pady：设置控件周围y方向空白区域保留大小

# place 给精确的坐标来定位
tk.Label(window,text=1).place(x=200,y=150,anchor="nw") # 锚定点(anchor)是西北角
                
window.mainloop()