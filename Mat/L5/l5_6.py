s = input()

# s = "123412342134"
dig = [0] * 10
# dig [0 3 3 3 3 0 0 0 0 0]
#     [0 1 2 3 4 5 6 7 8 9]

for c in s:
    dig[int(c)] += 1

print(*dig)
