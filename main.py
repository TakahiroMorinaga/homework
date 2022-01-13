#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk



root=tk.Tk()
root.configure(bg='white')
root.geometry('500x700')
root.title('電卓')

lbl=tk.Label(root, font=("メイリオ",30),text="0")
lbl.place(x=225,y=50)

#numberList=['0','1','2','3','4','5','6','7','8','9']
#displayNumber=tk.Label(root,text='0')

firstNum=0
secondNum=0


def button1push():
	if lbl['text'] == '0':
		lbl['text'] = '1'
	else:
		lbl['text'] = lbl['text'] +'1'
button=tk.Button(root, text="1",command=button1push,width=10,height=5).place(x=0,y=100)

#	global firstNum
#	firstNum=firstNum*10+1	
#	print("1")
#	lbl['text']=firstNum

#button=tk.Button(root, text="1",command=button1push,width=10,height=5).place(x=0,y=100)


def button2push():
	if lbl['text'] == '0':
		lbl['text'] = '2'
	else:
		lbl['text'] = lbl['text'] +'2'
button=tk.Button(root, text="2",command=button2push,width=10,height=5).place(x=125,y=100)

def button3push():
	if lbl['text'] == '0':
		lbl['text'] = '3'
	else:
		lbl['text'] = lbl['text'] +'3'
button=tk.Button(root, text="3",command=button3push,width=10,height=5).place(x=250,y=100)

#cal=['+']
def buttonpluspush():
	global firstNum
	global cal	
	firstNum= lbl['text']
	lbl['text']='0'
	cal="+"
#	print("+")
button=tk.Button(root, text="+",command=buttonpluspush,width=10,height=5).place(x=375,y=100)

def button4push():
	if lbl['text'] == '0':
		lbl['text'] = '4'
	else:
		lbl['text'] = lbl['text'] +'4'
button=tk.Button(root, text="4",command=button4push,width=10,height=5).place(x=0,y=200)

def button5push():
	if lbl['text'] == '0':
		lbl['text'] = '5'
	else:
		lbl['text'] = lbl['text'] +'5'
button=tk.Button(root, text="5",command=button5push,width=10,height=5).place(x=125,y=200)

def button6push():
	if lbl['text'] == '0':
		lbl['text'] = '6'
	else:
		lbl['text'] = lbl['text'] +'6'

button=tk.Button(root, text="6",command=button6push,width=10,height=5).place(x=250,y=200)
def buttonMinuspush():
	global firstNum
	global cal	
	firstNum= lbl['text']
	lbl['text']='0'
	cal="-"
	print("-")

button=tk.Button(root, text="-",command=buttonMinuspush,width=10,height=5).place(x=375,y=200)
def button7push():
	if lbl['text'] == '0':
		lbl['text'] = '7'
	else:
		lbl['text'] = lbl['text'] +'7'
button=tk.Button(root, text="7",command=button7push,width=10,height=5).place(x=0,y=300)

def button8push():
	if lbl['text'] == '0':
		lbl['text'] = '8'
	else:
		lbl['text'] = lbl['text'] +'8'
button=tk.Button(root, text="8",command=button8push,width=10,height=5).place(x=125,y=300)

def button9push():
	if lbl['text'] == '0':
		lbl['text'] = '9'
	else:
		lbl['text'] = lbl['text'] +'9'
button=tk.Button(root, text="9",command=button9push,width=10,height=5).place(x=250,y=300)

def buttonPluspush():
	global firstNum
	global cal	
	firstNum= lbl['text']
	lbl['text']='0'
	cal="÷"
	print("÷")
button=tk.Button(root, text="÷",command=buttonPluspush,width=10,height=5).place(x=375,y=300)

def buttonClearpush():
#	global firstNum
#	lal['']=0
	lbl['text']='0'
#	print("clear")

button=tk.Button(root, text="clear",command=buttonClearpush,width=10,height=5).place(x=0,y=400)
def button0push():
	if lbl['text'] == '0':
		lbl['text'] = '0'
	else:
		lbl['text'] = lbl['text'] +'0'
button=tk.Button(root, text="0",command=button0push,width=10,height=5).place(x=125,y=400)


def buttonEqualpush():
	
#	lbl['text']=firstNum
	firstNumInt=int(firstNum)
	secondNum=lbl['text']
	secondNumInt=int(secondNum)

	if  cal == "+":
		result = firstNumInt + secondNumInt
		lbl['text']=result
	elif cal == "-":
		result = firstNumInt - secondNumInt
		lbl['text']=result
	elif cal == "÷":
		result = firstNumInt / secondNumInt
		lbl['text']=result
	elif cal == "×":
		result = firstNumInt * secondNumInt
		lbl['text']=result
			
	else:
		label['text']='0'
#	print("=")

button=tk.Button(root, text="=",command=buttonEqualpush,width=10,height=5).place(x=250,y=400)

def buttonMultiplypush():
	print("×")
button=tk.Button(root, text="×",command=buttonMultiplypush,width=10,height=5).place(x=375,y=400)


#def sum(number1,number2):
#	return number1+number2
#def minus(number1,number2):
#	return number1-number2
#def multiply(number1,number2):
#	return number1*number2
#def divide(number1,number2):
#	return number1/number2


#if  cal == '+':
#	result = firstNumInt + secondNumInt
#else:
#	lbl['text'] = '0'
		

#numberList=[0,1,2,3,4,5,6,7,8,9]
#displayNumber=tk.Label(root,text='0')




#def push():
#	print()

#def calculate():
#	global number
#	number = 




root.mainloop()