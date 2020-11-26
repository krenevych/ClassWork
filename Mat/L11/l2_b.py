

N = int(input("N= "))

S = 1
a = 1
for k in range(2, N+1):
    a = -a
    S += a / k

print(S)

# 10:   0.6456349206349207
# 31:   0.7090162022075269