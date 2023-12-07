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
