def prime(n):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def inverse(n):
    res = 0
    while n > 0:
        res = res * 10 + n % 10
        n //= 10

    return res


counter = 0

a, b = [int(i) for i in input().split()]

if a == 1:
    a += 1

for i in range(a, b + 1):
    inv = inverse(i)
    if prime(i) and prime(inv):
        counter += 1

print(counter)
