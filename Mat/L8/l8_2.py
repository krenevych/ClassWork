
# 3 * 2 = 2 + 2 + 2 = 2 * 2 + 2
#                     2 + 2 = 1 * 2 + 2
#                               2 = 0 * 2 + 2
#                                     0

# f(n , m) = m + ... + m = m * (n-1) + m
#            ---- n ---

# f(0,  m) = 0
# f(n , m) = f(n - 1, m) + m

def mult(n, m):
    if n == 0:
        return 0
    else:
        return mult(n-1, m) + m

print(mult(4, 5))