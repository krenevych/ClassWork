
def readMatrix(filename):
    try:
        matrix = []
        row_len = None
        with open(filename) as f:
            for line in f:
                row = [float(el) for el in line.split()]
                if row_len == None:
                    row_len = len(row)
                else:
                    assert row_len == len(row)
                matrix.append(row)
        return matrix
    except FileNotFoundError:
        return None
    except ValueError:
        return None
    except AssertionError:
        return None

def writeMatrix(matrix, filename):
    with open(filename, "w") as f:
        for row in matrix:
            print(*row, file=f)

def sumMatrix(a, b):
    assert len(a) == len(b)
    assert len(a[0]) == len(b[0])
    n = len(a)
    m = len(a[0])

    c = []
    for i in range(n):
        row = [0] * m
        c.append(row)

    for i in range(n):
        for j in range(m):
            c[i][j] = a[i][j] + b[i][j]

    return c


def multMatrix(a, b):
    assert len(a[0]) == len(b)

    c = []
    for i in range(len(a)):
        row = [0] * len(b[0])
        c.append(row)

    n = len(c)     # кількість рядків
    m = len(c[0])  # кількість стовпчиків

    for i in range(n):
        for j in range(m):
            for k in range(len(a[0])):
                c[i][j] += a[i][k] * b[k][j]

    return c


a = readMatrix("t4a.txt")
b = readMatrix("t4b.txt")

# c = sumMatrix(a, b)
c = multMatrix(a, b)
print(c)

writeMatrix(c, "t4c.txt")