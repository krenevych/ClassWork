from Stat1.OOP3.Equation import Equation


class QuadraticEquation(Equation):

    def __init__(self, a, b, c):
        super().__init__(b, c)
        self.a = a

    def __str__(self):
        return "%dx^2 + " % self.a + super().__str__()

    def solve(self):
        if self.a == 0:
            return super().solve()
        else:
            d = self.b ** 2 - 4 * self.a * self.c
            if d < 0:
                return []
            elif d == 0:
                return [-self.b / (2 * self.a)]
            else:
                d = d ** 0.5
                x1 = (-self.b - d) / (2 * self.a)
                x2 = (-self.b + d) / (2 * self.a)
                solutions = [x1, x2]
                solutions.sort()
                return solutions


if __name__ == "__main__":
    eq = QuadraticEquation(0, 2, 1)  # 1 solution: -0.5
    print(eq)
    print(eq.solve())
    print()

    eq = QuadraticEquation(0, 0, 1)  # 0 solution
    print(eq)
    print(eq.solve())
    print()

    eq = QuadraticEquation(0, 0, 0)  # inf solution
    print(eq)
    print(eq.solve())
    print()

    eq = QuadraticEquation(1, 2, 1) # 1 solution = -1
    print(eq)
    print(eq.solve())
    print()

    eq = QuadraticEquation(1, -3, 2) # 2 solution = [1, 2]
    print(eq)
    print(eq.solve())
    print()

    eq = QuadraticEquation(1, -3, 9) # 0 solution
    print(eq)
    print(eq.solve())
    print()
