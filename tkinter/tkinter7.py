import tkinter as tk
window=tk.Tk()
window.title("QQ")
window.geometry("600x800")

canvas=tk.Canvas(window,bg="grey",width=600,height=600)
canvas.pack()
image_file=tk.PhotoImage(file="C:\\Users\\ALEX\\Desktop\\資料暫存\\水印1.png") # 创造一个变量存放要讀取图片
pic=canvas.create_image(10,10,anchor="nw",image=image_file) # 参数10,10就是图片放入画布的坐标，anchor是图片的锚定点
x0,y0,x1,y1=300,100,400,300
line=canvas.create_line(x0,y0,x1,y1)
oval=canvas.create_oval(x0,y0,x1,y1,fill="red") # 填充色为`red`
arc=canvas.create_arc(x0+50,y0+100,x1+50,y1+100,start=0,extent=180) # 创建一个扇形，0度到180度
rect=canvas.create_rectangle(400,350,580,300+280) # 创建一个矩形

def moveit():
    canvas.move(pic,0,5) # 也就是横坐标移动0个单位，纵坐标移动5个单位
b=tk.Button(window,text="move down",command=moveit).pack() # pack()可不分行直接放在後面

window.mainloop()
