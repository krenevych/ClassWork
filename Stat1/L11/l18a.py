
N = int(input())

D2 = 7
D1 = 39

for n in range(3, N + 1):
    D2, D1 = D1, 7 * D1 - 10 * D2
    print(D1)
