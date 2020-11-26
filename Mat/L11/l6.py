# 2, 1, -4 -11 -10  13 56 73 -22 -263

N = int(input("N= "))

D_prev_prev = 2
D_prev      = 1
for n in range(3, N+1):
    D_prev_prev, D_prev = D_prev, 2 * D_prev - 3 * D_prev_prev
    print(D_prev)
