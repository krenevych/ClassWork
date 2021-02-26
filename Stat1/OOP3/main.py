from Stat1.OOP3.BiQuadraticEquation import BiQuadraticEquation
from Stat1.OOP3.Equation import Equation
from Stat1.OOP3.QuadraticEquation import QuadraticEquation

list_eq = []
with open("input01.txt") as f:
    for line in f:
        try:
            list_coef = [int(coef) for coef in line.split()]
            if len(list_coef) == 2:
                eq = Equation(list_coef[0], list_coef[1])
                list_eq.append(eq)
            elif len(list_coef) == 3:
                eq = QuadraticEquation(list_coef[0], list_coef[1], list_coef[2])
                list_eq.append(eq)
            elif len(list_coef) == 5:
                eq = BiQuadraticEquation(list_coef[0], list_coef[2], list_coef[4])
                list_eq.append(eq)

        except ValueError:
            pass

eqs_0 = []
eqs_1 = []
eqs_2 = []
eqs_3 = []
eqs_4 = []
eqs_inf = []

for eq in list_eq:
    solutions = eq.solve()
    if Equation.INF_NUM_SOL in solutions:
        eqs_inf.append(eq)
    elif len(solutions) == 0:
        eqs_0.append(eq)
    elif len(solutions) == 1:
        eqs_1.append(eq)
    elif len(solutions) == 2:
        eqs_2.append(eq)
    elif len(solutions) == 3:
        eqs_3.append(eq)
    elif len(solutions) == 4:
        eqs_4.append(eq)



print("===================:")
print("мають один розв’язок:")
print("===================:")
for eq in eqs_1:
    print(eq)

print("===================:")
print("мають два розв’язки:")
print("===================:")
for eq in eqs_2:
    print(eq)

print("===================:")
print("мають три розв’язки:")
print("===================:")
for eq in eqs_3:
    print(eq)

print("===================:")
print("мають чотири розв’язки:")
print("===================:")
for eq in eqs_4:
    print(eq)

print("===================:")
print("мають нескінченну кількість розв’язків:")
print("===================:")
for eq in eqs_inf:
    print(eq)

