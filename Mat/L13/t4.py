def readMatrix(file_name):
    matrix = []
    with open(file_name, "r") as f:
        for line in f:
            row = [float(el) for el in line.split()]
            matrix.append(row)
    return matrix

def writeMatrix(M, file_name):
    with open(file_name, "w") as f:
        for row in M:
            print(*row, file=f)

def sumMatrix(A, B):
    # assert len(A) == len(B)
    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(A[i])):
            C[i].append(A[i][j] + B[i][j])
    return C

A = readMatrix("t4A.txt")
B = readMatrix("t4B.txt")
# print(A)

C = sumMatrix(A, B)
writeMatrix(C, "t4_sum_out.txt")
