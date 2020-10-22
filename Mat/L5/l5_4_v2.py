N = int(input())

lst = []
for i in range(N):
    el = int(input())
    lst.append(el)

# [25998, 33582, 23443, 12343, 96841, 92846]
#   0       1      2      3     4       5
for i in range(N // 2):
    a = lst[i]
    lst[i] = lst[N - 1 - i]
    lst[N - 1 - i] = a
    # lst[i], lst[N - 1 - i] = lst[N - 1 - i], lst[i]

print(*lst)