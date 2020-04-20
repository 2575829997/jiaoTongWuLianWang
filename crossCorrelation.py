import os
import xlrd
from PIL import Image
import pandas as pd 
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
f = Figure(figsize=(5, 4), dpi=100)
f_plot = f.add_subplot(111)
filename=r"E:\qq下载的\交通物联网\naodu625_strain_temp.xls"
data = xlrd.open_workbook(filename)
sheet_name='温度'
sh = data.sheet_by_name(sheet_name)


def drawbar(corr_nm1):
    width = 0.35
    ind = np.arange(len(corr_nm1))  # the x locations for the groups
    f_plot.bar(ind - width/2, corr_nm1, width, color='SkyBlue', label='Men')
    canvs.draw()


#位移温度
def draw_D_T(col):
    f_plot.clear()
    test_VD1 =int(col)-1
    if test_VD1<13:
        sheet_name='温度'
        sh = data.sheet_by_name(sheet_name)
        col_test_VD1 = sh.col_values(test_VD1,start_rowx=1)#取指定列的温度
        s_test=pd.Series(col_test_VD1) #给这一列每一排前面标顺序012345
        corr_nm1 = []
        sheet_name='挠度'
        sh = data.sheet_by_name(sheet_name)
        for j in range(1,11):
            col3 = sh.col_values(j,start_rowx=1)
            s3=pd.Series(col3)
            corr_test=s_test.corr(s3) #corr,求相关系数的函数
            if corr_test<0:
                corr_nm1.append(-corr_test)
            else :
                corr_nm1.append(corr_test)
        f_plot.set(title='ver_d&temprature',xlabel='ver_d&temperature',ylabel='corr_num')
        drawbar(corr_nm1)

##位移应变
def draw_D_Y(col):
    f_plot.clear()
    test_VD2 = int(col)-1
    if test_VD2<13:
        sheet_name='应变'
        sh = data.sheet_by_name(sheet_name)
        col_test_VD2 = sh.col_values(test_VD2,start_rowx=1)
        s_test1=pd.Series(col_test_VD2)
        corr_nm2 = []
        sheet_name='挠度'
        sh = data.sheet_by_name(sheet_name)
        for i in range(0,12):
            col_y = sh.col_values(i,start_rowx=1)
            s_y=pd.Series(col_y)
            corr_test1=s_test1.corr(s_y) 
            if corr_test1<0:
                corr_nm2.append(-corr_test1)
            else :
                corr_nm2.append(corr_test1)
        f_plot.set(title='ver_d&YB',xlabel='ver_d&YB',ylabel='corr_num')
        drawbar(corr_nm2)
        
#温度应变
def draw_Y_T(col):
    f_plot.clear()
    test_YB1 = int(col)-1
    if test_YB1<13 :
        sheet_name='温度'
        sh = data.sheet_by_name(sheet_name)
        col_test_YB1 = sh.col_values(test_YB1,start_rowx=1)
        s_test2=pd.Series(col_test_YB1)
        corr_nm3 = []
        sheet_name='应变'
        sh = data.sheet_by_name(sheet_name)
        for k in range(1,32):
            col_yt = sh.col_values(k,start_rowx=1)
            s_yt=pd.Series(col_yt)
            corr_test2=s_test2.corr(s_yt) 
            if corr_test2<0:
                corr_nm3.append(-corr_test2)
            else :
                corr_nm3.append(corr_test2)
        f_plot.set(title='YB&temprature',  xlabel='YB&temperature',ylabel='corr_num')
        drawbar(corr_nm3)
def draw_each():
    root2 = tkinter.Toplevel()
    root2.title('数据可视化（周期估算）')
    root2.geometry("800x850+650+100")   #窗口大小和窗口位置
    global canvs 
    canvs=FigureCanvasTkAgg(f, root2)
    canvs.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    ft1 = tkFont.Font(family='Fixdsys', size=15, weight=tkFont.BOLD)
    # tkinter.Button(root2, text='pic2', command=draw_picture2).pack()
    # tkinter.Button(root2, text='pic3', command=draw_picture3).pack()
    L1 = tkinter.Label(root2, text="选择位移和温度(不超过12)",font=ft1)
    L1.pack(fill='both')

    var1=StringVar()
    E11 = tkinter.Entry(root2, bd =5, textvariable=var1)
    E11.pack(fill='both')
    B1 = tkinter.Button(root2, text ="选择测试点", command = lambda:draw_D_T(var1.get()),bg = 'green',font=ft1)
    B1.pack(fill='both')
    L1 = tkinter.Label(root2, text="-------------------------------------",font=ft1)
    L1.pack(fill='both')

    L1 = tkinter.Label(root2, text="选择位移和应变(不超过12)",font=ft1)
    L1.pack(fill='both')
    var2=StringVar()
    E12 = tkinter.Entry(root2, bd =5,textvariable=var2)
    E12.pack(fill='both')
    B1 = tkinter.Button(root2, text ="选择测试点", command = lambda:draw_D_Y(var2.get()),bg = 'green',font=ft1)
    B1.pack(fill='both')
    L1 = tkinter.Label(root2, text="-------------------------------------",font=ft1)
    L1.pack(fill='both')

    L1 = tkinter.Label(root2, text="选择应变和温度(不超过12)",font=ft1)
    L1.pack(fill='both')
    var3=StringVar()

    E13 = tkinter.Entry(root2, bd =5,textvariable=var3)
    E13.pack(fill='both')
    B1 = tkinter.Button(root2, text ="选择测试点",  command = lambda:draw_Y_T(var3.get()),bg = 'green',font=ft1)
    B1.pack(fill='both')

  

    root2.mainloop()