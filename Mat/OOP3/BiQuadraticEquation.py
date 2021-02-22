from Mat.OOP3.QuadraticEquation import QuadraticEquation


class BiQuadraticEquation(QuadraticEquation):

    def __str__(self):
        return ("%dx**4 + %dx**2 + %d = 0" % (self.a, self.b, self.c))

    def solve(self):
        #  x**4 + 2x**2 + 1 = 0
        #  y**2 + 2x + 1 = 0 => list of solutions = [...] = [-3, 9]
        #  y**2 + 2x + 1 = 0 => list of solutions = [...] = ["inf"]
        # y = x**2 = -3 => []
        # y = x**2 = 9 => [-3, 3]
        solution_of_quadratic_equation = super().solve()
        solutions = []
        for sol in solution_of_quadratic_equation:
            if sol == BiQuadraticEquation.INF:
                solutions.append(BiQuadraticEquation.INF)
            elif sol > 0:
                x1 = sol ** 0.5
                solutions.append(-x1)
                solutions.append(x1)
            elif sol == 0:
                solutions.append(0)

        return solutions

if __name__ == "__main__":
    eq = BiQuadraticEquation(1, 2, 1)
    print(eq)
    print(eq.solve())

    eq = BiQuadraticEquation(0, 0, 1)
    print(eq)
    print(eq.solve())

    eq = BiQuadraticEquation(0, 0, 0)
    print(eq)
    print(eq.solve())

    eq = BiQuadraticEquation(0, 1, 1)
    print(eq)
    print(eq.solve())

    eq = BiQuadraticEquation(0, 1, -1)
    print(eq)
    print(eq.solve())

    eq = BiQuadraticEquation(1, -3, 2)
    print(eq)
    print(eq.solve())


