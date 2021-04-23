from tkinter import *
from tkinter.filedialog import askopenfilename

root = Tk()  # створюємо головне вікно програми


listbox = Listbox(root,        # батьківський віджет
                  width=30, height=10) # ширина і висота списку
listbox.pack()


def updateList():
    filename = askopenfilename()
    print(filename)

    with open(filename) as inputFile:
        text : str = inputFile.read()
        lst = text.split()
        listbox.delete(0, END)  # видалення всіх елементів списку
        for word in lst:
            listbox.insert(END, word)


btn = Button(root,  # батьківське вікно
             text="Open file"  # надпис на кнопці
             , width=30, height=5  # ширина та висота
             , bg="white", fg="black"  # колір фону і напису
             , command=updateList
             )

btn.pack()
root.mainloop()
