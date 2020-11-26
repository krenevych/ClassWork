
x = float(input("x = "))
N = int(input("N = "))

a = x
for k in range(2, N + 1):
    a = a * x * (k-1) / k

print(a)

a = x ** N / N
print(a)

