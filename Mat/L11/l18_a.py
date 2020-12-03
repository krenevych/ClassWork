

# D_1 = 7, D_2 = 39
# D_n = 7D_(n-1) - 10D_(n-2), n >=3


N = int(input("N = "))

D2 = 7
D1 = 39
for n in range(3, N+1):
    D2, D1 = D1, 7 * D1 - 10*D2
    print(D1)
