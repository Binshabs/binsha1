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
l1=Label(root,text="enter first no:")
e1=Entry(root)
l2=Label(root,text="enter student no:")
e2=Entry(root)
l3=Label(root,text="result")
e3=Entry(root)

bt1=Button(root,text="add")
button=Button(root,text="exit",command=root.quit)

l1.grid(row=0,column=0)
e1.grid(row=0,column=1)
l2.grid(row=1,column=0)
e2.grid(row=1,column=1)
l3.grid(row=2,column=0)
e3.grid(row=2,column=1)

bt1.grid(row=3,column=0)
button.grid(row=3,column=1)





root.mainloop()