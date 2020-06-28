import tkinter as tk
window=tk.Tk()
window.title("QQ")
window.geometry("200x200")

l=tk.Label(window,text="",bg="yellow")
l.pack()

counter=0
def do_job():
    global counter
    l.config(text="do "+str(counter))
    counter+=1

menubar=tk.Menu(window) # 创建一个菜单栏，在窗口的上方
filemenu=tk.Menu(menubar,tearoff=0) # 定义一个空菜单单元。tearoff若设置为1这个菜单是可以独立出来的，0的话就不可以独立出来。
menubar.add_cascade(label="File",menu=filemenu) # 将上面定义的空菜单命名为`File`，放在菜单栏中
# 在`File`中加入小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
filemenu.add_cascade(label="New",command=do_job)
filemenu.add_cascade(label="Open",command=do_job)
filemenu.add_cascade(label="Save",command=do_job)
filemenu.add_separator() # 加一条分割线
filemenu.add_cascade(label="Exit",command=window.quit) # tk內建的關閉命令操作

editmenu=tk.Menu(menubar,tearoff=0) 
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_cascade(label="Cut",command=do_job)
editmenu.add_cascade(label="Copy",command=do_job)
editmenu.add_cascade(label="Paste",command=do_job)

submenu=tk.Menu(filemenu,tearoff=0) # 再在`File`上创建一个空的菜单
filemenu.add_cascade(label="Import",menu=submenu,underline=0) # 给`submenu`命名为`Import`。 underline:菜单調用的快捷鍵
submenu.add_cascade(label="submenu_1",command=do_job)

window.config(menu=menubar) # 把window的menu參數定為menubar，即把上面做的menubar放上QQwindow

window.mainloop()
