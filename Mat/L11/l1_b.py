import math

N = int(input("N= "))
x = float(input("x= "))

a = 1
for k in range(1, N+1):
    a = -a * x * x / ((2 * k -1) * 2 * k)

print(a)

a1 = (-1)**N * x ** (2 * N) / math.factorial(2 * N)
print(a1)