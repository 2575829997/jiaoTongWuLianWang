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
#温度12  位移45  应变12
f = Figure(figsize=(5, 4), dpi=100)
f_plot = f.add_subplot(111)
filename=r"E:\qq下载的\交通物联网\naodu625_strain_temp.xls"
data = xlrd.open_workbook(filename)
sheet_name='温度'
sh = data.sheet_by_name(sheet_name)
def draw_T(col):  
    f_plot.clear()
    print(col)
    test_TEM = int(col)-1
    if test_TEM<13:
        col_test_TEM = sh.col_values(test_TEM,start_rowx=1) #从第一排开始取test-TEW这列
        x=np.arange(0,1078,1)
        y=np.array(col_test_TEM)  
        print(y)                             
        f_plot.set(title='temprature_self',xlabel='time  /10min',ylabel='temprature')
        f_plot.plot(x,y)                                                                
    canvs.draw() 


def draw_D(col):
    f_plot.clear()
    test_VD = int(col)-1
    if test_VD<46:
        sheet_name='应变'
        sh = data.sheet_by_name(sheet_name)
        col_test_VD = sh.col_values(test_VD,start_rowx=1)
        x=np.arange(0,1078,1)
        y=np.array(col_test_VD)
        print(y)
        f_plot.set(title='ver_d_self',
                    xlabel='time  /10min',ylabel='ver_d')
        f_plot.plot(x,y)
        canvs.draw()
def draw_Y(col):
    f_plot.clear()
    test_YB = int(col)-1
    if test_YB<13:
        sheet_name='挠度'
        sh_y= data.sheet_by_name(sheet_name)
        col_test_YB = sh_y.col_values(test_YB,start_rowx=1)
        x=np.arange(0,1078,1)
        y=np.array(col_test_YB)
        print(y)
        f_plot.set(title='YB_self',
                    xlabel='time  /10min',ylabel='YingBian')
        f_plot.plot(x,y)
    canvs.draw()
def draw_data():
    root2 = tkinter.Toplevel()
    root2.title('数据可视化（周期估算）')
    root2.geometry("800x850+650+100")   #窗口大小和窗口位置
    global canvs 
    canvs=FigureCanvasTkAgg(f, root2)
    canvs.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    ft1 = tkFont.Font(family='Fixdsys', size=15, weight=tkFont.BOLD)
    # tkinter.Button(root2, text='pic2', command=draw_picture2).pack()
    # tkinter.Button(root2, text='pic3', command=draw_picture3).pack()
    L1 = tkinter.Label(root2, text="选择温度(最多到12列)",font=ft1)
    L1.pack(fill='both')

    var1=StringVar()
    E11 = tkinter.Entry(root2, bd =5, textvariable=var1)
    E11.pack(fill='both')
    B1 = tkinter.Button(root2, text ="选择测试点", command = lambda:draw_T(var1.get()),bg = 'green',font=ft1)
    B1.pack(fill='both')
    L1 = tkinter.Label(root2, text="-------------------------------------",font=ft1)
    L1.pack(fill='both')

    L1 = tkinter.Label(root2, text="选择位移(最多到45列)",font=ft1)
    L1.pack(fill='both')
    var2=StringVar()
    E12 = tkinter.Entry(root2, bd =5,textvariable=var2)
    E12.pack(fill='both')
    B1 = tkinter.Button(root2, text ="选择测试点", command = lambda:draw_D(var2.get()),bg = 'green',font=ft1)
    B1.pack(fill='both')
    L1 = tkinter.Label(root2, text="-------------------------------------",font=ft1)
    L1.pack(fill='both')

    L1 = tkinter.Label(root2, text="选择应变(最多到12列)",font=ft1)
    L1.pack(fill='both')
    var3=StringVar()

    E13 = tkinter.Entry(root2, bd =5,textvariable=var3)
    E13.pack(fill='both')
    B1 = tkinter.Button(root2, text ="选择测试点",  command = lambda:draw_Y(var3.get()),bg = 'green',font=ft1)
    B1.pack(fill='both')

  

    root2.mainloop()