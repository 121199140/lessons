from tkinter import *
import random
size_x, size_y = 1280, 700

def put_button():
    global b
    b = Button(root, text='Нажми', activebackground='red', command=click)
    b.place(x=size_x/2, y=size_y-40)

def click():
    global x0, y0, d
    b.destroy()
    colors = random.choice(['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange','pink', 'purple', 'red', 'yellow', 'violet', 'indigo', 'chartreuse', 'lime'])
    a = random.randint(1,3)
    x0 = random.randint(10, size_x/2)
    y0 = random.randint(10, size_y/2)
    d = random.randint(10, size_x/5)
    put_button()
    canvas.delete("all")
    if a == 1:
            canvas.create_rectangle(x0, y0, x0+d, y0+d, outline="#fb0", fill=colors)
    elif a == 2:
            canvas.create_oval(x0, y0, x0 + d, y0 + d, fill=colors)
    elif a == 3:
            canvas.create_polygon(x0, y0, x0+2*d , y0+2*d , x0+d, y0, fill=colors)

    root.update()

root = Tk()
root.title('Игра')
root.geometry('1280x700')
root.resizable(False, False)
canvas = Canvas(root, width=size_x, height=size_y)
canvas.pack()
put_button()
root.mainloop()
