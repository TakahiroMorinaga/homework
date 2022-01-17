#!/usr/bin/env python
# -*- coding: utf-8 -*-


#csvファイルへのアクセス

#import csv
#f=open("kadai2.csv","r")
#reader=csv.reader(f)
#data=[e for e in reader]
#print(data)
#f.close()


#ユーザー入力テキストの読み込み

#import csv

#with open("kadai2.csv")as f:
#	line=csv.reader(f, delimiter',')
#print(list(line)[0])

#UIの設定

import tkinter as tk

root=tk.Tk()
root.title("matcha login page")
root.geometry("500x400")

#ラベル配置
lbl1=tk.Label(root,text="LOGIN Page",fg="black")
lbl1.pack()
lbl1.place(x=200,y=85)

lbl2=tk.Label(root,text="Welcome to matcha!",fg="green",width="100",font=("MSゴシック",30,"bold"))
lbl2.pack()

lbl3=tk.Label(root,text="input your information",fg="black")
lbl3.pack()
lbl3.place(x=175,y=120)

lbl4=tk.Label(root,text="User ID",fg="black",font=("MSゴシック",20,"bold"))
lbl4.pack()
lbl4.place(x=100,y=180)

lbl5=tk.Label(root,text="Password",fg="black",font=("MSゴシック",20,"bold"))
lbl5.pack()
lbl5.place(x=100,y=250)

#テキストボックス配置
txt1=tk.Entry(root,width=21)
txt1.pack()
txt1.place(x=220,y=180)

txt1=tk.Entry(root,show="*",width=21)
txt1.pack()
txt1.place(x=220,y=250)



#ボタン定義
def btn1pushed():
#	for x in range(len(kadaidata)):
#		if kadaidata[x]

#def btn2pushed(widget):
#	print("clicked")

def transition_button(widget):
	widget.destroy()
	signUpPage=tkinter.Tk()
	signUpPage.geometry("500x400")





#ボタン配置
#メモ:macではボタン背景の色は変えられない？
btn1=tk.Button(root,text="LOGIN", width=11, height=3,font=("MSゴシック",15,"bold"),fg="green")
btn1.pack()
btn1.place(x=100,y=310)


btn2=tk.Button(root,text="SIGN UP",width=11, height=3,command="transition_button",font=("MSゴシック",15,"bold"),fg="green")
btn2.pack()
btn2.place(x=280,y=310)

tk.mainloop()