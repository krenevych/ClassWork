from tkinter import *

root = Tk()  # створюємо головне вікно програми

entry = Entry(
    root,
    width=70,
    font="Arial 20",
)

lab = Label(
    root,
    width=70,
    font="Arial 20",
    text="Введіть текст вище та натисніть кнопку"
)


def check():
    global entry, lab
    text = entry.get()
    if text == text[::-1]:
        lab["text"] = "Введений текст є паліндромом"
    else:
        lab["text"] = "Введений текст НЕ є паліндромом"


btn = Button(
    root,
    width=20, height=5,
    text="Hello!",
    font="Перевірити",
    command=check
)

entry.pack()
lab.pack()
btn.pack()

root.mainloop()  # запускаємо цикл головного вікна
