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
app=Tk()
app.title("calculator")
