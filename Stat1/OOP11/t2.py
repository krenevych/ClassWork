from tkinter import *
root = Tk()  # створюємо головне вікно програми



# Поле введення
ent = Entry(root
            , font="Arial 18"
            , width=20
            )
ent.pack()

listbox = Listbox(root,        # батьківський віджет
                  width=30, height=10) # ширина і висота списку
listbox.pack()


def updateList():
    text : str = ent.get()
    lst = text.split()
    listbox.delete(0, END)  # видалення всіх елементів списку
    for word in lst:
        listbox.insert(END, word)


btn = Button(root,  # батьківське вікно
             text="Check to palindrome"  # надпис на кнопці
             , width=30, height=5  # ширина та висота
             , bg="white", fg="black"  # колір фону і напису
             , command=updateList
             )

btn.pack()
root.mainloop()
