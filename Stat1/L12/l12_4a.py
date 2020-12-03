eps = 0.00001
x = 169

xn = x / 2
xn_prev = xn
n = 0
while True:
    n += 1
    xn = 0.5 * (xn + x / xn)
    if abs(xn - xn_prev) < eps:
        break
    xn_prev = xn

print(xn, n)
print(x ** 0.5)
