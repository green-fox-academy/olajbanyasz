from tkinter import *

master = Tk()
size = 600
w = Canvas(master, width=size, height=size)
w.pack()


for i in range(0,size, int(size/20)):
    y1 = int(size-i)
    x2 = int(i)
    w.create_line(0,y1,x2,0, fill="#000000")

mainloop()
