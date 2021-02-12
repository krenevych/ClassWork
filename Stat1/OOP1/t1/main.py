from Stat1.OOP1.t1.QuadraticEquation import QuadraticEquation

list_eq = []
with open("input01.txt") as f:
    for line in f:
        try:
            a, b, c = [int(coef) for coef in line.split()]
            list_eq.append(QuadraticEquation(a, b, c))
        except ValueError:
            pass

eqs_0 = []
eqs_1 = []
eqs_2 = []
eqs_inf = []

for equation in list_eq:
    solutions = equation.solve()
    if len(solutions) == 0:
        eqs_0.append(equation)
    elif len(solutions) == 1:
        if solutions[0] == QuadraticEquation.INF_NUM_SOL:
            eqs_inf.append(equation)
        else:
            eqs_1.append(equation)
    else:
        eqs_2.append(equation)

print("не мають розв’язків")
for eq in eqs_0:
    eq.show()

print("мають один розв’язок")
for eq in eqs_1:
    eq.show()

print("мають два розв’язки")
for eq in eqs_2:
    eq.show()

print("мають нескінченну кількість розв’язків")
for eq in eqs_inf:
    eq.show()

max = None
min = None
for eq in eqs_1:
    solution = eq.solve()[0]
    if max == None:
        max = eq
    else:
        solution_max = max.solve()[0]
        if solution_max < solution:
            max = eq
    if min == None:
        min = eq
    else:
        solution_min = min.solve()[0]
        if solution_min > solution:
            min = eq

if min != None:
    print("Рівняння з мінімальним розв'язком:")
    min.show()
    print(min.solve())
if max != None:
    print("Рівняння з масимальним розв'язком:")
    max.show()
    print(max.solve())

