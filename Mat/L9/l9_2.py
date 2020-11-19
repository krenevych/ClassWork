
n = int(input())
lst_elem = [int(i) for i in input().split()]

# print(lst_elem)
# [3, 3, 5, 4, 2, 3, 3]

freq = {}
for el in lst_elem:
    if el in freq:
        freq[el] += 1
    else:
        freq[el] = 1

major = -1
for el in freq:
    if freq[el] > n // 2:
        major = el
        break

print(major)

