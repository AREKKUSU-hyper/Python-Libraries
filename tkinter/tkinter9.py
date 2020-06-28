import tkinter as tk
window=tk.Tk()
window.title("QQ")
window.geometry("400x400")

tk.Label(window,text="on the QQ").pack()

frm=tk.Frame(window)
frm.pack()
frm_l=tk.Frame(frm)
frm_r=tk.Frame(frm)

# 控制小的`frm`部件在大的`frm`的相对位置
frm_l.pack(side="left")
frm_r.pack(side="right")

tk.Label(frm_l,text="on the left frame_No.1").pack()
tk.Label(frm_l,text="on the left frame_No.2").pack()
tk.Label(frm_r,text="on the right frame_No.1").pack()

window.mainloop()