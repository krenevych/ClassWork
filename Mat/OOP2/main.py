from turtle import *
from random import randint
from Triangle import Triangle

reset()      # Ініціалізуємо режим малювання

colors = ["#228B22", "#008080", "#FF0000",
          "#FF00FF", "#FFFF00", "#A9A9A9"]

MAXCOORD = 500

for i in range(100):
    # reset()

    x1 = randint(-MAXCOORD, MAXCOORD)
    y1 = randint(-MAXCOORD, MAXCOORD)
    x2 = randint(-MAXCOORD, MAXCOORD)
    y2 = randint(-MAXCOORD, MAXCOORD)
    x3 = randint(-MAXCOORD, MAXCOORD)
    y3 = randint(-MAXCOORD, MAXCOORD)
    t = Triangle(x1, y1, x2, y2, x3, y3)

    index = randint(0, len(colors) - 1)
    color = colors[index]
    t.setColor(color)
    pen = randint(1, 20)
    t.setPensize(pen)
    t.draw()

mainloop()       # Затримуємо вікно на екрані

