
# 0! = 1
# 5! = 1 * 2 * 3 * 4 * 5 = 4! * 5

# f(n) = n!

# f(0) = 1
# f(n) = f(n-1) * n

def f(n):
    if n == 0:
        return 1
    else:
        return f(n - 1) * n

print(f(5))

# f(5) = 24 * 5 = 120
#         6 * 4
#         2 * 3
#         1 * 2
#         1 * 1
#         1