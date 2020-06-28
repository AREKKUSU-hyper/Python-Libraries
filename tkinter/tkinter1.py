import tkinter as tk
# 窗口主体框架 
window=tk.Tk()
window.title("my window")
window.geometry("800x600") # 寬度x高度; 設定視窗大小爲800*600
window.resizable(0, 0) #fix the size of window(將視窗的X,Y大小設定不可調整)

# 窗口内容
l=tk.Label(window,
        text="OMG!QQ!!大屁股!!!", # 标签的文字
        bg="purple", # 背景颜色
        font=("Times New Roman",18), # 字体和字体大小
        width=24, height=3) # 此處寬&高是以字符為單位
l.pack()  # 固定窗口位置
var=tk.StringVar() # 文字变量储存器
display=tk.Label(window,
        textvariable=var, # 使用 textvariable 替换 text, 因为这个可以变化
        bg="green",
        font=("Arial",12),
        width=15, height=2) # 此處寬&高是以字符為單位
display.pack()

on_hit=False # 默认初始状态为 False
def hit_me():
    global on_hit
    if on_hit==False:  # 从 False 状态变成 True 状态
        on_hit=True
        var.set("QQ hit me")  # 设置标签的文字
    else:              # 从 True 状态变成 False 状态
        on_hit=False
        var.set("")

b=tk.Button(window,
        text="hit me", # 显示在按钮上的文字
        width=20,height=2,
        command=hit_me) # 点击按钮時执行的命令
b.pack() # 按钮位置
window.mainloop()