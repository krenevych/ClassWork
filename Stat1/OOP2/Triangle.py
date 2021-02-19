from turtle import *


class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

        self.color = "black"
        self.thickness = 1
        self.fillColor = None

    def setColor(self, color):
        self.color = color

    def setFillColor(self, color):
        self.fillColor = color

    def setThickness(self, thickness):
        self.thickness = thickness

    def draw(self):
        currentColor = pencolor()
        currentThickness = pensize()

        pencolor(self.color)
        pensize(self.thickness)
        up()

        fillcolor(self.fillColor)

        setpos(self.x1, self.y1)
        down()
        begin_fill()
        goto(self.x2, self.y2)
        goto(self.x3, self.y3)
        goto(self.x1, self.y1)
        end_fill()
        up()

        pencolor(currentColor)
        pensize(currentThickness)



if __name__ == "__main__":
    reset()

    t = Triangle(0, 0, 200, 0, 0, 100)
    t.setColor("#FF0000")
    t.setFillColor("#0000CD")
    t.setThickness(5)
    t.draw()

    mainloop()
