#!/usr/bin/env python
# -*- coding: utf-8 -*-


#csvファイルへのアクセス

#from csv import writer
#data added to the list
#userdata=["name","UserID","email","age","height"]

#with open("kadai2data.csv","w", encoding="utf-8",newline="")as f_object:
#   writerObject = writer(f_object)
#   writerObject.writerow(userdata)
#   f_object.close()




#UIの設定

import tkinter as tk
import tkinter.messagebox as msg
import pandas as pd
import csv



#ページ遷移設定



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

#ユーザ入力値の保持
#str_name=tk.StringVar()
#str_UserID=tk.StringVar()
#str_email=tk.StringVar()
#int_age=tk.IntringVar()
#int_height=Int.StringVar()



#   dataset =[]
    
#    canvas2txt2=tk.Entry(root,width=21) 
#    dataset.append(canvas2txt2.get())
    

#    canvas2txt3=tk.Entry(root,width=21)
#    dataset.append(canvas2txt3.get())

#    canvas2txt4=tk.Entry(root,width=21)
#    dataset.append(canvas2txt4.get())

#    canvas2txt5=tk.Entry(root,width=21)
#    dataset.append(canvas2txt5.get())

#    canvas2txt6=tk.Entry(root,width=21)
#    dataset.append(canvas2txt6.get())

#    with open("kadai2data.csv","a",newline="") as csvFile:
#        writer=csv.writer(csvFile)
#       writer.writerow(dataset)
#        print(dataset)


 #  return






def transition_button_signup(widget):
    widget.place_forget() # canvas(widget)を隠す                          
    canvas2 = tk.Canvas(width=500, height=400)
    canvas2.place(x=0, y=0)




#sign upページ
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

#def signup_button_pushed_on_canvas2(widget):
#    dataset=["a" ,"b","c"]
#    dataset.append(canvas2txt2("a"))
#    dataset.append(canvas2txt3("b"))
#    dataset.append(canvas2txt4("c"))
#    dataset.append(canvas2txt5("a"))
#    dataset.append(canvas2txt6("b"))

#    with open("kadai2data.csv","a",newline="") as csvFile:
#        writer=csv.writer(csvFile)
#        writer.writerow(detaset)

#    return


#Loginページ
def transition_button_login(widget):
    widget.place_forget() # canvas(widget)を隠す                          
    canvas3 = tk.Canvas(width=500, height=400)
    canvas3.place(x=0, y=0)

    canvas3lbl1=tk.Label(root,text=" Your information",fg="black")
    canvas3lbl1.place(x=200,y=10)
    

    canvas3lbl2=tk.Label(root,text="Your Name",fg="black",font=("MSゴシック",12,"bold"))
    canvas3lbl2.place(x=100,y=100)
    

    canvas3lbl3=tk.Label(root,text="Your User ID",fg="black",font=("MSゴシック",12,"bold"))
    canvas3lbl3.place(x=100,y=140)
   

    canvas3lbl4=tk.Label(root,text="Your email",fg="black",font=("MSゴシック",12,"bold"))
    canvas3lbl4.place(x=100,y=180)
    
    canvas3lbl5=tk.Label(root,text="Your age",fg="black",font=("MSゴシック",12,"bold"))
    canvas3lbl5.place(x=100,y=220)
    
    canvas3lbl6=tk.Label(root,text="Your height",fg="black",font=("MSゴシック",12,"bold"))
    canvas3lbl6.place(x=100,y=260)
    

    btn3btn1=tk.Button(canvas3,text="Back to Home",width=11, height=3,font=("MSゴシック",15,"bold"),fg="green")
    btn3btn1.place(x=170,y=310)
  

#def  signup_button_pushed_on_canvas2():
#    print("hello")


    
    
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

lbl5=tk.Label(root,text="Password",fg="black",font=("MSゴシック",20,"bold"))
lbl5.pack()
lbl5.place(x=100,y=250)

#テキストボックス配置
txt1=tk.Entry(root,width=21)
txt1.pack()
txt1.place(x=220,y=180)

txt2=tk.Entry(root,show="*",width=21)
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


#root.mainloop()
tk.mainloop()