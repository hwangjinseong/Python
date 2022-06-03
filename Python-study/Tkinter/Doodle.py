# 낙서장 만들기

# 펜 색상 바꾸기
def blue():
    global color
    color = "blue"
def red():
    global color
    color = "red"
# 펜 굵기 바꾸기
def thin():
    global pensize
    pensize = 1
def thick():
    global pensize
    pensize = 7

def onStart(e):
    global prevx, prevy
    prevx = e.x
    prevy = e.y

def onDraw(e):
    global prevx, prevy, canvas, color, pensize
    curx = e.x
    cury = e.y
    canvas.create_line(prevx, prevy, curx, cury, width=pensize, fill=color)
    prevx = curx
    prevy = cury

from tkinter import *
from turtle import color, pensize
w = Tk()
w.geometry("400x400+10+10")
prevx=0
prevy=0
pensize=3
color="black"

canvas = Canvas(w, width=400, height=350, bg="beige")
canvas.grid(row=0, column=0, columnspan=4)

bb = Button(w, text="파랑펜", bg="blue", fg="white", command=blue)
rb = Button(w, text="빨강펜", bg="red", fg="white", command=red)
nb = Button(w, text="가는펜", command=thin)
kb = Button(w, text="굵은펜", command=thick)
bb.grid(row=1, column=0)
rb.grid(row=1, column=1)
nb.grid(row=1, column=2)
kb.grid(row=1, column=3)

canvas.bind('<ButtonPress-1>', onStart)
canvas.bind('<B1-Motion>', onDraw)

w.mainloop()