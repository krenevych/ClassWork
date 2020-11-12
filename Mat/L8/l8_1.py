
# 0! = 1
# 5! = 1 * 2 * 3 * 4 * 5 = 4! * 5

# f(n) = n!

# f(0) = 1
# f(n) = f(n-1) * n

def f(n):
    if n == 0:  # термінальний випадок
        return 1
    else:      # рекурсивна гілка
        prev = f(n - 1)
        return prev * n

print(f(5))