import tkinter as tk
window=tk.Tk()
window.title("my window")
window.geometry("200x200")

l=tk.Label(window,text="empty",bg="yellow",width=20)
l.pack()

def print_selection():
    if (var1.get()==1) & (var2.get()==1):
        l.config(text="I love both")
    elif (var1.get()==1) & (var2.get()==0):
        l.config(text="I love only Python")
    elif (var1.get()==0) & (var2.get()==1):
        l.config(text="I love only C++")
    else:
        l.config(text="I do not love either")

var1=tk.IntVar()
var2=tk.IntVar()

c1=tk.Checkbutton(window,text="Python",variable=var1,onvalue=1,offvalue=0, 
                command=print_selection)
                # 选中这checkbutton，onvalue的值1就会放入var1， 然后var1将其赋值给参数variable
c2=tk.Checkbutton(window,text="C++",variable=var2,onvalue=1,offvalue=0,
                command=print_selection)
c1.pack()
c2.pack()

window.mainloop()