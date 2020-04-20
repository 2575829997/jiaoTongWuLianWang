import os
import xlrd
from PIL import Image
from PIL import ImageTk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
import tkinter
from tkinter import StringVar
import tkinter.font as tkFont
import tkinter.messagebox #弹窗库
import dataVisual as dv
import crossCorrelation as cc
def show():
    a=E1.get()
    b=E1.get()
    a='1'
    b='1'
    if a== '1'and b == '1':
        str1 = tkinter.messagebox.showinfo(title='提示',message = '恭喜密码正确')
        if str1 == 'ok':
            root.destroy()
            root1 = tkinter.Tk()
            root1.title('桥梁监测信息关联分析可视化系统')
            root1.geometry("800x670+650+200")   #窗口大小和窗口位置
            canvas = tkinter.Canvas(root1, width = 800,height = 470)  
            image = Image.open(r"C:\Users/admin\Desktop\python\pdx.png") 
            global im #加上这句话就显示出照片 
            im = ImageTk.PhotoImage(image)  
            canvas.create_image(400,235,image = im)
            canvas.pack()
            tkinter.Button(root1, text = '****************▂▃▅▆▇▇▇▇数据可视化（周期估算）▇▇▇▇▆▅▃▂****************',
            font=12,height=2,
            command = dv.draw_data).pack(fill='both')
            tkinter.Button(root1, text = '****************▂▃▅▆▇▇▇▇选择互相关（相关系数）▇▇▇▇▆▅▃▂****************',
            font=12,height=2,
            command = cc.draw_each).pack(fill='both')
            tkinter.Button(root1, text = '****************▂▃▅▆▇▇▇▇选择自相关（自相关图）▇▇▇▇▆▅▃▂****************',
            font=12,height=2,
            command = dv.draw_data).pack(fill='both')
            tkinter.Button(root1, text = '****************▂▃▅▆▇▇▇▇各数据不同点间的互相关▇▇▇▇▆▅▃▂****************',
            font=12,height=2,
            command =dv.draw_data).pack(fill='both')
            root1.mainloop()
    else:
        string_a = '密码或账号错误 ，请重新输入！'
        tkinter.messagebox.showinfo(title='提示', message = string_a)
root = tkinter.Tk()
root.geometry("350x120+800+400")   #窗口大小和窗口位置
root.title('登陆')
tkinter.Label(root, text="随便输入都可以登录",font=20).grid(row=3, column=1)
tkinter.Label(root, text="账号：",font=20).grid(row=0, column=0)
tkinter.Label(root, font=20,text="密码：").grid(row=1, column=0)
E1 = tkinter.Entry(root, bd =5)
E1.grid(row=0, column=1)
E2 = tkinter.Entry(root, bd =5)
E2.grid(row=1, column=1)
tkinter.Button(root, text="登 陆", font=12,  width=10, command=show).grid(row=2, column=0)
tkinter.Button(root, text="注 册", font=12, width=10, command=show ).grid(row=2, column=1)
tkinter.Button(root, text="退 出", font=12, width=10, command=root.destroy).grid(row=2, column=2)
root.mainloop()