# 1 1 2 3 5 8 13

fibs = [0] * 20001

def F(n):
    if fibs[n] != 0:
        return fibs[n]

    if n == 1 or n == 2:
        fibs[n] = 1
    else:
        fibs[n] = F(n - 1) + F(n - 2)

    return fibs[n]


t = int(input())
for i in range(t):
    n = int(input())
    print(F(n))

