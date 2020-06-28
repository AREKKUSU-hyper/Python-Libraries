import tkinter as tk
window=tk.Tk()
window.title("QQ window")
window.geometry("400x400")

var1=tk.StringVar()
l=tk.Label(window,textvariable=var1,bg="yellow",font=("Times New Roman",12),width=10)
l.pack()

def print_selection():
    value=lb.get(lb.curselection())  # 获取当前选中的文本
    var1.set(value) # 为label设置值

b=tk.Button(window,text="print selection",width=15,height=2,command=print_selection)
b.pack()

# 创建一个Listbox和变量var2，并将var2的值赋给Listbox
var2=tk.StringVar()
var2.set((11,22,33,44))
lb=tk.Listbox(window,listvariable=var2)

#创建一个list并将值循环添加到Listbox控件中
list_items=[1,2,3,4]
for item in list_items:
    lb.insert("end",item) # 从最后一个位置开始加入值
lb.insert(1,"first")  # 在第一个位置加入'first'字符
lb.insert(2,"second")
lb.delete(2)  # 删除第二个位置的字符
lb.delete(3)
lb.pack()

window.mainloop()



