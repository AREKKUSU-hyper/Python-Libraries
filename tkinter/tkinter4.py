import tkinter as tk
window=tk.Tk()
window.title("QQ window")
window.geometry("400x400")

var=tk.StringVar()
l=tk.Label(window,text="empty",bg="yellow",font=("Times New Roman",16),width=20)
l.pack()

def print_selection():
    l.config(text="You have selected "+var.get())

# Radiobutton 选择按钮
b1=tk.Radiobutton(window,text="Option A",
                variable=var,value="A", # 把value的值A放到变量var中，然后赋值给variable
                command=print_selection)
b1.pack()
b2=tk.Radiobutton(window,text="Option B",
                variable=var,value="B",
                command=print_selection)
b2.pack()
b3=tk.Radiobutton(window,text="Option C",
                variable=var,value="C",
                command=print_selection)
b3.pack()


window.mainloop()