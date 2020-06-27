from tkinter import *
from tkinter import messagebox

def addition(num1,num2,lblres):
    result=num1+num2
    lblres.config(text="Result is %d"%result)

def subtraction(num1,num2,lblres):
    result=num1-num2
    lblres.config(text="Result is %d"%result)

def multiplication(num1,num2,lblres):
    result=num1*num2
    lblres.config(text="Result is %d"%result)

def division(num1,num2,lblres):
    try:
        result=num1/num2
        lblres.config(text="Result is %d"%result)
    except ZeroDivisionError:
        messagebox.showerror('Error','You cannot Divide By Zero')

def clear(ennum1,ennum2,lblres):
    ennum1.delete(0,END)
    ennum2.delete(0,END)
    lblres.config(text="")

win=Tk()
win.title('GUI of Calculator')
win.geometry('360x360+550+200')

lblhead=Label(win, fg='red', text="Welcome To Calculator", font=('TimesNewRoman',15,'bold'))
lblhead.place(x=60,y=0)

lblnum1=Label(win, text="Enter Num 1 :", font=('TimesNewRoman',13,'bold'))
lblnum1.place(x=20,y=50)

ennum1=Entry(win,width=15, font=('TimesNewRoman',15,'bold'))
ennum1.place(x=150,y=50)

lblnum2=Label(win, text="Enter Num 2 :", font=('TimesNewRoman',13,'bold'))
lblnum2.place(x=20,y=100)

ennum2=Entry(win,width=15, font=('TimesNewRoman',15,'bold'))
ennum2.place(x=150,y=100)

lblres=Label(win, font=('TimesNewRoman',20,'bold'))
lblres.place(x=100,y=270)

btn1=Button(win,padx=10,pady=3,text='+',bg='salmon',font=('Consolas',15,'bold'),command=lambda:addition(int(ennum1.get()),int(ennum2.get()),lblres))
btn1.place(x=10,y=200)

btn2=Button(win,padx=10,pady=3,text='-',bg='salmon',font=('Consolas',15,'bold'),command=lambda:subtraction(int(ennum1.get()),int(ennum2.get()),lblres))
btn2.place(x=70,y=200)

btn3=Button(win,padx=10,pady=3,text='*',bg='salmon',font=('Consolas',15,'bold'),command=lambda:multiplication(int(ennum1.get()),int(ennum2.get()),lblres))
btn3.place(x=130,y=200)

btn4=Button(win,padx=10,pady=3,text='/',bg='salmon',font=('Consolas',15,'bold'),command=lambda:division(int(ennum1.get()),int(ennum2.get()),lblres))
btn4.place(x=190,y=200)

btn5=Button(win,padx=10,pady=3,text='Clear',bg='salmon',font=('Consolas',15,'bold'),command=lambda:clear(ennum1,ennum2,lblres))
btn5.place(x=250,y=200)

win.mainloop()

