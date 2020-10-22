# 1326123698700

digits = [0] * 10

n = int(input())

while n > 0:
    d = n % 10
    n //= 10
    digits[d] += 1


print(*digits)