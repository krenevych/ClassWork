from tkinter import *
from tkinter.filedialog import askopenfilename

root = Tk()  # створюємо головне вікно програми


textbox = Text(root,         # батьківський віджет
            font='Arial 14', # шрифт
            wrap='word')     # чи переносити текст по словах
textbox.pack()


def update():
    filename = askopenfilename()
    print(filename)

    with open(filename) as inputFile:
        text : str = inputFile.read()
        textbox.delete('1.0', END)
        textbox.insert('1.0', text)


btn = Button(root,  # батьківське вікно
             text="Open file"  # надпис на кнопці
             , width=30, height=5  # ширина та висота
             , bg="white", fg="black"  # колір фону і напису
             , command=update
             )

btn.pack()
root.mainloop()
