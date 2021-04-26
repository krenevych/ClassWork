from tkinter import *


def readFile(file_name, textbox):
    with open(file_name, encoding="UTF-8") as f:
        textbox.insert('1.0', f.read())


def main():
    root = Tk()  # створюємо головне вікно програми
    textbox = Text(root,            # батьківський віджет
                   font='Arial 14', # шрифт
                   wrap='word')     # чи переносити текст по словах
    textbox.pack()

    readFile("input.txt", textbox)


    root.mainloop()  # запускаємо цикл головного вікна


if __name__ == "__main__": main()