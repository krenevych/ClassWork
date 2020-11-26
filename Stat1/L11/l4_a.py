

N = int(input("N= "))

D = 1
for n in range(1, N+1):
    D = 1 + 1 / D

print(D)

# N= 20   # 1.618033985017358
# N= 100  # 1.618033988749895