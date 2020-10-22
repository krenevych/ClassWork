


# s = input()
# l1 = s.split()
#
# print(s)
# print(l1)
#
# l2 = [int(i) for i in l1]
#
# print(l2)

N = int(input())
lst = [int(i) for i in input().split()]

# print(max(lst))

M = lst[0]
for i in range(1, N):
    if lst[i] > M:
        M = lst[i]

print(M)