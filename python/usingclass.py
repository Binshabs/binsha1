# from tkinter import *
# class myclass:
#     def __init__(self,rootone):
#         frame=Frame(rootone)
#         frame.pack()
#         self.okbtn=Button(frame,text="ok",command=self.oks)
#         self.okbtn.pack()
#         self.qbtn=Button(frame,text="quit",command=frame.quit)
#         self.qbtn.pack()
#     def oks(self):
#         print("hello team")
# root=Tk()
# obj=myclass(root)
# root.mainloop()
        
        
        
        
"""example pgm"""

from tkinter import *
root=Tk()
frame=Frame(root)
frame.pack()
l1=Label(frame,text="enter first no:")
l1.pack()
e1=Entry(frame)
e1.pack()
l2=Label(frame,text="enter second no:")
l2.pack()
e2=Entry(frame)
e2.pack()
frr=Frame(root)
frr.pack()
bt1=Button(frr,text="add")
bt1.grid(row=0,column=0)
bt2=Button(frr,text="exit",command=exit)
bt2.grid(row=0,column=1)
fm=Frame(root)
fm.pack()
l3=Label(fm,text="Result")
l3.pack()

root.mainloop()