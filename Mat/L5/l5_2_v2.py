N = int(input())
lst = [int(i) for i in input().split()]

for el in range(N):
    if lst[el] >= 0:
        lst[el] += 2

# DO NOT USE IT IF YOU NEED MODIFY LIST
# for el in lst:   # lst = [1, 2, 3, -4]
#                    # el = lst[3]
#     if el >= 0:
#         el += 2
#     print(el)

print(*lst)  # lst2 = [1, 2, 3]  *lst = 1, 2, 3