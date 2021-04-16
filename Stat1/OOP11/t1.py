from tkinter import *
root = Tk()  # створюємо головне вікно програми

def checkIfPalindrom():
    line = ent.get().strip()
    if line == line[::-1]:
        lab["text"] = "'%s' є паліндромом" % line
    else:
        lab["text"] = "'%s' НЕ є паліндромом" % line


# Поле введення
ent = Entry(root, font="Arial 18")
ent.pack()

lab = Label(root,
            font="Arial 18",
            bg = "red",
            text="Результат")
lab.pack()

btn = Button(root,  # батьківське вікно
             text="Check to palindrome",  # надпис на кнопці
             width=30, height=5,  # ширина та висота
             bg="white", fg="black",  # колір фону і напису
             command=checkIfPalindrom)

btn.pack()
root.mainloop()
