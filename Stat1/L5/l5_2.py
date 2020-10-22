
N = int(input())
lst = [int(i) for i in input().split()]

# approach 1
# for el in lst:
#     if el >= 0:
#         print(el + 2, end=" ")
#     else:
#         print(el, end=" ")

# approach 2
# DO NOT USE SUCH APPROACH IF YOU NEED MODIFY LIST

    # lst = [1, 2, 3, -4]
    # el = lst[0] => el = 1
    # el = lst[1]
    # ...

    # for el in lst:   # el = lst[поточний індекс]
    #     if el >= 0:
    #         el += 2
    #     print(el)
    # print(*lst)  # ==> print(lst[0], lst[1], lst[2],.. )

    # for el in lst:
    #     print(el, end=" ")

# for i in range(N):
#     if lst[i] >= 0:
#         lst[i] += 2
#
# print(*lst)

# approach 3
new_lst = [el + 2 if el >= 0 else el for el in lst]
print(*new_lst)
