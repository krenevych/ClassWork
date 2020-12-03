eps = 0.00001
x = 13

a = x / 2
n = 0

while abs(a ** 2 - x) >= eps:
    n += 1
    a = 0.5 * (a + x / a)

print(a, n)