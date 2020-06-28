import tkinter as tk
# 窗口主体框架
window=tk.Tk()
window.title("my window")
window.geometry("800x600")

# 窗口内容（窗口上的控件）
e=tk.Entry(window,show=None)
# e=tk.Entry(window,show="*") # 创建输入框entry，用户输入任何内容都显示为*
e.pack()

def insert_point():
    var=e.get()
    t.insert("insert",var) # 插入於點擊的位置
def insert_end():
    var=e.get()
    t.insert("end",var) # 插入於文本尾部
def insert_1_1():
    var=e.get()
    t.insert(1.0,var) # 插入於特定位置

b1=tk.Button(window,text="insert by point",width=15,height=2,command=insert_point)
b1.pack()
b2=tk.Button(window,text="insert at end",command=insert_end) # 寬高為預設
b2.pack()
b3=tk.Button(window,text="insert at 第一行第一列",command=insert_1_1)
b3.pack()

t=tk.Text(window,height=2) # 创建一个文本框
t.pack()

window.mainloop()
