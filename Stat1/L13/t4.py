
def readMatrix(filename):
    matrix = []
    with open(filename) as f:
        for line in f:
            row = [float(el) for el in line.split()]
            # print(row)
            matrix.append(row)
    return matrix

def writeMatrix(matrix, filename):
    with open(filename, "w") as f:
        for row in matrix:
            print(*row, file=f)

def sumMatrix(a, b):
    c = []
    for i in range(len(a)):
        c.append([])
        for j in range(len(a[i])):
            c[i].append(a[i][j] + b[i][j])

    return c


a = readMatrix("t4a.txt")
b = readMatrix("t4b.txt")

c = sumMatrix(a, b)
print(c)

# writeMatrix(M, "t4b.txt")