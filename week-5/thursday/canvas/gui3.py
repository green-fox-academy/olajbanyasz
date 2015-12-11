from tkinter import *
import math

master = Tk()
size = 400
w = Canvas(master, width=size, height=size)
w.pack()

c = int(size/2)
d = 50
a = math.sin(1.04719)

for i in range(d):
    z = i*(size/d)
    v = z*a
    w.create_line(z,size,size/2-z/2,size-size*a+v, fill="#000000")

mainloop()
