from tkinter import *
import random
score, max_score = 0, 20
size_x, size_y = 1280, 700


def put():
    global b
    b = Button(root, text='Нажми', activebackground='red', command=click)
    b.place(x=random.randint(10, size_x), y=random.randint(2, size_y))


def click():
    global score
    b.destroy()
    if score <= max_score:
        score += 1
        put()
    else:
        Label(root, text='Поздравляем\n Вы виграли').place(relx=0.5, rely=0.5)


root = Tk()
root.title('Игра')
root.geometry('1280x700')
root.resizable(False, False)
put()
root.mainloop()
