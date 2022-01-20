#!/usr/bin/env python
# -*- coding: utf-8 -*-



#!/usr/bin/env python
# -*- coding: utf-8 -*-



import tkinter as tk
import tkinter.messagebox as msg
import pandas as pd
import csv
import tkinter.ttk as ttk


#sign up page

def signup_button_pushed_on_canvas2():

    name=str_name.get()
    UserID=str_UserID.get()
    email=str_email.get()
    age=int_age.get()
    height=int_height.get()

    if name=='' or UserID=='' or email=='' or age=='' or height=='':
        msg.showinfo("お知らせ","データが未入力です。")
    else:
        df=pd.DataFrame({"name":[name],"UserID":[UserID],"email":[email],"age":[age],"height":[height]})
        df.to_csv("kadai2data.csv",mode="a",header=False,index=False)
        msg.showinfo("お知らせ","登録が完了しました。")




def transition_button_signup(widget):
    widget.place_forget() # canvas(widget)を隠す                          
    canvas2 = tk.Canvas(width=500, height=400)
    canvas2.place(x=0, y=0)




    canvas2lbl1=tk.Label(root,text="input your information",fg="black")
    canvas2lbl1.place(x=175,y=10)
    

    canvas2lbl2=tk.Label(root,text="Enter your Name",fg="black",font=("MSゴシック",12,"bold"))
    canvas2lbl2.place(x=100,y=100)
    canvas2txt2=tk.Entry(root,width=21,textvariable=str_name)
    canvas2txt2.place(x=220,y=100)
    

    canvas2lbl3=tk.Label(root,text="Enter User ID",fg="black",font=("MSゴシック",12,"bold"))
    canvas2lbl3.place(x=100,y=140)
    canvas2txt3=tk.Entry(root,width=21,textvariable=str_UserID)
    canvas2txt3.place(x=220,y=140)

    canvas2lbl4=tk.Label(root,text="Enter your email",fg="black",font=("MSゴシック",12,"bold"))
    canvas2lbl4.place(x=100,y=180)
    canvas2txt4=tk.Entry(root,width=21,textvariable=str_email)
    canvas2txt4.place(x=220,y=180)

    canvas2lbl5=tk.Label(root,text="Enter your age",fg="black",font=("MSゴシック",12,"bold"))
    canvas2lbl5.place(x=100,y=220)
    canvas2txt5=tk.Entry(root,width=21,textvariable=int_age)
    canvas2txt5.place(x=220,y=220)

    canvas2lbl6=tk.Label(root,text="Enter your height",fg="black",font=("MSゴシック",12,"bold"))
    canvas2lbl6.place(x=100,y=260)
    canvas2txt6=tk.Entry(root,width=21,textvariable=int_height)
    canvas2txt6.place(x=220,y=260)

    btn2btn1=tk.Button(canvas2,text="SIGN UP",width=11,height=3,command=signup_button_pushed_on_canvas2,font=("MSゴシック",15,"bold"),fg="green")
    btn2btn1.place(x=170,y=310)

def backhome_button(widget):

    widget.place_forget() # canvas(widget)を隠す                          
    canvas1=tk.Canvas(width=500,height=400)
    canvas1.place(x=0,y=0)

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

    lbl5=tk.Label(root,text="email",fg="black",font=("MSゴシック",20,"bold"))
    lbl5.pack()
    lbl5.place(x=100,y=250)

    lbl6Error=tk.Label(root,text="")
    lbl6Error.place(x=175,y=140)


#Loginページ
def transition_button_login(widget):
    widget.place_forget() # canvas(widget)を隠す                          
    canvas3 = tk.Canvas(width=500, height=400)
    canvas3.place(x=0, y=0)

    canvas3lbl1=tk.Label(root,text=" Your information",fg="black")
    canvas3lbl1.place(x=200,y=10)
    

    canvas3lbl2=tk.Label(root,text="Error",fg="black",font=("MSゴシック",12,"bold"))
    canvas3lbl2.place(x=100,y=100)
    

    canvas3lbl3=tk.Label(root,text="Error",fg="black",font=("MSゴシック",12,"bold"))
    canvas3lbl3.place(x=100,y=140)
   

    canvas3lbl4=tk.Label(root,text="Error",fg="black",font=("MSゴシック",12,"bold"))
    canvas3lbl4.place(x=100,y=180)
    
    canvas3lbl5=tk.Label(root,text="Error",fg="black",font=("MSゴシック",12,"bold"))
    canvas3lbl5.place(x=100,y=220)
    
    canvas3lbl6=tk.Label(root,text="Error",fg="black",font=("MSゴシック",12,"bold"))
    canvas3lbl6.place(x=100,y=260)

    

#    btn3btn1=tk.Button(canvas3,text="Back to Home",width=11, height=3,font=("MSゴシック",15,"bold"),fg="green")
#    btn3btn1.place(x=170,y=310)
  

    
    
    userInfo="kadai2data.csv"
    txt1_value=txt1.get()
    txt2_value=txt2.get()

    with open(userInfo) as f:
        infoList=csv.reader(f)

        useridInfo = txt1_value
        mailInfo = txt2_value

        for user in infoList:
            if user[1] == useridInfo:
                if user[2] == mailInfo:
#                    canvas3.tkraise()
                    canvas3lbl2["text"]=user[0]
                    canvas3lbl3["text"]=user[1]
                    canvas3lbl4["text"]=user[2]
                    canvas3lbl5["text"]=user[3]
                    canvas3lbl6["text"]=user[4]
                    
                    
            else:
                lbl6Error["text"]="error"


#logined page when sccess

   
#UI設定  


#rootメインウインドウの設定
root=tk.Tk()
root.title("matcha user page")
root.geometry("500x400")

canvas1=tk.Canvas(width=500,height=400)
canvas1.place(x=0,y=0)


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

lbl5=tk.Label(root,text="email",fg="black",font=("MSゴシック",20,"bold"))
lbl5.pack()
lbl5.place(x=100,y=250)

lbl6Error=tk.Label(root,text="")
lbl6Error.place(x=175,y=140)

#テキストボックス配置
txt1=tk.Entry(root,show="*",width=21)
txt1.pack()
txt1.place(x=220,y=180)

txt2=tk.Entry(root,width=21)
txt2.pack()
txt2.place(x=220,y=250)




#ボタン配置
#メモ:macではボタン背景の色は変えられない？
btn1=tk.Button(root,text="LOGIN", width=11, height=3,command=lambda:transition_button_login(canvas1),font=("MSゴシック",15,"bold"),fg="green")
btn1.pack()
btn1.place(x=100,y=310)


btn2=tk.Button(canvas1,text="SIGN UP",width=11, height=3,command=lambda:transition_button_signup(canvas1),font=("MSゴシック",15,"bold"),fg="green")
btn2.pack()
btn2.place(x=280,y=310)

str_name=tk.StringVar()
str_UserID=tk.StringVar()
str_email=tk.StringVar()
int_age=tk.StringVar()
int_height=tk.StringVar()


root.tkraise()
tk.mainloop()