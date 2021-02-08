from Mat.OOP1.t1.QuadraticEquation import QuadraticEquation

def readEquations(filename):
    listEquations = []
    with open(filename) as f:
        for line in f:
            try:
                a, b, c = [float(coef) for coef in line.split()]
            except ValueError:
                break
            eq = QuadraticEquation(a, b, c)

            listEquations.append(eq)
    return listEquations


lst = readEquations("input01.txt")

lstNoSol = []
lstOneSol = []
lstInfSol = []
lstTwoSol = []

for eq in lst:
    lstSol = eq.getSolution()
    if len(lstSol) == 0:
        lstNoSol.append(eq)
    elif len(lstSol) == 1:
        if lstSol[0] != QuadraticEquation.INF:
            lstOneSol.append(eq)
        else:
            lstInfSol.append(eq)
    else:
        lstTwoSol.append(eq)


print("Не мають розв'язків:")
print("===================:")
for eq in lstNoSol:
    eq.show()
print("мають один розв’язок:")
print("===================:")
for eq in lstOneSol:
    eq.show()
print("мають два розв’язки:")
print("===================:")
for eq in lstTwoSol:
    eq.show()
print("мають нескінченну кількість розв’язків:")
print("===================:")
for eq in lstInfSol:
    eq.show()
