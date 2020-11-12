
#            1               0                   C(0, 0)
#          1   1             1              C(1, 0)   C(1, 1)
#        1   2   1           2         C(2, 0)    C(2, 1)   C(2, 2)
#      1   3   3   1         3      C(3, 0)    C(3, 1)   C(3, 2)   C(3, 3)
#    1   4   6   4   1       4  C(4, 0)  C(4, 1)   C(4, 2)   C(4, 3)   C(4, 4)

# C(2, 1) = C(1, 0) + C(1, 1)
# C(3, 2) = C(2, 1) + C(2, 2)


# C(n, 0) = 1, C(n, n) = 1, n >= 0
# C(n, k) = C(n-1, k-1) + C(n-1, k)

def C(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return C(n-1, k-1) + C(n-1, k)

for n in range(5):
    for k in range(n + 1):
        print(C(n, k), end=" ")
    print()