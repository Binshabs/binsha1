"""example pgm"""

# from tkinter import *
# root=Tk()
# frame=Frame(root)
# frame.pack()
# l1=Label(frame,text="enter first no:")
# l1.pack()
# e1=Entry(frame)
# e1.pack()
# l2=Label(frame,text="enter second no:")
# l2.pack()
# e2=Entry(frame)
# e2.pack()
# frr=Frame(root)
# frr.pack()
# bt1=Button(frr,text="add")
# bt1.grid(row=0,column=0)
# bt2=Button(frr,text="exit",command=exit)
# bt2.grid(row=0,column=1)
# fm=Frame(root)
# fm.pack()
# l3=Label(fm,text="Result")
# l3.pack()
# root.mainloop()

"""read and print """

# from tkinter import *
# def result():
#     num1=float(e1.get())
#     num2=float(e2.get())
#     res.set(num1+num2)
# app=Tk()
# app.title("calculator")
# l1=Label(app,text="enter first number")
# l1.pack()
# e1=Entry(app)
# e1.pack()
# l2=Label(app,text="enter second number")
# l2.pack()
# e2=Entry(app)
# e2.pack()
# btn=Button(app,text="sum",command=result)
# btn.pack()
# res=StringVar()
# res.set("result")
# l3=Label(app,textvariable=res)
# l3.pack()
# app.mainloop()


"""example pgm"""

# from tkinter import *
# def add():
#     num1=float(e1.get())
#     num2=float(e2.get())
#     res.set(num1+num2)
# def mul():
#     num1=float(e1.get())
#     num2=float(e2.get())
#     res.set(num1*num2)
# def div():
#     num1=float(e1.get())
#     num2=float(e2.get())
#     res.set(num1/num2)
# def sub():
#     num1=float(e1.get())
#     num2=float(e2.get())
#     res.set(num1-num2)
# app=Tk()
# app.title("calculator")
# l1=Label(app,text="enter first number")
# l1.pack()
# e1=Entry(app)
# e1.pack()
# l2=Label(app,text="enter second number")
# l2.pack()
# e2=Entry(app)
# e2.pack()
# btn=Button(app,text="add",command=add)
# btn.pack()
# btn=Button(app,text="mul",command=mul)
# btn.pack()
# btn=Button(app,text="div",command=div)
# btn.pack()
# btn=Button(app,text="sub",command=sub)
# btn.pack()
# res=StringVar()
# res.set("result")
# l3=Label(app,textvariable=res)
# l3.pack()
# app.mainloop()

"""BMI CALCULATOR"""
from tkinter import *
root=Tk()
root.title("Bmi")
def Bmi():
    n1=float(e1.get())
    n2=float(e2.get())
    n3=n2/100
    r=n1/(n3**2)
    res.set(r)
    if r<18.5:
       bmi.set('under weight')
    elif r<24.9:
       bmi.set('normal weight')
    elif r<29.9:
       bmi.set('over weight')
    else:
       bmi.set('obesity')
       
l1=Label(root,text="weight in kg")
e1=Entry(root)
l2=Label(root,text="height in cm")
e2=Entry(root)
btn=Button(root,text="calculate",command=Bmi)
res=StringVar()
res.set("")
bmi=StringVar()
bmi.set("")

l3=Label(root,text="result")
e3=Entry(root,textvariable=res)
l4=Label(root,text="BMI Categories")
e4=Entry(root,textvariable=bmi)
l1.grid(row=0,column=0)
e1.grid(row=0,column=1)
l2.grid(row=1,column=0)
e2.grid(row=1,column=1)
btn.grid(row=2,column=1)
l3.grid(row=3,column=0)
e3.grid(row=3,column=1)
l4.grid(row=4,column=0)
e4.grid(row=4,column=1)

root.mainloop()
