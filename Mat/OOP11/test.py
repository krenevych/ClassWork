from tkinter import *

root = Tk()  # створюємо головне вікно програми

def hello():
    print("Hello!")

btn = Button(
    root,
    width=20, height=5,
    text="Hello!",
    font="Arial 20",
    command=hello
)

btn.pack()


root.mainloop()  # запускаємо цикл головного вікна