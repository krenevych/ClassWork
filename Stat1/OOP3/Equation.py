class Equation:
    INF_NUM_SOL = "inf"

    def __init__(self, b, c):
        self.b = b
        self.c = c

    def show(self):
        print(self)

    def __str__(self):
        return "%dx + %d = 0" % (self.b, self.c)

    def solve(self):
        if self.b != 0:
            # 2x + 1 = 0 => 1 solution
            return [-self.c / self.b]
        else:
            if self.c != 0:
                # 0x + 1 = 0 => 0 solution
                return []
            else:
                # 0x + 0 = 0 => inf solution
                return [self.INF_NUM_SOL]


if __name__ == "__main__":
    eq = Equation(2, 1)   # 1 solution: -0.5
    print(eq)
    print(eq.solve())

    eq = Equation(0, 1)  # 0 solution
    print(eq)
    print(eq.solve())

    eq = Equation(0, 0)  # inf solution
    print(eq)
    print(eq.solve())
