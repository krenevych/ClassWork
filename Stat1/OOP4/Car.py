from Mat.OOP4.Figure import Rectangle, Circle, Figure
from turtle import *


class Car(Figure):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)


        self.properties = [
            Rectangle(self._x, self._y, 300, 70, "red"),
            Rectangle(self._x + 50, self._y + 70, 200, 30, "red"),
            Circle(self._x + 50, self._y, 20, "black"),
            Circle(self._x + 250, self._y, 20, "black"),
            Rectangle(self._x + 50, self._y + 75, 100, 10, "red")
        ]


    def _draw(self, color):
        for el in self.properties:
            el._draw(color)


if __name__ == "__main__":
    # Ініціалізація turtle
    home()
    delay(10)


    car = Car(-100, 100, "red")
    car.show()
    car.hide()

    mainloop()