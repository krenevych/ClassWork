n = int(input())
elems = [int(el) for el in input().split()]
freq = {el: elems.count(el) for el in elems}

# print(elems)
# print(freq)

res = []
for el in elems[::-1]:
    if freq[el] >= 2 and el not in res:
        res.insert(0, el)

if len(res) == 0:
    print("NO")
else:
    print(*res)