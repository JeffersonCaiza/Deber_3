from tkinter import *
tk = Tk()
x=0
y=0
canvas = Canvas(tk, width=960, height=609)
canvas.pack()
fondo=PhotoImage(file="cancha.png")
canvas.create_image(0,0, anchor=NW, image=fondo)
my_image=PhotoImage(file="balon1.png")
canvas.create_image(468,292, anchor=NW, image=my_image)


def moveball(event):
    global y,x
    if event.keysym == 'Up':
        canvas.move(2, 0, -3)
        y=y+1
    elif event.keysym == 'Down':
        canvas.move(2, 0, 3)
        y=y-1
    elif event.keysym == 'Left':
        canvas.move(2, -3, 0)
        x=x-1
    else:
        canvas.move(2, 3, 0)
        x=x+1

    print(str(x),''+str(y))


    if ((x==-153 and y==0) or (x==154 and y==0)):
        print('GOL')
    if ((x==-153 and y==1) or (x==154 and y==1)):
        print('GOL')
    if ((x==-153 and y==2) or (x==154 and y==2)):
        print('GOL')
    if ((x==-153 and y==3) or (x==154 and y==3)):
        print('GOL')
    if ((x==-153 and y==4) or (x==154 and y==4)):
        print('GOL')
    if ((x==-153 and y==5) or (x==154 and y==5)):
        print('GOL')
    if ((x==-153 and y==6) or (x==154 and y==6)):
        print('GOL')
    


    if ((x==-153 and y==-1) or (x==154 and y==-1)):
        print('GOL')
    if ((x==-153 and y==-2) or (x==154 and y==-2)):
        print('GOL')
    if ((x==-153 and y==-3) or (x==154 and y==-3)):
        print('GOL')
    if ((x==-153 and y==-4) or (x==154 and y==-4)):
        print('GOL')
    if ((x==-153 and y==-5) or (x==154 and y==-5)):
        print('GOL')
    if ((x==-153 and y==-6) or (x==154 and y==-6)):
        print('GOL')
    if ((x==-153 and y==-7) or (x==154 and y==-7)):
        print('GOL')

    
canvas.bind_all('<KeyPress-Up>', moveball)
canvas.bind_all('<KeyPress-Down>', moveball)
canvas.bind_all('<KeyPress-Left>', moveball)
canvas.bind_all('<KeyPress-Right>', moveball)


tk.mainloop()