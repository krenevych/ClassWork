n = int(input())
elems = [int(el) for el in input().split()]

freq = {el: elems.count(el) for el in elems}

major = -1
for key in freq:
    if freq[key] > n // 2:
        major = key
        break

print(major)