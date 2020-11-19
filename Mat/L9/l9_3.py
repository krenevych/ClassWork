N = int(input())
lst_elem = [int(i) for i in input().split()]

freq = {elem: lst_elem.count(elem) for elem in lst_elem}

for el in lst_elem:
    if freq[el] == 1:
        print(el, end=" ")