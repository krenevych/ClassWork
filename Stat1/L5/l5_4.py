n = int(input())

lst = []
for i in range(n):
    x = int(input())
    lst.append(x)

# reversed_na = lst[::-1]
# lst.reverse()
# print(*lst)
# print(*reversed_na)

# [0, 1, 2, 3, 4, 5, 6] => [6, 5, 4, 3, 2, 1, 0]
# [0, 1, 2, 4, 1, 6] => [6, 5, 4, 2, 1, 0]

for i in range(n // 2):
    lst[i], lst[n - 1 - i] = lst[n - 1 - i], lst[i]

print(*lst)

# lst_reversed = []
# for i in range(n):
#
#     from_end = lst[n - 1 - i]
#     # print(from_end)
#
#     lst_reversed.append(from_end)
#
# print(*lst_reversed)