#學習創建窗口菜單欄，包括多個下拉菜單及子菜單。
import tkinter as tk

root  = tk.Tk()
root.title("學習Menubar")
root.geometry('400x400')

label1 = tk.Label(root,text='',bg='lightyellow',width=40)
label1.pack()

#在root窗口創建一個菜單欄組件
menubar = tk.Menu(root)

#1.1在menubar上再創建一個菜單欄組件
filemenu = tk.Menu(menubar,tearoff = 0)

#1.2按鈕'file'下的按鈕動作，改變label1的顯示
def new_files():
    label1.config(text='新建',width=30)

def save_files():
    label1.config(text='保存',bg='darkgreen')

def open_files():
    label1.config(text='打開',bg='lightgreen')

def press_view():
    label1.config(text='功能正在完善')

def submenu_view():
    label1.config(text='子菜單')

#1.3將"file"按鈕添加在filemenu上
menubar.add_cascade(label = 'file',menu = filemenu)

#1.4添加file下拉菜單的按鈕，並增加點擊動作.“命名按鈕+按鈕動作”
filemenu.add_command(label='新建',command = new_files)
filemenu.add_command(label='保存',command = save_files)
filemenu.add_command(label='打開',command = open_files)
filemenu.add_separator()
filemenu.add_command(label='Exit',command = root.quit)#root.exit也行

#2.在menubar上創建第二個菜單欄組件
editmenu = tk.Menu(menubar,tearoff = 0)
menubar.add_cascade(label = '編輯',menu = editmenu)
editmenu.add_command(label='COPY',command = press_view)
editmenu.add_command(label='PASTE',command = press_view)
editmenu.add_command(label='CUT',command = press_view)
editmenu.add_command(label='DELETE',command = press_view)

#3.創建filemenu下拉菜單的子菜單
submenu = tk.Menu(filemenu)
filemenu.add_cascade(label = 'Import',menu = submenu,underline = 0)
submenu.add_command(label='Submenu1',command = submenu_view)

#將生成好的menubar更新至root窗口
root.config(menu = menubar)

root.mainloop() 