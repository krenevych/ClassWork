N = int(input())

lst = []
for i in range(N):
    el = int(input())
    lst.append(el)

reverse = lst[::-1]

print(*reverse)
