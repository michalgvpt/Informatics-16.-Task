import tkinter as tk
import random as rnd
root=tk.Tk()
root.title('Necklace')
width=750
height=750
canvas = tk.Canvas(root,width=width,height=height,bg='white')
canvas.pack()
colours=['pink','yellow','green','blue']
count=40
size=40
moveable=[]
processing=[]
counter=0
nit_len=36
needle=tk.PhotoImage(file='Needle/koralik_nit.png')
canvas.create_image(0,height-55, image=needle, anchor=tk.NW)

def setup():
    global moveable
    for i in range(40):
        x=rnd.randrange(0,width-size)
        y=rnd.randrange(0,height-size-50)
        moveable.append(canvas.create_oval(x,y,x+size,y+size,fill=colours[i//10]))

def click(e):
    global processing, moveable
    list1=canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if len(list1)!=0 and list1[0] in moveable and len(processing) == 0 and counter < 10:
        processing.append(list1[0])
        moveable.remove(list1[0])
        mover()

def mover():
    global processing
    coor=canvas.coords(processing[0])
    f_pos=[width-size,height-size]
    dx=f_pos[0]-coor[0]-size//2
    dy=f_pos[1]-coor[1]-size//2
    if dx!=0 and dy!=0:
        if dx>=dy:
            dx=dx//dy
            dy=1
        else:
            dy=abs(dy//dx)
            dx=dx//abs(dx)
    canvas.move(processing[0],dx,dy)
    if (coor[1]+coor[3])//2 == 710:
        move_on_nit()
    else:
        canvas.after(4,mover)

def move_on_nit():
    global processing, nit_len, counter
    a = canvas.coords(processing[0])
    if a[0] > nit_len:
        canvas.move(processing[0], -2, 0)
        canvas.after(4, move_on_nit)
    else:
        counter += 1
        processing = []
        nit_len += size

canvas.bind('<Button-1>',click)
setup()
root.mainloop()