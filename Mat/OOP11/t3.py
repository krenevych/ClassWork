from tkinter import *
from tkinter.filedialog import askopenfilename


def readFile(file_name, textbox : Text):
    textbox.delete('1.0', END)

    with open(file_name, encoding="UTF-8") as f:
        textbox.insert('1.0', f.read())


def main():
    root = Tk()  # створюємо головне вікно програми

    global textbox
    textbox = Text(root,            # батьківський віджет
                   font='Arial 14', # шрифт
                   wrap='word')     # чи переносити текст по словах
    textbox.pack()

    btn = Button(root,
                 width=20, height=2,
                 text="Open file",
                 font="Перевірити",
                 command=dialog_open_file
    )
    btn.pack()

    root.mainloop()  # запускаємо цикл головного вікна


def dialog_open_file():
    global textbox
    filename = askopenfilename()
    readFile(filename, textbox)

if __name__ == "__main__": main()