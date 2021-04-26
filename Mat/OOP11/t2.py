from tkinter import *

root = Tk()  # створюємо головне вікно програми

entry = Entry(
    root,
    width=70,
    font="Arial 20",
)

listbox = Listbox(
    root,
    width=70,
    height = 15
)


def show_words():
    global entry, listbox
    content : str = entry.get()
    words = content.split()
    listbox.delete(0, END)
    for word in words:
        listbox.insert(END, word)


btn = Button(
    root,
    width=20, height=5,
    text="Hello!",
    font="Перевірити",
    command=show_words
)

entry.pack()
listbox.pack()
btn.pack()

root.mainloop()  # запускаємо цикл головного вікна
