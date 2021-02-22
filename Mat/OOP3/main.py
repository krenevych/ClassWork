from Mat.OOP3.BiQuadraticEquation import BiQuadraticEquation
from Mat.OOP3.Equation import Equation
from Mat.OOP3.QuadraticEquation import QuadraticEquation


def readEquations(filename):
    listEquations = []
    with open(filename) as f:
        for line in f:
            try:
                list_coef = [float(coef) for coef in line.split()]
                if len(list_coef) == 2:
                    eq = Equation(list_coef[0], list_coef[1])
                    listEquations.append(eq)
                elif len(list_coef) == 3:
                    eq = QuadraticEquation(list_coef[0], list_coef[1], list_coef[2])
                    listEquations.append(eq)
                elif len(list_coef) == 5:
                    eq = BiQuadraticEquation(list_coef[0], list_coef[2], list_coef[4])
                    listEquations.append(eq)

            except ValueError:
                break

    return listEquations


lst = readEquations("input01.txt")
# for eq in lst:
#     print(eq)


lstNoSol = []
lstOneSol = []
lstTwoSol = []
lstThreeSol = []
lstFourSol = []
lstInfSol = []

for eq in lst:
    lstSol = eq.solve()

    if len(lstSol) == 0:
        lstNoSol.append(eq)
    elif len(lstSol) == 1:
        if lstSol[0] != Equation.INF:
            lstOneSol.append(eq)
        else:
            lstInfSol.append(eq)
    elif len(lstSol) == 2:
        lstTwoSol.append(eq)
    elif len(lstSol) == 3:
        lstThreeSol.append(eq)
    else:
        lstFourSol.append(eq)

print("===================:")
print("Не мають розв'язків:")
print("===================:")
for eq in lstNoSol:
    eq.show()


max_eq = lstOneSol[0] if len(lstOneSol) > 0 else None
max_sol = lstOneSol[0].solve()[0] if len(lstOneSol) > 0 else None
print("===================:")
print("мають один розв’язок:")
print("===================:")
for eq in lstOneSol:
    eq.show()

    sol = eq.solve()[0]
    if sol > max_sol:
        max_eq = eq
        max_sol = sol

print("===================:")
print("мають два розв’язки:")
print("===================:")
for eq in lstTwoSol:
    eq.show()

print("===================:")
print("мають три розв’язки:")
print("===================:")
for eq in lstThreeSol:
    eq.show()

print("===================:")
print("мають чотири розв’язки:")
print("===================:")
for eq in lstFourSol:
    eq.show()

print("===================:")
print("мають нескінченну кількість розв’язків:")
print("===================:")
for eq in lstInfSol:
    eq.show()


print("рівняння, що має найбільший розв’язок серед розв’язків усіх рівнянь, що мають рівно один розв’язок")
print(max_eq)
print("розв'язок")
print(max_sol)