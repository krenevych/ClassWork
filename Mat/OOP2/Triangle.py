from turtle import *

# https://trinket.io/docs/colors

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

        self.color = "black"
        self.pensize = 2

    def draw(self):
        up()
        setpos(self.x1, self.y1)

        current_color = pencolor()
        current_pensize = pensize()
        pencolor(self.color)
        pensize(self.pensize)
        down()
        goto(self.x2, self.y2)
        goto(self.x3, self.y3)
        goto(self.x1, self.y1)
        up()
        pencolor(current_color)
        pensize(current_pensize)

    def setColor(self, color):
        self.color = color

    def setPensize(self, penSize):
        self.pensize = penSize
