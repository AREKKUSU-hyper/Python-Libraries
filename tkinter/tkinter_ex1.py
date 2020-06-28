import tkinter as tk
from tkinter import messagebox as mgb
import pickle
window=tk.Tk()
window.title("WELCOME TO QQ's PYTHON")
window.geometry("450x300")

# welcome image
canvas=tk.Canvas(window,height=200,width=500) # 创建画布
image_file=tk.PhotoImage(file="welcome.gif") # 加载图片文件
image=canvas.create_image(0,0,anchor="nw",image=image_file) # 将图片置于画布上
canvas.pack(side="top") # 放置画布（为上端）

# user information
tk.Label(window,text="Username: ").place(x=50,y=150) # 创建一个`label`名为`Username: `置于坐标（50,150）
tk.Label(window,text="Password: ").place(x=50,y=190)

var_user_name=tk.StringVar() # 定义变量
var_user_name.set("example@gmail.com") # 变量赋值'example@python.com'(設定預設值)
entry_user_name=tk.Entry(window,textvariable=var_user_name) # 创建一个`entry`，显示为变量`var_usr_name`
entry_user_name.place(x=160,y=150)

var_user_password=tk.StringVar()
entry_user_password=tk.Entry(window,textvariable=var_user_password,show="*") # `show`这个参数将输入的密码变为`***`的形式
entry_user_password.place(x=160,y=190)

# login and sign_up button
def usr_login():
    usr_name=var_user_name.get()
    usr_pwd=var_user_password.get() # 获取用户输入的`usr_name`和`usr_pwd`
    try: # 当我们第一次访问用户信息文件时是不存在的，所以这里设置异常捕获。
        with open("users_info.pickle",mode="rb") as usrs_file:
            usrs_info=pickle.load(usrs_file)
    except FileNotFoundError: 
        with open("users_info.pickle",mode="wb") as usrs_file:
            usrs_info={"admin":"admin"} # 管理员用户和密码写入，即用户名为`admin`密码为`admin`。
            pickle.dump(usrs_info,usrs_file)
    if usr_name in usrs_info:
        if usr_pwd==usrs_info[usr_name]: # 如果用户名和密码与文件中的匹配成功
            mgb.showinfo(title="WELCOME",message="How are you? "+usr_name)
        else:                            # 如果用户名匹配成功，而密码输入错误
            mgb.showerror(title="ERROR",message="Error, your password is wrong, please try again.")
    else:                                # 如果发现用户名不存在
        # 提示需不需要注册新用户 
        to_sign_up=mgb.askyesno(title="WELCOME",message="You have not signed up yet. Sign up today?")
        if to_sign_up:                   # 等同 if True:
            usr_sign_up()
def usr_sign_up():
    def sign_to_QQ_Python():
        # 获取我们注册时输入Entry框的信息
        nn=new_name.get()
        np=new_pwd.get()
        npf=new_pwd_confirm.get()        
        try:
            with open("users_info.pickle",mode="rb") as usrs_file: # 打开我们记录数据的文件，将注册信息读出
                exist_usrs_info=pickle.load(usrs_file)
        except FileNotFoundError: 
            with open("users_info.pickle",mode="wb") as usrs_file:
                exist_usrs_info={"admin":"admin"}
                pickle.dump(exist_usrs_info,usrs_file)
        if np != npf:                                   # 判断两次密码输入一致與否
            mgb.showerror(title="ERROR",message="Error, password and confirm password must be the same!")
        elif nn in exist_usrs_info:                     # 判断用户名是否已存在数据文件中
            mgb.showerror(title="ERROR",message="Error, the username has already been signed up!")
        else:                                           # 将注册输入的信息记录到文件当中，并提示注册成功
            exist_usrs_info[nn]=np
            with open("users_info.pickle",mode="wb") as usrs_file:
                pickle.dump(exist_usrs_info,usrs_file)
            mgb.showinfo(title="WELCOME",message="Hey "+nn+", you have successfully signed up!")
            window_sign_up.destroy()                    # 然后销毁窗口

    # 在主体窗口上创建一个注册窗口
    window_sign_up=tk.Toplevel(window)
    window_sign_up.title('Sign up window')
    window_sign_up.geometry("350x200")
    
    new_name=tk.StringVar()
    new_name.set("example@gmail.com") # 将最初显示定为"example@gmail.com"
    tk.Label(window_sign_up,text="Username: ").place(x=10,y=10)
    entry_new_name=tk.Entry(window_sign_up,textvariable=new_name) # 创建一个注册名的`entry`，变量为`new_name`
    entry_new_name.place(x=150,y=10)

    new_pwd=tk.StringVar()
    tk.Label(window_sign_up,text="Password: ").place(x=10,y=50)
    entry_new_pwd=tk.Entry(window_sign_up,textvariable=new_pwd,show="*")
    entry_new_pwd.place(x=150,y=50)

    new_pwd_confirm=tk.StringVar()
    tk.Label(window_sign_up,text="Confirm password: ").place(x=10,y=90)
    entry_new_pwd_confirm=tk.Entry(window_sign_up,textvariable=new_pwd_confirm,show="*")
    entry_new_pwd_confirm.place(x=150,y=90)

    btn_window_sign_up=tk.Button(window_sign_up,text="Sign up",command=sign_to_QQ_Python)
    btn_window_sign_up.place(x=150,y=130)

btn_login=tk.Button(window,text="Login",command=usr_login) # 定义一个`button`按钮，名为`Login`,触发命令为`usr_login`
btn_login.place(x=140,y=230)
btn_sign_up=tk.Button(window,text="Sign up",command=usr_sign_up)
btn_sign_up.place(x=240,y=230)

window.mainloop()