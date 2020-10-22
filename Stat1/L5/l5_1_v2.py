
N = int(input())

lst = [int(i) for i in input().split()]

M = lst[0]
for i in range(1, N):
    if lst[i] > M:
        M = lst[i]

print(M)
