"""ROOT"""

# from tkinter import Tk
# root=Tk()
# root.mainloop()


"""LABEL"""


# from tkinter import *
# root=Tk()
# label=Label(root,text="hello team")
# label.pack()
# root.mainloop()


"""BUTTON"""

# from tkinter import *
# root=Tk()
# button=Button(root,text="login",bg="green",fg="white")
# button.pack()
# root.mainloop()

"""FRAME"""

# from tkinter import *
# root=Tk()
# frame=Frame(root)
# frame.pack()
# button=Button(frame,text="login",bg="green",fg="white")
# button.pack()
# root.mainloop()

"""FILL"""

# from tkinter import *
# root=Tk()

# button1=Button(root,text="login",bg="green",fg="white")
# button1.pack(fill="x",side="bottom")
# button2=Button(root,text="login",bg="red",fg="white")
# button2.pack(fill="y",side="left")

# button3=Button(root,text="login",bg="green",fg="white")
# button3.pack(fill="x",side="right")
# button4=Button(root,text="login",bg="red",fg="white")
# button4.pack(fill="y",side="left")
# root.mainloop()


"""ENTRY"""

# from tkinter import *
# root=Tk()
# ent=Entry(root).pack()
# button=Button(root,text="login",bg="green",fg="white")
# button.pack()

# root.mainloop()

"""GRID"""

# from tkinter import *
# root=Tk()
# l1=Label(root,text="User Name")
# e1=Entry(root)
# l2=Label(root,text="Password")
# e2=Entry(root)
# bt=Button(root,text="Login")
# l1.grid(row=0,column=0)
# e1.grid(row=0,column=1)
# l2.grid(row=1,column=0)
# e2.grid(row=1,column=1)
# bt.grid(row=2,column=1)
# root.mainloop()

"""example pgm"""

from tkinter import *
root=Tk()
l1=Label(root,text="User Name")
e1=Entry(root)
l2=Label(root,text="Mobile")
e2=Entry(root)
l3=Label(root,text="Email")
e3=Entry(root)
l4=Label(root,text="Age")
e4=Entry(root)
l5=Label(root,text="Password")
e5=Entry(root)
l6=Label(root,text="Confirm password")
e6=Entry(root)
bt1=Button(root,text="Login",bg="black",fg="white")
bt2=Button(root,text="cancel",bg="black",fg="white")
l1.grid(row=0,column=0)
e1.grid(row=0,column=1)
l2.grid(row=1,column=0)
e2.grid(row=1,column=1)
l3.grid(row=2,column=0)
e3.grid(row=2,column=1)
l4.grid(row=3,column=0)
e4.grid(row=3,column=1)
l5.grid(row=4,column=0)
e5.grid(row=4,column=1)
l6.grid(row=5,column=0)
e6.grid(row=5,column=1)


bt1.grid(row=7,column=0)
bt2.grid(row=7,column=1)
root.mainloop()
