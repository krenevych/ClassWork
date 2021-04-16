from tkinter import *
root = Tk() # створюємо головне вікно програми

def Fib(n): # функція обчислення n-го числа Фібоначчі
    f1 = f2 = 1
    for i in range(n-1):
        f1, f2 = f2 + f1, f1
    return f1

# Функція, що викликається як реакція програми на натиск ЛКМ
def calculate(): # функція обробки події натиску кнопки
    try:
        n = int(ent.get()) # беремо з поля значення
    except ValueError:
        lab["text"] = "Помилка"
    else:
        f = Fib(n)
        lab["text"] = "Fib({}) = {}".format(n, f)

# створюємо графічні елементи поле введення, напис, кнопка.
ent = Entry(root, font="Arial 18")
lab = Label(root, font="Arial 18")
btn = Button(root, text="Обчислити", font="Arial 18", command=calculate)

# розміщуємо графічні елементи у вікні.
ent.pack()
lab.pack()
btn.pack()

root.mainloop()  # запускаємо головний цикл
