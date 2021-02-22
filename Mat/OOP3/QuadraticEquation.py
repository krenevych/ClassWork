from Mat.OOP3.Equation import Equation


class QuadraticEquation(Equation):

    def __init__(self, a, b, c):
        super().__init__(b, c)
        self.a = a

    def solve(self):
        if self.a == 0:
            # 0x**2 + 2x + 1 = 0
            return super().solve()
        else:
            d = self.discr()
            if d < 0:
                return []
            elif d == 0:
                # x**2 + 2x + 1 = 0
                return [-self.b / (2 * self.a)]
            else:
                d_2 = d ** 0.5
                x1 = (-self.b - d_2) / (2 * self.a)
                x2 = (-self.b + d_2) / (2 * self.a)
                solutions = [x1, x2]
                solutions.sort()
                return solutions

    def discr(self):
        return self.b ** 2 - 4 * self.a * self.c

    def __str__(self):
        return ("%dx**2 +" % self.a +
                super().__str__())


if __name__ == "__main__":
    eq = QuadraticEquation(1, 2, 1)
    print(eq)
    print(eq.solve())

    eq = QuadraticEquation(1, 2, 8)
    print(eq)
    print(eq.solve())

    eq = QuadraticEquation(1, -3, 2)
    print(eq)
    print(eq.solve())

    eq = QuadraticEquation(0, 2, 1)
    print(eq)
    print(eq.solve())

    eq = QuadraticEquation(0, 0, 1)
    print(eq)
    print(eq.solve())

    eq = QuadraticEquation(0, 0, 0)
    print(eq)
    print(eq.solve())
