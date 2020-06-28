import tkinter as tk
window=tk.Tk()
window.title("my window")
window.geometry("200x200")

l=tk.Label(window,text="empty",bg="yellow",width=20)
l.pack()

def print_selection(v): # 参数v即将滚动条定位的数据
    l.config(text="You have selected "+ v)

s=tk.Scale(window,label="try me",   # label是指scale部件名称
            from_=5,to=11,          # 参数从5到11，即滚动条最小值为5最大值为11
            orient=tk.HORIZONTAL,   # 滚动条的方向，HORIZONTAL橫向
            length=200,             # 参数length是指滚动条部件的长度。和其他部件width不同，width是以字符为单位，而length是像素为单位
            showvalue=0,            # 滚动条上方的显示。showvalue=0 or False，上方无显示；showvalue=1 or True，则会显示
            tickinterval=3,         # 坐标的间隔 5.00 8.00 11.00
            resolution=0.01,        # 0.01就是保留2位小数。如果保留一位就是resolution=0.1
            command=print_selection)# Scale帶有默認傳入值，故上方功能裡要定義參數。
s.pack()

window.mainloop()