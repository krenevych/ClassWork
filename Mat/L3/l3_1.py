# m * n = m + m + ... + m

n = int(input("n = "))
m = int(input("m = "))

res = 0
i = 0
while i < n:
    res += m
    i += 1

print("m * n = ", res)
