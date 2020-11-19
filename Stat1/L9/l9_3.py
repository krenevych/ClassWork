N = int(input())
elems = [int(el) for el in input().split()]

freq = {el: elems.count(el) for el in elems}

for el, count in freq.items():
    if count == 1:
        print(el, end=" ")
