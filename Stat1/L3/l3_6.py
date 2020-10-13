n = int(input())
# n = 256 -> 652

# 256 = ((0 * 10 + 6) * 10 + 5) * 10 + 2

inv = 0

while n > 0:
    ost = n % 10
    inv = inv * 10 + ost
    n = n // 10

print(inv)
