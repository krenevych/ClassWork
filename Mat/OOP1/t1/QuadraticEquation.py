# ax**2 + bx + c = 0


class QuadraticEquation:

    INF = "inf"

    def __init__(self, a, b=0, c=0):
        if (isinstance(a, QuadraticEquation)):
            self.a = a.a
            self.b = a.b
            self.c = a.c
        else:
            self.a = a
            self.b = b
            self.c = c

    def show(self):
        print("%0.2fx**2 + %0.2fx + %0.2f = 0"
              % (self.a, self.b, self.c))

    def getSolution(self):
        if self.a == 0 and self.b == 0:
            if self.c != 0:
                return []
            else:
                return [QuadraticEquation.INF]
        elif self.a == 0 and self.b != 0:
            return [-self.c / self.b]
        else:
            D = self.b ** 2 - 4 * self.a * self.c
            if D < 0:
                return []
            elif D == 0:
                return [-self.b / (2 * self.a)]
            else:
                d2 = D ** 0.5
                x1 = (-self.b - d2)/ (2 * self.a)
                x2 = (-self.b + d2)/ (2 * self.a)
                [x1, x2].sort()
                return [x1, x2]


if __name__ == "__main__":
    # eq1 = QuadraticEquation(0, 0, 0)
    # print(eq1.getSolution())
    # eq2 = QuadraticEquation(1, 2, 1)
    # print(eq2.getSolution())
    # eq3 = QuadraticEquation(1, 2, 4)
    # print(eq3.getSolution())
    # eq3 = QuadraticEquation(1, 3, 2)
    # print(eq3.getSolution())

    eq2 = QuadraticEquation(1, 2, 1)
    myNewEq = QuadraticEquation(eq2)
    # myNewEq = eq2
    myNewEq.a = 0
    eq2.show()
    myNewEq.show()