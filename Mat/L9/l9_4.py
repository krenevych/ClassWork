n = int(input())
lst_elem = [int(i) for i in input().split()]
freq = {elem: lst_elem.count(elem) for elem in lst_elem}

res_lst = []
for el in lst_elem[::-1]:
    if el not in res_lst and freq[el] > 1:
        res_lst.insert(0, el)

if len(res_lst) > 0:
    print(*res_lst)
else:
    print("NO")

