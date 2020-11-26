
N = int(input("N = "))

S = 1
a = 1
for n in range(2, N+1):
    a = -a
    S += a / n

print(S)

# N = 20   # 0.6687714031754279