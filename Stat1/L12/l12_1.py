# a = 135
# 1,
# 1 + 1/2,
# ....
# S_n = 1 + 1/2 + ... + 1/n

# S_1 = 1
# S_n = S_(n-1) + 1/n, n>=2

a = float(input("a = "))
# N = int(input("N = "))

S = 1
n = 1
while S <= a:
# for n in range(2, N+1):
    n += 1
    S += 1/n

print(S, n)