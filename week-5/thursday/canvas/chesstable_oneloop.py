from tkinter import *

master = Tk()

w = Canvas(master, width=400, height=400)
w.pack()


size = 50
for i in range(64):
    x = i % 8
    y = i // 8
    if (x+y) % 2 == 0:
        color = "#000000"
    else:
        color = "#ffffff"

    w.create_rectangle(x*size,y*size,(x+1)*size,(y+1)*size, fill=color)












mainloop()
