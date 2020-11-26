x = float(input("x = "))
N = int(input("N = "))

a = 1
for k in range(1, N+1):
    a = - a * x*x / (2 * k * (2 * k - 1))

print(a)

import math

k = N
a = (-1)**k * x ** (2*k) / math.factorial(2 * k)
print(a)