from tkinter import *
root = Tk()  # створюємо головне вікно програми

def hello():
    res = ent.get()
    # print("Hello, %s!" % res)
    lab["text"] = "Hello, %s!" % res

# Поле введення
ent = Entry(root, font="Arial 18")
ent.pack()

lab = Label(root,
            font="Arial 18",
            bg = "red",
            text="Результат")
lab.pack()

btn = Button(root,  # батьківське вікно
             text="Click me",  # надпис на кнопці
             width=30, height=5,  # ширина та висота
             bg="white", fg="black",  # колір фону і напису
             command=hello)

btn.pack()
root.mainloop()
