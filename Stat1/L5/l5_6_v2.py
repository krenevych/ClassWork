# 1326123698700

digits = [0] * 10
# digits = [0, 2, 1, 1, 0, 0, 1, 0, 0, 0]
#          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = input()

for c in n:

    i = int(c)
    digits[i] += 1

print(*digits)