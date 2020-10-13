n = int(input())
# n = 256 -> 652

# 256 = ((0 * 10 + 6) * 10 + 5) * 10 + 2

orig_n = n

inv = 0

while n > 0:
    ost = n % 10
    inv = inv * 10 + ost
    n = n // 10

if orig_n == inv:
    print("Yes")
else:
    print("No")
