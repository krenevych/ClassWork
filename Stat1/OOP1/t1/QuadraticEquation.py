class QuadraticEquation:
    INF_NUM_SOL = "inf"

    def __init__(self, a, b=None, c=None):
        if isinstance(a, QuadraticEquation):
            self.a = a.a
            self.b = a.b
            self.c = a.c
        else:
            self.a = a
            self.b = b
            self.c = c

    def show(self):
        print("%dx^2 + %dx + %d = 0" % (
            self.a, self.b, self.c))

    def discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    # ax^2 + bx + c = 0
    def solve(self):
        if self.a == 0:
            # bx + c = 0
            if self.b == 0:
                # c = 0
                if self.c == 0:
                    # 0 = 0
                    return [QuadraticEquation.INF_NUM_SOL]
                else:
                    # 4 = 0
                    return []
            else:
                return [-self.c / self.b]
        else:
            d = self.discriminant()
            if d < 0:
                return []
            elif d == 0:
                x = - self.b / (2 * self.a)
                return [x]
            else:
                d_2 = d ** 0.5
                x1 = (- self.b - d_2) / (2 * self.a)
                x2 = (- self.b + d_2) / (2 * self.a)
                lst = [x1, x2]
                [lst].sort()
                return lst

# print(__name__)

if __name__ == "__main__":
    # -74x^2 + 21x - 33 = 0
    eq = QuadraticEquation(1, 2, 1)
    eq.show()
    print(eq.solve())

    eq2 = QuadraticEquation(eq)
    eq2.b = 0
    eq2.c = -eq2.c
    eq2.show()
    print(eq2.solve())



