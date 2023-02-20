from tkinter import *
from tkinter import ttk
global lbl2

def clear():
    entry.delete(0, END)  # удаление введенного текста
    lbl2["text"] = ""

def display():

    lbl2["text"] = entry.get()  # получение введенного текста
    lbl2["font"] = ("Consolas", 12, "bold")


root = Tk()
root.title("Задание 10 Итоговое тестирование модуль 2")
root.geometry("1250x600")

lbl2 = ttk.Label()
lbl2.pack(anchor=NW, padx=6, pady=100)
entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=15)

# вставка начальных данных
entry.insert(0, "Введите ФИО")

display_button = ttk.Button(text="Приветствовать", command=display)
display_button.pack(side=LEFT, anchor=N, padx=6, pady=6)

clear_button = ttk.Button(text="Очистить поле ввода", command=clear)
clear_button.pack(side=LEFT, anchor=N, padx=6, pady=6)
lbl1 = Label(text="Приветствую Вас: ", font=("Consolas", 12, "bold"), fg="red")
lbl1.place(x=5, y=5)

root.mainloop()