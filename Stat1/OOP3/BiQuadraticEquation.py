from Stat1.OOP3.QuadraticEquation import QuadraticEquation


class BiQuadraticEquation(QuadraticEquation):

    def __str__(self):
        return "%dx^4 + %dx^2 + %d = 0" % (
            self.a, self.b, self.c)

    def solve(self):
        # y = x^2
        # ay^2 + yx + c=0
        solutions_of_quadratic_equation = super().solve()  # [y1, y2]
        # y^2 - y1 = 0
        # y^2 - y2 = 0
        solutions = []
        for sol in solutions_of_quadratic_equation:
            # y^2 + 0x - sol = 0
            if sol == self.INF_NUM_SOL:
                solutions.append(self.INF_NUM_SOL)
                break

            eq1 = QuadraticEquation(1, 0, -sol)
            solutions += eq1.solve()
        solutions.sort()
        return solutions


if __name__ == "__main__":
    eq = BiQuadraticEquation(0, 1, -4)  # x^2 - 4 = 0
    print(eq)
    print(eq.solve())
    print()

    eq = BiQuadraticEquation(1, 2, 1)  # x^4 + 2x^2 + 1 = 0
    print(eq)
    print(eq.solve())
    print()

    eq = BiQuadraticEquation(1, -2, 1)  # x^4 - 2x^2 + 1 = 0 => 2 solution = [-1, 1]
    print(eq)
    print(eq.solve())
    print()

    eq = BiQuadraticEquation(1, -3, 2)  # 4 solution = [-sqr(2), -1, 1,  sqr(2)]
    print(eq)
    print(eq.solve())
    print()
