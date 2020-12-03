eps = 0.00001
x = 169

xn = x / 2
n = 0
while True:
    n += 1
    xn = 0.5 * (xn + x / xn)
    if abs(xn ** 2 - x) < eps:
        break

print(xn, n)
print(x ** 0.5)
