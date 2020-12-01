
a = float(input("a = "))
# N = int(input("N = "))
# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37, 49, 65, 86, 114, 151, 200, 265,

P3 = 1
P2 = 1
P1 = 1
n = 2
# for n in range(3, N+1):
while P1 <= a:
    n += 1
    P3, P2, P1 = P2, P1, P2 + P3
    # print(P1, n)

print(P2, n - 1)
