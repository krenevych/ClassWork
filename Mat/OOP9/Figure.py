from abc import ABCMeta, abstractmethod
from turtle import *


class Figure(metaclass=ABCMeta):
    """ Клас Фігура """

    def __init__(self, x, y, color):
        """ Конструктор

        :param x: координата x положення фігури
        :param y: координата y положення фігури
        :param color: колір фігури
        """
        self._x = x  # _x - координата x
        self._y = y  # _y - координата y
        self._visible = False  # _visible - чи є фіруга видимою на екрані
        self._color = color    # _color - колір фігури

    @abstractmethod
    def _draw(self, color):
        """ Допоміжний віртуальний метод, що зображує фігуру заданим кольором
        Тут здійснюється лише декларація методу, а конкретна
        реалізація буде здійснюватися у конкретних нащадках
        :param color: колір
        """
        pass

    def show(self):
        """ Зображує фігуру на екрані """
        if not self._visible:
            self._visible = True
            self._draw(self._color)

    def hide(self):
        """ Ховає фігуру (робить її невидимою на екрані) """
        if self._visible:
            self._visible = False
            # щоб сховати фігуру, потрібно
            # зобразити її кольором фону.
            self._draw(bgcolor())

    def move(self, dx, dy):
        """ Переміщує об'єкт
        :param dx: зміщення у пікселях по осі X
        :param dy: зміщення у пікселях по осі Y
        """
        isVisible = self._visible
        if isVisible:
            self.hide()
        self._x += dx
        self._y += dy
        if isVisible:
            self.show()


######################  клас Circle  ###########################
################################################################
class Circle(Figure):
    """ Клас Коло """

    def __init__(self, x, y, r, color):
        """ Конструктор
        Ініціалізує положення кола, його радіус і колір
        :param x: координата x центру кола
        :param y: координата y центру кола
        :param r: радіус кола
        :param color: колір кола
        """
        super().__init__(x, y, color)  # Обов’язковий виклик конструктора базового класу
        self._r = r  # _r - радіус кола

    def _draw(self, color):
        """ Допоміжний метод, що зображує коло заданим кольором
        :param color: колір
        """
        pencolor(color)
        up()
        # малює починаючи знизу кола
        setpos(self._x, self._y - self._r)
        down()
        circle(self._r)
        up()


################################################################
################################################################
# Перевірка роботи описаних класів.
if __name__ == '__main__':
    # Ініціалізація turtle
    home()
    delay(30)

    # f = Figure(0, 0, "blue")
    # f.show()

    ###### Перевірка кола ############
    c = Circle(120, 120, 50, "blue")
    c.show()
    c.move(-30, -140)
    c.hide()


    mainloop()
