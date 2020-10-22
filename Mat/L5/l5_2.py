N = int(input())
lst = [int(i) for i in input().split()]

lst2 = [el + 2 if el >= 0 else el for el in lst]



# print(lst2)
#
# for el in lst2:
#     print(el, end=" ")
#
# print()

print(*lst2)  # lst2 = [1, 2, 3]  *lst = 1, 2, 3