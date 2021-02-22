class Equation:

    INF = "inf"

    def __init__(self, b, c):
        self.b = b
        self.c = c

    def solve(self):
        if self.b != 0:
            # 4x = 5 => 1
            return [-self.c / self.b]
        else:
            if self.c == 0:
                # 0x = 0 => inf
                return [Equation.INF]
            else:
                # 0x = 5 => 0
                return []

    def show(self):
        print(self)

    def __str__(self):
        return "%dx + %d = 0" % (self.b, self.c)


if __name__ == "__main__":

    eq = Equation(2, 1)
    print(eq)
    print(eq.solve())

    eq = Equation(0, 1)
    print(eq)
    print(eq.solve())

    eq = Equation(0, 0)
    print(eq)
    print(eq.solve())
