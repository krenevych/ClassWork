def readMatrix(file_name):
    try:
        with open(file_name, "r") as f:
            matrix = []
            for line in f:
                row = [float(el) for el in line.split()]
                matrix.append(row)
            return matrix
    except FileNotFoundError:
        return None
    except ValueError:
        print("Wrong file format")
        return None


def writeMatrix(M, file_name):
    with open(file_name, "w") as f:
        for row in M:
            print(*row, file=f)


def sumMatrix(A, B):
    assert len(A) == len(B)  # кількість рядків у обох матрицях однакова
    assert len(A[0]) == len(B[0])  # кількість стовпчиків у обох матрицях однакова

    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(A[i])):
            C[i].append(A[i][j] + B[i][j])
    return C


def mult(A, B):
    assert len(A[0]) == len(B)  # кількість стовпчиків лівої матриці
    # дорівнює кількості рядків правої матриці

    C = []
    for i in range(len(A)):
        row = [0] * len(B[0])
        C.append(row)

    n = len(C)  # кількість рядків
    m = len(C[0])  # кількість стовпчиків

    for i in range(n):
        for j in range(m):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]

    return C


def isMartEqual(A, B):
    assert len(A) == len(B)
    n = len(A)  # кількість рядків
    assert len(A[0]) == len(B[0])
    m = len(A[0])  # кількість стовпчиків
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                return False
    return True


A = readMatrix("t4A.txt")
B = readMatrix("t4B.txt")
# C = readMatrix("t4C.txt")

# AB = mult(A, B)
# if isMartEqual(AB, C):
#     print("A * B = C")
# else:
#     print("A * B != C")

C = mult(A, B)
writeMatrix(C, "t4C1.txt")

# C = sumMatrix(A, B)
# writeMatrix(C, "t4_sum_out.txt")


print(C)
