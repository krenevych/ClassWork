def prime(n):
    for i in range(2, (int)(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 123 -> 321
def invert(n):
    res = 0
    while n > 0:
        res = res * 10 + n % 10
        n = n // 10

    return res

a, b = [int(i) for i in input().split()]

counter = 0
for i in range(a, b + 1):
    inv_i = invert(i)
    if prime(i) and prime(inv_i):
        counter += 1

print(counter)
