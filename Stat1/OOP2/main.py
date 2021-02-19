from random import randint

from Triangle import Triangle

colors = [
    "#FF0000",
    "#2E8B57",
    "#FF1493",
    "#D2691E",
    "#87CEFA",
    "#ADFF2F"
]

MAXCOORD = 500

for i in range(100):
    x1 = randint(-MAXCOORD, MAXCOORD)
    y1 = randint(-MAXCOORD, MAXCOORD)
    x2 = randint(-MAXCOORD, MAXCOORD)
    y2 = randint(-MAXCOORD, MAXCOORD)
    x3 = randint(-MAXCOORD, MAXCOORD)
    y3 = randint(-MAXCOORD, MAXCOORD)
    t = Triangle( x1, y1, x2, y2, x3, y3)
    indexColor = randint(0, len(colors) - 1)
    indexFillColor = randint(0, len(colors) - 1)
    t.setColor(colors[indexColor])
    t.setFillColor(colors[indexFillColor])
    thickness = randint(0, 10)
    t.setThickness(thickness)
    t.draw()