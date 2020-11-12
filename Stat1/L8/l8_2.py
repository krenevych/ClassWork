

# 3 * 4 = 4 + 4 + 4 = 2 * 4 + 4
#                     2 * 4 = 4 + 4 = 1 * 4 + 4
#                                     1 * 4 = 0 * 4 + 4
#                                               0

# n * m = (n - 1) * m + m

# mult(n,m) = n * m

# mult(0, m) = 0
# mult(n,m) = mult(n-1, m) + m

def mult(n, m):
    if n == 0:
        return 0
    else:
        return mult(n - 1, m) + m

print(mult(3, 4))
print(mult(0, 4))
