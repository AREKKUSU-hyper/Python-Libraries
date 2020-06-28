import tkinter as tk
window=tk.Tk()
window.title("QQ")
window.geometry("400x400")
from tkinter import messagebox as mgb
    
def hit_me():
    # mgb.showinfo(title="Hi, it's QQ",message="HaHaHaHa") # 提示信息对话窗 # return 'ok'
    # mgb.showwarning(title="Hi, it's QQ",message="Nononono") # 提出警告对话窗 # return 'ok'
    # mgb.showerror(title="Hi, it's QQ",message="No!!never!") # 提出错误对话窗 # return 'ok'

    # A=mgb.askquestion(title="Hi, it's QQ",message="yes or no") # 询问选择对话窗 # return 'yes' , 'no' 
    # if A =="yes":                                              # 可利用返回值繼續編程
    #     print("QQ said yes")

    # print(mgb.askyesno(title="Hi, it's QQ",message="yes or no")) # return True, False
    # print(mgb.askretrycancel(title='Hi', message='retry or cancel')) # return True, False
    # print(mgb.askokcancel(title='Hi', message='ok or cancel')) # return True, False
    print(mgb.askyesnocancel(title="Hi", message="yes, no or cancel")) # return True, False, None

tk.Button(window,text="hit me",command=hit_me).pack()
window.mainloop()
