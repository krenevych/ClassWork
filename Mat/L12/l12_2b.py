# x = float(input("x = "))
x = 3.1415
eps = 0.0000000000000000001
a = 1
S = 1
n = 0

while abs(a) >= eps:
    # for n in range(1, 100):
    n += 1
    a *= - x * x / (2 * n * (2 * n - 1))
    S += a

print(S, n)
